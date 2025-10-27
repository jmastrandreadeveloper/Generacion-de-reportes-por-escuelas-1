import pandas as pd

def conservar_columnas(dataframe: pd.DataFrame, listaDeColumnasAConservar, dejarFilasUnicas=False):
    """
    Devuelve un DataFrame que conserva únicamente las columnas especificadas.
    
    Parámetros:
    - dataframe: DataFrame de entrada.
    - listaDeColumnasAConservar: Lista de columnas a conservar.
    - dejarFilasUnicas: Si es True, elimina filas duplicadas en el DataFrame resultante.

    Retorna:
    - Un DataFrame con las columnas especificadas y, opcionalmente, con filas únicas.
    """
    # Conservar solo las columnas especificadas
    dataframe = dataframe[listaDeColumnasAConservar]
    
    # Dejar filas únicas si se especifica
    if dejarFilasUnicas:
        dataframe = dataframe.drop_duplicates()
        
    return dataframe