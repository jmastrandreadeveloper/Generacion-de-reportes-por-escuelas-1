# esta función genera tablas donde existe una columna que tiene todos los cursos de la escuela
# y en las otrass columnas contendrá diferentes tipos de datos de acuerdo a lo que se le envíe 
# dentro de los parámetros, 
# los datos que recibirá son listas y diccionarios que ya han sido procesados

# la forma será la siguiente:
# un diccionario que contiene en la clave el nombre de la columna
# en los datos asociados a la clave contendrá o una lista u otros diccionarios
import os
import sys
import numpy
import json
import pandas as pd

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..' ))
sys.path.append(project_root)

from src.modelos.__commonsLibs_.obtener_lista_de_cursos_normalizados.group_df_lista_de_cursos_normalizados import filter_df_lista_de_cursos_normalizados 
from src.modelos.__commonsLibs_.contar_alumnos_por_escuela_y_curso_____.group_contar_alumnos_por_escuela_y_curso_____ import contar_alumnos_por_escuela_y_curso______filter
from src.modelos.Libs.convertir_diccionario_a_lista import convertir_diccionario_a_lista
from src.modelos.Libs.totalizar_columnas import totalizar_columnas

import src.tools.utils as u

def unir_dataframes_por_curso(data_dict):
    """
    Une los DataFrames del diccionario data_dict usando 'CURSO_NORMALIZADO' como clave común,
    manteniendo los nombres de las claves del diccionario como nombres de columna.
    También convierte los valores a enteros, elimina NaN reemplazándolos con 0 y agrega una fila con los totales.

    Parámetros:
        data_dict (dict): Diccionario donde cada clave tiene un DataFrame con 'CURSO_NORMALIZADO'.

    Retorna:
        pd.DataFrame: DataFrame final con valores combinados, en enteros y con una fila de totales.
    """
    df_final = None

    for key, df in data_dict.items():
        if isinstance(df, pd.DataFrame):
            # Buscar la columna de valores (excluyendo 'Escuela_ID' y 'CURSO_NORMALIZADO')
            value_col = [col for col in df.columns if col not in ['Escuela_ID', 'CURSO_NORMALIZADO']]
            if value_col:
                df = df.rename(columns={value_col[0]: key})
            
            # Eliminar 'Escuela_ID' para evitar duplicaciones
            df = df.drop(columns=['Escuela_ID'], errors='ignore')

            # Unir DataFrames sucesivamente
            if df_final is None:
                df_final = df
            else:
                df_final = pd.merge(df_final, df, on='CURSO_NORMALIZADO', how='outer')

    # Reemplazar NaN con 0 y convertir todas las columnas numéricas a enteros
    df_final = df_final.fillna(0).astype({col: int for col in df_final.columns if col != 'CURSO_NORMALIZADO'})

    # Agregar fila con los totales
    total_row = df_final.drop(columns=['CURSO_NORMALIZADO']).sum(numeric_only=True)
    total_row['CURSO_NORMALIZADO'] = 'TOTAL'
    #df_final = pd.concat([df_final, pd.DataFrame([total_row])], ignore_index=True)

    return df_final , total_row

