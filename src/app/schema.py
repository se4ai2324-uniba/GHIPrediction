"""module for pydentic schemas"""
import sys
sys.path.insert(0,'src/models')
from pydantic import BaseModel

class Params(BaseModel):
    """class representing xgbooster model"""
    name:str
    params:dict[str,str]


class Results(BaseModel):
    name:str
    results:str






#print(Xgbooster(name="xgbooster", params={'max_depth':[4,5,6], 'n_estimator':[100,160,10]}))
