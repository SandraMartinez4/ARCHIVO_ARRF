# views.py

from django.shortcuts import render
# Solo importamos lo que necesitamos para cargar el dataset
from .nsl_kdd_loader import cargar_dataset 

def home(request):
    df, atributos = cargar_dataset()
    
    # 1. Definir la cantidad de filas a mostrar
    # Aquí puedes cambiar el 500 para mostrar más o menos filas
    NUM_FILAS_A_MOSTRAR = 500  

    # 2. Preparar las variables para la tabla dinámica:
    column_headers = atributos 
    
    # Obtiene los VALORES de las primeras N filas como una lista de listas
    data_table = df.head(NUM_FILAS_A_MOSTRAR).values.tolist()
    
    # 3. Renderizar solo con los datos de la tabla y atributos
    return render(request, "dashboard/home.html", {
        "atributos": atributos, 
        "column_headers": column_headers, # NUEVA VARIABLE
        "data_table": data_table,       # NUEVA VARIABLE (Contiene más filas)
        # Se eliminaron 'plot' y 'columna'
    })
    
    