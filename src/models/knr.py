"""module to implement training for k-nearest regressor"""
import csv
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
import joblib
from sklearn.preprocessing import RobustScaler
from train_model import best_hyper, grid_log, save_metrics
from train_model import save_model, stampa, predict_and_results, use_split
from codecarbon import EmissionsTracker

def train_knr():
    """function to train the model"""
    knr = KNeighborsRegressor()
    param_grid = {
        'n_neighbors': list(range(5,10,1)),
        'metric' : ['euclidean', 'manhattan', 'chebyshev', 'minkowski']
        }
    x_train, y_train, x_test, _ = use_split('split_train', 'split_test')
    estimator, grid, _ = best_hyper(param_grid, x_train, y_train, knr)
    result=test_model(estimator)
    save_model(estimator, 'knr')
    grid_log("knr", knr, grid, result, x_test)
    save_metrics(result, 'knr')
    write_params(grid.best_params_)
    return result

def test_model(model):
    """function to test the model"""
    _, _, x_test, y_test = use_split('split_train', 'split_test')
    risultati = predict_and_results(model, x_test, y_test)
    stampa(risultati, "KNR")
    return risultati

def write_params(dati_dict):
    df = pd.DataFrame([dati_dict])
    nome_file_csv = 'src/models/params/knr_params.csv'
    df.to_csv(nome_file_csv, index=False)

tracker=EmissionsTracker(output_dir="reports\codecarbon", output_file="knr_emissions.csv")
tracker.start()
train_knr()
tracker.stop()
