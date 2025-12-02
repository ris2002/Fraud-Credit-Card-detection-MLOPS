import logging
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
import pandas as pd
import numpy as np
from typing import Tuple
from typing_extensions import Annotated


class Evaluation_And_Prediction_Strategy:

    def model_prediction(self,trained_model:np.ndarray,X_test_data:np.ndarray)->np.ndarray:
        try:
            predicted_model=trained_model.predict(X_test_data)
            logging.info('Predicted the model')
            return predicted_model
        except Exception as e:
            logging.error(f'Error predicting the Y values')
            raise e
    def accuracy_scores(self,predicted_model:np.ndarray,y_test_data:pd.DataFrame)->float:
        try:
            
            acc_score=float(accuracy_score(y_test_data,predicted_model))
            logging.error(f'Calculated the accuracy_score {acc_score}')
            return acc_score

        except Exception as e:
            logging.info(f'Err generating accuracy score :{e}')
            raise e
    def confustion_matrixs(self,predicted_model:np.ndarray,y_test_data)->Tuple[Annotated[int,'True_Positive'],Annotated[int,'True_Negative'],Annotated[int,'False_Positive'],Annotated[int,'False_Negative']]:
        try:
            
            matrix=confusion_matrix(y_test_data,predicted_model)
            logging.info(f'Calculated the confusion matrix {matrix}')
            True_Negative=int(matrix[0][0])
            True_Positive=int(matrix[1][1])
            False_Negative=int(matrix[1][0])
            False_Positive=int(matrix[0][1])
            return True_Positive,True_Negative,False_Positive,False_Negative
        except Exception as e:
            logging.error(f'Err generating confustion_matrix :{e}')
            raise e
    def classification_reports(self,predicted_model:np.ndarray,y_test_data)->str:
        try:
            reports=classification_report(y_test_data,predicted_model)
            logging.info(f'Successfully calculated the reports:{reports}')
            return reports

        except Exception as e:
            logging.error(f'Err generating classification_report :{e}')
            raise e