# en esta parte construimos el reporte de la medición 1 de Fluidez Lectora
# para el mes de mayo del año 2025
# leeremos los datos de la medición 1 de Fluidez Lectora
# y construiremos un reporte con los resultados obtenidos
# y lo guardaremos en un archivo de texto JSON
# para cada supervisión

import pandas as pd
import os
import sys
import json
import ast  # Para convertir strings en diccionarios
from datetime import datetime

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..' , '..' , '..'))
sys.path.append(project_root)
import src.tools.utils as u
import src.tools.prettyJSON as pJ

from src.tools.print_dataframe import print_dataframe as printDF 
import src.modelos.__commonsLibs_.dataTable.dataTable as dT3
from src.modelos.__commonsLibs_.obtener_lista_de_Escuelas_por_Supervisión.set_get_df_lista_de_Escuela_ID_por_Supervisión import get_df_escuelas_por_supervision_con_datos
import src.modelos.__commonsLibs_.contar_alumnos_por_escuela_____.group_contar_alumnos_por_escuela_____ as contar_alumnos_por_escuela # contar_alumnos_por_escuela.contar_alumnos_por_escuela______filter()
import src.modelos._Análisis_Fluidez_Lectora.contar_alumnos_por_escuela_y_desempeño.group_contar_alumnos_por_escuela_y_desempeño as contar_alumnos_por_escuela_y_desempeño #contar_alumnos_por_escuela_y_desempeño.filtrar_alumnos_por_escuela_y_desempeño_group()
import src.modelos._Análisis_Fluidez_Lectora.contar_alumnos_por_escuela_curso_y_desempeño.group_contar_alumnos_por_escuela_curso_y_desempeño as contar_alumnos_por_escuela_curso_y_desempeño # contar_alumnos_por_escuela_curso_y_desempeño.filtrar_alumnos_por_escuela_curso_y_desempeño_group()
import src.modelos.__commonsLibs_.obtener_lista_de_Supervisiones.set_get_df_lista_de_Supervisiones as get_df_lista_de_Supervisiones
import src.modelos._Análisis_Fluidez_Lectora.ordenar_por_criticidad.ordenar_dataFrame_por_nivel_de_criticidad as ordenCriticidadDataFrame
import src.modelos._Análisis_Fluidez_Lectora.calcular_desempeño_por_escuela.group_calcular_desempeño_por_escuela as desempeño_por_escuela
import src.modelos._Análisis_Fluidez_Lectora.calcular_desempeño_por_escuela_y_curso.group_calcular_desempeño_por_escuela_y_curso as porcentajeDesPorEyCur

import src._main_.Fluidez_Lectora_medición_1.Año_2025.mes_05_mayo.reporte_por_supervisión.reporte_por_supervisión_PDFs as Fluidez_Lectora_PDFs

# 1-LEER LOS ARCHIVOS NECESARIOS PARA EL REPORTE
# 1.1-Archivo de datos institucionales

PATH_file_df_nominal_df_datos_institucionales = 'data/processed/transformed/Nominal/df_nominal_df_datos_institucionales.csv'
csv_path_df_nominal_df_datos_institucionales = os.path.join(project_root, PATH_file_df_nominal_df_datos_institucionales)
dataFrame_df_nominal_df_datos_institucionales = u.cargar_csv(csv_path_df_nominal_df_datos_institucionales)
#printDF('dataFrame_df_nominal_df_datos_institucionales ' , dataFrame_df_nominal_df_datos_institucionales, )

# 1.2-Archivo alumnos por escuela
PATH_file_df_nominal_cantidad_de_alumnos_por_escuela = 'data/processed/transformed/Nominal/df_nominal_cantidad_de_alumnos_por_escuela.csv'
csv_path_df_nominal_cantidad_de_alumnos_por_escuela = os.path.join(project_root, PATH_file_df_nominal_cantidad_de_alumnos_por_escuela)
dataFrame_df_nominal_cantidad_de_alumnos_por_escuela = u.cargar_csv(csv_path_df_nominal_cantidad_de_alumnos_por_escuela)
#printDF('dataFrame_df_nominal_cantidad_de_alumnos_por_escuela ' , dataFrame_df_nominal_cantidad_de_alumnos_por_escuela, )

PATH_file_df_Fluidez_3_cantidad_de_alumnos_por_escuela = 'data/processed/transformed/Fluidez/df_Fluidez_3_cantidad_de_alumnos_por_escuela.csv'
csv_path_df_Fluidez_3_cantidad_de_alumnos_por_escuela = os.path.join(project_root, PATH_file_df_Fluidez_3_cantidad_de_alumnos_por_escuela)
dataFrame_df_Fluidez_3_cantidad_de_alumnos_por_escuela = u.cargar_csv(csv_path_df_Fluidez_3_cantidad_de_alumnos_por_escuela)

# 1.3-Archivo alumnos por escuela y desempeño
PATH_file_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_desempeño = 'data/processed/transformed/Fluidez/df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_desempeño.csv'
csv_path_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_desempeño = os.path.join(project_root, PATH_file_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_desempeño)
dataFrame_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_desempeño = u.cargar_csv(csv_path_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_desempeño)
#printDF('dataFrame_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_desempeño ' , dataFrame_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_desempeño, )

# 1.4-Archivo alumnos por escuela curso y desempeño
PATH_file_df_Fluidez_3_cantidad_de_alumnos_por_escuela_curso_y_desempeño = 'data/processed/transformed/Fluidez/df_Fluidez_3_cantidad_de_alumnos_por_escuela_curso_y_desempeño.csv'
csv_path_df_Fluidez_3_cantidad_de_alumnos_por_escuela_curso_y_desempeño = os.path.join(project_root, PATH_file_df_Fluidez_3_cantidad_de_alumnos_por_escuela_curso_y_desempeño)
dataFrame_df_Fluidez_3_cantidad_de_alumnos_por_escuela_curso_y_desempeño = u.cargar_csv(csv_path_df_Fluidez_3_cantidad_de_alumnos_por_escuela_curso_y_desempeño)
#printDF('dataFrame_df_Fluidez_3_cantidad_de_alumnos_por_escuela_curso_y_desempeño ' , dataFrame_df_Fluidez_3_cantidad_de_alumnos_por_escuela_curso_y_desempeño, )

########################
# -Archivo porcentaje de desempeño por escuela
PATH_file_df_Fluidez_3_calcular_porcentaje_desempeno_por_escuela = 'data/processed/transformed/Fluidez/df_Fluidez_3_calcular_porcentaje_desempeno_por_escuela.csv'
csv_path_df_Fluidez_3_calcular_porcentaje_desempeno_por_escuela = os.path.join(project_root, PATH_file_df_Fluidez_3_calcular_porcentaje_desempeno_por_escuela)
dataFrame_df_Fluidez_3_calcular_porcentaje_desempeno_por_escuela = u.cargar_csv(csv_path_df_Fluidez_3_calcular_porcentaje_desempeno_por_escuela)
#printDF('dataFrame_df_Fluidez_3_calcular_porcentaje_desempeno_por_escuela ' , dataFrame_df_Fluidez_3_calcular_porcentaje_desempeno_por_escuela, )

# Archivo porcentaje de desempeño por escuela y curso
PATH_file_df_Fluidez_3_calcular_porcentaje_desempeno_por_escuela_y_curso = 'data/processed/transformed/Fluidez/df_Fluidez_3_calcular_porcentaje_desempeno_por_escuela_y_curso.csv'
csv_path_df_Fluidez_3_calcular_porcentaje_desempeno_por_escuela_y_curso = os.path.join(project_root, PATH_file_df_Fluidez_3_calcular_porcentaje_desempeno_por_escuela_y_curso)
dataFrame_df_Fluidez_3_calcular_porcentaje_desempeno_por_escuela_y_curso = u.cargar_csv(csv_path_df_Fluidez_3_calcular_porcentaje_desempeno_por_escuela_y_curso)
#printDF('dataFrame_df_Fluidez_3_cantidad_de_alumnos_por_escuela_curso_y_desempeño ' , dataFrame_df_Fluidez_3_cantidad_de_alumnos_por_escuela_curso_y_desempeño, )




