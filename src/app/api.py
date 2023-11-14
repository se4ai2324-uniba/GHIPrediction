"""module for APIs"""
from fastapi import FastAPI, Request
from src.app.schema import Params, Results, Models, Predict, GHI
import pandas as pd
from pathlib import Path
from functools import wraps
from datetime import datetime
from http import HTTPStatus
import joblib
from sklearn.preprocessing import RobustScaler
import json

app=FastAPI()

@app.get("/")
async def root():
    return {"message":"Benvenuto nel GHI Prediction Project"}


@app.get("/best_model/")
async def calcola_risultati():  
    model = Params
    results = Results
    params = pd.read_csv('src/models/params/xgb_params.csv', delimiter = ',')
    dizionario_valori = params.iloc[0].to_dict()
    model.name = "XgBooster"
    model.params = dizionario_valori
    with open('models/best_metrics.metrics', 'r') as file:
        prima_riga = str(file.readline().strip())
        results.r2 = prima_riga
        seconda_riga = str(file.readline().strip())
        results.rmse = seconda_riga
    return {"name": model.name, "params": model.params, "r2": results.r2, "rmse": results.rmse}


@app.get("/models")
async def model_list():
    model_list = ["Linear Regression", "Random Forest Regressor", "XGBooster", "K-Neighboor Regressor"]
    
    string = "I modelli usati sono: "
    return {f"{string}{model_list}"}


@app.get("/model/{name}")
async def models(name:str):
    
    return {f"Il modello selezionato è: {name}"}


@app.get("/model/{name}/params")
async def model_results(name):
    model = Params
    if name == "KNR":
        model = read_params("knr", "K-Neighbor Regressor")
    elif name == "XGB":
        model = read_params("xgb", "XgBooster")
    elif name == "RF":
        model = read_params("rf", "Random Forest")
    elif name == "LR":
        model = read_params("lr", "linear Regression")
    else:
        return {"Inserire nome valido"}

    return {"name": model.name, "params": model.params}


@app.post("/prediction")
async def predict_GHI(request: Predict)->GHI:

    res = GHI
    data = [[request.temperature, request.dni, request.humidity]]
    ghi = predict(data)
    res.predicted_GHI = ghi
    return res







#USEFUL FUNCTIONS

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