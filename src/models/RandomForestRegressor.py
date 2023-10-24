
from sklearn.ensemble import RandomForestRegressor
from train_model import bestHyper
from train_model import x_train, y_train, x_test, y_test
import pickle
from train_model import stampa, predictAndResults

class RandomForest:

    def trainRandomForest(self):
      
        rf = RandomForestRegressor()
        param_grid = {
            'max_depth':  [4,5,6],
            'n_estimators' : list(range(100,160, 10))}
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
        risultati = predictAndResults(model, x_test, y_test)
        stampa(risultati, "RandomForest")


rf = RandomForest()
best = rf.trainModel()
rf.testModel(best)