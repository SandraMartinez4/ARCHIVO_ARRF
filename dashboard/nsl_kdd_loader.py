import os
import pandas as pd 
import arff        
# Eliminamos todas las importaciones de gráficas (base64, matplotlib, io)

DATASET_PATH = os.path.join(os.path.dirname(__file__), "datasets/NSL-KDD/KDDTrain+.arff")

def cargar_dataset():
    """
    Carga el dataset NSL-KDD desde el archivo .arff y lo convierte a un DataFrame de pandas.
    """
    with open(DATASET_PATH, 'r') as f:
        data = arff.load(f) 
    
    atributos = [attr[0] for attr in data['attributes']]
    df = pd.DataFrame(data['data'], columns=atributos)
    
    return df, atributos
