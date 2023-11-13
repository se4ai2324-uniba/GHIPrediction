"""module for APIs"""
from fastapi import FastAPI, Request
from src.app.schema import Params, Results
import pandas as pd
from pathlib import Path
import pickle
from functools import wraps
from datetime import datetime
from http import HTTPStatus





app=FastAPI()

# @app.get("/best_model")
# async def root(best_model:Models):
#     return{
#         "message":"The best model is"
#         }





# def construct_response(f):
#     """Construct a JSON response for an endpoint's results."""

#     @wraps(f)
#     def wrap(request: Request, args, **kwargs):
#         results = f(request,args, **kwargs)

#         # Construct response
#         response = {
#             "message": results["message"],
#             "method": request.method,
#             "status-code": results["status-code"],
#             "timestamp": datetime.now().isoformat(),
#             "url": request.url._url,
#         }

#         # Add data
#         if "data" in results:
#             response["data"] = results["data"]

#         return response

#     return wrap

# @app.get("/", tags=["General"])  # path operation decorator
# @construct_response
# def _index(request: Request):
#     client_host = request.client.host
#     """Root endpoint."""

#     response = {
#         "message": HTTPStatus.OK.phrase,
#         "status-code": HTTPStatus.OK,
#         "data": {"message": "Welcome to IRIS classifier! Please, read the /docs!"},
#     }
#     return response

@app.get("/")
async def root():
    return {"message":"Test"}


@app.get("/best_model/")
def calcola_risultati():  
    model = Params
    results = Results
    params = pd.read_csv('src/models/params/xgb_params.csv', delimiter = ',')
    dizionario_valori = params.iloc[0].to_dict()
    model.name = "XgBooster"
    model.params = dizionario_valori
    return {"name": model.name, "params": model.params}


#QUESTA FUNZIONA
# @app.get("/best_model/")
# def calcola_risultati():  
#     model = Params
#     params = pd.read_csv('src/models/params/xgb_params.csv', delimiter = ',')
#     dizionario_valori = params.iloc[0].to_dict()
#     model.name = "XgBooster"
#     model.params = dizionario_valori
#     return {"name": model.name, "params": model.params}