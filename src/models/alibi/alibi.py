import sys
from alibi_detect.cd import TabularDrift
sys.path.insert(0, "src/models/")
from train_model import use_split

#Alibi Detector
x_train, _ , x_test, _ = use_split('split_train', 'split_test')
cat = ['Temperature','DNI','Relative Humidity']
x_train_array = x_train.to_numpy()
x_test_array = x_test.to_numpy()
cd = TabularDrift(x_train_array, p_val = .05)

# Monitoraggio del drift sui dati di test
drift_result = cd.predict(x_test_array)

# Visualizzazione dei risultati
labels = ['No!', 'Yes!']
print('Drift? {}'.format(labels[drift_result['data']['is_drift']]))

for f in range(cd.n_features):
    fname = cat[f]
    stat_val, p_val = drift_result['data']['distance'][f], drift_result['data']['p_val'][f]
    print(f'{fname} -- K-S {stat_val:.3f} -- p-value {p_val:.3f}')
print(drift_result['data']['threshold'])

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