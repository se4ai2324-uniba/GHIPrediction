from sklearn.model_selection import train_test_split
import pandas as pd

class Split():

    def __init__(self):
        pass 


    def split_dataset(self):
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
    
    def saveSplit(self, file, name):
        file.to_csv(f"data/interim/{name}.csv", index = False)
    
split = Split()

x_train, x_test, y_train, y_test = split.split_dataset()

x_train = x_train.rename(columns={'0': 'x_train'})
x_train = x_train.rename(columns={'1': 'x_train'})
x_train = x_train.rename(columns={'2': 'x_train'})
x_test = x_test.rename(columns={'0': 'x_test'})
x_test = x_test.rename(columns={'1': 'x_test'})
x_test = x_test.rename(columns={'2': 'x_test'})
y_train = y_train.rename(columns={'GHI': 'y_train'})
y_test = y_test.rename(columns={'GHI': 'y_test'})

# Concatena i DataFrame in un unico DataFrame
concatenated_train = pd.concat([x_train, y_train], axis = 1, ignore_index=True)
concatenated_test = pd.concat([x_test, y_test], axis = 1, ignore_index=True)

# Salva il DataFrame concatenato in un file CSV
split.saveSplit(concatenated_train, "split_train")
split.saveSplit(concatenated_test, "split_test")


