import streamlit as st
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
import string
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer



# Load the model
model = joblib.load('models/models/final_model.pkl')
tfidf_vectorizer = joblib.load('models/models/vectorizer.pkl')

# Function to clean text
stemmer = LancasterStemmer()
stop_words = set(stopwords.words('english'))

# Define the clean_text function
def clean_text(text):
    text = text.lower()  # Lowercase all characters
    text = re.sub(r'@\S+', '', text)  # Remove Twitter handles
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'pic.\S+', '', text)
    text = re.sub(r"[^a-zA-Z+']", ' ', text)  # Keep only characters
    text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text + ' ')  # Keep words with length > 1 only
    text = "".join([i for i in text if i not in string.punctuation])
    words = nltk.word_tokenize(text)
    stopwords = nltk.corpus.stopwords.words('english')  # Remove stopwords
    text = " ".join([i for i in words if i not in stopwords and len(i) > 2])
    text = re.sub("\s[\s]+", " ", text).strip()  # Remove repeated/leading/trailing spaces
    return text

# Function to predict genre
def predict_genre(text):
    # Clean the text
    cleaned_text = clean_text(text)
    # Transform the text
    transformed_text = tfidf_vectorizer.transform([cleaned_text])
    # Predict the genre
    predicted_genre = model.predict(transformed_text)
    return predicted_genre

# Streamlit app
st.title('Movie Genre Prediction')
st.write('Enter a movie plot summary and the model will predict the genre.')

# User input
user_input = st.text_area('Enter movie plot summary here:')

# Predict button
if st.button('Predict'):
    # Make prediction
    prediction = predict_genre(user_input)
    # Display prediction
    st.write('Predicted genre: ', prediction)