import pandas as pd

def ordenar_df_por_columna(df , columna):
    return df.sort_values(by=columna, ascending=True)