import pandas as pd

def renombrar_columnas(dataframe : pd.DataFrame , diccionarioDeColumnas):
    dataframe.rename(
        columns=diccionarioDeColumnas, 
        inplace = True
    )
    return dataframe