from airflow.decorators import task,dag
import logging
from data_ingestion import ingest_data
from data_cleaning import model_cleaning


@dag
def run_training_pipeline():
    csv_path='/opt/airflow/Datasets/creditcard_2.csv'
    task_ingestion=ingest_data(csv_path)
    task_cleaning=model_cleaning(task_ingestion)
    task_ingestion>>task_cleaning


pipeline=run_training_pipeline()