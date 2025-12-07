import logging
import mlflow
import mlflow.sklearn
from helper_evaluator import Evaluation_And_Prediction_Strategy
import os
from airflow.decorators import task
import pickle

@task
def model_eval():
    try:
        evaluation = Evaluation_And_Prediction_Strategy()

        mlflow.set_tracking_uri('http://host.docker.internal:5050')
        mlflow.set_experiment('fraud_credit_card')

        # Load test data (FIX THIS PATH IF NEEDED)
        with open('/opt/airflow/config/data_pkl_files/x_test_data.pkl', 'rb') as f:
            X_test = pickle.load(f)

        with open('/opt/airflow/config/data_pkl_files/y_test_data.pkl', 'rb') as f:
            y_test = pickle.load(f)

        # Load model correctly
        model_path = '/opt/airflow/config/model_pkl_files/svm_model.pkl'

        with open(model_path, 'rb') as f:
            svm_trained_model = pickle.load(f)

        # Evaluate model
        svm_model_prediction = evaluation.model_prediction(svm_trained_model, X_test)
        svm_acc_score = evaluation.accuracy_scores(svm_model_prediction, y_test)

        # Log to MLflow
        with mlflow.start_run(run_name='svm_trained_model') as run:
            mlflow.log_metric('accuracy_scores', svm_acc_score)

        logging.info('Done Evaluating SVM model')

    except Exception as e:
        logging.error(f'Error Caused while Evaluating and Predictinng the model: {e}')
        raise e
