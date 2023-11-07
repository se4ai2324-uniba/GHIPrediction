
"""module for preprocessing the data"""
import pytest
import pandas as pd
from sklearn.preprocessing import RobustScaler

class Preprocessing:
    """class representing the preprocessing process"""
    def pre_processing(self):
        """function to preprocess data frame"""
        df = pd.read_csv('data/raw/FinaleBari.csv', header=0)
        i = df[((df.GHI == 0))].index
        new_df = df.drop(i)
        new_new_df = new_df.drop(columns = ['DHI','Year','Month','Day','Hour', 'Minute',
        'Precipitable Water', 'Dew Point', 'Cloud Type', 'Surface Albedo','Wind Speed','Pressure'])
        current_df = new_new_df.fillna(0)
        return current_df

    def scalarization(self, current_df):
        """function to scalarize data frame"""
        scaler = RobustScaler()
        tmp = current_df.drop('GHI', axis = 1)
        scaler.fit(tmp)
        df_transformed = scaler.transform(tmp)
        return df_transformed

preprocessing = Preprocessing()
final_df = preprocessing.pre_processing()
ghi = final_df.GHI
dfS = preprocessing.scalarization(final_df)
dfNew = pd.DataFrame(dfS)
dfNew.to_csv('data/processed/PreprocessedData.csv', header=['Temperature', 'DNI',
'Relative Humidity'])
ghi.to_csv('data/processed/GHI.csv')

def test_scalarization():
    """utility test fuction"""
    data_processor=Preprocessing()
    data={'A':[1,2,3], 'B':[4,5,6], 'GHI':[7,8,9]}
    df=pd.DataFrame(data)

    result=data_processor.scalarization(df)
    assert result is not None
    assert result.shape[1]==df.shape[1]-1

test_scalarization()
