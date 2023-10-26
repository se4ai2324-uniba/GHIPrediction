from train_model import save_model, save_metrics

xgb_metrics = [] 
linear = [] 
randomForest = [] 
knr = [] 

def read_and_assign(name, array):

    with open(f"models/{name}.metrics", 'r') as fd:
        for line in fd:
            # Rimuovi spazi bianchi e caratteri di nuova riga
            line = line.strip()
            # Aggiungi la riga all'array
            array.append(float(line))
        array.append(name)



read_and_assign("linear", linear)
read_and_assign("randomForestRegressor", randomForest)
read_and_assign("xgb", xgb_metrics)
read_and_assign("knr", knr)

def compareR2(array, array2, array3, array4):
    listaNum = []
    lista = []
    for array in [array, array2, array3, array4]:
        listaNum = array[:2]
        listaNum = [float(element) for element in listaNum]
        lista.append(listaNum)
    max = 1000
    maxR2 = 0
    best = []
    for i in lista:
        if i[1] < max:
                print(i[1])
                max = i[1]
                maxR2 = i[0]
                best = i
        else:
            if  i[1] == max:
                if i[0] > maxR2:
                        maxR2 = i[0]
                        max = i[1]
                        best = i
                elif i[0] == maxR2:
                        best = i
                        maxR2 = i[0]
                        max = i[1]
                        best = i
    return best


risultati_confronto = []

def compare(i, array, array2, array3, array4):
    model = ""
    for elemento in i:
         if elemento in array:
              model = array[2]
         elif elemento in array2:
              model = array2[2]
         elif elemento in array3:
              model = array3[2]
         elif elemento in array4: 
              model = array4[2]
    return model
        
migliore = compareR2(linear, randomForest, xgb_metrics, knr)
modello = compare(migliore, linear, randomForest, knr, xgb_metrics)
