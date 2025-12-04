from task_functions.data_cleaning import model_cleaning
from task_functions.data_ingestion import ingest_data
from task_functions.model_evaluation import model_eval
from task_functions.model_training import train_model


def pipeline_training(data_set_path):
    df=ingest_data(data_set_path)
    
    X_train,y_train, X_test, y_test=model_cleaning(df)
    model=train_model(X_train,y_train)
    model_eval(model,X_test,y_test)

