import pandas as pd
import sys
import numpy as np
sys.path.insert(0, "src/models/")
from train_model import best_hyper
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
import xgboost as xg

def test_knr():
    krn = KNeighborsRegressor()
    param_grid = {
        'n_neighbors': list(range(5,10,1)),
        'metric' : ['euclidean', 'manhattan', 'chebyshev', 'minkowski']
        }
    head = ['Temperature', 'DNI', 'Humidity']

    x_train = np.array([[0.5205, 0.0732, 0.8231],
               [0.5205, 0.0732, 0.8231],
               [0.5205, 0.0732, 0.8231],
               [0.5205, 0.0732, 0.8231],
               [0.5205, 0.0732, 0.8231],
               [0.5205, 0.0732, 0.8231],
               [0.5205, 0.0732, 0.8231],
               [0.5205, 0.0732, 0.8231],
               [0.5205, 0.0732, 0.8231],
               [0.5205, 0.0732, 0.8231]])
    y_train = np.array([[448],
               [448],
               [448],
               [448],
               [448],
               [448],
               [448],
               [448],
               [448],
               [448]])

    x_train = pd.DataFrame(x_train, columns=head)
    y_train = pd.DataFrame(x_train)
   

    best_estimator, result, n_split = best_hyper(param_grid, x_train, y_train, krn)
    assert best_estimator is not None
    assert result is not None
    assert n_split == 10


def test_xgb():
    xgb = xg.XGBRegressor(objective ='reg:squarederror')
    param_grid = {
        'learning_rate': [0.1,0.5,0.8,1],
        'max_depth': [2,5,10],
        'n_estimators' : [50,100]}
    head = ['Temperature', 'DNI', 'Humidity']

    x_train = np.array([[0.5205, 0.0732, 0.8231],
               [0.5205, 0.0732, 0.8231],
               [0.5205, 0.0732, 0.8231],
               [0.5205, 0.0732, 0.8231],
               [0.5205, 0.0732, 0.8231],
               [0.5205, 0.0732, 0.8231],
               [0.5205, 0.0732, 0.8231],
               [0.5205, 0.0732, 0.8231],
               [0.5205, 0.0732, 0.8231],
               [0.5205, 0.0732, 0.8231]])
    y_train = np.array([[448],
               [448],
               [448],
               [448],
               [448],
               [448],
               [448],
               [448],
               [448],
               [448]])

    x_train = pd.DataFrame(x_train, columns=head)
    y_train = pd.DataFrame(x_train)
   

    best_estimator, result, n_split = best_hyper(param_grid, x_train, y_train, xgb)
    assert best_estimator is not None
    assert result is not None
    assert n_split == 10

def test_rf():
    rf = RandomForestRegressor()
    param_grid = {
        'max_depth':  [4,5,6],
        'n_estimators' : list(range(100,160, 10))}
    
    head = ['Temperature', 'DNI', 'Humidity']

    x_train = np.array([[0.5205, 0.0732, 0.8231],
               [0.5205, 0.0732, 0.8231],
               [0.5205, 0.0732, 0.8231],
               [0.5205, 0.0732, 0.8231],
               [0.5205, 0.0732, 0.8231],
               [0.5205, 0.0732, 0.8231],
               [0.5205, 0.0732, 0.8231],
               [0.5205, 0.0732, 0.8231],
               [0.5205, 0.0732, 0.8231],
               [0.5205, 0.0732, 0.8231]])
    y_train = np.array([[448],
               [448],
               [448],
               [448],
               [448],
               [448],
               [448],
               [448],
               [448],
               [448]])

    x_train = pd.DataFrame(x_train, columns=head)
    y_train = pd.DataFrame(x_train)
   

    best_estimator, result, n_split = best_hyper(param_grid, x_train, y_train, rf)
    assert best_estimator is not None
    assert result is not None
    assert n_split == 10