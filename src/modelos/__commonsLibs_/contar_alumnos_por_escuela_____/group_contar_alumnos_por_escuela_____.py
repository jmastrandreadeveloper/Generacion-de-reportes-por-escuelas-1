import pandas as pd
import os
import sys
import json

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..' ))
sys.path.append(project_root)
import src.tools.utils as u
import src.modelos.Libs.validar_columna as valCols
from  src.modelos.Libs.filtrado_condicional import aplicar_condiciones_avanzadas

# def contar_alumnos_por_escuela______group(dataframe):
#     required_columns = ['Escuela_ID', 'Alumno_ID']

#     # Validar las columnas requeridas
#     missing_columns = valCols.validar_columnas(dataframe, required_columns)

#     if missing_columns:
#         raise ValueError(f'Columnas faltantes en el DataFrame: {{missing_columns}}')

#     result = dataframe.groupby(['Escuela_ID']).agg({'Alumno_ID': 'count'})
#     result.reset_index(inplace=True)
#     result.rename(columns={'Alumno_ID': 'matricula_por_escuela'}, inplace=True)
#     return result

def contar_alumnos_por_escuela______group(dataframe):
    required_columns = ['Escuela_ID', 'Alumno_ID']

    # Validar las columnas requeridas
    missing_columns = valCols.validar_columnas(dataframe, required_columns)

    if missing_columns:
        raise ValueError(f'Columnas faltantes en el DataFrame: {missing_columns}')

    # Contar alumnos únicos por escuela
    result = (
        dataframe
        .groupby('Escuela_ID')
        .agg({'Alumno_ID': 'nunique'})
        .reset_index()
        .rename(columns={'Alumno_ID': 'matricula_por_escuela'})
    )

    return result


def contar_alumnos_por_escuela______filter(Escuela_ID, dataframe, show_index=True, columns=None, orientacion='records', condiciones=None):
    try:
        # Filtramos el DataFrame por Escuela_ID (aunque no exista)
        dFrame_filtrado = dataframe[dataframe['Escuela_ID'] == Escuela_ID]

        # Aplicamos condiciones adicionales si hay
        if condiciones:
            dFrame_filtrado = aplicar_condiciones_avanzadas(dFrame_filtrado, condiciones)

        # Si no hay datos, devolvemos la estructura con matrícula en 0
        if dFrame_filtrado.empty:
            return [{"Escuela_ID": Escuela_ID, "matricula_por_escuela": 0}]

        # Si se especifican columnas, verificamos que existan
        if columns:
            missing_columns = set(columns) - set(dFrame_filtrado.columns)
            if missing_columns:
                raise ValueError(f'Columnas faltantes en el DataFrame filtrado: {missing_columns}')
            dFrame_filtrado = dFrame_filtrado[columns]

        # Si show_index es False, quitamos el índice
        if not show_index:
            dFrame_filtrado = dFrame_filtrado.reset_index(drop=True)

        return dFrame_filtrado.to_dict(orient=orientacion)

    except Exception as e:
        raise ValueError(f'Error al filtrar el DataFrame: {e}')

    
# def contar_alumnos_por_escuela______filter(Escuela_ID, dataframe, show_index=True, columns=None, orientacion='records', condiciones=None):
#     try:
#         if Escuela_ID not in dataframe['Escuela_ID'].unique():
#             return 0  # No se encuentra el ID

#         dFrame_filtrado = dataframe[dataframe['Escuela_ID'] == Escuela_ID]

#         if condiciones:
#             dFrame_filtrado = aplicar_condiciones_avanzadas(dFrame_filtrado, condiciones)

#         if dFrame_filtrado.empty:
#             return 0  # No hay datos después de aplicar condiciones

#         if columns:
#             missing_columns = set(columns) - set(dFrame_filtrado.columns)
#             if missing_columns:
#                 raise ValueError(f'Columnas faltantes en el DataFrame filtrado: {missing_columns}')
#             dFrame_filtrado = dFrame_filtrado[columns]

#         if not show_index:
#             dFrame_filtrado = dFrame_filtrado.reset_index(drop=True)

#         return dFrame_filtrado.to_dict(orient=orientacion)

    except Exception as e:
        raise ValueError(f'Error al filtrar el DataFrame: {e}')
    
# Llamar a la función de prueba si el script se ejecuta directamente
if __name__ == '__main__':
    Escuela_ID = 5236# 5236  # Reemplaza con un ID de escuela válido
    PATH_file = 'data/processed/transformed/Fluidez/df_Fluidez_3_cantidad_de_alumnos_por_escuela.csv'
    csv_path = os.path.join(project_root, PATH_file)
    dataFrame = u.cargar_csv(csv_path)
    

    # declaro algunas condiciones adicionales para el filtrado final
    condiciones = {       
        
    }

    data = contar_alumnos_por_escuela______filter(
        Escuela_ID, # la clave a buscar
        dataFrame, # el dataframe
        True, # se resetea el índice ? 
        ['Escuela_ID',  'matricula_por_escuela' , ], # qué columnas quiero mostrar 
        'records', # Opciones: 'dict', 'list', 'series', 'split', 'records', 'index'
        condiciones=None # le paso condiciones adicionales al resultado final o None
    )
    print('el valor de matricula_por_escuela para ese Escuela_ID es  ' , data[0]['matricula_por_escuela'])
    
    print(json.dumps(
        data,
        indent=4,
        ensure_ascii=False))
    
    print('...fin..!')

