import pickle
import string
import nltk
from flask import Flask, render_template, request, redirect, url_for
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

nltk.download("punkt")
nltk.download("stopwords")

app = Flask(__name__, template_folder='templates')
ps = PorterStemmer()
prediction = ""
model = pickle.load(open('models/final_model.pkl', 'rb'))
vectorizer = pickle.load(open('models/vectorizer_final.pkl', 'rb'))


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = [i for i in y if i not in stopwords.words("english") and i not in string.punctuation]
    y = [ps.stem(i) for i in text]
    out = " ".join(y)
    return out


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
            message = request.form['emailContent']
            query = transform_text(message)
            vect = vectorizer.transform([query]).toarray()
            out = model.predict(vect)
            if out == 0:
                prediction = "HAM"
                return redirect(url_for('ham'))
            else:
                prediction = "SPAM!"
                return redirect(url_for("spam"))
        except Exception as e:
            return render_template("error.html", error_message=e)
    else:
        return render_template("predict.html")


@app.route("/spam")
def spam():
    return render_template("spam.html")


@app.route("/ham")
def ham():
    return render_template("ham.html")


if __name__ == '__main__':
    app.run()