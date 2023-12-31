# Iris Flower Prediction Project

This project is a Django-based web application that predicts the species of iris flowers based on their sepal length, sepal width, petal length, and petal width. The prediction model used is a Logistic Regression model, which has been tuned using GridSearchCV for optimal performance.

## Project Structure


### [irisapp/](./irisapp/)

This is the main Django application directory. It contains the following:

- [models/](./irisapp/models/): This directory contains the data and model files for the project.
  - [iris.csv](./irisapp/models/iris.csv): The dataset used for training the model.
  - [iris_modelling.ipynb](irisapp/models/iris_modelling.ipynb): A Jupyter notebook that contains the code for training and tuning the model.
  - [iris_model.joblib](irisapp/models/iris_model.joblib): The trained Logistic Regression model.

- [__init__.py](./irisapp/__init__.py): An empty file that tells Python that this directory should be considered a Python package.

- [urls.py](./irisapp/urls.py): The URL declarations for this Django application.

- [views.py](./irisapp/views.py): The views of the application. This is where the main functionality of the application is implemented.

### [irisproject/](./irisproject/)

This is the main project directory. It contains the following:

- [__init__.py](./irisproject/__init__.py): An empty file that tells Python that this directory should be considered a Python package.

- [asgi.py](./irisproject/asgi.py): An entry-point for ASGI-compatible web servers to serve your project.

- [settings.py](./irisproject/settings.py): Settings/configuration for this Django project.

- [urls.py](./irisproject/urls.py): The URL declarations for this Django project.

- [wsgi.py](./irisproject/wsgi.py): An entry-point for WSGI-compatible web servers to serve your project.

### [templates/](./irisapp/templates/): This directory contains the HTML templates for the application.
  - [error.html](./irisapp/templates/error.html): The template for displaying error messages.
  - [home.html](./irisapp/templates/home.html): The template for the home page.
  - [output.html](./irisapp/templates/output.html): The template for displaying the prediction result.
  - [predict.html](./irisapp/templates/predict.html): The template for the page where users input the flower parameters.

This directory contains the HTML templates for the application. It has the same files as `irisapp/templates/`.

### [manage.py](./manage.py)

A command-line utility that lets you interact with this Django project in various ways.

## Running the Project

To run the project, navigate to the `Irisproject/` directory and run the following command:

```bash
pip install pipenv
pipenv install
python manage.py runserver
```

This will start the Django development server. You can access the web application by navigating to `http://localhost:8000/` or 'http://127.0.0.1:8000/' in your web browser.