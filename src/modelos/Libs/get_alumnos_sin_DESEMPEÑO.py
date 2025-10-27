def get_alumnos_sin_DESEMPEÑO(dataframe):
    return dataframe[dataframe['DESEMPEÑO'] == '-']