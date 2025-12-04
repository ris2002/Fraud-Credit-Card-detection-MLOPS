import logging
from airflow.decorators import task
import pandas as pd
import os
import pickle


class Ingest_Data:
    def ingest_data_(self,dataset_path)->pd.DataFrame:
        try:
           df=pd.read_csv(dataset_path)
           
           
           logging.info('Data converted PD')
           return df
        except Exception as e:
            logging.error(f'Error loading csv _file{e}')
            raise e

        



@task
def ingest_data(dataset_path)->pd.DataFrame:
    ingestion=Ingest_Data()
    df=ingestion.ingest_data_(dataset_path)
    with open ('/opt/airflow/config/Ingested_Data/ingested_data.pkl','wb') as f:
        pickle.dump(df,f)
    logging.info('Data ingestion done')
   




        