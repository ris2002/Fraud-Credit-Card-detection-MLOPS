import logging
import pandas as pd
import numpy as np
from helper_trainer import SVM_Trainer_Class
from sklearn.base import ClassifierMixin
import json
import pickle
from airflow.decorators import task
@task
def train_model()->ClassifierMixin:
    try:
        with open('/opt/airflow/config/data_pkl_files/x_train_data.pkl','rb') as f:
            X_train=pickle.load(f)
        with open('/opt/airflow/config/data_pkl_files/y_train_data.pkl','rb') as f:
            y_train=pickle.load(f)
        config_path='/opt/airflow/helper_functions/config.json'
        with open(config_path,'r') as f:
            config=json.load(f)

        svm=SVM_Trainer_Class()

        svm_trained_model=svm.train_model(X_train,y_train,**config['svm'])
        logging.info('Successfully Trained SVM model')
        with open('/opt/airflow/config/model_pkl_files/svm_model.pkl','wb') as f:
            pickle.dump(svm_trained_model,f)
        logging.info('Successfully put the svm_model in a pkl file')

        
    except Exception as e:
        logging.error(f'Error Training the model:{e}')
        raise e
