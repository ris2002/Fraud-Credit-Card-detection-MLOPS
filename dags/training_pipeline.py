from airflow.decorators import task,dag
import logging
from data_ingestion import ingest_data
from data_cleaning import model_cleaning
from datetime import timedelta

#default_args={"retries":2,"retry_delay":timedelta(minutes=5),"execution_timeout":timedelta(hours=1)}
@dag(dag_id='ml_training_pipeline_04', schedule='@once')
def run_training_pipeline():
    csv_path='/opt/airflow/Datasets/creditcard_2.csv'
    task_ingestion=ingest_data(csv_path)
    task_cleaning=model_cleaning()
    task_ingestion>>task_cleaning


pipeline=run_training_pipeline()