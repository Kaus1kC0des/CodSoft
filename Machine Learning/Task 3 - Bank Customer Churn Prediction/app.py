import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib

# Load the trained model
model = joblib.load("data/final_XGB_model.pkl")

# Function to collect inputs from the user
def get_user_input():
    CreditScore = st.sidebar.text_input('Credit Score', 650)
    Geography = st.sidebar.selectbox('Geography', ['France', 'Germany', 'Spain'])
    Gender = st.sidebar.selectbox('Gender', ['Male', 'Female'])
    Age = st.sidebar.text_input('Age', 35)
    Tenure = st.sidebar.text_input('Tenure', 5)
    Balance = st.sidebar.text_input('Balance', 125000.0)
    NumOfProducts = st.sidebar.text_input('Number of Products', 2)
    HasCrCard = st.sidebar.selectbox('Has Credit Card', ['Yes', 'No'])
    IsActiveMember = st.sidebar.selectbox('Is Active Member', ['Yes', 'No'])
    EstimatedSalary = st.sidebar.text_input('Estimated Salary', 100000.0)

    # Encoding the categorical variables
    Geography = 1 if Geography == 'France' else 2 if Geography == 'Germany' else 3
    Gender = 1 if Gender == 'Male' else 0
    HasCrCard = 1 if HasCrCard == 'Yes' else 0
    IsActiveMember = 1 if IsActiveMember == 'Yes' else 0

    # Create a data frame from the inputs
    user_data = pd.DataFrame({
        'CreditScore': [float(CreditScore)],
        'Geography': [Geography],
        'Gender': [Gender],
        'Age': [float(Age)],
        'Tenure': [float(Tenure)],
        'Balance': [float(Balance)],
        'NumOfProducts': [float(NumOfProducts)],
        'HasCrCard': [HasCrCard],
        'IsActiveMember': [IsActiveMember],
        'EstimatedSalary': [float(EstimatedSalary)]
    })

    return user_data

# Get user input
user_input = get_user_input()

# Add a button for the prediction
if st.sidebar.button('Predict'):
    # Make prediction
    prediction = model.predict(user_input)

    # Display prediction
    st.write(f"This customer is {prediction[0]*100:.2f}% likely to leave")