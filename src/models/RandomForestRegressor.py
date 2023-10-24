
from sklearn.ensemble import RandomForestRegressor
from train_model import bestHyper
from train_model import x_train, y_train

class RandomForest:

    def trainRandomForest(self):
      
        rf = RandomForestRegressor()
        param_grid = {
            'max_depth':  [4,5,6],
            'n_estimators' : list(range(100,160, 10))}
        result = bestHyper(param_grid, x_train, y_train, rf)
        best_randomB = result.best_estimator_

        return best_randomB


rf = RandomForest()
rf.trainRandomForest()