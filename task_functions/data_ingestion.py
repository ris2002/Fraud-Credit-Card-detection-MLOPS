import logging
import kagglehub
import pandas as pd
from dotenv import load_dotenv
import os
from kaggle import KaggleApi

load_dotenv()
os.environ['KAGGLE_USERNAME'] = os.getenv('KAGGLE_USERNAME')
os.environ['KAGGLE_KEY'] = os.getenv('KAGGLE_KEY')
api=KaggleApi()
api.authenticate()
dataset_ref = "mczielinski/creditcardfraud"
cache_path = "./data/creditcard.csv"
if not os.path.exists(cache_path):
    print("Downloading dataset...")
    api.dataset_download_files(dataset_ref, path="./data", unzip=True)
else:
    print("Using cached dataset...")
class Ingest_Data:
    def ingest_data_from_kaggle(self,cache_path)->pd.DataFrame:
        try:
           df=pd.read_csv(cache_path)
           return df
        except Exception as e:
            logging.error(f'Error loading csv _file{e}')
            raise e

        



def ingest_data()->pd.DataFrame:
    ingestion=Ingest_Data()
    df=ingestion.ingest_data_from_kaggle(cache_path)
    logging.info('Data ingestion done')
    return df




        