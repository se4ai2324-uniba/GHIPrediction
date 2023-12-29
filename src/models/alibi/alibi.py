import sys
import joblib
import pandas as pd
import csv
from alibi_detect.cd import TabularDrift
sys.path.insert(0, "src/models/")
from train_model import use_split

def alibi_detector(x_test, count):
    #Alibi Detector
    x_train, _ , _, _ = use_split('split_train', 'split_test')
    cat = ['Temperature','DNI','Relative Humidity']
    x_train_array = x_train.to_numpy()
    cd = TabularDrift(x_train_array, p_val = .05)

    # Monitoraggio del drift sui dati di test
    drift_result = cd.predict(x_test)

    # Visualizzazione dei risultati
    labels = ['No!', 'Yes!']
    print('Drift? {}'.format(labels[drift_result['data']['is_drift']]), "Index:", count)
    string = str(labels[drift_result['data']['is_drift']]) + "Index:" + str(count) + '\n'
    with open('data/external/drift_results.txt', 'a') as file:
    # Scrivi la nuova stringa nel file
        file.write(string)
    for f in range(cd.n_features):
        fname = cat[f]
        stat_val, p_val = drift_result['data']['distance'][f], drift_result['data']['p_val'][f]
        print(f'{fname} -- K-S {stat_val:.3f} -- p-value {p_val:.3f}')
    print(drift_result['data']['threshold'])


# Percorso del file CSV
percorso_file_csv = 'data/external/user_requests.csv'

# Leggi il CSV in un DataFrame
df = pd.read_csv(percorso_file_csv)
test = df.rename(columns={'0':'Temperature', '1':'DNI', '2': 'Relative Humidity'})
scaler = joblib.load('models/scaler.pkl')
transformed = scaler.transform(test)

# Itera attraverso le righe del DataFrame e applica la tua funzione
count = 0
for riga in transformed:
    riga = riga.reshape((1, -1))
    count += 1
    alibi_detector(riga, count)

'''
Drift? No!
Temperature -- K-S 0.011 -- p-value 0.879
DNI -- K-S 0.013 -- p-value 0.728
Relative Humidity -- K-S 0.016 -- p-value 0.460
'''



#test randomico
# print('Secondo test')
# data = np.random.randint(1, 1000 + 1, size=(1000, 3))
# column_names = [f"Col{col+1}" for col in range(3)]
# test = pd.DataFrame(data, columns=column_names)
# test = test.to_numpy()
# drift_result = cd.predict(test)

# labels = ['No!', 'Yes!']
# print('Drift? {}'.format(labels[drift_result['data']['is_drift']]))

# for f in range(cd.n_features):
#     fname = cat[f]
#     stat_val, p_val = drift_result['data']['distance'][f], drift_result['data']['p_val'][f]
#     print(f'{fname} -- K-S {stat_val:.3f} -- p-value {p_val:.3f}')
# print(drift_result['data']['threshold'])