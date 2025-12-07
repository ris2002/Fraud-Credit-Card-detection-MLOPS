from airflow.decorators import task,dag
import logging
from data_ingestion import ingest_data
from data_cleaning import model_cleaning
from datetime import timedelta
from model_training import train_model
from model_evaluation import model_eval

#default_args={"retries":2,"retry_delay":timedelta(minutes=5),"execution_timeout":timedelta(hours=1)}
@dag(dag_id='ml_training_pipeline_04', schedule='@once')
def run_training_pipeline():
    csv_path='/opt/airflow/Datasets/creditcard_2.csv'
    task_ingestion=ingest_data(csv_path)
    logging.info('Done ingesting the data')
    task_cleaning=model_cleaning()
    logging.info('Done cleaning the data')
    task_training=train_model()
    logging.info('Done trainingthe model')
    task_evaluation=model_eval()
    logging.info('Done evaluating the model')
    task_ingestion>>task_cleaning>>task_training>>task_evaluation


pipeline=run_training_pipeline()