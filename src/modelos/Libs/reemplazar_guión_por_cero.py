import pandas as pd

def reemplazar_guion_por_cero(df, columna):
    """
    Reemplaza los valores '-' por 0 en una columna específica de un DataFrame.
    
    :param df: DataFrame de pandas.
    :param columna: Nombre de la columna donde se reemplazarán los valores.
    :return: DataFrame con los valores reemplazados.
    """
    df[columna] = df[columna].replace('-', 0)
    return df
