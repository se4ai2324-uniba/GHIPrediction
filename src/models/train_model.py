from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import sys
import pandas as pd
import mlflow
from mlflow.models import infer_signature
import xgboost as xg

sys.path.insert(0, "src/data")
import math


def use_split(csv1, csv2):
    train = pd.read_csv(f"data/interim/{csv1}.csv")
    test = pd.read_csv(f"data/interim/{csv2}.csv")
    train = train.rename(columns={'0':'Temperature', '1':'DNI', '2': 'Humidity'})
    test = test.rename(columns={'0':'Temperature', '1':'DNI', '2': 'Humidity'})
    x_train = train.iloc[:, :3]
    y_train = train.iloc[:, 3]
    x_test = test.iloc[:, :3]
    y_test = test.iloc[:, 3]

    return x_train, y_train, x_test, y_test

def bestHyper(param_grid, x_train, y_train, model):
  search = GridSearchCV(model, param_grid, cv = 10, scoring='neg_root_mean_squared_error')
  result = search.fit(x_train, y_train)
  mean =  result.cv_results_['mean_test_score']
  params = result.cv_results_['params']
  print('Best Score: %s' % result.best_score_)
  print('Best Hyperparameters: %s' % result.best_params_)
  print(" ")
  return result.best_estimator_, result


#TODO nel predict
def predictAndResults(best, x_test, y_test):
  pred = best.predict(x_test)
  result = metrics(y_test, pred)
  return result
    

def metrics(test, prediction):
  result = []
  result.append(r2_score(test, prediction))
  result.append(math.sqrt(mean_squared_error(test, prediction)))
  return result

def stampa(arr, name):
  print("The result of prediction on x_test of " + name + " are:")
  print("Root Mean Squared Error: ", arr[1])
  print("R2: ", arr[0])

def gridLog(modelName, model, grid, result, x_test, best):
  mlflow.set_tracking_uri("http://127.0.0.1:5000")

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
    "pip": ["mlflow==2.3", "scikit-learn==0.23.2", "cloudpickle==1.6.0", f"xgboost=={xg.__version__}"],
    "name": "mlflow-env",
    }

    signature = infer_signature(x_test, best.predict(x_test))
    if isinstance(model, xg.XGBRegressor):
      mlflow.xgboost.log_model(xgb_model=best, artifact_path="models", conda_env=conda_env, signature=signature)  
    else:
      mlflow.sklearn.log_model(sk_model=best, artifact_path="models", conda_env=conda_env, signature=signature)  
    mlflow.log_artifact(f"models/{modelName}.pkl")
    mlflow.end_run()
  