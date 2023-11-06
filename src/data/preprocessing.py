
import pandas as pd
from sklearn.preprocessing import RobustScaler

#Clean csv
class Preprocessing:
  def preProcessing(self):
    df = pd.read_csv('data/raw/FinaleBari.csv', header=0) 
    i = df[((df.GHI == 0))].index
    df = df.drop(i)
    df = df.drop(columns = ['DHI','Year','Month','Day','Hour', 'Minute', 'Precipitable Water', 'Dew Point', 'Cloud Type', 'Surface Albedo','Wind Speed','Pressure'])
    df = df.fillna(0)
    return df

#Scalarization
  def scalarization(self):
    scaler = RobustScaler()
    tmp = df.drop('GHI', axis = 1)
    scaler.fit(tmp)
    dfTransformed = scaler.transform(tmp)
    return dfTransformed
  


preprocessing = Preprocessing()

df = preprocessing.preProcessing()
ghi = df.GHI

dfS = preprocessing.scalarization()

dfNew = pd.DataFrame(dfS)
dfNew.to_csv('data/processed/PreprocessedData.csv', header=['Temperature', 'DNI', 'Relative Humidity'])
ghi.to_csv('data/processed/GHI.csv')
