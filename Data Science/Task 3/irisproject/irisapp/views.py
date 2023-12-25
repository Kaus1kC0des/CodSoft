import os

from django.shortcuts import render, redirect
from django.http import HttpResponse
from joblib import load
import numpy as np  # Adjust the model import if needed

# Load the model within the views.py file
iris_model = load("models/iris_model.joblib")

def home(request):
    return render(request, 'home.html')

def predict(request):
    if request.method == 'POST':
        try:
            data = request.POST.to_dict()
            data = [float(v) for v in data.values()]  # Convert form values to floats
            data = np.array(data, dtype=np.float64).reshape(1, -1)  # reshape for prediction
            prediction = iris_model.predict(data)[0]  # Extract single prediction

            if prediction == 0:
                predicted_class = "Iris Setosa"
            elif prediction == 1:
                predicted_class = "Iris Versicolour"
            else:
                predicted_class = "Iris Virginica"

            return render(request, 'output.html', {'prediction': predicted_class})
        except Exception as e:
            # Handle and log exceptions
            return render(request, 'error.html', {'error': e})
    else:
        return render(request, 'predict.html')

# def output(request):
#     return render(request, 'output.html', {'prediction': ""})  # Optional view
print(os.getcwd())