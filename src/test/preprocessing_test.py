"""module containing testing functions for preprocessing module"""
import sys
import pytest
import pandas as pd
sys.path.insert(0, "src/data/")
from preprocessing import Preprocessing, final_df

@pytest.fixture
def dataframe():
    """needed to recall final_df as fixture"""
    return final_df

def test_scalarization(dataframe):
    """utility test fuction"""
    data_processor=Preprocessing()
    data=dataframe
    result=data_processor.scalarization(data)
    assert result is not None
    assert result.shape[1]==data.shape[1]-1
