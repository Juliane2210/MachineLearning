import os
import sys

import numpy as np
import pandas as pd
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

# function save_object that takes a file path and an object as parameters.
#  The function attempts to create the directory path if it doesn't exist,
# and then it saves the object using the dill serializer to the specified file path.
# If any exception occurs, it raises a custom exception.


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)

# function evaluate_models that takes training and test data, a dictionary of models, and a dictionary of corresponding parameters.
# The function performs hyperparameter tuning using GridSearchCV, fits each model to the training data, makes predictions on both the training and test sets,
# and evaluates the models using R-squared scores.
# The results are stored in a dictionary (report).
# If an error occurs, a custom exception is raised.


def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para = param[list(models.keys())[i]]

            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)


# train model
           # model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)
            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)


# function load_object that takes a file path as a parameter.
# The function opens the file path in read-binary mode and loads the object using dill.
# If an error occurs, a custom exception is raised.
def load_object(file_path):
    try:
        # opening that file path in read bite mode and loading the pickle file
        with open(file_path, 'rb') as file_obj:
            return dill.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
