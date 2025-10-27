import pandas as pd
from typing import List, Hashable

def columna_a_lista(df: pd.DataFrame, nombre_columna: Hashable) -> List:
    """
    Devuelve los valores de una columna de un DataFrame como lista de Python.

    Parámetros
    ----------
    df : pd.DataFrame
        DataFrame de origen.
    nombre_columna : hashable
        Nombre (etiqueta) de la columna cuyas celdas quieres obtener.

    Devuelve
    --------
    list
        Lista con los valores de la columna, en el orden en que aparecen.

    Ejemplos
    --------
    >>> lista = columna_a_lista(df, "Curso ")
    >>> print(lista)
    ['1°', '1°', '1°', '1°', '1°', '1°']
    """
    if nombre_columna not in df.columns:
        raise KeyError(f"La columna '{nombre_columna}' no existe en el DataFrame")

    # .tolist() convierte la Serie en lista de Python
    return df[nombre_columna].tolist()
