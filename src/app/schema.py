"""module for pydentic schemas"""
import sys
sys.path.insert(0,'src/models')
from pydantic import BaseModel

class ListModels(BaseModel):
    """class to represent models list schema"""
    description: str
    lista: list

class Params(BaseModel):
    """class to represent params shape schema"""
    params: dict

class ParamsAndResults(BaseModel):
    """class representing models params and results schema"""
    name:str
    params:dict
    r2: float
    rmse: float

class Models(BaseModel):
    """class to represent models and params schema"""
    name: str
    model: Params

class Predict(BaseModel):
    """class to represent prediction input schema"""
    temperature: float
    dni: float
    humidity: float

class GHI(BaseModel):
    """class to represent prediction result schema"""
    predicted_GHI : float
