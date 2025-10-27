# ESTA FUNCIÓN UNE VARIOS DATAFRAMES DE ALUMNOS POR ALUMNO_ID
# SE USA PARA OBTENER LISTADOS DE ALUMNOS CON MEDICIONES DE PALABRAS DE DIFERENTES OPERATIVOS
import os
import sys
import json
import ast  # Para convertir strings en diccionarios
import pandas as pd
import numpy as np

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..' , '..'))
print('project_root : ', project_root)
sys.path.append(project_root)

import src.tools.utils as u
from src.tools.print_dataframe import print_dataframe as printDF 

# def enforce_column_types(df, column_types):
#     """
#     Fuerza los valores de las columnas del DataFrame a los tipos de datos especificados.
    
#     :param df: DataFrame de entrada.
#     :param column_types: Diccionario con las columnas y sus tipos deseados, 
#                          por ejemplo: {'columna1': int, 'columna2': float}
#     :return: DataFrame con las columnas convertidas a los tipos especificados.
#     """
#     for col, dtype in column_types.items():
#         if col in df.columns:
#             try:
#                 # Reemplazar '-' por NaN en columnas numéricas antes de convertir
#                 if pd.api.types.is_numeric_dtype(dtype):
#                     df.loc[:, col] = pd.to_numeric(df[col], errors="coerce")
                
#                 # Intentar convertir la columna al tipo especificado
#                 df.loc[:, col] = df[col].astype(dtype, errors="ignore")

#             except Exception as e:
#                 print(f"⚠️ Advertencia: No se pudo convertir '{col}' a {dtype}. Error: {e}")

#     return df

def enforce_column_types(df, column_types):
    """
    Fuerza los valores de las columnas del DataFrame a los tipos de datos especificados.
    
    :param df: DataFrame de entrada.
    :param column_types: Diccionario con las columnas y sus tipos deseados, 
                         por ejemplo: {'columna1': int, 'columna2': float}
    :return: DataFrame con las columnas convertidas a los tipos especificados.
    """
    for col, dtype in column_types.items():
        if col in df.columns:
            try:
                df[col] = df[col].astype(dtype)
            except ValueError:
                print(f"Advertencia: No se pudo convertir la columna '{col}' al tipo {dtype}. Verifica los datos.")
    
    return df

def forzar_tipo_columna_con_guion(df, columnas_tipo):
    """
    Fuerza los tipos de datos de las columnas especificadas, pero mantiene los valores '-' sin cambios.
    
    :param df: DataFrame de entrada.
    :param columnas_tipo: Diccionario con las columnas y los tipos deseados, 
                           por ejemplo: {'columna1': int, 'columna2': float}.
    :return: DataFrame con las columnas convertidas al tipo especificado.
    """
    for col, dtype in columnas_tipo.items():
        if col in df.columns:
            # Función que convierte los valores sin afectar el guion '-'
            df[col] = df[col].apply(lambda x: x if x == "-" else dtype(x) if pd.notna(x) else x)
    
    return df



# def unir_dataframes_nominales_por_Columna(diccionario_DataFrames, common_column, show_columns, column_types):
#     df_list = []  # Lista de DataFrames procesados

#     # Verificar nombres de columnas antes de comenzar
#     print("Columnas en cada DataFrame antes de procesar:")
#     for key, (df, rename_dict) in diccionario_DataFrames.items():
#         print(f"\n{key}: {df.columns.tolist()}")

#     # Procesar cada DataFrame
#     for key, (df, rename_dict) in diccionario_DataFrames.items():
#         df = df.rename(columns=rename_dict)  # Renombrar columnas según el diccionario
#         columnas_a_mantener = list(set([common_column] + show_columns))  # Asegurar columnas necesarias
#         df = df[columnas_a_mantener] if all(col in df.columns for col in columnas_a_mantener) else df  # Filtrar
#         df_list.append(df)  # Guardar el DataFrame procesado

#     # Tomamos el último DataFrame como base
#     df_base = df_list[-1].copy()

