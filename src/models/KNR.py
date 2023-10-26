from sklearn.neighbors import KNeighborsRegressor
from train_model import bestHyper, gridLog
import pickle
from train_model import stampa, predictAndResults, use_split
import pandas as pd

class KNR:

    def trainKNR(self):
       
        knr = KNeighborsRegressor()
        param_grid = {
            'n_neighbors': list(range(5,10,1)),
            'metric' : ['euclidean', 'manhattan', 'chebyshev', 'minkowski']
                    }
        
        x_train, y_train, x_test, _ = use_split('split_train', 'split_test')
        estimator, grid = bestHyper(param_grid, x_train, y_train, knr)
        result=self.testModel(estimator)
        self.save_model(estimator)
        gridLog("knr", knr, grid, result, x_test, estimator)
        #best_random = grid.best_estimator_

        return estimator, result
    
    def save_model(self, model):
        pickle.dump(model, open("models/knr.pkl", "wb"))

    def testModel(self, model):
        _, _, x_test, y_test = use_split('split_train', 'split_test')
        risultati = predictAndResults(model, x_test, y_test)
        stampa(risultati, "KNR")
        return risultati


knr = KNR()
knr.trainKNR()

  
