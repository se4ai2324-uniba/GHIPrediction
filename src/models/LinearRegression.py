from sklearn import linear_model
from sklearn.model_selection import cross_val_score
from train_model import predictAndResults
import pickle
from train_model import stampa, predictAndResults, use_split, save_metrics, save_model
import mlflow
from mlflow.models import infer_signature
import dagshub
class Linear:

    def trainLinear(self):
        lr = linear_model.LinearRegression()
        x_train, y_train, x_test, _ = use_split('split_train', 'split_test')
        folds = 10
        linear = cross_val_score(lr, x_train, y_train, scoring = 'neg_root_mean_squared_error' ,cv = folds)
        #model può essere utile se si vuole stampare i valori, e quindi calcolare la media, della cross validation
        model = lr.fit(x_train, y_train)
        dagshub.init(repo_owner='se4ai2324-uniba', repo_name='GHIPrediction', mlflow=True)
        mlflow.set_tracking_uri("https://dagshub.com/se4ai2324-uniba/GHIPrediction.mlflow")
        mlflow.start_run()
        print("Logging parameters")
        mlflow.log_param("folds", folds)
        save_model(model, 'linear')
        result = self.testModel(model)
        print("Logging metrics")
        mlflow.log_metric("R2", f"{result[0]}")
        mlflow.log_metric("RMSE", f"{result[1]}")
        print("Logging model")    
        conda_env = {
        "channels": ["conda-forge"],
        "dependencies": ["python=3.8.8", "pip"],
        "pip": ["mlflow==2.3", "scikit-learn==0.23.2", "cloudpickle==1.6.0"],
        "name": "mlflow-env",}
        signature = infer_signature(x_test, model.predict(x_test))
        mlflow.sklearn.log_model(sk_model=model, artifact_path="models", conda_env=conda_env, signature=signature)  
        mlflow.log_artifact("models/linear.pkl")
        mlflow.end_run()
        save_metrics(result, 'linear')
        return model

    def testModel(self, model):
        _, _, x_test, y_test = use_split('split_train', 'split_test')
        risultati = predictAndResults(model, x_test, y_test)
        stampa(risultati, "Linear Regression")
        return risultati


lr = Linear()
lr.trainLinear()
 