#     print("\nColumnas en df_base después de copiar el último DataFrame:", df_base.columns.tolist())

#     # Unimos los demás DataFrames sobre el último
#     for df in df_list[:-1]:
#         df_base = df_base.merge(df, on=common_column, how="left", suffixes=("", "_dup"))

#     u.guardar_dataframe_a_csv(df_base,'/data/processed/transformed/Fluidez/'  + '_01-UNION_DATAFRAMES_TRES_OPERATIVOS_2024_2025.csv')
    
    
#     print("\nColumnas en df_base después del merge:", df_base.columns.tolist())

#     # Asegurar que todas las columnas de `show_columns` estén presentes en `df_base`
#     for col in show_columns:
#         if col not in df_base.columns:
#             df_base[col] = "-"

#     u.guardar_dataframe_a_csv(df_base,'/data/processed/transformed/Fluidez/'  + '_02-SHOW COLUMNS_DATAFRAMES_TRES_OPERATIVOS_2024_2025.csv')

#     print("\nColumnas en df_base después de agregar show_columns:", df_base.columns.tolist())

#     # Rellenar datos faltantes solo si la columna ya existe
#     for col in df_base.columns:
#         if col in show_columns:
#             for df in df_list[:-1]:
#                 if col in df.columns:
#                     df_base[col] = df_base[col].fillna(df[col])

#     # Reemplazar valores faltantes con '-'
#     for col in df_base.columns:
#         if col not in show_columns:
#             df_base[col].fillna("-", inplace=True)

#     # Aplicar tipos de datos a las columnas
#     df_base = enforce_column_types(df_base, column_types)

#     return df_base[show_columns] if show_columns else df_base

def unir_dataframes_nominales_por_Columna(diccionario_DataFrames, common_column, show_columns, column_types):
    df_list = []  # Lista de DataFrames procesados

    # Procesar cada DataFrame
    for key, (df, rename_dict) in diccionario_DataFrames.items():
        df = df.rename(columns=rename_dict)  # Renombrar columnas según el diccionario
        columnas_a_mantener = list(set([common_column] + show_columns))  # Asegurar columnas necesarias
        df = df[columnas_a_mantener] if all(col in df.columns for col in columnas_a_mantener) else df  # Filtrar
        df_list.append(df)  # Guardar el DataFrame procesado

    # Tomamos el último DataFrame como base
    df_base = df_list[-1].copy()

    # Unimos los demás DataFrames sobre el último
    for df in df_list[:-1]:
        df_base = df_base.merge(df, on=common_column, how="left", suffixes=("", "_dup"))
    
    # Eliminar las columnas duplicadas (_dup) y mantener las originales del último DataFrame
    df_base = df_base.loc[:, ~df_base.columns.str.endswith("_dup")]

    # Filtrar solo las columnas en show_columns
    columnas_finales = [common_column] + [col for col in show_columns if col in df_base.columns]
    df_base = df_base[columnas_finales]

    # Si alguna columna en show_columns no existe, agregarla con "-"
    for col in show_columns:
        if col not in df_base.columns:
            df_base[col] = "-"
    
    # Eliminar columnas repetidas, conservando solo la primera aparición
    df_base = df_base.loc[:, ~df_base.columns.duplicated()]

    # rellenar con - las columnas vacias
    df_filled = df_base.applymap(lambda x: "-" if pd.isna(x) or x == "" else x)    

    # Aplicar tipos de datos a las columnas
    df_typed = forzar_tipo_columna_con_guion(df_filled, column_types)    

    return df_typed


