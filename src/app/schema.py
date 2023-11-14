"""module for pydentic schemas"""
import sys
sys.path.insert(0,'src/models')
from pydantic import BaseModel

class Params(BaseModel):
    """class representing xgbooster model"""
    name:str
    params:dict[str,str]


class Results(BaseModel):
    r2:str
    rmse:str

class Models(BaseModel):
    #model: Params
    res: Results

class Predict(BaseModel):
    temperature: float
    dni: float
    humidity: float

class GHI(BaseModel):
    predicted_GHI : float
