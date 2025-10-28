# views.py

from django.shortcuts import render
# Solo importamos lo que necesitamos para cargar el dataset
from .nsl_kdd_loader import cargar_dataset 

def home(request):
    df, atributos = cargar_dataset()
    
    # 1. Definir la cantidad exacta de filas a mostrar
    NUM_FILAS_A_MOSTRAR = 20  # <--- CAMBIO AQUÍ: Mostrar solo 20 filas

    # 2. Preparar las variables para la tabla dinámica:
    column_headers = atributos 
    
    # Obtiene los VALORES de las primeras 20 filas como una lista de listas
    data_table = df.head(NUM_FILAS_A_MOSTRAR).values.tolist()
    
    # 3. Renderizar solo con los datos de la tabla (no se necesita 'atributos' si no se usa)
    # Sin embargo, lo dejamos por si quieres reintroducir el <ul> más tarde.
    return render(request, "dashboard/home.html", {
        "atributos": atributos, 
        "column_headers": column_headers,
        "data_table": data_table,       
    })