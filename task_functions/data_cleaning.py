from helper_functions.helper_cleaner import Pre_Process_Strategy
import logging
import pandas as pd
import numpy as np
from typing import Tuple
from typing_extensions import Annotated
import pickle


def model_cleaning(df:pd.DataFrame)->Tuple[Annotated[np.ndarray,'X_train'],Annotated[np.ndarray,'y_train'],Annotated[np.ndarray,'X_test'],Annotated[pd.DataFrame,'y_test']]:
    try:
        pre_process=Pre_Process_Strategy()
        X_train, X_test, y_train, y_test=pre_process.clean_and_preprocess(df)
        logging.info('Pre_Processing is done')
        with open ('config/data_pkl_files/x_train_data.pkl','wb') as f:
            pickle.dump(X_train,f)
        with open ('config/data_pkl_files/y_train_data.pkl','wb') as f:
            pickle.dump(y_train,f)
        with open ('config/data_pkl_files/x_test_data.pkl','wb') as f:
            pickle.dump(X_test,f)
        with open ('config/data_pkl_files/y_test_data.pkl','wb') as f:
            pickle.dump(y_test,f)
        
        return X_train, y_train, X_test, y_test
    except Exception as e:
        logging.error(f'Error in cleaning and pre pre-processing the data:{e}')
        raise e