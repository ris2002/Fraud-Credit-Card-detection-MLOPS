from task_functions.data_cleaning import model_cleaning
from task_functions.data_ingestion import ingest_data
from task_functions.model_evaluation import model_eval
from task_functions.model_training import train_model


def pipeline_training():
    df=ingest_data
    model_cleaning(df)
    train_model(df)
    model_eval(df)

