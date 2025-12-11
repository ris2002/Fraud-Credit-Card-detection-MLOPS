FROM python:3.11.0-slim
WORKDIR /app
COPY requirements.txt .
COPY deployment_folder /app/deployment_folder 
COPY config/data_pkl_files /app/config/data_pkl_files 
#The config folder holds all the model pkl files and data pkl files since it contains a lot of data it is gitignored

EXPOSE 8000