# Llamar a la función de prueba si el script se ejecuta directamente
if __name__ == '__main__':
    Escuela_ID = 9  # Reemplaza con un ID de escuela válido
    
    # lista de cursos por escuela
    PATH_file_df_Escuela_ID_CURSO_NORMALIZADO_list = 'data/processed/transformed/Nominal/df_nominal_df_Escuela_ID_CURSO_NORMALIZADO_list.csv'
    csv_path_PATH_file_df_nominal_df_Escuela_ID_CURSO_NORMALIZADO_list = os.path.join(project_root, PATH_file_df_Escuela_ID_CURSO_NORMALIZADO_list)
    df_nominal_df_Escuela_ID_CURSO_NORMALIZADO_list = u.cargar_csv_2(csv_path_PATH_file_df_nominal_df_Escuela_ID_CURSO_NORMALIZADO_list)
    
    # la matrícula por curso del archivo de fluidez lectora total con alumnos incluidos = Si y alumnos con y sin desempeño
    PATH_file_df_Fluidez_1_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count = 'data/processed/transformed/Fluidez/df_Fluidez_1_cantidad_de_alumnos_por_escuela_y_curso.csv'
    csv_path_PATH_file_df_alumnos_con_DESEMPEÑO_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count = os.path.join(project_root, PATH_file_df_Fluidez_1_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count)
    df_Fluidez_1_df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count = u.cargar_csv_2(csv_path_PATH_file_df_alumnos_con_DESEMPEÑO_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count)

    # en esta parte se deben seguir agregando las otras columnas que queremos que salgan..

    # alumnos con DESEMPEÑO

    # alumnos con SIN DESEMPEÑO

    # alumnos con > 300 palabras
    
    
    # incluids = SI
    PATH_file_df_Fluidez_1_df_alumnos_incluidos_SI_FL_1_df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count = 'data/processed/transformed/Fluidez/df_Fluidez_1_cantidad_de_alumnos_incluidos_SI_por_escuela_y_curso.csv'
    csv_path_PATH_file_df_Fluidez_1_df_alumnos_incluidos_SI_FL_1_df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count = os.path.join(project_root, PATH_file_df_Fluidez_1_df_alumnos_incluidos_SI_FL_1_df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count)
    df_Fluidez_1_df_alumnos_incluidos_SI_FL_1_df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count = u.cargar_csv_2(csv_path_PATH_file_df_Fluidez_1_df_alumnos_incluidos_SI_FL_1_df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count)

    # incluids = NO
    PATH_file_df_Fluidez_1_df_alumnos_incluidos_NO_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count = 'data/processed/transformed/Fluidez/df_Fluidez_1_cantidad_de_alumnos_incluidos_NO_por_escuela_y_curso.csv'
    csv_path_PATH_file_df_Fluidez_1_df_alumnos_incluidos_NO_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count = os.path.join(project_root, PATH_file_df_Fluidez_1_df_alumnos_incluidos_NO_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count)
    df_Fluidez_1_df_alumnos_incluidos_NO_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count = u.cargar_csv_2(csv_path_PATH_file_df_Fluidez_1_df_alumnos_incluidos_NO_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count)

    # incluids = SI

    # matrícula por curso?



    data_dict = {        
        'Curso'                 : filter_df_lista_de_cursos_normalizados(Escuela_ID , df_nominal_df_Escuela_ID_CURSO_NORMALIZADO_list),
        'Alumnos con Desempeño' : pd.DataFrame(contar_alumnos_por_escuela_y_curso______filter(Escuela_ID , df_Fluidez_1_df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count)),
        'Alumnos incluidos SI'  : pd.DataFrame(contar_alumnos_por_escuela_y_curso______filter(Escuela_ID , df_Fluidez_1_df_alumnos_incluidos_SI_FL_1_df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count)),
        'Alumnos incluidos NO'  : pd.DataFrame(contar_alumnos_por_escuela_y_curso______filter(Escuela_ID , df_Fluidez_1_df_alumnos_incluidos_NO_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count)),        
    }

    [tabla_final, total_row] = unir_dataframes_por_curso(data_dict)
    print(tabla_final)
    print(total_row)

    # Ver el resultado
    print(json.dumps(tabla_final.to_dict(orient='records'),indent=4,ensure_ascii=False)) # Opciones: 'dict', 'list', 'series', 'split', 'records', 'index'

    # HACER QUE LOS TOTALES SE VEAN POR SEPARADO

    # HACER QUE UNA TABLA QUE PUEDA UNIR POR UNA COLUMNA EN COMUN









    # print(pd.DataFrame(contar_alumnos_por_escuela_y_curso______filter(Escuela_ID , df_Fluidez_1_df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count)))
    
    # [resultado_listas,resultado_diccionarios] = construir_tabla('CURSO_NORMALIZADO','matricula_por_escuela_y_curso',data_dict)
    # #print(resultado_listas)
    # #print(resultado_diccionarios)

    # resultado_listas_json = convertir_diccionario_a_lista(resultado_listas)
    # resultado_listas_json_con_totales = totalizar_columnas(resultado_listas_json)
    # # el último diccionario tiene el total de las columnas!
    # print(resultado_listas_json_con_totales)


# entrada = {
#     "Curso": ["2°", "3°", "4°", "5°", "6°", "7°"],
#     "Matriculas": [{"Curso": "2°", "Matrícula": 88}, {"Curso": "3°", "Matrícula": 97},
#                    {"Curso": "4°", "Matrícula": 110}, {"Curso": "5°", "Matrícula": 113},
#                    {"Curso": "6°", "Matrícula": 113}, {"Curso": "7°", "Matrícula": 115}],
#     'Alumnos con Desempeño' : [{"Curso": "2°", "Matrícula": 188}, 
#                    {"Curso": "6°", "Matrícula": 113}, {"Curso": "7°", "Matrícula": 115}],
#     'Alumnos sin Desempeño' : [{"Curso": "4°", "Matrícula": 110}, {"Curso": "5°", "Matrícula": 113},
#                     {"Curso": "7°", "Matrícula": 115}]
# }

# def construir_tabla(main_base_key , sub_base_key , data_dict : dict,) -> list:
#     """
#     es muy importante tener en cuenta lo que hacen main_base_key , sub_base_key; actuan como 
#     los indicadores que deben estar dentro de los diccionarios que van a usarse para construir las columnas
#     de la tabla
#     esta función va a devolver en dos formatos los datos a partir del formato 'resultado_listas', se puede construir
#     otro formato igual a lo que necesitamos como los datos de un json para ser filtrado!
#     """
#     # main_base_key , sub_base_key representan la clave principal y la clave sub base para la construcción
#     # de la tabla, por ejemplo si se trata de Curso, significa que la primera columna va a ser Curso y que dentro
#     # de los diccionario que etán dentro de la listas de las otras columnas va a aparecer también
#     # mientras que la sub_base_key será la segunda clave de los diccionarios dentro de la lista pasada como columna
#     # Extraer la lista de cursos del primer elemento del diccionario
#     cursos = data_dict.get(main_base_key, [])
    
