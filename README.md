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
