# views.py

from django.shortcuts import render
# Solo importamos lo necesario
from .nsl_kdd_loader import cargar_dataset 

def home(request):
    df, atributos = cargar_dataset()
    
    # Definir la cantidad de filas a mostrar (20 filas)
    NUM_FILAS_A_MOSTRAR = 20  

    # Preparar las variables para la tabla dinámica
    column_headers = atributos 
    
    # Obtiene los VALORES de las primeras 20 filas como una lista de listas
    data_table = df.head(NUM_FILAS_A_MOSTRAR).values.tolist()
    
    # Renderizar con las variables necesarias para la tabla
    return render(request, "dashboard/home.html", {
        "column_headers": column_headers, # Encabezados de la tabla
        "data_table": data_table,        # Datos de las 20 filas
        # Ya no se pasa la variable 'atributos' ni nada de gráficas
    })