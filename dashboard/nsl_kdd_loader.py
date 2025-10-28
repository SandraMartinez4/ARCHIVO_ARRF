import pandas as pd
import arff
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
import os

DATASET_PATH = os.path.join(os.path.dirname(__file__), "datasets/NSL-KDD/KDDTrain+.arff")

def cargar_dataset():
    with open(DATASET_PATH, 'r') as f:
        data = arff.load(f)
    atributos = [attr[0] for attr in data['attributes']]
    df = pd.DataFrame(data['data'], columns=atributos)
    return df, atributos

def generar_grafico_columna(columna):
    df, _ = cargar_dataset()
    plt.figure(figsize=(8,6))
    sns.histplot(df[columna])
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode()
    plt.close()
    return image_base64