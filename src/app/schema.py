"""module for pydentic schemas"""
import sys
sys.path.insert(0,'src/models')
from xgbooster import train_xgbooster
from pydantic import BaseModel

class Xgbooster(BaseModel):
    """class representing xgbooster model"""
    name:str
    params:dict[str,list[int]]
    
result=train_xgbooster()
print(result.best_params_)
#print(Xgbooster(name="xgbooster", params={'max_depth':[4,5,6], 'n_estimator':[100,160,10]}))
