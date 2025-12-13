import logging
import pandas as pd
import numpy as np
from helper_trainer import SVM_Trainer_Class
from sklearn.base import ClassifierMixin
import json
import pickle
import mlflow
import mlflow.sklearn
from airflow.decorators import task
from helper_trainer import Random_Forest_Trainer_Class
@task
def train_model()->ClassifierMixin:
    try:
        mlflow.set_tracking_uri('http://host.docker.internal:5050')
        mlflow.set_experiment('fraud_credit_card')
        with open('/opt/airflow/config/data_pkl_files/x_train_data.pkl','rb') as f:
            X_train=pickle.load(f)
        with open('/opt/airflow/config/data_pkl_files/y_train_data.pkl','rb') as f:
            y_train=pickle.load(f)
        config_path='/opt/airflow/helper_functions/config.json'
        with open(config_path,'r') as f:
            config=json.load(f)

        svm=SVM_Trainer_Class()
        rfc=Random_Forest_Trainer_Class()

        
      

        
        with mlflow.start_run(run_name='svm_trained_model') as run:
            svm_trained_model=svm.train_model(X_train,y_train,**config['svm'])
            logging.info('Successfully Trained SVM model')
            mlflow.sklearn.log_model(sk_model=svm_trained_model,artifact_path='svm_model')
            run_id=run.info.run_id
            mlflow.register_model(
            model_uri=f'runs:/{run_id}/svm',
            name='svm_trained_model' )
        with mlflow.start_run(run_name='Random_Forest_trained_model') as run:
            random_forest_trained=rfc.train_model(X_train,y_train,**config['rfc'])
            logging.info('Successfully Trained RF model')
            mlflow.sklearn.log_model(sk_model= random_forest_trained,artifact_path='random_forest_model')
            run_id=run.info.run_id
            mlflow.register_model(
            model_uri=f'runs:/{run_id}/random_forest_model',
            name='Random_Forest_trained_model' )




        with open('/opt/airflow/config/model_pkl_files/svm_model.pkl','wb') as f:
            pickle.dump(svm_trained_model,f)
        logging.info('Successfully put the svm_model in a pkl file')
        with open('/opt/airflow/config/model_pkl_files/random_forest_model.pkl','wb') as f:
            pickle.dump(random_forest_trained,f)
        logging.info('Successfully put the svm_model in a pkl file')

        
    except Exception as e:
        logging.error(f'Error Training the model:{e}')
        raise e
