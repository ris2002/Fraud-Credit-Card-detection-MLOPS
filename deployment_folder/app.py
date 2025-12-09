from helper_functions.helper_cleaner import Pre_Process_Strategy
import logging
import mlflow
import fastapi
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from typing import List
app=FastAPI()
mlflow.set_tracking_uri('http://host.docker.internal:5050')
mlflow.set_experiment('fraud_credit_card')

cleaning_process=Pre_Process_Strategy()# no need of cleaner fuction
model_svm=mlflow.pyfunc.load_model('models:/svm_trained_model/1')


class Data_Input(BaseModel):
    data:List[float] # fast api doesnt parse np.array , LIST tells fast api that its an array

@app.post('/svm_predict_model')
def predict_svm_model(row_data: Data_Input):
    try:
       input_df=pd.DataFrame([row_data.data])
       prediction=model_svm(input_df)
       logging.info('Prediction Done')
       return{"prediction": prediction.tolist()}
        
    except Exception as e:
        logging.error(f'SVM model_prediction_ not working')


