# ML_Track_MLFlow_2

#### create a requirements.txt file and write mlflow,xgboost,scikit-learn,jupyter,pandas,hyperopt,seaborn,and xgboost

#### converted parquet to csv for easy processing

#### in notebook created basic preprocessing nd saved the model in notebook_model

#### create a new directory for MLFlow Experiment

#### inside mlflow_experiment create first file [mlflow_tracking_1.py](mlflow_experiment%2Fmlflow_tracking_1.py)
#### initially you can run mlflow in local like "**mlflow -ui**" but it will throw an error because we did not set any database to store all artifacts and all.
![img.png](img%2Fimg.png)

#### another way is **mlflow is mlflow ui --backend-store-uri sqlite:///mlflow.db**
![img_1.png](img%2Fimg_1.png)

#### now in [mlflow_tracking_1.py](mlflow_experiment%2Fmlflow_tracking_1.py) : import mlflow and set tracking uri as http://127.0.0.1:5000
#### 
