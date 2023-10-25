import xgboost as xg
from train_model import bestHyper
import pickle
from train_model import  predictAndResults, stampa, use_split
import pandas as pd
import mlflow

class XGBooster:

    def trainXGBoost(self):
      
        xgb = xg.XGBRegressor(objective ='reg:squarederror')
        param_grid = {
            'learning_rate': [0.1,0.5,0.8,1],
            'max_depth': [2,5,10],
            'n_estimators' : [50,100]}
        x_train, y_train, _, _ = use_split('split_train', 'split_test')
        estimator, result = bestHyper(param_grid, x_train, y_train, xgb)
        best_randomB = result.best_estimator_

        return  estimator, result
    

    def save_model(self, model):
        pickle.dump(model, open("models/xgb.pkl", "wb"))

    def trainModel(self):
        xgb = XGBooster()
        modello, best  = xgb.trainXGBoost()
        xgb.save_model(modello)
        return best

    def testModel(self, model):
        _, _, x_test, y_test = use_split('split_train', 'split_test')
        risultati = predictAndResults(model, x_test, y_test)
        stampa(risultati, "XGBooster")


xgb = XGBooster()
best = xgb.trainModel()
xgb.testModel(best)

