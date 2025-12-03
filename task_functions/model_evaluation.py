import pandas as pd
import logging
import mlflow
from helper_functions.helper_evaluator import Evaluation_And_Prediction_Strategy
def model_eval()->None:
    try:
        evaluation=Evaluation_And_Prediction_Strategy()
        model_prediction=evaluation.model_prediction()
        
    except Exception as e:
        logging.error(f'Error Caused while Evaluating and Predictinng the model:{e}')
        raise e