#esto es para probar
if __name__ == '__main__':

    # LEER -OPERATIVO 1 AÑO ANTERIOR MAYO APROX
    PATH_file_df_Fluidez_1_alumnos_con_MÁXIMA_cant_palabras = 'data/processed/transformed/Fluidez/df_Fluidez_1_alumnos_con_MÁXIMA_cant_palabras.csv'
    csv_path_df_Fluidez_1_alumnos_con_MÁXIMA_cant_palabras = os.path.join(project_root, PATH_file_df_Fluidez_1_alumnos_con_MÁXIMA_cant_palabras)
    dataFrame_df_Fluidez_1_alumnos_con_MÁXIMA_cant_palabras = u.cargar_csv(csv_path_df_Fluidez_1_alumnos_con_MÁXIMA_cant_palabras)

    # LEER -OPERATIVO 2 ÚLTMO AÑO NOVIEMBRER APROX
    PATH_file_df_Fluidez_2_alumnos_con_MÁXIMA_cant_palabras = 'data/processed/transformed/Fluidez/df_Fluidez_2_alumnos_con_MÁXIMA_cant_palabras.csv'
    csv_path_df_Fluidez_2_alumnos_con_MÁXIMA_cant_palabras = os.path.join(project_root, PATH_file_df_Fluidez_2_alumnos_con_MÁXIMA_cant_palabras)
    dataFrame_df_Fluidez_2_alumnos_con_MÁXIMA_cant_palabras = u.cargar_csv(csv_path_df_Fluidez_2_alumnos_con_MÁXIMA_cant_palabras)

    # LEER -OPERATIVO 3 AÑO ACTUAL MAYO APROX
    PATH_file_df_Fluidez_3_alumnos_con_MÁXIMA_cant_palabras = 'data/processed/transformed/Fluidez/df_Fluidez_3_alumnos_con_MÁXIMA_cant_palabras.csv'
    csv_path_df_Fluidez_3_alumnos_con_MÁXIMA_cant_palabras = os.path.join(project_root, PATH_file_df_Fluidez_3_alumnos_con_MÁXIMA_cant_palabras)
    dataFrame_df_Fluidez_3_alumnos_con_MÁXIMA_cant_palabras = u.cargar_csv(csv_path_df_Fluidez_3_alumnos_con_MÁXIMA_cant_palabras)

    data_dict_1 = {
        'Primera_Medición_Año_Anterior':[
                dataFrame_df_Fluidez_1_alumnos_con_MÁXIMA_cant_palabras
                ,
                {'Cant. palabras' :  'Cant. palabras 1° med. 2024' , 'DESEMPEÑO' : 'Desemp. 1° med. 2024' },
        ]
        ,
        'ültima_Medición_Año_Anterior':[
                dataFrame_df_Fluidez_2_alumnos_con_MÁXIMA_cant_palabras
                ,
                {'Cant. palabras' :  'Cant. palabras 3° med. 2024' , 'DESEMPEÑO' : 'Desemp. 3° med. 2024' } ,
        ]
        ,
        'Primera_Medición_Año_Actual':[
                dataFrame_df_Fluidez_3_alumnos_con_MÁXIMA_cant_palabras
                ,
                {'Cant. palabras' :  'Cant. palabras 1° med. 2025'   , 'DESEMPEÑO' : 'Desemp. 1° med. 2025' },
        ]
        ,       
    }

    union = pd.DataFrame()

    
    union = unir_dataframes_nominales_por_Columna(
        data_dict_1 , 
        'Alumno_ID' , 
        ['Alumno_ID', 'Apellido', 'Nombre', 'Escuela_ID', 'Curso ', 'División', 'Cant. palabras 1° med. 2024' , 'Cant. palabras 3° med. 2024' ,  'Cant. palabras 1° med. 2025' , 'Desemp. 1° med. 2025' ],
        {'Alumno_ID' : int, 'Apellido' : str, 'Nombre' : str , 'Escuela_ID' : int , 'Curso ' : str , 'División' : str , 'Cant. palabras 1° med. 2024' : int , 'Cant. palabras 3° med. 2024' : int ,  'Cant. palabras 1° med. 2025' : int , 'Desemp. 1° med. 2025' : str} 
    )
    #u.guardar_dataframe_a_csv(union,'/data/processed/transformed/Fluidez/'  + '_UNION_DATAFRAMES_TRES_OPERATIVOS_2024_2025.csv')

    printDF('union ' , union)

    for col in union.columns:
        print(f"Columna: {col}, Tipo de dato: {union[col].dtype}")  
