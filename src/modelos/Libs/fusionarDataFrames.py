from functools import reduce
import pandas as pd

def fusionarDataFrames(listaDeDataframes , columna):
    print('...fusionando dataframes :')
    # https://stackoverflow.com/questions/44327999/python-pandas-merge-multiple-dataframes
    df_merged = reduce(lambda  left,right: pd.merge(left,right,on=[columna],how='outer'), listaDeDataframes).fillna(0)
    # cambiar el orden de las filas para que quede primero el nivel critico, luego el basico, despues le medio y el ultimo el avanzado..
    return df_merged