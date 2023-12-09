"""module for splitting the dataset"""
import pandas as pd
from sklearn.model_selection import train_test_split
from codecarbon import EmissionsTracker

class Split():
    """class representing the splitting process"""

    def split_dataset(self):
        """function to split the dataset in train and test"""
        y_bari= pd.read_csv('data/processed/GHI.csv')
        x_bari = pd.read_csv('data/processed/PreprocessedData.csv')
        fc=y_bari.columns[0]
        y_bari = y_bari.drop(fc, axis=1)
        fc=x_bari.columns[0]
        x_bari = x_bari.drop(fc, axis=1)
        x_trainb, x_testb, y_trainb, y_testb = train_test_split(x_bari,y_bari,test_size=0.3)
        return x_trainb, x_testb, y_trainb, y_testb

    def get_train(self):
        """function to retrieve the split"""
        x = Split.split_dataset(self)
        return x

    def save_split(self, file, name):
        """function to save to csv"""
        file.to_csv(f"data/interim/{name}.csv", index = False)

split = Split()
x_train, x_test, y_train, y_test = split.split_dataset()
x_train = x_train.rename(columns={'Temperature': 'x_train'})
x_train = x_train.rename(columns={'DNI': 'x_train'})
x_train = x_train.rename(columns={'Relative Humidity': 'x_train'})
x_test = x_test.rename(columns={'Temperature': 'x_test'})
x_test = x_test.rename(columns={'DNI': 'x_test'})
x_test = x_test.rename(columns={'Relative Humidity': 'x_test'})
y_train = y_train.rename(columns={'GHI': 'y_train'})
y_test = y_test.rename(columns={'GHI': 'y_test'})

tracker=EmissionsTracker(output_dir="reports/codecarbon", output_file="split_dataset_emissions.csv")
tracker.start()
# Concatena i DataFrame in un unico DataFrame
concatenated_train = pd.concat([x_train, y_train], axis = 1, ignore_index=True)
concatenated_test = pd.concat([x_test, y_test], axis = 1, ignore_index=True)
#concatenated_train = concatenated_train.rename(columns={
# '0':'Temperature', '1':'DNI', '2': 'Humidity'})
#concatenated_test = concatenated_test.rename(columns={
# '0':'Temperature', '1':'DNI', '2': 'Humidity'})
# Salva il DataFrame concatenato in un file CSV
split.save_split(concatenated_train, "split_train")
split.save_split(concatenated_test, "split_test")
tracker.stop()
