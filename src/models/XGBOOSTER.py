import xgboost as xg
from train_model import bestHyper, gridLog
import pickle
from train_model import  predictAndResults, stampa, use_split, save_metrics, save_model

class XGBooster:

    def trainXGBoost(self):
      
        xgb = xg.XGBRegressor(objective ='reg:squarederror')
        param_grid = {
            'learning_rate': [0.1,0.5,0.8,1],
            'max_depth': [2,5,10],
            'n_estimators' : [50,100]}
        x_train, y_train, x_test, _ = use_split('split_train', 'split_test')
        estimator, grid = bestHyper(param_grid, x_train, y_train, xgb)
        result = self.testModel(estimator)
        save_model(estimator, 'xgb')
        gridLog("xgb", xgb, grid, result, x_test, estimator)
        save_metrics(result, 'xgb')
        return  result
    

    def testModel(self, model):
        _, _, x_test, y_test = use_split('split_train', 'split_test')
        risultati = predictAndResults(model, x_test, y_test)
        stampa(risultati, "XGBooster")
        return risultati

xgb = XGBooster()
xgb.trainXGBoost()

