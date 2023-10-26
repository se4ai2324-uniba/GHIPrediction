from sklearn.neighbors import KNeighborsRegressor
from train_model import bestHyper, gridLog, save_metrics, save_model
import pickle
from train_model import stampa, predictAndResults, use_split


class KNR:

    def trainKNR(self):
       
        knr = KNeighborsRegressor()
        param_grid = {
            'n_neighbors': list(range(5,10,1)),
            'metric' : ['euclidean', 'manhattan', 'chebyshev', 'minkowski']
                    }
        
        x_train, y_train, x_test, y_test = use_split('split_train', 'split_test')
        estimator, grid = bestHyper(param_grid, x_train, y_train, knr)
        result=self.testModel(estimator)
        save_model(estimator, 'knr')
        gridLog("knr", knr, grid, result, x_test, estimator)
        save_metrics(result, 'knr')
        #best_random = grid.best_estimator_

        return result

    def testModel(self, model):
        _, _, x_test, y_test = use_split('split_train', 'split_test')
        risultati = predictAndResults(model, x_test, y_test)
        stampa(risultati, "KNR")
        return risultati


knr = KNR()
knr.trainKNR()


  
