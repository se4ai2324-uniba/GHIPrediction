"""module for comparing the models' results"""
import pickle
from train_model import save_model, save_metrics
from codecarbon import EmissionsTracker

xgb_metrics = []
linear = []
random_forest = []
knr = []

def read_and_assign(name, array):
    """function to read the metrics and append them in the file"""
    with open(f"models/{name}.metrics", 'r', encoding="utf-8") as fd:
        for line in fd:
            # Rimuovi spazi bianchi e caratteri di nuova riga
            line = line.strip()
            # Aggiungi la riga all'array
            array.append(float(line))
        array.append(name)

# for add another model just create a module, add it in the dvc pipeline,
# call the saved model and the matric with the same name
# and add a read_and_assign with the same name
read_and_assign("linear", linear)
read_and_assign("randomForestRegressor", random_forest)
read_and_assign("xgb", xgb_metrics)
read_and_assign("knr", knr)

def compare_r2(array1, array2, array3, array4):
    """function to compare R2 metric"""
    lista_num = []
    lista = []
    for i in [array1, array2, array3, array4]:
        lista_num = i[:2]
        lista_num = [float(element) for element in lista_num]
        lista.append(lista_num)
    maximum = 1000
    max_r2 = 0
    best = []
    for i in lista:
        if i[1] < maximum:
            print(i[1])
            maximum = i[1]
            max_r2 = i[0]
            best = i
        else:
            if  i[1] == maximum:
                if i[0] > max_r2:
                    max_r2 = i[0]
                    maximum = i[1]
                    best = i
                elif i[0] == max_r2:
                    best = i
                    max_r2 = i[0]
                    maximum = i[1]
                    best = i
    return best

def compare(i, array1, array2, array3, array4):
    """function to compare models"""
    model = ""
    for elemento in i:
        if elemento in array1:
            model = array1[2]
        elif elemento in array2:
            model = array2[2]
        elif elemento in array3:
            model = array3[2]
        elif elemento in array4:
            model = array4[2]
    return model

tracker=EmissionsTracker(output_dir="reports/codecarbon", output_file="compare_emissions.csv")
tracker.start()
best_metrics = compare_r2(linear, random_forest, xgb_metrics, knr)
best_model = compare(best_metrics, linear, random_forest, knr, xgb_metrics)
load_model = pickle.load(open(f"models/{best_model}.pkl", 'rb'))
with open('models/best_model.txt', 'w') as file:
    # Scrivi la nuova stringa nel file
    file.write(best_model)

save_model(load_model, 'best_model')
save_metrics(best_metrics, 'best_metrics')
tracker.stop()
#test action

