
from sklearn.ensemble import RandomForestRegressor
from train_model import bestHyper
import pickle
from train_model import stampa, predictAndResults, use_split
import pandas as pd
import mlflow

class RandomForest:

    def trainRandomForest(self):
      
        rf = RandomForestRegressor()
        param_grid = {
            'max_depth':  [4,5,6],
            'n_estimators' : list(range(100,160, 10))}
        x_train, y_train, _, _ = use_split('split_train', 'split_test')
        estimator, result = bestHyper(param_grid, x_train, y_train, rf)
        best_randomB = result.best_estimator_

        return estimator, best_randomB
    def save_model(self, model):
        pickle.dump(model, open("models/randomForest.pkl", "wb"))

    def trainModel(self):
        rf = RandomForest()
        modello, best = rf.trainRandomForest()
        rf.save_model(modello)
        return best
    
    def testModel(self, model):
        _, _, x_test, y_test = use_split('split_train', 'split_test')
        risultati = predictAndResults(model, x_test, y_test)
        stampa(risultati, "RandomForest")


rf = RandomForest()
best = rf.trainModel()
rf.testModel(best)