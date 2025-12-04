import logging
import pandas as pd
import numpy as np
from helper_functions.helper_trainer import SVM_Trainer_Class
from sklearn.base import ClassifierMixin
import json
import pickle
def train_model(X_train:np.ndarray,y_train:pd.DataFrame)->ClassifierMixin:
    try:
        config_path='/Users/rishilboddula/Desktop/MLOPS/Fraud-Credit-Card-detection-MLOPS/helper_functions/config.json'
        with open(config_path,'r') as f:
            config=json.load(f)

        svm=SVM_Trainer_Class()

        svm_trained_model=svm.train_model(X_train,y_train,**config['svm'])
        logging.info('Successfully Trained SVM model')
        return svm_trained_model
    except Exception as e:
        logging.error(f'Error Training the model')
