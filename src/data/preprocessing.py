"""module for preprocessing the data"""
import pandas as pd
import joblib
from sklearn.preprocessing import RobustScaler
from codecarbon import EmissionsTracker

class Preprocessing:
    """class representing the preprocessing process"""
    def __init__(self):
        pass

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
        joblib.dump(scaler, f"models/scaler.pkl" )
        df_transformed = scaler.transform(tmp)
        return df_transformed

    def find_minmax_ghi(self,df):
        valore_massimo_colonna = df['GHI'].max()
        valore_minimo_colonna = df['GHI'].min()
        return valore_massimo_colonna, valore_minimo_colonna

tracker=EmissionsTracker(output_dir="reports/codecarbon", output_file="preprocessing_emissions.csv")
tracker.start()
preprocessing = Preprocessing()
final_df = preprocessing.pre_processing()
max_value, min_value = preprocessing.find_minmax_ghi(final_df)
ghi = final_df.GHI
dfS = preprocessing.scalarization(final_df)
dfNew = pd.DataFrame(dfS)
dfNew.to_csv('data/processed/PreprocessedData.csv', header=['Temperature', 'DNI',
'Relative Humidity'])
ghi.to_csv('data/processed/GHI.csv')
tracker.stop()
