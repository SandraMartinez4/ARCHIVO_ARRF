import pandas as pd
import base64 # Aunque no se usa, lo dejamos si estaba, pero eliminamos las librerías de gráfico
import os
import pandas as pd
import arff
# Eliminamos: import matplotlib.pyplot as plt
# Eliminamos: import io

DATASET_PATH = os.path.join(os.path.dirname(__file__), "datasets/NSL-KDD/KDDTrain+.arff")

def cargar_dataset():
    with open(DATASET_PATH, 'r') as f:
        data = arff.load(f) 
    atributos = [attr[0] for attr in data['attributes']]
    df = pd.DataFrame(data['data'], columns=atributos)
    return df, atributos

# Se eliminó la función generar_grafico_columna()
