"""module containing testing functions for traning module"""
import sys
import pytest
import numpy as np
import pandas as pd
import xgboost as xg
sys.path.insert(0, "src/models/")
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from train_model import use_split, best_hyper

@pytest.fixture
def testing_use_split():
    return use_split('split_train', 'split_test')

def test_knr(testing_use_split):
    """testing function for knr model"""
    knr = KNeighborsRegressor()
    param_grid = {
        'n_neighbors': list(range(5,10,1)),
        'metric' : ['euclidean', 'manhattan', 'chebyshev', 'minkowski']
        }
    
    x_train, y_train, _, _ = testing_use_split

    best_estimator, result, n_split = best_hyper(param_grid, x_train, y_train, knr)
    assert best_estimator is not None
    assert result is not None
    assert n_split == 10


def test_xgb(testing_use_split):
    """testing function for xgb model"""
    xgb = xg.XGBRegressor(objective ='reg:squarederror')
    param_grid = {
        'learning_rate': [0.1,0.5,0.8,1],
        'max_depth': [2,5,10],
        'n_estimators' : [50,100]}

    x_train, y_train, _, _ = testing_use_split
    best_estimator, result, n_split = best_hyper(param_grid, x_train, y_train, xgb)
    assert best_estimator is not None
    assert result is not None
    assert n_split == 10

def test_rf(testing_use_split):
    """testing function for rf model"""
    rf = RandomForestRegressor()
    param_grid = {
        'max_depth':  [4,5,6],
        'n_estimators' : list(range(100,160, 10))}
    x_train, y_train, _, _ = testing_use_split
    best_estimator, result, n_split = best_hyper(param_grid, x_train, y_train, rf)
    assert best_estimator is not None
    assert result is not None
    assert n_split == 10
