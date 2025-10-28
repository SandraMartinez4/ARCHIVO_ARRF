
    # views.py

from django.shortcuts import render
from .nsl_kdd_loader import cargar_dataset 

def home(request):
    df, atributos = cargar_dataset()
    
    # Cantidad de filas a mostrar (20, como solicitaste anteriormente)
    NUM_FILAS_A_MOSTRAR = 20  

    # Preparar la tabla
    column_headers = atributos 
    data_table = df.head(NUM_FILAS_A_MOSTRAR).values.tolist()
    
    # ----------------------------------------------------
    # CAMBIO: Asegurarse de pasar 'atributos' a la plantilla
    # ----------------------------------------------------
    return render(request, "dashboard/home.html", {
        "atributos": atributos,          # <--- VARIABLE REINTRODUCIDA
        "column_headers": column_headers,
        "data_table": data_table,        
    })