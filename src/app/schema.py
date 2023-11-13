"""module for pydentic schemas"""
import sys
sys.path.insert(0,'src/models')
from knr import train_knr
from pydantic import BaseModel

class Knr(BaseModel):
    """class representing xgbooster model"""
    name:str
    params:dict[str,list[int]]
    
result=train_knr()




#print(Xgbooster(name="xgbooster", params={'max_depth':[4,5,6], 'n_estimator':[100,160,10]}))
