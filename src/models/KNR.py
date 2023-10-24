from sklearn.neighbors import KNeighborsRegressor
from train_model import bestHyper
from train_model import x_train, y_train
import pickle

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
        xgb = KNR()
        modello, _ = xgb.trainKNR()
        xgb.save_model(modello)


knr = KNR()
knr.trainModel()