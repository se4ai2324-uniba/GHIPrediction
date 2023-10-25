from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import sys
import pandas as pd
import mlflow

sys.path.insert(0, "src/data")
import math


def use_split(csv1, csv2):
    train = pd.read_csv(f"data/interim/{csv1}.csv")
    test = pd.read_csv(f"data/interim/{csv2}.csv")
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

def gridLog(model_name, param_grid, x_train, y_train, model):
   best, cv_results = bestHyper(param_grid, x_train, y_train, model)
   with mlflow.start_run() as run:  
        mlflow.log_param("folds", cv_results.cv)

        print("Logging parameters")
        params = list(cv_results.param_grid.keys())
        for param in params:
            valori=[]
            for key,value in cv_results.param_grid.items():
              if key == param:
                 valori.append(value)
              for i in valori:
               print(i)
               mlflow.log_param(param, i)

        print("Logging metrics")
        for score_name in [score for score in cv_results if "mean_test" in score]:
            mlflow.log_metric(score_name, f"{score_name}")

        print("Logging model")        
        mlflow.sklearn.log_model(cv_results.best_estimator_, model_name)

        # print("Logging CV results matrix")
        # tempdir = tempfile.TemporaryDirectory().name
        # os.mkdir(tempdir)
        # timestamp = datetime.now().isoformat().split(".")[0].replace(":", ".")
        # filename = "%s-%s-cv_results.csv" % (model_name, timestamp)
        # csv = os.path.join(tempdir, filename)
        # with warnings.catch_warnings():
        #     warnings.simplefilter("ignore")
        #     pd.DataFrame(cv_results).to_csv(csv, index=False)
        
        #mlflow.log_artifact(csv, "cv_results")

        #res=predictAndResults(best, x_test, y_test)

        run_id = run.info.run_uuid
        experiment_id = run.info.experiment_id
        mlflow.end_run()
        print(mlflow.get_artifact_uri())
        print("runID: %s" % run_id)

        return best, cv_results