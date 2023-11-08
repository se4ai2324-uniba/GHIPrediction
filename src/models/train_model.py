"""module to implemen utility functions for training and testing"""
import sys
import pickle
import math
import dagshub
import mlflow
import pandas as pd
import xgboost as xg
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score, mean_squared_error
from mlflow.models import infer_signature

sys.path.insert(0, "src/data")

def save_metrics(results, file_name):
    """function to save the metrics"""
    with open(f"models/{file_name}.metrics", 'w', encoding='utf-8') as fd:
        fd.write(str(results[0]))
        fd.write("\n")
        fd.write(str(results[1]))

def save_model(model, name):
    """function to save the model"""
    pickle.dump(model, open(f"models/{name}.pkl", "wb"))

def use_split(csv1, csv2):
    """function to split data"""
    train = pd.read_csv(f"data/interim/{csv1}.csv")
    test = pd.read_csv(f"data/interim/{csv2}.csv")
    train = train.rename(columns={'0':'Temperature', '1':'DNI', '2': 'Humidity'})
    test = test.rename(columns={'0':'Temperature', '1':'DNI', '2': 'Humidity'})
    x_train = train.iloc[:, :3]
    y_train = train.iloc[:, 3]
    x_test = test.iloc[:, :3]
    y_test = test.iloc[:, 3]

    return x_train, y_train, x_test, y_test

def best_hyper(param_grid, x_train, y_train, model):
    """function to get best hyperparameters"""
    search = GridSearchCV(model, param_grid, cv = 10, scoring='neg_root_mean_squared_error')
    result = search.fit(x_train, y_train)
    print(f'Best Score: {result.best_score_} ')
    print(f'Best Hyperparameters: {result.best_params_}')
    print(" ")
    return result.best_estimator_, result, search.n_splits_

def predict_and_results(best, x_test, y_test):
    """function to predict and see results"""
    pred = best.predict(x_test)
    result = metrics(y_test, pred)
    return result

def metrics(test, prediction):
    """function to get metrics results"""
    result = []
    result.append(r2_score(test, prediction))
    result.append(math.sqrt(mean_squared_error(test, prediction)))
    return result

def stampa(arr, name):
    """function to print metrics"""
    print("The result of prediction on x_test of " + name + " are:")
    print("Root Mean Squared Error: ", arr[1])
    print("R2: ", arr[0])

def grid_log(model_name, model, grid, result, x_test):
    """function to print gridserachcv results"""
    dagshub.init(repo_owner='se4ai2324-uniba', repo_name='GHIPrediction', mlflow=True)
    mlflow.set_tracking_uri("https://dagshub.com/se4ai2324-uniba/GHIPrediction.mlflow")

    with mlflow.start_run() as run:
        mlflow.log_param("folds", grid.cv)
        print("Logging parameters")
        params = grid.best_params_
        for key,value in params.items():
            mlflow.log_param(key, value)
        print("Logging metrics")
        mlflow.log_metric("R2", f"{result[0]}")
        mlflow.log_metric("RMSE", f"{result[1]}")
        print("Logging model")
        conda_env = {
        "channels": ["conda-forge"],
        "dependencies": ["python=3.8.8", "pip"],
        "pip": ["mlflow==2.3", "scikit-learn==0.23.2", "cloudpickle==1.6.0",
        f"xgboost=={xg.__version__}"],
        "name": "mlflow-env",
        }
        signature = infer_signature(x_test, grid.best_estimator_.predict(x_test))
        if isinstance(model, xg.XGBRegressor):
            mlflow.xgboost.log_model(xgb_model=grid.best_estimator_, artifact_path="models",
            conda_env=conda_env, signature=signature)
        else:
            mlflow.sklearn.log_model(sk_model=grid.best_estimator_, artifact_path="models",
            conda_env=conda_env, signature=signature)
        mlflow.log_artifact(f"models/{model_name}.pkl")
        mlflow.end_run()
  