##########################







# 1.5-Archivo lista de supervisiones
PATH_file_df_nominal_datos_institucionales_Lista_de_Supervisiones = 'data/processed/transformed/Nominal/df_nominal_datos_institucionales_Lista_de_Supervisiones.csv'
csv_path_df_nominal_datos_institucionales_Lista_de_Supervisiones = os.path.join(project_root, PATH_file_df_nominal_datos_institucionales_Lista_de_Supervisiones)
dataFrame_df_nominal_datos_institucionales_Lista_de_Supervisiones = u.cargar_csv(csv_path_df_nominal_datos_institucionales_Lista_de_Supervisiones)
#printDF('dataFrame_df_nominal_df_datos_institucionales ' , dataFrame_df_nominal_df_datos_institucionales, )

# LEER EL ARCHIVO DE EXCEL DONDE ESTÁN TODOS LOS LINKS A LOS INFORMES DE LAS ESCUELAS
# 'E:\GitHub\python_data_analysis_v3\src\_main_\Fluidez_Lectora_medición_1\Año_2025\mes_05_mayo\data\raw\_LINKS INFORMES ESCUELA EJEMPLO.xlsx'
PATH_file_df_LINKS_A_INFORMES_DE_ESCUELAS = 'src/_main_/Fluidez_Lectora_medición_1/Año_2025/mes_05_mayo/data/raw/_LINKS INFORMES ESCUELA EJEMPLO.xlsx'
xls_path_df_LINKS_A_INFORMES_DE_ESCUELAS = os.path.join(project_root, PATH_file_df_LINKS_A_INFORMES_DE_ESCUELAS)
dataFrame_df_LINKS_A_INFORMES_DE_ESCUELAS = u.load_excel(xls_path_df_LINKS_A_INFORMES_DE_ESCUELAS)

# VARIABLES GLOBALES
# -PARA DETERMINAR SI SE PONE GRADO O CURSO DEPENDIENDO DEL NIVEL DE LA ESCUELA
tipo_grado_o_curso = ''
# -PARA CALCULAR LA FECHA EN LA QUE SE HIZO EL INFORME
hoy = datetime.now()

# recorrer la lista de supervisiones y generar un reporte para cada una
lista_de_supervisiones = get_df_lista_de_Supervisiones.get_df_lista_de_Supervisiones(dataFrame_df_nominal_datos_institucionales_Lista_de_Supervisiones , 'df_nominal')#['Supervisión'][0]


def convertir_df_a_lista_apilada(df, columna_clave='Número'):
    lista = []

    for _, fila in df.iterrows():
        obj = {
            columna_clave: str(fila[columna_clave]),
            'Avanzado': fila.get('Avanzado', 0),
            'Medio': fila.get('Medio', 0),
            'Básico': fila.get('Básico', 0),
            'Crítico': fila.get('Crítico', 0)
        }
        lista.append(obj)

    return lista

def orden_por_criticidad_multiple(df):
    return df.sort_values(
        by=['Crítico', 'Básico', 'Medio', 'Avanzado', 'Total'],
        ascending=[False, False, False, False, False]
    )


"""

import pandas as pd


# def generar_tabla_matricula_por_desempeno_y_ordenar(
#     lista_de_Escuelas_por_Supervisión,
#     dataFrame_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_desempeño,
#     contar_alumnos_por_escuela_y_desempeño,
#     ordenCriticidadDataFrame,
#     condiciones=None):

#     # condiciones = {
#     #         "DESEMPEÑO": ['Avanzado', 'Medio' , 'Básico', 'Crítico'],  # Valores a filtrar],
#     #         "AND": False  # Lógica AND ,  "AND": False  # Lógica OR
#     #     }
    


#     # Valores por defecto para las condiciones
#     if condiciones is None:
#         condiciones = {
#             "DESEMPEÑO": ['Avanzado', 'Medio', 'Básico', 'Crítico'],
#             "AND": False
#         }

#     # Lista de desempeños en el orden deseado
#     orden_desempeños = condiciones.get("DESEMPEÑO", ['Avanzado', 'Medio', 'Básico', 'Crítico'])

#     # Lista para guardar los resúmenes por escuela
#     resumen_por_escuela = []

#     for unaEscuela in lista_de_Escuelas_por_Supervisión:
#         # Filtrar y obtener datos de la escuela
#         cantidad_de_alumnos = contar_alumnos_por_escuela_y_desempeño.filtrar_alumnos_por_escuela_y_desempeño_group(
#             unaEscuela['Escuela_ID'],
#             dataFrame_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_desempeño,
#             True,
#             ['Escuela_ID', 'DESEMPEÑO', 'matricula_por_escuela_y_desempeño'],
#             'records',
#             condiciones=condiciones
#         )

#         # Inicializar estructura de una fila
#         fila_resumen = {
#             'Escuela_ID': unaEscuela['Escuela_ID'],
#             'Número': unaEscuela.get('Número', ''),
#             'Escuela': unaEscuela.get('Escuela', ''),
#             'Avanzado': 0,
#             'Medio': 0,
#             'Básico': 0,
#             'Crítico': 0,
#             'Total': 0
#         }

#         # Cargar los valores por desempeño
#         for fila in cantidad_de_alumnos:
#             desempeño = fila['DESEMPEÑO']
#             cantidad = fila['matricula_por_escuela_y_desempeño']
#             if desempeño in orden_desempeños:
#                 fila_resumen[desempeño] = cantidad
#                 fila_resumen['Total'] += cantidad

#         # Guardar fila en lista
#         resumen_por_escuela.append(fila_resumen)

#     # Crear el DataFrame
#     df_resumen = pd.DataFrame(resumen_por_escuela)

#     # Agregar fila de totales
#     totales = {
#         'Escuela_ID': 'TOTAL',
#         'Número': '',
#         'Escuela': '',
#         'Avanzado': df_resumen['Avanzado'].sum(),
#         'Medio': df_resumen['Medio'].sum(),
#         'Básico': df_resumen['Básico'].sum(),
#         'Crítico': df_resumen['Crítico'].sum()
#     }
#     totales['Total'] = (
#         totales['Avanzado'] +
#         totales['Medio'] +
#         totales['Básico'] +
#         totales['Crítico']
#     )

#     # Ordenar por criticidad
#     df_ordenado_por_criticidad = ordenCriticidadDataFrame.ordenar_por_criticidad(df_resumen)

#     # Agregar la fila de totales al final
#     df_ordenado_por_criticidad = pd.concat([df_ordenado_por_criticidad, pd.DataFrame([totales])], ignore_index=True)

#     return df_ordenado_por_criticidad

import pandas as pd
"""

