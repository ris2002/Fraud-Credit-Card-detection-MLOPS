import logging
from airflow.decorators import task
import pandas as pd
import os

@task
class Ingest_Data:
    def ingest_data_from_kaggle(self,dataset_path)->pd.DataFrame:
        try:
           df=pd.read_csv(dataset_path)
           
           
           logging.info('Data converted PD')
           return df
        except Exception as e:
            logging.error(f'Error loading csv _file{e}')
            raise e

        



def ingest_data(dataset_path)->pd.DataFrame:
    ingestion=Ingest_Data()
    df=ingestion.ingest_data_from_kaggle(dataset_path)
    logging.info('Data ingestion done')
    return df




        