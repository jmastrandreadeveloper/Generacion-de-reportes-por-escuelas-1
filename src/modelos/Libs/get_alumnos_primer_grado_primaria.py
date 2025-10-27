def get_alumnos_primer_grado_primaria(dataframe):
    return dataframe[
        (dataframe['CURSO_NORMALIZADO'] == '1°') & 
        (dataframe['Nivel'] == 'Primario')
    ].copy()