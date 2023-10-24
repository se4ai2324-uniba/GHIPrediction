from train_model import x_train, y_train, x_test, y_test
import pickle

class Carica:
        def load_model(self,path):
            loaded_model = pickle.load(open(path, "rb"))
            return loaded_model


def predict_XG():
    up = Carica()
    loaded = up.load_model("models/xgb.pkl")
    pred = loaded.predict(x_test)
    
    return pred

pred = predict_XG()
print(pred)


