import pandas as pd

def fix_columna_subcue(dataframe : pd.DataFrame):
    dataframe.loc[dataframe['subcue'] == '-', :] = 0
    return dataframe