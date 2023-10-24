from sklearn.neighbors import KNeighborsRegressor
from train_model import bestHyper
from train_model import x_train, y_train

class KNR:

    def trainKNR(self):
       
        knr = KNeighborsRegressor()
        param_grid = {
            'n_neighbors': list(range(5,10,1)),
            'metric' : ['euclidean', 'manhattan', 'chebyshev', 'minkowski']
                    }
        
        result = bestHyper(param_grid, x_train, y_train, knr)
        best_randomB = result.best_estimator_

        return best_randomB


knr = KNR()
knr.trainKNR()