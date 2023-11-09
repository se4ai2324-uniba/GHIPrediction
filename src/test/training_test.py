"""module containing testing functions for traning module"""
import sys
import pytest
import numpy as np
import pandas as pd
import xgboost as xg
sys.path.insert(0, "src/models/")
from train_model import best_hyper
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from train_model import save_model, stampa, predict_and_results, use_split
from knr import test_model

@pytest.fixture
def testing_test_model():
    return test_model

def test_knr():
    """testing function for knr model"""
    knr = KNeighborsRegressor()
    param_grid = {
        'n_neighbors': list(range(5,10,1)),
        'metric' : ['euclidean', 'manhattan', 'chebyshev', 'minkowski']
        }
    head = ['Temperature', 'DNI', 'Humidity']
    
    x_train, y_train, x_test, _ = use_split('split_train', 'split_test')
    # x_train = pd.DataFrame(x_train, columns=head)
    # y_train = pd.DataFrame(x_train)
    estimator, grid, _ = best_hyper(param_grid, x_train, y_train, knr)
    result= test_model(estimator)
    #save_model(estimator, 'knr')
    #grid_log("knr", knr, grid, result, x_test)
    #save_metrics(result, 'knr')

    best_estimator, result, n_split = best_hyper(param_grid, x_train, y_train, krn)
    assert best_estimator is not None
    assert result is not None
    assert n_split == 10


# def test_xgb():
#     """testing function for xgb model"""
#     xgb = xg.XGBRegressor(objective ='reg:squarederror')
#     param_grid = {
#         'learning_rate': [0.1,0.5,0.8,1],
#         'max_depth': [2,5,10],
#         'n_estimators' : [50,100]}
#     head = ['Temperature', 'DNI', 'Humidity']

#     x_train = np.array([[0.5205, 0.0732, 0.8231],
#                [0.5205, 0.0732, 0.8231],
#                [0.5205, 0.0732, 0.8231],
#                [0.5205, 0.0732, 0.8231],
#                [0.5205, 0.0732, 0.8231],
#                [0.5205, 0.0732, 0.8231],
#                [0.5205, 0.0732, 0.8231],
#                [0.5205, 0.0732, 0.8231],
#                [0.5205, 0.0732, 0.8231],
#                [0.5205, 0.0732, 0.8231]])
#     y_train = np.array([[448],
#                [448],
#                [448],
#                [448],
#                [448],
#                [448],
#                [448],
#                [448],
#                [448],
#                [448]])

#     x_train = pd.DataFrame(x_train, columns=head)
#     y_train = pd.DataFrame(x_train)
#     best_estimator, result, n_split = best_hyper(param_grid, x_train, y_train, xgb)
#     assert best_estimator is not None
#     assert result is not None
#     assert n_split == 10

# def test_rf():
#     """testing function for rf model"""
#     rf = RandomForestRegressor()
#     param_grid = {
#         'max_depth':  [4,5,6],
#         'n_estimators' : list(range(100,160, 10))}
#     head = ['Temperature', 'DNI', 'Humidity']
#     x_train = np.array([[0.5205, 0.0732, 0.8231],
#                [0.5205, 0.0732, 0.8231],
#                [0.5205, 0.0732, 0.8231],
#                [0.5205, 0.0732, 0.8231],
#                [0.5205, 0.0732, 0.8231],
#                [0.5205, 0.0732, 0.8231],
#                [0.5205, 0.0732, 0.8231],
#                [0.5205, 0.0732, 0.8231],
#                [0.5205, 0.0732, 0.8231],
#                [0.5205, 0.0732, 0.8231]])
#     y_train = np.array([[448],
#                [448],
#                [448],
#                [448],
#                [448],
#                [448],
#                [448],
#                [448],
#                [448],
#                [448]])

#     x_train = pd.DataFrame(x_train, columns=head)
#     y_train = pd.DataFrame(x_train)
#     best_estimator, result, n_split = best_hyper(param_grid, x_train, y_train, rf)
#     assert best_estimator is not None
#     assert result is not None
#     assert n_split == 10
