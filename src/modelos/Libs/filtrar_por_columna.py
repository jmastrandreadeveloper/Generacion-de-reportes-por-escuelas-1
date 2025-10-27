import pandas as pd

def filtrar_por_columna(dataframe : pd.DataFrame,columna,condición):
    return dataframe[dataframe[columna] == condición] 