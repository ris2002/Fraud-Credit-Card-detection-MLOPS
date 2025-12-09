import logging
import numpy as np
import pandas as pd
from typing import Tuple
from typing_extensions import Annotated
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.decomposition import PCA
class Pre_Process_Strategy:
    def clean_and_preprocess(self,df:pd.DataFrame)->Tuple[Annotated[np.ndarray,'X_train'],Annotated[np.ndarray,'y_train'],Annotated[np.ndarray,'X_test'],Annotated[pd.DataFrame,'y_test']]:# after smote  y_train will become nd arrays
        try:
            df=df.drop_duplicates()
            # inplace=True means Modify the DataFrame directly instead of returning a new one.
            df = df.sample(frac=0.02, random_state=42) #AIRFLOW TESTING 
            X=df.drop(columns=['Time','Class'])
            Y=df['Class']
           
            scalar=StandardScaler()
            X_scaled=scalar.fit_transform(X)
            pca=PCA(n_components=10)#This keeps the first 2 principal components, meaning your data is reduced to 2 dimensions.If your dataset originally has:100 features → reduced to 10 features50 features → reduced to 10 features8 features → ❌ cannot use 10 components (max is 8)
            X_pca=pca.fit_transform(X_scaled)
            
            X_train, X_test, y_train, y_test=train_test_split(X_pca,Y,test_size=0.2,random_state=2)
            smote=SMOTE(random_state=431)
            X_train_resampled,y_train_resampled=smote.fit_resample(X_train,y_train)
            return X_train_resampled, y_train_resampled, X_test, y_test
        except Exception as e:
            logging.error(f'Error in the Pre_Process_Startegy:{e}')
            raise e
    def clean_annd_preprocess_deployment_data(self,df:pd.DataFrame)->None:#no need of cleaner function as the data from the deployment data is going to be cleaed and downnloaded to pickle files from the training and testig dataset itself
        pass
        




