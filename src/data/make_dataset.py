import pandas as pd

class Dataset:
  
#Create CSV
    def finalDf(self, df, df1, df2, name):
        data = [df, df1, df2]
        final = pd.DataFrame()
        final = pd.concat(data)
        final.to_csv(f"data/raw/{name}", index = False)
        df = pd.read_csv(f"data/raw/{name}", delimiter = ',')
        return df
    

dataset = Dataset()
dfB1 = pd.read_csv('data/raw/2017.csv', delimiter = ',')
dfB2 = pd.read_csv('data/raw/2018.csv', delimiter = ',')
dfB3 = pd.read_csv('data/raw/2019.csv', delimiter = ',')
dfBari = dataset.finalDf(dfB1, dfB2, dfB3, 'FinaleBari.csv')
