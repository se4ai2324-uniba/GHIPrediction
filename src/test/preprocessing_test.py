import pandas as pd
import sys
sys.path.insert(0, "src/data/")
from preprocessing import Preprocessing

def test_scalarization():
    """utility test fuction"""
    data_processor=Preprocessing()
    data={'A':[1,2,3], 'B':[4,5,6], 'GHI':[7,8,9]}
    df=pd.DataFrame(data)

    result=data_processor.scalarization(df)
    assert result is not None
    assert result.shape[1]==df.shape[1]-1

test_scalarization()