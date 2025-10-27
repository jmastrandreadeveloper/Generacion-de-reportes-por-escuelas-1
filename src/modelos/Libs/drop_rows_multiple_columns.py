import pandas as pd

def drop_rows_multiple_columns(dataframe  : pd.DataFrame , columnas, valores_a_eliminar):
    # Crear una máscara booleana que indica las filas a conservar
    mascara = pd.Series([True] * len(dataframe))
    for columna in columnas:
        if columna in dataframe.columns:
            mascara &= ~dataframe[columna].isin(valores_a_eliminar)
    return dataframe[mascara]