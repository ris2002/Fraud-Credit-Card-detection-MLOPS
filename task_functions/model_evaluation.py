import pandas as pd
import logging
import mlflow
from helper_functions.helper_evaluator import Evaluation_And_Prediction_Strategy
from sklearn.base import ClassifierMixin
import numpy as np
def model_eval(trained_model:ClassifierMixin,X_test:np.ndarray,y_test:pd.DataFrame)->float:
    try:
        evaluation=Evaluation_And_Prediction_Strategy()
        model_prediction=evaluation.model_prediction(trained_model,X_test)
        acc=evaluation.accuracy_scores(model_prediction,y_test)
        print(acc)
        return acc

    except Exception as e:
        logging.error(f'Error Caused while Evaluating and Predictinng the model:{e}')
        raise e