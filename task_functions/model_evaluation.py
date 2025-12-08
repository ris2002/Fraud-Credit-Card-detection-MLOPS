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

        
        with open('/opt/airflow/config/data_pkl_files/x_test_data.pkl', 'rb') as f:
            X_test = pickle.load(f)

        with open('/opt/airflow/config/data_pkl_files/y_test_data.pkl', 'rb') as f:
            y_test = pickle.load(f)

       

        with open('/opt/airflow/config/model_pkl_files/svm_model.pkl', 'rb') as f:
            svm_trained_model = pickle.load(f)
        with open('/opt/airflow/config/model_pkl_files/random_forest_model.pkl','rb') as f:
            rfc_model=pickle.load(f)

        
        svm_model_prediction = evaluation.model_prediction(svm_trained_model, X_test)
        svm_acc_score = evaluation.accuracy_scores(svm_model_prediction, y_test)

        SVM_TP,SVM_TN,SVM_FP,SVM_FN=evaluation.confustion_matrixs(svm_model_prediction,y_test)

        rfc_model_prediction = evaluation.model_prediction(rfc_model, X_test)
        rfc_acc_score = evaluation.accuracy_scores(rfc_model_prediction, y_test)
        RFC_TP,RFC_TN,RFC_FP,RFC_FN=evaluation.confustion_matrixs(rfc_model_prediction,y_test)

       
        with mlflow.start_run(run_name='svm_trained_model') as run:
            mlflow.log_metric('accuracy_scores', svm_acc_score)
            mlflow.log_metric('true_positive',SVM_TP)
            mlflow.log_metric('true_negative',SVM_TN)
            mlflow.log_metric('false_positive',SVM_FP)
            mlflow.log_metric('false_negative',SVM_FN)


        with mlflow.start_run(run_name='Random_Forest_trained_model') as run:
            mlflow.log_metric('accuracy_scores', rfc_acc_score)
            mlflow.log_metric('true_positive',RFC_TP)
            mlflow.log_metric('true_negative',RFC_TN)
            mlflow.log_metric('false_positive',RFC_FP)
            mlflow.log_metric('false_negative',RFC_FN)

        logging.info('Done Evaluating SVM model')

    except Exception as e:
        logging.error(f'Error Caused while Evaluating and Predictinng the model: {e}')
        raise e
