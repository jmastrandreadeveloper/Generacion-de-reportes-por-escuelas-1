import pandas as pd

def quitar_columnas(dataframe: pd.DataFrame, listaDeColumnasAQuitar, dejarFilasUnicas):
    # Verificar cuáles columnas están presentes
    columnas_presentes = [col for col in listaDeColumnasAQuitar if col in dataframe.columns]
    columnas_faltantes = [col for col in listaDeColumnasAQuitar if col not in dataframe.columns]
    
    if columnas_faltantes:
        print(f"Advertencia: Las siguientes columnas no están en el DataFrame y se ignorarán: {columnas_faltantes}")
    
    # Quitar solo las columnas que existen
    dataframe = dataframe.drop(columns=columnas_presentes)
    
    # Dejar filas únicas si se especifica
    if dejarFilasUnicas:
        dataframe = dataframe.drop_duplicates()
    
    return dataframe