
from sklearn.ensemble import RandomForestRegressor
from train_model import bestHyper, gridLog
import pickle
from train_model import stampa, predictAndResults, use_split, save_metrics

class RandomForest:

    def trainRandomForest(self):
      
        rf = RandomForestRegressor()
        param_grid = {
            'max_depth':  [4,5,6],
            'n_estimators' : list(range(100,160, 10))}
        x_train, y_train, x_test, _ = use_split('split_train', 'split_test')
        estimator, grid = bestHyper(param_grid, x_train, y_train, rf)
        result = self.testModel(estimator)
        self.save_model(estimator)
        gridLog("randomForestRegressor",rf, grid, result, x_test, estimator)
        save_metrics(result, 'randomForestRegressor')
        return result
    def save_model(self, model):
        pickle.dump(model, open("models/randomForestRegressor.pkl", "wb"))
    
    def testModel(self, model):
        _, _, x_test, y_test = use_split('split_train', 'split_test')
        risultati = predictAndResults(model, x_test, y_test)
        stampa(risultati, "RandomForest")
        return risultati


rf = RandomForest()
rf.trainRandomForest()