from django.shortcuts import render
from .nsl_kdd_loader import cargar_dataset, generar_grafico_columna

def home(request):
    df, atributos = cargar_dataset()
    df_html = df.head(50).to_html(classes="table table-striped")
    columna = df.select_dtypes(include=['float64', 'int64']).columns[0]
    plot = generar_grafico_columna(columna)
    return render(request, "dashboard/home.html", {"df_html": df_html, "atributos": atributos, "plot": plot, "columna": columna})