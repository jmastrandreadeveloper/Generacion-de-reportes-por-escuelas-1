import pandas as pd
import os
import sys
import json

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..' ))
sys.path.append(project_root)
import src.tools.utils as u
import src.modelos.Libs.validar_columna as valCols
from  src.modelos.Libs.filtrado_condicional import aplicar_condiciones_avanzadas

def contar_alumnos_por_escuela_curso_y_division______group(dataframe):
    required_columns = ['Escuela_ID', 'Curso ', 'División', 'Alumno_ID']

    # Validar las columnas requeridas
    missing_columns = valCols.validar_columnas(dataframe, required_columns)

    if missing_columns:
        raise ValueError(f'Columnas faltantes en el DataFrame: {{missing_columns}}')

    result = dataframe.groupby(['Escuela_ID', 'Curso ', 'División']).agg({'Alumno_ID': 'count'})
    result.reset_index(inplace=True)
    result.rename(columns={'Alumno_ID': 'matricula_por_escuela_curso_y_division'}, inplace=True)
    return result

def contar_alumnos_por_escuela_curso_y_division_sin_duplicados_de_alumnos_group(dataframe):
    required_columns = ['Escuela_ID', 'Curso ', 'División', 'Alumno_ID']

    # Validar las columnas requeridas
    missing_columns = valCols.validar_columnas(dataframe, required_columns)

    if missing_columns:
        raise ValueError(f'Columnas faltantes en el DataFrame: {missing_columns}')

    # Eliminar duplicados de alumnos dentro de la misma escuela, curso y división
    dataframe_sin_duplicados = dataframe.drop_duplicates(subset=['Escuela_ID', 'Curso ', 'División', 'Alumno_ID'])

    # Contar alumnos únicos por grupo
    result = dataframe_sin_duplicados.groupby(['Escuela_ID', 'Curso ', 'División']).agg({'Alumno_ID': 'count'})

    result.reset_index(inplace=True)
    result.rename(columns={'Alumno_ID': 'matricula_por_escuela_curso_y_division'}, inplace=True)

    return result

def contar_alumnos_por_escuela_curso_y_division______filter(Escuela_ID, dataframe, show_index=True, columns=None, orientacion='records', condiciones=None):
    try:
        if Escuela_ID not in dataframe['Escuela_ID'].unique():
            return []

        dFrame_filtrado = dataframe[dataframe['Escuela_ID'] == Escuela_ID]
        if condiciones:
            dFrame_filtrado = aplicar_condiciones_avanzadas(dFrame_filtrado, condiciones)

        if columns:
            missing_columns = set(columns) - set(dFrame_filtrado.columns)
            if missing_columns:
                raise ValueError(f'Columnas faltantes en el DataFrame filtrado: {missing_columns}')
            dFrame_filtrado = dFrame_filtrado[columns]

        if not show_index:
            dFrame_filtrado = dFrame_filtrado.reset_index(drop=True)

        return dFrame_filtrado.to_dict(orient=orientacion)
    except Exception as e:
        raise ValueError(f'Error al filtrar el DataFrame: {e}')
    

# Llamar a la función de prueba si el script se ejecuta directamente
if __name__ == '__main__':
    Escuela_ID = 989  # Reemplaza con un ID de escuela válido
    PATH_file = 'data/processed/transformed/Nominal/df_nominal_matemática_cantidad_de_alumnos_por_escuela_curso_y_división.csv'
    csv_path = os.path.join(project_root, PATH_file)
    dataFrame = u.cargar_csv(csv_path)
    
    # declaro algunas condiciones adicionales para el filtrado final
    condiciones = {
        "Curso ": ["1°"],  # Cursos 2° o 5°
        #"matricula_por_escuela_curso_y_division": {"range": [15, 90]},  # Entre 15 y 90 alumnos
        #"División": ["A", "B"], # División A o B
        "AND": True  # Lógica AND ,  "AND": False  # Lógica OR
    }

    data = contar_alumnos_por_escuela_curso_y_division______filter(
        Escuela_ID, # la clave a buscar
        dataFrame, # el dataframe
        True, # se resetea el índice ? 
        ['Curso ', 'División' , 'matricula_por_escuela_curso_y_division' , ], # qué columnas quiero mostrar 
        'records', # Opciones: 'dict', 'list', 'series', 'split', 'records', 'index'
        condiciones=condiciones # le paso condiciones adicionales al resultado final o None
    )
    
    print(json.dumps(
        data,
        indent=4,
        ensure_ascii=False))
    
    print('...fin..!')

