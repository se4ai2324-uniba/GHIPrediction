"""module for APIs"""
import joblib
import uvicorn
import pandas as pd
from fastapi import FastAPI, status, HTTPException
from schema import Params, Predict, GHI, Models, ParamsAndResults, ListModels

app=FastAPI()

@app.get("/", description="Base root")
async def root():
    """base root"""
    return {"name":"GHI-Prediction",
        "message":"Welcome to GHI-Prediction Project",
        "github":"https://github.com/se4ai2324-uniba/GHIPrediction",
        "contributors":["Francesco Didio","Giovanni Federico Poli","Donato Francioso"]}


@app.get("/best_model/", status_code=status.HTTP_200_OK,
description="this function returns the best model's results", response_model=ParamsAndResults)
async def best_results():
    """function to list results of best model""" 
    params = pd.read_csv('src/models/params/xgb_params.csv', delimiter = ',')
    dizionario_valori = params.iloc[0].to_dict()
    name = "XgBooster"
    params = dizionario_valori
    with open('models/best_metrics.metrics', 'r', encoding='utf-8') as file:
        prima_riga = str(file.readline().strip())
        r2 = prima_riga
        seconda_riga = str(file.readline().strip())
        rmse = seconda_riga
    response = ParamsAndResults(name= name, params= params, r2=r2, rmse=rmse)
    return response


@app.get("/models", status_code=status.HTTP_200_OK,
description="this function returns all the models used in the comparison",
response_model=ListModels)
async def model_list():
    """function to list every model""" 
    models_list = ["Linear Regression", "Random Forest Regressor",
     "XGBooster", "K-Neighboor Regressor"]

    string = "I modelli usati sono: "
    response = ListModels(description=string, lista=models_list)
    return response


@app.get("/model/{name}/params", status_code=status.HTTP_200_OK, response_model=Params,
description="this function returns the parameters for every model. [RF, KNR, LR, XGB]",)
async def model_results(name):
    """function to list params of every model""" 
    if name == "KNR":
        model = read_params("knr", "K-Neighbor Regressor")
    elif name == "XGB":
        model = read_params("xgb", "XgBooster")
    elif name == "RF":
        model = read_params("rf", "Random Forest")
    elif name == "LR":
        model = read_params("lr", "linear Regression")
    else:
        raise HTTPException(status_code=404,
        detail="modello non trovato, scegliere tra [LR, RF, XGB, KNR]")
    response = Params(name=model.name, params=model.params)
    return response


@app.post("/prediction", status_code=status.HTTP_200_OK,
description="this function returns the ghi prediction from user input", response_model=GHI)
async def predict_ghi(request: Predict)->GHI:
    """function to predict GHI with user input""" 
    data = [[request.temperature, request.dni, request.humidity]]
    ghi = predict(data)
    response=GHI(predicted_GHI=ghi.item())
    return response


#----------------USEFUL FUNCTIONS-------------------
def read_params(path, name):
    """function to read parameters from file""" 
    model = Models
    params = pd.read_csv(f'src/models/params/{path}_params.csv', delimiter = ',')
    dizionario_valori = params.iloc[0].to_dict()
    model.name = name
    model.params = dizionario_valori
    return model

def predict(data):
    """function to implement prediction""" 
    model_path = 'models/best_model.pkl'
    model = joblib.load(model_path)
    scaler = joblib.load('models/scaler.pkl')
    transformed = scaler.transform(data)
    predizione = model.predict(transformed)
    return predizione

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port="8000")
