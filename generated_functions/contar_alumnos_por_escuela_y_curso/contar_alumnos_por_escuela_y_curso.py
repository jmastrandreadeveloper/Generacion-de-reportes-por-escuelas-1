import pandas as pd

def contar_alumnos_por_escuela_y_curso_group(dataframe):
    required_columns = ['Escuela_ID', 'CURSO_NORMALIZADO', 'Alumno_ID']
    missing_columns = [col for col in required_columns if col not in dataframe.columns]
    if not missing_columns:
        result = dataframe.groupby(['Escuela_ID', 'CURSO_NORMALIZADO']).agg({'Alumno_ID': 'count'})
        return result.reset_index()
    else:
        raise ValueError(f'Las columnas especificadas no existen en el dataframe. Columnas faltantes: {missing_columns}')

