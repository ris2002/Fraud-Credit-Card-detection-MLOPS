import logging
from sklearn.svm import SVC
from abc import abstractmethod,ABC
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier



class Model_Training_Strategies(ABC):
    @abstractmethod
    def train_model(self,X_train:np.ndarray,y_train:np.ndarray,**kwargs):
        pass

class SVM_Trainer_Class(Model_Training_Strategies):
    def train_model(self,X_train:np.ndarray,y_train:np.ndarray,**kwargs):
        try:
            svm=SVC(**kwargs)
            model=svm.fit(X_train,y_train)
            return model
        except Exception as e:
            logging.error(f'Error training SVM model:{e}')
            raise e

class Random_Forest_Trainer_Class(Model_Training_Strategies):
    def train_model(self,X_train:np.ndarray,y_train:np.ndarray,**kwargs):
        try:
            random_forest=RandomForestClassifier(**kwargs)
            model=random_forest.fit(X_train,y_train)
            return model
        except Exception as e:
            logging.error(f'Error training RFC model:{e}')
            raise e
class KNN_Trainer_Class(Model_Training_Strategies):
    def train_model(self,X_train:np.ndarray,y_train:np.ndarray,**kwargs):
        pass
class Decision_Trees_Trainer_Class(Model_Training_Strategies):
    def train_model(self,X_train:np.ndarray,y_train:np.ndarray,**kwargs):
        pass
class XGboost_Trainer_Class(Model_Training_Strategies):
    def train_model(self,X_train:np.ndarray,y_train:np.ndarray,**kwargs):
        pass
