"""module for APIs"""
import joblib
import uvicorn
import csv
import pandas as pd
from fastapi import FastAPI, status
from schema import Predict, GHI, Models, ParamsAndResults
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

with open('models/best_model.txt', 'r', encoding='utf-8') as file: BEST_MODEL = file.read()

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Instrumentator().instrument(app).expose(app, endpoint="/metrics") #allows prometheus to gather metrics

@app.get("/", description="Base root")
async def root():
    """base root"""
    return {"name":"GHI-Prediction",
        "message":"Welcome to GHI-Prediction Project",
        "github":"https://github.com/se4ai2324-uniba/GHIPrediction",
        "contributors":["Francesco Didio","Giovanni Federico Poli","Donato Francioso"]}

#TODO modify xgb into best_model 
@app.get("/best_model", status_code=status.HTTP_200_OK,
description="this function returns the best model's results", response_model=ParamsAndResults)
async def best_results():
    """function to list results of best model""" 
    params = pd.read_csv(f'src/models/params/{BEST_MODEL}_params.csv', delimiter = ',')
    dizionario_valori = params.iloc[0].to_dict()
    name = BEST_MODEL.upper()
    params = dizionario_valori
    with open('models/best_metrics.metrics', 'r', encoding='utf-8') as file:
        prima_riga = str(file.readline().strip())
        r2 = prima_riga
        seconda_riga = str(file.readline().strip())
        rmse = seconda_riga
    response = ParamsAndResults(name= name, params= params, r2=r2, rmse=rmse)
    return response


@app.post("/prediction", status_code=status.HTTP_200_OK,
description="this function returns the ghi prediction from user input", response_model=GHI)
async def predict_ghi(request: Predict)->GHI:
    """function to predict GHI with user input""" 
    data = [[request.temperature, request.dni, request.humidity]]
    csv_file_path = 'data/external/user_requests.csv'
    with open(csv_file_path, mode='a') as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(data[0])
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
    uvicorn.run(app, host="0.0.0.0", port="8000")
