from sklearn.neighbors import KNeighborsRegressor
from train_model import bestHyper
from train_model import x_train, y_train, x_test, y_test
import pickle
from train_model import stampa, predictAndResults

class KNR:

    def trainKNR(self):
       
        knr = KNeighborsRegressor()
        param_grid = {
            'n_neighbors': list(range(5,10,1)),
            'metric' : ['euclidean', 'manhattan', 'chebyshev', 'minkowski']
                    }
        
        estimator, result = bestHyper(param_grid, x_train, y_train, knr)
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
        risultati = predictAndResults(model, x_test, y_test)
        stampa(risultati, "KNR")


knr = KNR()
best = knr.trainModel()
knr.testModel(best)
  