def generar_tabla_matricula_por_desempeno_y_ordenar(
    lista_de_Escuelas_por_Supervisión,
    dataFrame_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_desempeño,
    contar_alumnos_por_escuela_y_desempeño,
    condiciones=None,
    orden_por_criticidad_func=None
):
    if condiciones is None:
        condiciones = {
            "DESEMPEÑO": ['Avanzado', 'Medio', 'Básico', 'Crítico'],
            "AND": False
        }

    orden_desempeños = condiciones.get("DESEMPEÑO", ['Avanzado', 'Medio', 'Básico', 'Crítico'])

    resumen_por_escuela = []

    for unaEscuela in lista_de_Escuelas_por_Supervisión:
        cantidad_de_alumnos = contar_alumnos_por_escuela_y_desempeño.filtrar_alumnos_por_escuela_y_desempeño_group(
            unaEscuela['Escuela_ID'],
            dataFrame_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_desempeño,
            True,
            ['Escuela_ID', 'DESEMPEÑO', 'matricula_por_escuela_y_desempeño'],
            'records',
            condiciones=condiciones
        )

        fila_resumen = {
            #'Escuela_ID': unaEscuela['Escuela_ID'],
            'Número': unaEscuela.get('Número', ''),
            'Escuela': unaEscuela.get('Escuela', '')[:20],
            'Avanzado': 0,
            'Medio': 0,
            'Básico': 0,
            'Crítico': 0,
            'Total': 0
        }

        for fila in cantidad_de_alumnos:
            desempeño = fila['DESEMPEÑO']
            cantidad = fila['matricula_por_escuela_y_desempeño']
            if desempeño in orden_desempeños:
                fila_resumen[desempeño] = cantidad
                fila_resumen['Total'] += cantidad

        resumen_por_escuela.append(fila_resumen)

    df_resumen = pd.DataFrame(resumen_por_escuela)

    # Calcular criticidad
    df_resumen['Criticidad'] = df_resumen['Crítico'] / df_resumen['Total']
    df_resumen['Criticidad'] = df_resumen['Criticidad'].fillna(0)

    # Usar la función de orden si se proporciona
    if orden_por_criticidad_func:
        df_ordenado = orden_por_criticidad_func(df_resumen)
    else:
        df_ordenado = df_resumen.sort_values(by=['Criticidad', 'Escuela_ID'], ascending=[False, True])

    # Fila total
    fila_total = {
        #'Escuela_ID': 'TOTAL',
        'Número': 'TOTAL',
        'Escuela': '',
        'Avanzado': df_ordenado['Avanzado'].sum(),
        'Medio': df_ordenado['Medio'].sum(),
        'Básico': df_ordenado['Básico'].sum(),
        'Crítico': df_ordenado['Crítico'].sum(),
        'Total': df_ordenado['Total'].sum()
    }

    # Eliminar criticidad antes de devolver
    df_final = pd.concat([df_ordenado.drop(columns=['Criticidad']), pd.DataFrame([fila_total])], ignore_index=True)

    return df_final



def generar_tabla_por_escuela_y_ordenar_criticidad(
    lista_de_Escuelas_por_Supervisión,
    df_desempeno,
    filtrar_desempeno_por_escuela,
    orden_por_criticidad_func=None):

    # # # Lista de desempeños en el orden deseado
    # orden_desempeños = condiciones.get("DESEMPEÑO", ['Avanzado', 'Medio', 'Básico', 'Crítico'])

    resumen_por_escuela = {}

    condiciones = {
        "DESEMPEÑO": ['Avanzado', 'Medio', 'Básico', 'Crítico'],
        "AND": False
    }
    orden_desempeños = condiciones.get("DESEMPEÑO", ['Avanzado', 'Medio', 'Básico', 'Crítico'])

    for unaEscuela in lista_de_Escuelas_por_Supervisión:
        Escuela_ID = unaEscuela['Escuela_ID']
        Escuela = unaEscuela.get('Escuela', '')[0:20]
        Número = unaEscuela.get('Número', '')

        df_filtrada = filtrar_desempeno_por_escuela(df_desempeno, Escuela_ID)

        resumen_por_escuela[Escuela_ID] = {
            'Escuela_ID': Escuela_ID,
            'Número': Número,
            'Escuela': Escuela,
            'Avanzado': 0,
            'Medio': 0,
            'Básico': 0,
            'Crítico': 0,
            'Total': 0
        }

        for _, fila in df_filtrada.iterrows():
            desempeño = fila['DESEMPEÑO']
            cantidad = fila['porcentaje_desempeno']
            if desempeño in orden_desempeños:
                resumen_por_escuela[Escuela_ID][desempeño] += cantidad
                resumen_por_escuela[Escuela_ID]['Total'] += cantidad

    df_resumen = pd.DataFrame(resumen_por_escuela.values())
    df_resumen['Criticidad'] = df_resumen['Crítico'] / df_resumen['Total']
    df_resumen['Criticidad'] = df_resumen['Criticidad'].fillna(0)

    if orden_por_criticidad_func:
        df_ordenado = orden_por_criticidad_func(df_resumen)
    else:
        df_ordenado = df_resumen.sort_values(by=['Criticidad', 'Escuela_ID'], ascending=[False, True])

    return df_ordenado.drop(columns=['Criticidad'])



# def generar_tablas_por_curso_y_ordenar_criticidad(
#     lista_de_Escuelas_por_Supervisión,
#     alumnos_por_escuela_y_curso,
#     condiciones,
#     filtrar_alumnos_por_escuela_curso_y_desempeño_group,
#     orden_por_criticidad_func=None
# ):
#     resumen_por_curso = {}

#     for unaEscuela in lista_de_Escuelas_por_Supervisión:
#         Escuela_ID = unaEscuela['Escuela_ID']
#         Escuela = unaEscuela.get('Escuela', '') 
#         Escuela = Escuela[0:20] # recorto el nombre para que puedan entrar en la tabla        
#         Número = unaEscuela.get('Número', '')

#         data = filtrar_alumnos_por_escuela_curso_y_desempeño_group(
#             Escuela_ID,
#             alumnos_por_escuela_y_curso,
#             True,
#             ['Escuela_ID', 'Curso ', 'DESEMPEÑO', 'matricula_por_escuela_curso_y_desempeño'],
#             'records',
#             condiciones
#         )

#         for fila in data:
#             curso = fila['Curso ']
#             desempeño = fila['DESEMPEÑO']
#             cantidad = fila['matricula_por_escuela_curso_y_desempeño']

#             if curso not in resumen_por_curso:
#                 resumen_por_curso[curso] = {}

#             if Escuela_ID not in resumen_por_curso[curso]:
#                 resumen_por_curso[curso][Escuela_ID] = {
#                     'Escuela_ID': Escuela_ID,
#                     'Número': Número,
#                     'Escuela': Escuela,
#                     'Curso': curso,
#                     'Avanzado': 0,
#                     'Medio': 0,
#                     'Básico': 0,
#                     'Crítico': 0,
#                     'Total': 0
#                 }

#             if desempeño in orden_desempeños:
#                 resumen_por_curso[curso][Escuela_ID][desempeño] += cantidad
#                 resumen_por_curso[curso][Escuela_ID]['Total'] += cantidad

#     # Armar un DataFrame por curso
#     tablas_por_curso = {}

#     for curso, escuelas_dict in resumen_por_curso.items():
#         df = pd.DataFrame(escuelas_dict.values())
#         df['Criticidad'] = df['Crítico'] / df['Total']
#         df['Criticidad'] = df['Criticidad'].fillna(0)

#         if orden_por_criticidad_func:
#             df_ordenado = orden_por_criticidad_func(df)
#         else:
#             df_ordenado = df.sort_values(by=['Criticidad', 'Escuela_ID'], ascending=[False, True])

#         df_ordenado = df_ordenado.drop(columns=['Criticidad'])
#         tablas_por_curso[curso] = df_ordenado

#     return tablas_por_curso

# def generar_tablas_por_curso_y_ordenar_criticidad(
#     lista_de_Escuelas_por_Supervisión,
#     alumnos_por_escuela_y_curso,
#     condiciones,
#     filtrar_alumnos_por_escuela_curso_y_desempeño_group,
#     orden_por_criticidad_func=None
# ):
#     resumen_por_curso = {}
#     orden_desempeños = condiciones.get("DESEMPEÑO", ['Avanzado', 'Medio', 'Básico', 'Crítico'])

#     for unaEscuela in lista_de_Escuelas_por_Supervisión:
#         Escuela_ID = unaEscuela['Escuela_ID']
#         Escuela = unaEscuela.get('Escuela', '')[:20]
#         Número = unaEscuela.get('Número', '')

