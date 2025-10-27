import pandas as pd
import os
import sys
import json

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..' ))
sys.path.append(project_root)
import src.tools.utils as u
import src.modelos.Libs.validar_columna as valCols
from  src.modelos.Libs.filtrado_condicional import aplicar_condiciones_avanzadas

def contar_alumnos_por_nivel_y_curso______group(dataframe):
    required_columns = ['Nivel_Unificado', 'Curso ', 'Alumno_ID']

    # Validar las columnas requeridas
    missing_columns = valCols.validar_columnas(dataframe, required_columns)

    if missing_columns:
        raise ValueError(f'Columnas faltantes en el DataFrame: {{missing_columns}}')

    result = dataframe.groupby(['Nivel_Unificado', 'Curso ']).agg({'Alumno_ID': 'count'})
    result.reset_index(inplace=True)
    result.rename(columns={'Alumno_ID': 'matricula_por_nivel_y_curso'}, inplace=True)
    return result

def contar_alumnos_por_nivel_y_curso______filter(CURSO_NORMALIZADO, dataframe, show_index=True, columns=None, orientacion='records', condiciones=None):
    try:
        if CURSO_NORMALIZADO not in dataframe['Curso '].unique():
            return []

        dFrame_filtrado = dataframe[dataframe['Curso '] == CURSO_NORMALIZADO]
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
    CURSO_NORMALIZADO = '2°'  
    PATH_file = 'data/processed/transformed/Nominal/df_nominal_cantidad_de_alumnos_por_nivel_y_curso.csv'
    csv_path = os.path.join(project_root, PATH_file)
    dataFrame = u.cargar_csv(csv_path)
    
    # declaro algunas condiciones adicionales para el filtrado final
    condiciones = {
        "Nivel_Unificado": ["Secundario"],
    }

    data = contar_alumnos_por_nivel_y_curso______filter(
        CURSO_NORMALIZADO, # la clave a buscar
        dataFrame, # el dataframe
        True, # se resetea el índice ? 
        ['Curso ', 'matricula_por_nivel_y_curso' , ], # qué columnas quiero mostrar 
        'records', # Opciones: 'dict', 'list', 'series', 'split', 'records', 'index'
        condiciones=condiciones # le paso condiciones adicionales al resultado final
    )
    
    print(json.dumps(
        data,
        indent=4,
        ensure_ascii=False))
    
    print('...fin..!')
