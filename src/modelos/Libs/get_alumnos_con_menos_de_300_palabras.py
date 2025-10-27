import pandas as pd

def get_alumnos_con_menos_de_300_palabras(dataframe):
    # Hacer una copia del DataFrame original para evitar SettingWithCopyWarning
    dataframe = dataframe.copy()
    # Convertir los valores de 'Cantidad_de_palabras' a números, reemplazando los no numéricos con NaN
    dataframe['Cant. palabras'] = pd.to_numeric(dataframe['Cant. palabras'], errors='coerce')
    
    # Crear DataFrames separados para valores menores y mayores o iguales a 300
    return dataframe[dataframe['Cant. palabras'] < 300].copy()