#         data = filtrar_alumnos_por_escuela_curso_y_desempeño_group(
#             Escuela_ID,
#             alumnos_por_escuela_y_curso,
#             True,
#             ['Escuela_ID', 'Curso ', 'DESEMPEÑO', 'matricula_por_escuela_curso_y_desempeño'],
#             'records',
#             condiciones
#         )

#         for fila in data:
#             curso = fila['Curso ']
#             desempeño = fila['DESEMPEÑO']
#             cantidad = fila['matricula_por_escuela_curso_y_desempeño']

#             if curso not in resumen_por_curso:
#                 resumen_por_curso[curso] = {}

#             if Escuela_ID not in resumen_por_curso[curso]:
#                 resumen_por_curso[curso][Escuela_ID] = {
#                     'Escuela_ID': Escuela_ID,
#                     'Número': Número,
#                     'Escuela': Escuela,
#                     'Curso': curso,
#                     'Avanzado': 0,
#                     'Medio': 0,
#                     'Básico': 0,
#                     'Crítico': 0,
#                     'Total': 0
#                 }

#             if desempeño in orden_desempeños:
#                 resumen_por_curso[curso][Escuela_ID][desempeño] += cantidad
#                 resumen_por_curso[curso][Escuela_ID]['Total'] += cantidad

#     # Armar un DataFrame por curso
#     tablas_por_curso = {}

#     # obtengo la lista de los cursos y los devuelvo por acá también
#     # de esa manera puedo iterar sobre los cursos
#     lista_de_Cursos_de_la_Supervisión = []

#     for curso in sorted(resumen_por_curso.keys()):  # ← Orden ascendente de cursos
#         escuelas_dict = resumen_por_curso[curso]
#         df = pd.DataFrame(escuelas_dict.values())
#         df['Criticidad'] = df['Crítico'] / df['Total']
#         df['Criticidad'] = df['Criticidad'].fillna(0)

#         if orden_por_criticidad_func:
#             df_ordenado = orden_por_criticidad_func(df)
#         else:
#             df_ordenado = df.sort_values(by=['Criticidad', 'Escuela_ID'], ascending=[False, True])

#         df_ordenado = df_ordenado.drop(columns=['Criticidad'])
#         tablas_por_curso[curso] = df_ordenado

#         lista_de_Cursos_de_la_Supervisión.append(curso)

#     return tablas_por_curso , lista_de_Cursos_de_la_Supervisión
# def generar_tablas_por_curso_y_ordenar_criticidad(
#     lista_de_Escuelas_por_Supervisión,
#     alumnos_por_escuela_y_curso,
#     condiciones,
#     filtrar_alumnos_por_escuela_curso_y_desempeño_group,
#     orden_por_criticidad_func=None
# ):
#     resumen_por_curso = {}
#     orden_desempeños = condiciones.get("DESEMPEÑO", ['Avanzado', 'Medio', 'Básico', 'Crítico'])

#     for unaEscuela in lista_de_Escuelas_por_Supervisión:
#         Escuela_ID = unaEscuela['Escuela_ID']
#         Escuela = unaEscuela.get('Escuela', '')[:20]
#         Número = unaEscuela.get('Número', '')

#         data = filtrar_alumnos_por_escuela_curso_y_desempeño_group(
#             Escuela_ID,
#             alumnos_por_escuela_y_curso,
#             True,
#             ['Escuela_ID', 'Curso ', 'DESEMPEÑO', 'matricula_por_escuela_curso_y_desempeño'],
#             'records',
#             condiciones
#         )

#         for fila in data:
#             curso = fila['Curso ']
#             desempeño = fila['DESEMPEÑO']
#             cantidad = fila['matricula_por_escuela_curso_y_desempeño']

#             if curso not in resumen_por_curso:
#                 resumen_por_curso[curso] = {}

#             if Escuela_ID not in resumen_por_curso[curso]:
#                 resumen_por_curso[curso][Escuela_ID] = {
#                     'Escuela_ID': Escuela_ID,
#                     'Número': Número,
#                     'Escuela': Escuela,
#                     'Curso': curso,
#                     'Avanzado': 0,
#                     'Medio': 0,
#                     'Básico': 0,
#                     'Crítico': 0,
#                     'Total': 0
#                 }

#             if desempeño in orden_desempeños:
#                 resumen_por_curso[curso][Escuela_ID][desempeño] += cantidad
#                 resumen_por_curso[curso][Escuela_ID]['Total'] += cantidad

#     tablas_por_curso = {}
#     lista_de_Cursos_de_la_Supervisión = []

#     for curso in sorted(resumen_por_curso.keys()):  # Orden ascendente de cursos
#         escuelas_dict = resumen_por_curso[curso]
#         df = pd.DataFrame(escuelas_dict.values())

#         # Agrego columna criticidad antes de ordenar
#         df['Criticidad'] = df['Crítico'] / df['Total']
#         df['Criticidad'] = df['Criticidad'].fillna(0)

#         if orden_por_criticidad_func:
#             df_ordenado = orden_por_criticidad_func(df)
#         else:
#             df_ordenado = df.sort_values(by=['Criticidad', 'Escuela_ID'], ascending=[False, True])

#         df_ordenado = df_ordenado.drop(columns=['Criticidad'])

#         # Crear fila de totales
#         totales = df_ordenado[['Avanzado', 'Medio', 'Básico', 'Crítico', 'Total']].sum()
#         fila_total = pd.DataFrame([{
#             'Escuela_ID': '',
#             'Número': '',
#             'Escuela': 'TOTAL',
#             'Curso': curso,
#             'Avanzado': totales['Avanzado'],
#             'Medio': totales['Medio'],
#             'Básico': totales['Básico'],
#             'Crítico': totales['Crítico'],
#             'Total': totales['Total']
#         }])

#         df_ordenado = pd.concat([df_ordenado, fila_total], ignore_index=True)

#         tablas_por_curso[curso] = df_ordenado
#         lista_de_Cursos_de_la_Supervisión.append(curso)

#     return tablas_por_curso, lista_de_Cursos_de_la_Supervisión

# def generar_tablas_por_curso_y_ordenar_criticidad(
#     lista_de_Escuelas_por_Supervisión,
#     alumnos_por_escuela_y_curso,
#     condiciones,
#     filtrar_alumnos_por_escuela_curso_y_desempeño_group,
#     df_porcentaje_desempeno,
#     orden_por_criticidad_func=None
# ):
#     resumen_por_curso = {}
#     orden_desempeños = condiciones.get("DESEMPEÑO", ['Avanzado', 'Medio', 'Básico', 'Crítico'])

#     for unaEscuela in lista_de_Escuelas_por_Supervisión:
#         Escuela_ID = unaEscuela['Escuela_ID']
#         Escuela = unaEscuela.get('Escuela', '')[:20]
#         Número = unaEscuela.get('Número', '')

#         data = filtrar_alumnos_por_escuela_curso_y_desempeño_group(
#             Escuela_ID,
#             alumnos_por_escuela_y_curso,
#             True,
#             ['Escuela_ID', 'Curso ', 'DESEMPEÑO', 'matricula_por_escuela_curso_y_desempeño'],
#             'records',
#             condiciones
#         )

#         for fila in data:
#             curso = fila['Curso ']
#             desempeño = fila['DESEMPEÑO']
#             cantidad = fila['matricula_por_escuela_curso_y_desempeño']

#             if curso not in resumen_por_curso:
#                 resumen_por_curso[curso] = {}

