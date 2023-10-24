import xgboost as xg
from train_model import bestHyper
from train_model import x_train, y_train, x_test, y_test
import pickle

class XGBooster:


    def trainXGBoost(self):
      
        xgb = xg.XGBRegressor(objective ='reg:squarederror')
        param_grid = {
            'learning_rate': [0.1,0.5,0.8,1],
            'max_depth': [2,5,10],
            'n_estimators' : [50,100]}
        estimator, result = bestHyper(param_grid, x_train, y_train, xgb)
        best_randomB = result.best_estimator_

        return  estimator, result
    

    def save_model(self, model):
        pickle.dump(model, open("models/xgb.pkl", "wb"))

    def trainModel(self):
        xgb = XGBooster()
        modello, _ = xgb.trainXGBoost()
        xgb.save_model(modello)

xgb = XGBooster()
xgb.trainModel()
        

