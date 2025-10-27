import pandas as pd

def limpiar_curso(df, columna, prefijo):
    """
    Elimina el prefijo dado (regex) de la columna especificada.

    Args:
        df (pd.DataFrame): DataFrame original.
        columna (str): Nombre de la columna.
        prefijo (str): Prefijo como regex.

    Returns:
        pd.DataFrame: DataFrame con la columna modificada.
    """
    df = df.copy()
    # Forzar a string por si hay tipos mezclados
    df[columna] = df[columna].astype(str).str.replace(prefijo, '', regex=True).str.strip()
    return df