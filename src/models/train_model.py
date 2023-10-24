from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import sys
sys.path.insert(0, "src/data")
from split_dataset import Split
import math


obj = Split()

ox = obj.getTrain()

x_train, x_test, y_train, y_test = ox



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
  result.append(mean_absolute_error(test, prediction))
  print(result)
  return result

