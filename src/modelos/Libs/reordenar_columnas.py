import pandas as pd

def reordenar_columnas(dataframe: pd.DataFrame, listaDeColumnas):
    # Columnas presentes en el DataFrame
    columnas_presentes = [col for col in listaDeColumnas if col in dataframe.columns]
    
    # Columnas que faltan
    columnas_faltantes = [col for col in listaDeColumnas if col not in dataframe.columns]
    
    if columnas_faltantes:
        print(f"Advertencia: Las siguientes columnas no están en el DataFrame y se ignorarán: {columnas_faltantes}")
    
    # Reordenar solo las que existen
    dataframe = dataframe[columnas_presentes]
    return dataframe