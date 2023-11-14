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