#             if Escuela_ID not in resumen_por_curso[curso]:
#                 resumen_por_curso[curso][Escuela_ID] = {
#                     'Escuela_ID': Escuela_ID,
#                     'Número': Número,
#                     'Escuela': Escuela,
#                     'Curso': curso,
#                     'Avanzado': 0,
#                     'Medio': 0,
#                     'Básico': 0,
#                     'Crítico': 0,
#                     'Total': 0,
#                     '%Avanzado': 0,
#                     '%Medio': 0,
#                     '%Básico': 0,
#                     '%Crítico': 0,
#                 }

#             if desempeño in orden_desempeños:
#                 resumen_por_curso[curso][Escuela_ID][desempeño] += cantidad
#                 resumen_por_curso[curso][Escuela_ID]['Total'] += cantidad

#     tablas_por_curso = {}
#     lista_de_Cursos_de_la_Supervisión = []

#     for curso in sorted(resumen_por_curso.keys()):
#         escuelas_dict = resumen_por_curso[curso]
#         df = pd.DataFrame(escuelas_dict.values())

#         # Agregar criticidad
#         df['Criticidad'] = df['Crítico'] / df['Total']
#         df['Criticidad'] = df['Criticidad'].fillna(0)

#         # Agregar porcentajes desde el DataFrame externo
#         for idx, row in df.iterrows():
#             escuela_id = str(row['Escuela_ID'])
#             curso_actual = str(row['Curso']).strip()

#             df_filtro = porcentajeDesPorEyCur.filtrar_desempeno_por_escuela_y_curso(df_porcentaje_desempeno, escuela_id, curso_actual)

#             if not df_filtro.empty:
#                 for desempeño in orden_desempeños:
#                     porcentaje = df_filtro[df_filtro["DESEMPEÑO"] == desempeño]["porcentaje_desempeno"]
#                     if not porcentaje.empty:
#                         df.at[idx, f"%{desempeño}"] = round(float(porcentaje.iloc[0]), 2)
#                     else:
#                         df.at[idx, f"%{desempeño}"] = 0.0
#             else:
#                 for desempeño in orden_desempeños:
#                     df.at[idx, f"%{desempeño}"] = 0.0

#         # Ordenar si hay función personalizada
#         if orden_por_criticidad_func:
#             df_ordenado = orden_por_criticidad_func(df)
#         else:
#             df_ordenado = df.sort_values(by=['Criticidad', 'Escuela_ID'], ascending=[False, True])

#         df_ordenado = df_ordenado.drop(columns=['Criticidad'])

#         # Crear fila de totales
#         totales = df_ordenado[['Avanzado', 'Medio', 'Básico', 'Crítico', 'Total']].sum()

#         # Promedio ponderado de los porcentajes
#         total_matricula = totales['Total']
#         total_porcentajes = {}
#         for desempeño in orden_desempeños:
#             columna_porcentaje = f"%{desempeño}"
#             valores = df_ordenado[columna_porcentaje] * df_ordenado['Total']
#             promedio_ponderado = valores.sum() / total_matricula if total_matricula else 0
#             total_porcentajes[columna_porcentaje] = round(promedio_ponderado, 2)

#         fila_total = pd.DataFrame([{
#             'Escuela_ID': '',
#             'Número': '',
#             'Escuela': 'TOTAL',
#             'Curso': curso,
#             'Avanzado': totales['Avanzado'],
#             'Medio': totales['Medio'],
#             'Básico': totales['Básico'],
#             'Crítico': totales['Crítico'],
#             'Total': totales['Total'],
#             **total_porcentajes
#         }])

#         df_ordenado = pd.concat([df_ordenado, fila_total], ignore_index=True)

#         tablas_por_curso[curso] = df_ordenado
#         lista_de_Cursos_de_la_Supervisión.append(curso)

#     return tablas_por_curso, lista_de_Cursos_de_la_Supervisión



def generar_tablas_por_curso_y_ordenar_criticidad(
    lista_de_Escuelas_por_Supervisión,
    alumnos_por_escuela_y_curso,
    condiciones,
    filtrar_alumnos_por_escuela_curso_y_desempeño_group,
    df_porcentaje_desempeno,
    orden_por_criticidad_func=None
):
    resumen_por_curso = {}
    orden_desempeños = condiciones.get("DESEMPEÑO", ['Avanzado', 'Medio', 'Básico', 'Crítico'])

    for unaEscuela in lista_de_Escuelas_por_Supervisión:
        Escuela_ID = unaEscuela['Escuela_ID']
        Escuela = unaEscuela.get('Escuela', '')[:20]
        Número = unaEscuela.get('Número', '')

        data = filtrar_alumnos_por_escuela_curso_y_desempeño_group(
            Escuela_ID,
            alumnos_por_escuela_y_curso,
            True,
            ['Escuela_ID', 'Curso ', 'DESEMPEÑO', 'matricula_por_escuela_curso_y_desempeño'],
            'records',
            condiciones
        )

        for fila in data:
            curso = fila['Curso ']
            desempeño = fila['DESEMPEÑO']
            cantidad = fila['matricula_por_escuela_curso_y_desempeño']

            if curso not in resumen_por_curso:
                resumen_por_curso[curso] = {}

            if Escuela_ID not in resumen_por_curso[curso]:
                resumen_por_curso[curso][Escuela_ID] = {
                    'Escuela_ID': Escuela_ID,
                    'Número': Número,
                    'Escuela': Escuela,
                    'Curso': curso,
                    'Avanzado': 0,
                    'Medio': 0,
                    'Básico': 0,
                    'Crítico': 0,
                    'Total': 0,
                    'Avanzado_Porc': 0.0,
                    'Medio_Porc': 0.0,
                    'Básico_Porc': 0.0,
                    'Crítico_Porc': 0.0,
                }

            if desempeño in orden_desempeños:
                resumen_por_curso[curso][Escuela_ID][desempeño] += cantidad
                resumen_por_curso[curso][Escuela_ID]['Total'] += cantidad

    cantidades_por_curso = {}
    porcentajes_por_curso = {}
    lista_de_Cursos_de_la_Supervisión = []

    for curso in sorted(resumen_por_curso.keys()):
        escuelas_dict = resumen_por_curso[curso]
        df = pd.DataFrame(escuelas_dict.values())

        # Agregar criticidad
        df['Criticidad'] = df['Crítico'] / df['Total']
        df['Criticidad'] = df['Criticidad'].fillna(0)

        # Agregar porcentajes desde el DataFrame externo
        for idx, row in df.iterrows():
            escuela_id = str(row['Escuela_ID'])
            curso_actual = str(row['Curso']).strip()

            df_filtro = porcentajeDesPorEyCur.filtrar_desempeno_por_escuela_y_curso(df_porcentaje_desempeno, escuela_id, curso_actual)

            if not df_filtro.empty:
                for desempeño in orden_desempeños:
                    porcentaje = df_filtro[df_filtro["DESEMPEÑO"] == desempeño]["porcentaje_desempeno"]
                    if not porcentaje.empty:
                        df.at[idx, f"{desempeño}_Porc"] = round(float(porcentaje.iloc[0]), 2)
                    else:
                        df.at[idx, f"{desempeño}_Porc"] = 0.0
            else:
                for desempeño in orden_desempeños:
                    df.at[idx, f"{desempeño}_Porc"] = 0.0

        # Ordenar si hay función personalizada
        if orden_por_criticidad_func:
            df_ordenado = orden_por_criticidad_func(df)
        else:
            df_ordenado = df.sort_values(by=['Criticidad', 'Escuela_ID'], ascending=[False, True])

        df_ordenado = df_ordenado.drop(columns=['Criticidad'])

        # Crear fila de totales
        totales = df_ordenado[['Avanzado', 'Medio', 'Básico', 'Crítico', 'Total']].sum()

        total_matricula = totales['Total']
        total_porcentajes = {}
        for desempeño in orden_desempeños:
            columna_porcentaje = f"{desempeño}_Porc"
            valores = df_ordenado[columna_porcentaje] * df_ordenado['Total']
            promedio_ponderado = valores.sum() / total_matricula if total_matricula else 0
            total_porcentajes[columna_porcentaje] = round(promedio_ponderado, 2)

        fila_total = pd.DataFrame([{
            'Escuela_ID': '',
            'Número': '',
            'Escuela': 'TOTAL',
            'Curso': curso,
            'Avanzado': totales['Avanzado'],
            'Medio': totales['Medio'],
            'Básico': totales['Básico'],
            'Crítico': totales['Crítico'],
            'Total': totales['Total'],
            **total_porcentajes
        }])

        df_ordenado = pd.concat([df_ordenado, fila_total], ignore_index=True)

        # Separar en dos tablas: una para cantidades y otra para porcentajes
        #columnas_cant = ['Escuela_ID', 'Número', 'Escuela', 'Curso', 'Avanzado', 'Medio', 'Básico', 'Crítico', 'Total']
        #columnas_porc = ['Escuela_ID', 'Número', 'Escuela', 'Curso'] + [f"{d}_Porc" for d in orden_desempeños]
        columnas_cant = ['Número', 'Escuela',  'Avanzado', 'Medio', 'Básico', 'Crítico', 'Total']
        columnas_porc = ['Número', ] + [f"{d}_Porc" for d in orden_desempeños]

        cantidades_por_curso[curso] = df_ordenado[columnas_cant].copy()
        porcentajes_por_curso[curso] = df_ordenado[columnas_porc].copy()

        porcentajes_df = df_ordenado[columnas_porc].copy()

        # Quitar la última fila (totales)
        porcentajes_df = porcentajes_df.iloc[:-1]

        # Renombrar columnas que terminan en '_Porc'
        porcentajes_df.columns = [
            col.replace('_Porc', '') if col.endswith('_Porc') else col
            for col in porcentajes_df.columns
        ]

        porcentajes_por_curso[curso] = porcentajes_df
        
        lista_de_Cursos_de_la_Supervisión.append(curso)

    return cantidades_por_curso, porcentajes_por_curso, lista_de_Cursos_de_la_Supervisión







