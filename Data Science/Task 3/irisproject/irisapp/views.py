import os

from django.shortcuts import render, redirect
from django.http import HttpResponse
from joblib import load
import numpy as np  # Adjust the model import if needed

model = load(os.path.join(os.path.dirname(__file__), 'models/iris_model.joblib'))

#creating the home page
def home(request):
    return render(request, 'home.html')

def predict(request):
    if request.method == "GET":
        try:
            return render(request,'predict.html')
        except Exception as e:
            return render(request,'error.html',{'error':e})
    elif request.method == "POST":
        try:
            data = request.POST.dict()
            data.pop('csrfmiddlewaretoken')
            data = list(map(float, data.values()))
            data = np.array([data]).reshape(1, -1)
            prediction = model.predict(data)[0]
            if prediction == 0:
                prediction = 'Iris Setosa'
                return render(request, 'predict.html', {'prediction': "Iris Setosa"})
            elif prediction == 1:
                prediction = 'Iris Versicolor'
                return render(request, 'predict.html', {'prediction': "Iris Versicolor"})
            else:
                prediction = 'Iris Virginica'
                return render(request, 'predict.html', {'prediction': "Iris Virginica"})
        except Exception as e:
            return render(request,'error.html',{'error':e})
