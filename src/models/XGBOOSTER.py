"""module to implement training for xgbooster"""
import xgboost as xg
from .train_model import best_hyper, grid_log
from .train_model import predict_and_results, stampa, use_split, save_metrics, save_model

def train_xgbooster():
    """function to train the model"""
    xgb = xg.XGBRegressor(objective ='reg:squarederror')
    param_grid = {
        'learning_rate': [0.1,0.5,0.8,1],
        'max_depth': [2,5,10],
        'n_estimators' : [50,100]}
    x_train, y_train, x_test, _ = use_split('split_train', 'split_test')
    estimator, grid = best_hyper(param_grid, x_train, y_train, xgb)
    result = test_model(estimator)
    save_model(estimator, 'xgb')
    grid_log("xgb", xgb, grid, result, x_test)
    save_metrics(result, 'xgb')
    return  result


def test_model(model):
    """function to test the model"""
    _, _, x_test, y_test = use_split('split_train', 'split_test')
    risultati = predict_and_results(model, x_test, y_test)
    stampa(risultati, "XGBooster")
    return risultati

train_xgbooster()
