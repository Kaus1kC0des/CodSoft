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
from flask import redirect, url_for

app = Flask(__name__, template_folder='templates')
ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    del text  # free up memory space
    text = []
    for i in y:
        if i not in stopwords.words("english") and i not in string.punctuation:
            text.append(i)
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    out = " ".join(y)
    del y  # Free memory space
    del text  # Free memory space
    return out


prediction = ""

model = pickle.load(open('models/final_model.pkl', 'rb'))
vectorizer = pickle.load(open('models/vectorizer_final.pkl', 'rb'))


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict.html")
def predict_html():
    return render_template("predict.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        try:
            global prediction
            message = ""
            message = request.form['emailContent']
            # data = request.get_json()
            # message = data.get('emailContent')
            query = transform_text(message)
            vect = vectorizer.transform([query]).toarray()
            out = model.predict(vect)
            print(type(out[0]))
            if out == 0:
                prediction = "HAM"
                print(prediction)
                return redirect(url_for('ham'))
                # return output(prediction)
            else:
                prediction = "SPAM!"
                print(prediction)
                return redirect(url_for("spam"))
        except Exception as e:
            return render_template("error.html", error_message=e)
    else:
        return render_template("predict.html")


@app.route("/output")
def output(prediction):
    return render_template('output.html', prediction=prediction)

@app.route("/spam")
def spam():
    return render_template("spam.html")

@app.route("/ham")
def ham():
    return render_template("ham.html")


if __name__ == '__main__':
    app.run()