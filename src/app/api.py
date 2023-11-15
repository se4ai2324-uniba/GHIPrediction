"""module for APIs"""
from fastapi import FastAPI, Response, status, HTTPException
from schema import Params, Predict, GHI, Models, ParamsAndResults, ListModels
import pandas as pd
from pathlib import Path
from functools import wraps
from datetime import datetime
import joblib
import uvicorn
from fastapi.responses import JSONResponse

app=FastAPI()

@app.get("/")
async def root():
    return {"message":"Benvenuto nel GHI Prediction Project"}


@app.get("/best_model/", status_code=status.HTTP_200_OK, description="Risultati del miglior modello", response_model=ParamsAndResults)
async def calcola_risultati():  
    params = pd.read_csv('src/models/params/xgb_params.csv', delimiter = ',')
    dizionario_valori = params.iloc[0].to_dict()
    name = "XgBooster"
    params = dizionario_valori
    with open('models/best_metrics.metrics', 'r') as file:
        prima_riga = str(file.readline().strip())
        r2 = prima_riga
        seconda_riga = str(file.readline().strip())
        rmse = seconda_riga
    
    response = ParamsAndResults(name= name, params= params, r2=r2, rmse=rmse)
    return response


@app.get("/models", status_code=status.HTTP_200_OK, description="Ritorna la lista dei modelli utilizzati", response_model=ListModels)
async def model_list():
    model_list = ["Linear Regression", "Random Forest Regressor", "XGBooster", "K-Neighboor Regressor"]
    
    string = "I modelli usati sono: "
    response = ListModels(description=string, lista=model_list)
    return response


@app.get("/model/{name}/params", status_code=status.HTTP_200_OK, response_model=Params, description="Lettura dei parametri dei modelli. [RF, KNR, LR, XGB]",)
async def model_results(name):
    if name == "KNR":
        model = read_params("knr", "K-Neighbor Regressor")
    elif name == "XGB":
        model = read_params("xgb", "XgBooster")
    elif name == "RF":
        model = read_params("rf", "Random Forest")
    elif name == "LR":
        model = read_params("lr", "linear Regression")
    else:
        raise HTTPException(status_code=404, detail="modello non trovato, scegliere tra [LR, RF, XGB, KNR]")

    response = Params(name=model.name, params=model.params)
    return response

@app.post("/prediction", status_code=status.HTTP_200_OK, description="Usata per calcolare il GHI dati dei valori in input", response_model=GHI)
async def predict_GHI(request: Predict)->GHI:

    data = [[request.temperature, request.dni, request.humidity]]
    ghi = predict(data)
    response=GHI(predicted_GHI=ghi)
    return response


#----------------USEFUL FUNCTIONS-------------------

def read_params(path, name):
    model = Models
    params = pd.read_csv(f'src/models/params/{path}_params.csv', delimiter = ',')
    dizionario_valori = params.iloc[0].to_dict()
    model.name = name
    model.params = dizionario_valori
    return model

def predict(data):
    model_path = 'models/best_model.pkl'
    model = joblib.load(model_path)
    scaler = joblib.load('models/scaler.pkl')
    transformed = scaler.transform(data)
    predizione = model.predict(transformed)
    return predizione



uvicorn.run(app, host="127.0.0.1", port="8000")