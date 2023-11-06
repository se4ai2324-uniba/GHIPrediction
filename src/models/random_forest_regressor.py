
"""module to implement training for random forest regressor"""
from sklearn.ensemble import RandomForestRegressor
from .train_model import best_hyper, grid_log
from .train_model import stampa, predict_and_results
from .train_model import use_split, save_metrics, save_model

def train_random_forest():
    """function to train the model"""
    rf = RandomForestRegressor()
    param_grid = {
        'max_depth':  [4,5,6],
        'n_estimators' : list(range(100,160, 10))}
    x_train, y_train, x_test, _ = use_split('split_train', 'split_test')
    estimator, grid = bestHyper(param_grid, x_train, y_train, rf)
    result = test_model(estimator)
    save_model(estimator, 'randomForestRegressor')
    grid_log("randomForestRegressor",rf, grid, result, x_test)
    save_metrics(result, 'randomForestRegressor')
    return result

def test_model(model):
    """function to test the model"""
    _, _, x_test, y_test = use_split('split_train', 'split_test')
    risultati = predict_and_results(model, x_test, y_test)
    stampa(risultati, "RandomForest")
    return risultati

train_random_forest()
