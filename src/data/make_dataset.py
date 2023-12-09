"""module for creating the main .cvs file"""
import pandas as pd
from codecarbon import EmissionsTracker

def final_df(df, df1, df2, name):
    """function to read and create final data frame"""
    data = [df, df1, df2]
    final = pd.DataFrame()
    final = pd.concat(data)
    final.to_csv(f"data/raw/{name}", index = False)
    df = pd.read_csv(f"data/raw/{name}", delimiter = ',')
    return df

tracker=EmissionsTracker(output_dir="reports/codecarbon", output_file="make_dataset_emissions.csv")
tracker.start()
dfB1 = pd.read_csv('data/raw/2017.csv', delimiter = ',')
dfB2 = pd.read_csv('data/raw/2018.csv', delimiter = ',')
dfB3 = pd.read_csv('data/raw/2019.csv', delimiter = ',')
dfBari = final_df(dfB1, dfB2, dfB3, 'FinaleBari.csv')
tracker.stop()
