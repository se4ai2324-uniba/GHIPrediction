"""module for pydentic schemas"""
import sys
from typing import Optional
sys.path.insert(0,'src/models')
from pydantic import BaseModel

class ListModels(BaseModel):
    description: str
    lista: list

class Params(BaseModel):
    params: dict
class ParamsAndResults(BaseModel):
    """class representing xgbooster model"""
    name:str
    params:dict
    r2: float
    rmse: float

class Models(BaseModel):
    name: str
    model: Params

class Predict(BaseModel):
    temperature: float
    dni: float
    humidity: float

class GHI(BaseModel):
    predicted_GHI : float
