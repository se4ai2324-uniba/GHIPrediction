from sklearn.neighbors import KNeighborsRegressor
from train_model import gridLog
import pickle
from train_model import stampa, predictAndResults, use_split
import pandas as pd
import mlflow

class KNR:

    def trainKNR(self):
        knr = KNeighborsRegressor()
        param_grid = {
            'n_neighbors': list(range(5,10,1)),
            'metric' : ['euclidean', 'manhattan', 'chebyshev', 'minkowski']
                    }
        
        x_train, y_train, _, _ = use_split('split_train', 'split_test')
        estimator, result = gridLog('KNR', param_grid, x_train, y_train, knr)
        best_randomB = result.best_estimator_

        return estimator, best_randomB
    
    def save_model(self, model):
        pickle.dump(model, open("models/knr.pkl", "wb"))

    def trainModel(self):
        knr = KNR()
        modello, best = knr.trainKNR()
        knr.save_model(modello)
        return best

    def testModel(self, model):
        _, _, x_test, y_test = use_split('split_train', 'split_test')
        risultati = predictAndResults(model, x_test, y_test)
        stampa(risultati, "KNR")

knr = KNR()
best = knr.trainModel()
knr.testModel(best)
