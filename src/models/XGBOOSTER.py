"""module to implement training for xgbooster"""
import pandas as pd
import xgboost as xg
import csv
from train_model import best_hyper, grid_log
from train_model import predict_and_results, stampa, use_split, save_metrics, save_model

def train_xgbooster():
    """function to train the model"""
    xgb = xg.XGBRegressor(objective ='reg:squarederror')
    param_grid = {
        'learning_rate': [0.1,0.5,0.8,1],
        'max_depth': [2,5,10],
        'n_estimators' : [50,100]}
    x_train, y_train, x_test, _ = use_split('split_train', 'split_test')
    estimator, grid, _= best_hyper(param_grid, x_train, y_train, xgb)
    result = test_model(estimator)
    save_model(estimator, 'xgb')
    grid_log("xgb", xgb, grid, result, x_test)
    save_metrics(result, 'xgb')
    write_params(grid.best_params_)
    return  result

def test_model(model):
    """function to test the model"""
    _, _, x_test, y_test = use_split('split_train', 'split_test')
    risultati = predict_and_results(model, x_test, y_test)
    stampa(risultati, "XGBooster")
    return risultati

def write_params(dati_dict):
    df = pd.DataFrame([dati_dict])
    nome_file_csv = 'src/models/params/xgb_params.csv'
    df.to_csv(nome_file_csv, index=False)

train_xgbooster()
