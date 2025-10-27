import pandas as pd

def get_alumnos_con_DESEMPEÑO(dataframe):
    return dataframe[dataframe['DESEMPEÑO'] != '-']