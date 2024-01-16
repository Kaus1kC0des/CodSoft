from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from flask import Flask, render_template, request
import nltk
import pandas as pd
import numpy as np
nltk.download("punkt")
nltk.download("stopwords")
import pickle

import string
app = Flask(__name__,template_folder='templates')
ps = PorterStemmer()
def transform_text(text):
  text = text.lower()
  text = nltk.word_tokenize(text)
  y = []
  for i in text:
    if i.isalnum():
      y.append(i)
  del text # free up memory space
  text = []
  for i in y:
    if i not in stopwords.words("english") and i not in string.punctuation:
      text.append(i)
  y.clear()
  for i in text:
    y.append(ps.stem(i))
  out = " ".join(y)
  del y # Free memory space
  del text # Free memory space
  return out

prediction = ""

model = pickle.load(open('models/final_model.pkl', 'rb'))
vectorizer = pickle.load(open('models/vectorizer_final.pkl', 'rb'))



@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict", methods=["GET","POST"])
def predict():
  if request.method == "POST":
    try:
      global prediction
      data = request.get_json()
      message = data.get('emailContent')
      query = transform_text(message)
      vect = vectorizer.transform([query]).toarray()
      out = model.predict(vect)
      print(type(out[0]))
      if out == 0:
        prediction += "HAM"
        print(prediction)
        return render_template("output.html", prediction=prediction)
      else:
        prediction += "SPAM!!"
        print(prediction)
        return render_template("output.html", prediction=prediction)

    except Exception as e:
      return render_template("error.html",error_message=e)
  else:
    return render_template("predict.html")

@app.route("/output")
def output():
  return render_template('output.html',prediction=prediction)


if __name__ == '__main__':
    app.run()