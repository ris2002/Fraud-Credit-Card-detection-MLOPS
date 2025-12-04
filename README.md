# Fraud-Credit-Card-detection-MLOPS
Some architectural ideas and workflow patterns are adapted from my earlier project:
E-mail Spam Detection — MLOps-(Link: https://github.com/ris2002/E-mail-Spam-MLOPS-.git).
## Different thinngs to be done wrt to my 3rd Project
* Involving a feature store.
* In previous project I have construted pipeline immediately. This thimee I am going run the project without pipeline first and only after that I am going to create DAGS and Tasks.
* Usage of terraform
* Usage of config maps, secrets ,and  ingress in Kubernetes(K8S)


## SMOTE Synthetic Minority Oversampling Technique
* This method is used only for categorical techniques when have numical values as its data
* It is used when in a dataset there are imbalened classes.
* It creates synthetic data to balence the majority class.
* what it does is it takes onne minority class, then it also pics its neighbour and using those 2 it creates a synthetic class


## DVC
pip install dvc
git add .
git commit -m "Initialize DVC"
dvc add data/ here data is the folder name
git add data.dvc .gitignore
git commit -m "Track dataset with DVC"
Now that folder is not tracked by git but by dvc cacche. data.dvc is going to be stored in git
DVC (Data Version Control) is an open-source tool designed to manage large datasets, machine-learning models, experiments, and pipelines. It works alongside Git but handles the things Git cannot, such as big files, data updates, reproducible pipelines, and shared storage.
## Feature Stores


## Extra enhancements to my airflow
beyond the basic '@dag(dag_id='ml_training_pipeline_04', schedule='@once')' I have added anothher arg that is  default_args={
        "retries": 3,
        "retry_delay": timedelta(minutes=5),
        "execution_timeout": timedelta(hours=1),
    } basically- 'retries' means each task can retry 3 times if it fails,'retry_delay' means it gives 5 min gap in btw failing and retrying again,execution_timeout- means if the dag doesnt complete within 1 hr airflow kills it.

IT IS BEST PRACTICE TO AVOID INSTALLING FAST API AND UVICORN INSIDE AIRFLOW
I have done one mistake in 3rd project. In the DAG of that project I have returned the the csv_file converted to pandas annd gave it as an input to thhe nnext step. It worked in that project because thhe data set is small. The optimal way is to store it inn a pkl file and read thhe contnnats directly whhen in thhe function which uses it.
Do not return a value from a function, this is because if the value is large the dag will fail