#     # Diccionarios para almacenar resultados, comenzando con 'CURSO_NORMALIZADO'
#     resultado_listas = {main_base_key: cursos}
#     resultado_diccionarios = {main_base_key: {curso: curso for curso in cursos}}
    
#     # Procesar todas las claves excepto 'CURSO_NORMALIZADO'
#     for clave, lista_matriculas in data_dict.items():
#         if isinstance(lista_matriculas, str):  # Si es un string, convertirlo
#             lista_matriculas = ast.literal_eval(lista_matriculas)

#         # Ahora puedes procesar con seguridad
#         curso_a_matricula = {item[main_base_key]: item[sub_base_key] for item in lista_matriculas}
#     # for clave, lista_matriculas in data_dict.items():
#     #     if clave == main_base_key:
#     #         continue
        
#     #     # Crear un diccionario para los valores de matrícula de cada CURSO_NORMALIZADO
#     #     curso_a_matricula = {item[main_base_key]: item[sub_base_key] for item in lista_matriculas}
        
#         # Construir la lista final con los valores de matrícula o 0 si no se encuentra el CURSO_NORMALIZADO
#         resultado_listas[clave] = [curso_a_matricula.get(curso, 0) for curso in cursos]
        
#         # Construir un diccionario con los CURSO_NORMALIZADO y sus valores
#         resultado_diccionarios[clave] = {curso: curso_a_matricula.get(curso, 0) for curso in cursos}
    
#     return resultado_listas, resultado_diccionarios


# def construir_tabla(main_base_key, sub_base_key, data_dict: dict) -> tuple:
#     """
#     Construye dos formatos de tabla a partir de un diccionario de DataFrames.
    
#     Parámetros:
#     - main_base_key: Clave principal que define la primera columna (Ej: 'CURSO_NORMALIZADO').
#     - sub_base_key: Clave de la métrica dentro de cada DataFrame.
#     - data_dict: Diccionario donde las claves son nombres de métricas y los valores son DataFrames con columnas 
#       'CURSO_NORMALIZADO' y la métrica correspondiente.
    
#     Retorna:
#     - resultado_listas: Diccionario con listas, donde cada clave es una métrica y los valores son listas ordenadas.
#     - resultado_diccionarios: Diccionario anidado {clave: {curso: valor}} con las mismas métricas.
#     """
    
#     # Verificar que la clave principal está en el diccionario
#     if main_base_key not in data_dict:
#         raise KeyError(f"La clave '{main_base_key}' no está presente en el diccionario de datos.")

#     # Verificar que la clave principal sea un DataFrame válido
#     if not isinstance(data_dict[main_base_key], pd.DataFrame):
#         raise ValueError(f"La clave '{main_base_key}' debe contener un DataFrame.")

#     # Asegurar que la columna 'CURSO_NORMALIZADO' esté presente
#     if "CURSO_NORMALIZADO" not in data_dict[main_base_key].columns:
#         raise KeyError(f"La columna 'CURSO_NORMALIZADO' no está presente en el DataFrame '{main_base_key}'.")

#     # Obtener lista de cursos únicos y ordenados
#     cursos = sorted(data_dict[main_base_key]["CURSO_NORMALIZADO"].dropna().unique().tolist())

#     # Diccionarios de salida
#     resultado_listas = {main_base_key: cursos}
#     resultado_diccionarios = {main_base_key: {curso: curso for curso in cursos}}

#     # Iterar sobre las demás métricas en el diccionario
#     for clave, df in data_dict.items():
#         if clave == main_base_key:
#             continue  # Saltar la clave base
        
#         # Verificar que el valor sea un DataFrame válido
#         if not isinstance(df, pd.DataFrame):
#             raise ValueError(f"La clave '{clave}' debe contener un DataFrame.")

#         # Verificar que tenga la columna de curso y la métrica
#         if "CURSO_NORMALIZADO" not in df.columns:
#             raise KeyError(f"La columna 'CURSO_NORMALIZADO' no está en el DataFrame '{clave}'.")
#         if sub_base_key not in df.columns:
#             raise KeyError(f"La columna '{sub_base_key}' no está en el DataFrame '{clave}'.")

#         # Crear diccionario de curso -> valor métrico
#         curso_a_valor = dict(zip(df["CURSO_NORMALIZADO"], df[sub_base_key]))

#         # Construir listas y diccionarios con valores, colocando 0 si falta algún curso
#         resultado_listas[clave] = [curso_a_valor.get(curso, 0) for curso in cursos]
#         resultado_diccionarios[clave] = {curso: curso_a_valor.get(curso, 0) for curso in cursos}

#     return resultado_listas, resultado_diccionarios
