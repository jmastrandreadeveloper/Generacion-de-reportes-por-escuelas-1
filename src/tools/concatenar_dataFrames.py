# esta función concatenna varios dataframes en uno solo, y los guarda en un archivo CSV
import pandas as pd
import os

def dataframes_concatenados(df_list):
    """
    Concatenate multiple DataFrames and save to a CSV file.

    Parameters:
    df_list (list): List of DataFrames to concatenate.
    nombre_archivo (str): Name of the output CSV file.
    ruta_salida (str): Directory where the CSV file will be saved.

    Returns:
    None
    """
    # Concatenate all DataFrames in the list
    df_concatenado = pd.concat(df_list, ignore_index=True)

    return df_concatenado