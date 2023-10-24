from sklearn.model_selection import train_test_split
import pandas as pd

class Split():

    def __init__(self):
        pass 


    def split_dataset():
        y_bari= pd.read_csv('data/processed/GHI.csv')
        x_bari = pd.read_csv('data/processed/PreprocessedData.csv')
        fc=y_bari.columns[0]
        y_bari = y_bari.drop(fc, axis=1)

        fc=x_bari.columns[0]
        x_bari = x_bari.drop(fc, axis=1)

        x_trainB, x_testB, y_trainB, y_testB = train_test_split(x_bari,y_bari,test_size=0.3)    
        return x_trainB, x_testB, y_trainB, y_testB

    def getTrain(self):
        X = Split.split_dataset()
        return X
    