# Creamos un diccionario con los enlaces DE LOS INFORMES DE LAS ESCUELAS
diccionario_enlaces = dataFrame_df_LINKS_A_INFORMES_DE_ESCUELAS.set_index('Escuela_ID')['URL'].to_dict()

# Lista final con los reportes por supervisión
lista_reportes_por_supervision = []

for unaSupervisón in lista_de_supervisiones:

    if unaSupervisón != '-':
    
        print('Supervisión:', unaSupervisón)
        
        dict_reporte_por_Supervisión = {
            'Supervisión': unaSupervisón
        }

        # si en el nombre de la Supervisión está presente la palabra Primario, entonces
        # debemos grabar qué tipo de supervisión es y qué denominación usar en caso de usar Curso o Grado
        if 'Primario' in unaSupervisón:
            dict_reporte_por_Supervisión['Supervisión_tipo'] = 'Primaria'
            dict_reporte_por_Supervisión['Tipo_curso'] = 'Grado'
        else:
            dict_reporte_por_Supervisión['Supervisión_tipo'] = 'Secundaria'
            dict_reporte_por_Supervisión['Tipo_curso'] = 'Curso'



        # Obtenemos la lista completa de escuelas por supervisión
        lista_de_Escuelas_por_Supervisión = get_df_escuelas_por_supervision_con_datos(
            dataFrame_df_nominal_df_datos_institucionales, unaSupervisón
        )
        
        # Nueva lista simplificada con el enlace incluido
        # INSERTAR LA TABLA DE LOS LINKS DE LOS ESTABLECIMIENTOS, HAY QUE LEERLOS DE UN ARCHIVO CSV O DE UN EXCEL
        # HAY QUE LEER EL ARCHIVO CSV O EXCEL Y CONVERTIRLO EN UN DICCIONARIO
        lista_escuelas_con_enlace = []
        for escuela in lista_de_Escuelas_por_Supervisión:
            escuela_id = escuela.get('Escuela_ID')
            url = diccionario_enlaces.get(escuela_id)
            
            if url:
                #enlace_html = f'<a href="{url}" target="_blank">Ver Informe</a>'
                enlace_html = url
            else:
                enlace_html = 'Escuela sin Informe'
            
            escuela_simplificada = {
                #'Escuela_ID': escuela.get('Escuela_ID'),
                'Número': escuela.get('Número'),
                'Escuela': escuela.get('Escuela'),
                'Enlace al informe': enlace_html
            }
            lista_escuelas_con_enlace.append(escuela_simplificada)

        
        

        # (Opcional) también mantenés tu lista original de escuelas si la necesitás
        dict_reporte_por_Supervisión['Lista_Escuelas'] = lista_de_Escuelas_por_Supervisión

        # Guardamos la lista con enlaces en el diccionario de la supervisión
        dict_reporte_por_Supervisión['título_tabla_enlaces'] = 'Enlaces a los informes de Fluidez Lectora'
        dict_reporte_por_Supervisión['Escuelas_con_enlace'] = lista_escuelas_con_enlace

        # Guardamos el reporte completo en la lista final
        lista_reportes_por_supervision.append(dict_reporte_por_Supervisión)

        # Podés seguir usando estas listas si hacés cálculos más adelante
        if unaSupervisón != '-':
            list_Escuela_ID = []
            list_Matrícula = []
            list_Matrícula_censada = []

            

            for unaEscuela in lista_de_Escuelas_por_Supervisión:
                dict_matricula = {}

                matricula_censada = contar_alumnos_por_escuela.contar_alumnos_por_escuela______filter(
                    unaEscuela['Escuela_ID'],
                    dataFrame_df_Fluidez_3_cantidad_de_alumnos_por_escuela, # el dataframe
                    True, # se resetea el índice ? 
                    ['Escuela_ID',  'matricula_por_escuela' , ], # qué columnas quiero mostrar 
                    'records', # Opciones: 'dict', 'list', 'series', 'split', 'records', 'index'
                    condiciones=None # le paso condiciones adicionales al resultado final o None
                )
                
                matricula_nominal = contar_alumnos_por_escuela.contar_alumnos_por_escuela______filter(
                    unaEscuela['Escuela_ID'],
                    dataFrame_df_nominal_cantidad_de_alumnos_por_escuela, # el dataframe
                    True, # se resetea el índice ? 
                    ['Escuela_ID',  'matricula_por_escuela' , ], # qué columnas quiero mostrar 
                    'records', # Opciones: 'dict', 'list', 'series', 'split', 'records', 'index'
                    condiciones=None # le paso condiciones adicionales al resultado final o None
                )

                list_Escuela_ID.append(unaEscuela['Escuela_ID'])
                list_Matrícula_censada.append(matricula_censada[0]['matricula_por_escuela'])
                list_Matrícula.append(matricula_nominal[0]['matricula_por_escuela']) 
                
            dict_matricula = {'Escuela_ID' : list_Escuela_ID , 'matricula_censada' : list_Matrícula_censada , 'matricula_nominal' : list_Matrícula}
            #print(dict_matricula)
            # ahora tengo que convertir el diccionario en un dataframe y luego concatenar los dataframes
            data_dict_Cantidad_de_estudiantes_censados_por_establecimiento = {
            'datos_escuela':[
                pd.DataFrame({
                    'Escuela_ID':[escuela['Escuela_ID'] for escuela in lista_de_Escuelas_por_Supervisión],
                    'Número':[escuela['Número'] for escuela in lista_de_Escuelas_por_Supervisión],
                    'Escuela':[escuela['Escuela'] for escuela in lista_de_Escuelas_por_Supervisión],            
                }),
            ]
            }
            
            
            data_dict_Cantidad_de_estudiantes_censados_por_establecimiento = {
                'datos_escuela':[
                    pd.DataFrame({
                        'Escuela_ID':[escuela['Escuela_ID'] for escuela in lista_de_Escuelas_por_Supervisión],
                        'Número':[escuela['Número'] for escuela in lista_de_Escuelas_por_Supervisión],
                        'Escuela':[escuela['Escuela'][:20] for escuela in lista_de_Escuelas_por_Supervisión],            
                    }),
                    {'Escuela_ID' :  ['Escuela_ID' , ]}
                ],
                'matriculas' : [
                    pd.DataFrame(dict_matricula),
                    {'Escuela_ID' :  ['Escuela_ID' , ]},
                ],
            }

            # print( data_dict_Cantidad_de_estudiantes_censados_por_establecimiento['datos_escuela'][0])
            # print( data_dict_Cantidad_de_estudiantes_censados_por_establecimiento['matriculas'][0])

            tabla_data_dict_primera_tabla_del_informe_Supervisores , cabecera_tabla, cuerpo_tabla, total_tabla_cursos= dT3.dataTable(
                    data_dict_Cantidad_de_estudiantes_censados_por_establecimiento,         
                    common_column = 'Escuela_ID',
                    show_columns = [ 'Número' , 'Escuela' , 'matricula_censada', 'matricula_nominal',  ],
                    order_columns= [ 'Número' , 'Escuela' , 'matricula_censada', 'matricula_nominal',  ],
                    order_rows      = {'Número' : [escuela['Número'] for escuela in lista_de_Escuelas_por_Supervisión]},
                    operations_columns = {'Número' : 'Total' , 'matricula_censada' : 'sumar' , 'matricula_nominal' : 'sumar' , },
                    column_types = {'Número ' : str , 'Escuela' : str ,  'matricula_censada' : int , 'matricula_nominal' : int ,   },
                    rename_columns=[{'Número ':'Número' , 'Escuela' : 'Escuela' , 'matricula_censada' : 'Censados' , 'matricula_nominal' : 'Matrícula' ,  }],
                    show_total_row = True,
                    hide_zero_totals = False,
            )

            tabla_data_dict_primera_tabla_del_informe_Supervisores = tabla_data_dict_primera_tabla_del_informe_Supervisores.convert_dtypes()        

            # Convertir el DataFrame a JSON asegurando los enteros
            json_data_tabla_data_dict_primera_tabla_del_informe_Supervisores = json.dumps(
                    tabla_data_dict_primera_tabla_del_informe_Supervisores.to_dict(orient='records'),
                    indent=4,
                    ensure_ascii=False
            )

            dict_reporte_por_Supervisión['título_tabala_uno'] = 'Cantidad de estudiantes censados/as por establecimiento'
            dict_reporte_por_Supervisión['tabla_data_dict_primera_tabla_del_informe_Supervisores'] = json_data_tabla_data_dict_primera_tabla_del_informe_Supervisores

            
            
            # HACER AHORA LA TABLA DE 'RESULTADOS DE TODOS LOS CURSOS CENSADOS'
            dict_reporte_por_Supervisión['título_tabala_dos'] = 'RESULTADOS DE TODOS LOS CURSOS CENSADOS'
            dict_reporte_por_Supervisión['sub_título_tabala_dos'] = 'Proporción de estudiantes por escuela según nivel de desempeño en fluidez lectora'
            
            # HACER EN ESTA PARTE LOS DATOS PARA EL GRÁFICO DE LA PÁGINA 5
            # 'Proporción de estudiantes por escuela según nivel de desempeño en fluidez lectora'

            # preparo los datos para hacer el gráfico de todos los cursos censados o sea toda la escuela, 
            # vamos a udar el dataframe : 'dataFrame_df_Fluidez_3_calcular_porcentaje_desempeno_por_escuela'
            
            # Escuela_ID;DESEMPEÑO;matricula_por_escuela_y_desempeño;matricula_por_escuela;porcentaje_desempeno
            # 4;Avanzado;5;56;8.93
            # 4;Medio;37;56;66.07
            # 4;Básico;12;56;21.43
            # 4;Crítico;2;56;3.57
            # 5;Avanzado;26;146;17.81
            # 5;Medio;56;146;38.36
            # 5;Básico;39;146;26.71
            # 5;Crítico;25;146;17.12
            # 6;Avanzado;2;55;3.64
            # 6;Medio;16;55;29.09
            # 6;Básico;18;55;32.73
            # 6;Crítico;19;55;34.55
            # 8;Avanzado;8;68;11.76
            # 8;Medio;20;68;29.41
            # 8;Básico;20;68;29.41
            # 8;Crítico;20;68;29.41

        

            # lo que se hace es poder obtener todos los desempeños de las escuelas de la supervisión y poder generar el objeto
            # que vamo a poner en el JSON para que se pueda graficar
            df_desempeños_por_escuelas_de_la_supervision = generar_tabla_por_escuela_y_ordenar_criticidad(
                lista_de_Escuelas_por_Supervisión,
                dataFrame_df_Fluidez_3_calcular_porcentaje_desempeno_por_escuela,
                desempeño_por_escuela.filtrar_desempeno_por_escuela,
                orden_por_criticidad_func=orden_por_criticidad_multiple
            )       

            desempeños_por_escuelas_de_la_supervision = convertir_df_a_lista_apilada(df_desempeños_por_escuelas_de_la_supervision)  
            # guardo los resultados 
            dict_reporte_por_Supervisión['desempeños_por_escuelas_de_la_supervision'] = desempeños_por_escuelas_de_la_supervision        

            


            
            # DEBO SACAR LOS DESEMPEÑOS POR ESCUELA ES DECIR DE LA TOTALIDAD DE LA ESCUELA PERO DISCRIMINANDO POR DESEMPEÑO
            # USAMOS LA TABLA: dataFrame_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_desempeño

            # PRIMERO HACEMOS ALGO SIMILAR A LO QUE HICIMOS CON LOS DATOS DE LA ESCUELA
            data_dict_Cantidad_de_estudiantes_censados_por_establecimiento_SEGÚN_NIVEL_DE_DESEMPEÑO = {
                'datos_escuela':[
                    pd.DataFrame({
                        'Escuela_ID':[escuela['Escuela_ID'] for escuela in lista_de_Escuelas_por_Supervisión],
                        'Número':[escuela['Número'] for escuela in lista_de_Escuelas_por_Supervisión],
                        'Escuela':[escuela['Escuela'] for escuela in lista_de_Escuelas_por_Supervisión],           
                    }),
                ]
            }

            

            # declaro algunas condiciones adicionales para el filtrado final
            condiciones = {
                "DESEMPEÑO": ['Avanzado', 'Medio' , 'Básico', 'Crítico'],  # Valores a filtrar],
                "AND": False  # Lógica AND ,  "AND": False  # Lógica OR
            }

            
            # # Lista de desempeños en el orden deseado
            orden_desempeños = condiciones.get("DESEMPEÑO", ['Avanzado', 'Medio', 'Básico', 'Crítico'])

            """
            # # Lista para guardar los resúmenes por escuela
            # resumen_por_escuela = []

            # for unaEscuela in lista_de_Escuelas_por_Supervisión:

            #     # Reinicializar listas por cada escuela
            #     list_Escuela_ID = []
            #     list_DESEMPEÑO = []
            #     list_matricula_por_escuela_y_desempeño = []

            #     # Filtrar y obtener datos de la escuela
            #     cantidad_de_alumnos_por_escuela_y_desempeño = contar_alumnos_por_escuela_y_desempeño.filtrar_alumnos_por_escuela_y_desempeño_group(
            #         unaEscuela['Escuela_ID'],
            #         dataFrame_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_desempeño,
            #         True,
            #         ['Escuela_ID', 'DESEMPEÑO', 'matricula_por_escuela_y_desempeño'],
            #         'records',
            #         condiciones=condiciones
            #     )

            #     # Inicializar estructura de una fila
            #     fila_resumen = {
            #         'Escuela_ID': unaEscuela['Escuela_ID'],
            #         'Número': unaEscuela.get('Número', ''),
            #         'Escuela': unaEscuela.get('Escuela', ''),
            #         'Avanzado': 0,
            #         'Medio': 0,
            #         'Básico': 0,
            #         'Crítico': 0,
            #         'Total': 0
            #     }

            #     # Cargar los valores por desempeño
            #     for fila in cantidad_de_alumnos_por_escuela_y_desempeño:
            #         desempeño = fila['DESEMPEÑO']
            #         cantidad = fila['matricula_por_escuela_y_desempeño']
            #         if desempeño in orden_desempeños:
            #             fila_resumen[desempeño] = cantidad
            #             fila_resumen['Total'] += cantidad

            #     # Guardar fila en lista
            #     resumen_por_escuela.append(fila_resumen)

            # # Crear el DataFrame
            # df_resumen = pd.DataFrame(resumen_por_escuela)

            # # Agregar fila de totales
            # totales = {
            #     'Escuela_ID': 'TOTAL',
            #     'Número': '',
            #     'Escuela': '',
            #     'Avanzado': df_resumen['Avanzado'].sum(),
            #     'Medio': df_resumen['Medio'].sum(),
            #     'Básico': df_resumen['Básico'].sum(),
            #     'Crítico': df_resumen['Crítico'].sum()
            # }
            # totales['Total'] = (
            #     totales['Avanzado'] +
            #     totales['Medio'] +
            #     totales['Básico'] +
            #     totales['Crítico']
            # )

            # df_ordenado_por_criticidad = ordenCriticidadDataFrame.ordenar_por_criticidad(df_resumen)
            
            
            
            # ### acá ordenamos la tabla Cantidad de estudiantes por escuela según nivel de desempeño 'df_resumen'
            # # df_ordenado_por_criticidad
            # # if orden_por_criticidad_func:
            # #     df_ordenado = orden_por_criticidad_func(df_resumen)
            # # else:
            # #     df_ordenado = df_resumen.sort_values(by=['Criticidad', 'Escuela_ID'], ascending=[False, True])

            # # return df_ordenado.drop(columns=['Criticidad'])


            # # Agregar la fila de totales al DataFrame
            # df_ordenado_por_criticidad = pd.concat([df_ordenado_por_criticidad, pd.DataFrame([totales])], ignore_index=True)

            # Mostrar resultado
            #print(df_resumen)
            """

            df_resumen = generar_tabla_matricula_por_desempeno_y_ordenar(
                lista_de_Escuelas_por_Supervisión,
                dataFrame_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_desempeño,
                contar_alumnos_por_escuela_y_desempeño,
                #ordenCriticidadDataFrame
                orden_por_criticidad_func=orden_por_criticidad_multiple
            )

            # y ahora lo agrego al diccionario de reporte por supervisión
            # Convertir el DataFrame a JSON asegurando los enteros
            json_data_dict_Cantidad_de_estudiantes_censados_por_establecimiento_SEGÚN_NIVEL_DE_DESEMPEÑO = json.dumps(
                    df_resumen.to_dict(orient='records'),
                    indent=4,
                    ensure_ascii=False
            )
            
            
            dict_reporte_por_Supervisión['TÏTULO_Cantidad_de_estudiantes_censados_por_establecimiento_SEGÚN_NIVEL_DE_DESEMPEÑO'] = 'Cantidad de estudiantes censados por escuela según nivel de desempeño'
            dict_reporte_por_Supervisión['tabla_data_dict_Cantidad_de_estudiantes_censados_por_establecimiento_SEGÚN_NIVEL_DE_DESEMPEÑO'] = json_data_dict_Cantidad_de_estudiantes_censados_por_establecimiento_SEGÚN_NIVEL_DE_DESEMPEÑO         

            #contar_alumnos_por_escuela_curso_y_desempeño.filtrar_alumnos_por_escuela_curso_y_desempeño_group()

            df_filtrado = contar_alumnos_por_escuela_curso_y_desempeño.filtrar_alumnos_por_escuela_curso_y_desempeño_group(
                unaEscuela['Escuela_ID'],
                dataFrame_df_Fluidez_3_cantidad_de_alumnos_por_escuela_curso_y_desempeño,
                True,
                ['Escuela_ID','Curso ','DESEMPEÑO','matricula_por_escuela_curso_y_desempeño'],
                'records',
                condiciones=condiciones
            )        
            
            
            cantidades_por_curso, porcentajes_por_curso, lista_de_Cursos_de_la_Supervisión = generar_tablas_por_curso_y_ordenar_criticidad(
                lista_de_Escuelas_por_Supervisión,
                dataFrame_df_Fluidez_3_cantidad_de_alumnos_por_escuela_curso_y_desempeño,
                condiciones,
                contar_alumnos_por_escuela_curso_y_desempeño.filtrar_alumnos_por_escuela_curso_y_desempeño_group,  # <--- sin paréntesis
                dataFrame_df_Fluidez_3_calcular_porcentaje_desempeno_por_escuela_y_curso,
                ordenCriticidadDataFrame.ordenar_por_criticidad,
                
            )

            # cantidades_por_curso
            # Convertir a JSON serializable
            json_data_dict_cantidades_por_curso = {
                curso: df.to_dict(orient='records')
                for curso, df in cantidades_por_curso.items()
            }
            # (Opcional) Para ver en formato JSON legible
            json_data_formateado_cantidades_por_curso = json.dumps(json_data_dict_cantidades_por_curso, indent=4, ensure_ascii=False)
            # Guardar en el diccionario final del reporte
            dict_reporte_por_Supervisión['lista_de_Cursos_de_la_Supervisión'] = lista_de_Cursos_de_la_Supervisión
            dict_reporte_por_Supervisión['tabla_data_dict_Cantidad_de_estudiantes_censados_por_curso_SEGÚN_NIVEL_DE_DESEMPEÑO'] = json_data_dict_cantidades_por_curso

            ########################################################

            # porcentajes_por_curso
            # Convertir a JSON serializable
            json_data_dict_porcentajes_por_curso = {
                curso: df.to_dict(orient='records')
                for curso, df in porcentajes_por_curso.items()
            }
            # (Opcional) Para ver en formato JSON legible
            json_data_formateado__porcentajes_por_curso = json.dumps(json_data_dict_porcentajes_por_curso, indent=4, ensure_ascii=False)
            # Guardar en el diccionario final del reporte
            dict_reporte_por_Supervisión['lista_de_Cursos_de_la_Supervisión'] = lista_de_Cursos_de_la_Supervisión
            dict_reporte_por_Supervisión['tabla_data_dict_Porcentajes_de_estudiantes_censados_por_curso_SEGÚN_NIVEL_DE_DESEMPEÑO'] = json_data_dict_porcentajes_por_curso


            
                
            #exit()    
            print('-'*50)
            
        print('-'*150)      
        

        pJ.pretty_print_json(dict_reporte_por_Supervisión)
            
        # Aseguramos que `project_root` no tenga una barra final
        project_root = project_root.rstrip("\\/")
        # Construir la ruta correctamente
        ruta_json = os.path.join(
                "\\","src", "_main_", "Fluidez_Lectora_medición_1", "Año_2025", "mes_05_mayo",
                "reporte_por_supervisión", "reporte_por_supervisión_JSON",
                f"{dict_reporte_por_Supervisión['Supervisión']}_Fluidez_Lectora_Op_1_2025.json"

        )



        # Guardamos el JSON
        u.save_json(dict_reporte_por_Supervisión, ruta_json)

        # HAGO EL PDF
        Fluidez_Lectora_PDFs.hacer_reporte_PDF(dict_reporte_por_Supervisión,)

    #exit()
print('..fin..!')    

   
    