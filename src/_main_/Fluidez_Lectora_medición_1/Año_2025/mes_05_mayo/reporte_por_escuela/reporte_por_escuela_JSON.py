# ESTE PROGRAMA LO QUE HACE ES CREAR LOS ARCHIVOS JSON DE LOS REPORTES DE LAS ESCUELAS
# TOMA TODOS LOS DATOS NECESARIOS QUE SE HA PROCESADO Y CREA EL ARCHIVO CORRESPONDIENTE PARA
# CADA UNA DE LAS ESCUELAS

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
import src.modelos.__commonsLibs_.obtemer_lista_de_Escuelas.set_get_df_lista_de_Ecuela_ID as Escuela_IDs
import src.modelos.__commonsLibs_.obtemer_datos_institucionales.group_df_datos_institucionales as datos_institucionales
import src.modelos.__commonsLibs_.contar_alumnos_por_escuela_y_curso_____.group_contar_alumnos_por_escuela_y_curso_____ as contar_alumnos_por_escuela_y_curso
import src.modelos.__commonsLibs_.dataTable.dataTable as dT3
import src.modelos.__commonsLibs_.obtener_lista_de_cursos_normalizados.group_df_lista_de_cursos_normalizados as cursos
import src.modelos._Análisis_Fluidez_Lectora.contar_alumnos_por_escuela_curso_y_desempeño.group_contar_alumnos_por_escuela_curso_y_desempeño as fL_alumnos_por_escuela_curso_y_desempeño
import src.modelos.__commonsLibs_.filtrar_dataframe_nominal_alumnos.filtrar_dataframe_nominales_de_alumnos_por_escuela_y_curso as filtrar_dataframe_nominal_alumnos

import src._main_.Fluidez_Lectora_medición_1.Año_2025.mes_05_mayo.reporte_por_escuela.reporte_por_escuela_PDFs as Fluidez_Lectora_PDFs

# en esta parte construimos el reporte de la medición 1 de Fluidez Lectora
# para el mes de mayo del año 2025
# leeremos los datos de la medición 1 de Fluidez Lectora
# y construiremos un reporte con los resultados obtenidos
# y lo guardaremos en un archivo de texto JSON
# para cada escuela

# 1-leer los datos
# 2-crear las tablas
# 3-crear los dataframes unidos para los gráficos
# 4-crear los gráficos
# 5-guardar los gráficos en un archivo de imagen
# 6-guardar los datos en un archivo de texto JSON
# 7-fin

# datos que debe recibir: la lista de Escuela_IDs
# los dataframe involucrados en el reporte
# el nombre del informe se lo definimos nosotros en una variable

# 1-leer los datos

# -Leer la lista de cursos normalizados que se corresponde con los cursos que tiene la escuela
PATH_file_df_nominal_df_Escuela_ID_CURSO_NORMALIZADO_list = 'data/processed/transformed/Nominal/2025_04/df_nominal_df_Escuela_ID_CURSO_NORMALIZADO_list.csv'
csv_path_df_nominal_df_Escuela_ID_CURSO_NORMALIZADO_list = os.path.join(project_root, PATH_file_df_nominal_df_Escuela_ID_CURSO_NORMALIZADO_list)
dataFrame_df_nominal_df_Escuela_ID_CURSO_NORMALIZADO_list = u.cargar_csv(csv_path_df_nominal_df_Escuela_ID_CURSO_NORMALIZADO_list)


# Lista de Escuela_IDs (esta lista es la de todas lass escuelas)
PATH_file_df_nominal_datos_institucionales_Escuela_ID = Escuela_IDs.PATH_file_lista_de_Escuelas_ID_nominal
csv_path_df_nominal_datos_institucionales_Escuela_ID = os.path.join(project_root, PATH_file_df_nominal_datos_institucionales_Escuela_ID)
dataFrame_df_nominal_datos_institucionales_Escuela_ID = u.cargar_csv(csv_path_df_nominal_datos_institucionales_Escuela_ID)
listaTodasEscuela_IDs = Escuela_IDs.get_df_lista_de_Ecuela_ID(dataFrame_df_nominal_datos_institucionales_Escuela_ID,'df_nominal')
#print(listaEscuela_IDs)

# lista de escuelas del operativo de FL, se bassa en aquellas escuelas que tienen algo cargado en el operativo 2
PATH_file_df_Fluidez_2_df_Escuela_ID_FL = 'data/processed/transformed/Fluidez/2025_04/df_Fluidez_2_df_Escuela_ID_FL.csv'
csv_path_df_Fluidez_2_df_Escuela_ID_FL = os.path.join(project_root, PATH_file_df_Fluidez_2_df_Escuela_ID_FL)
dataFrame_df_Fluidez_2_df_Escuela_ID_FL = u.cargar_csv(csv_path_df_Fluidez_2_df_Escuela_ID_FL)
lista_Fluidez_2_Escuela_IDs = Escuela_IDs.get_df_lista_de_Ecuela_ID(dataFrame_df_Fluidez_2_df_Escuela_ID_FL,'df_Fluidez_2')

# lista de escuelas del operativo de FL, se bassa en aquellas escuelas que tienen algo cargado en el operativo 2
PATH_file_df_Fluidez_3_df_Escuela_ID_FL = 'data/processed/transformed/Fluidez/2025_04/df_Fluidez_3_df_Escuela_ID_FL.csv'
csv_path_df_Fluidez_3_df_Escuela_ID_FL = os.path.join(project_root, PATH_file_df_Fluidez_3_df_Escuela_ID_FL)
dataFrame_df_Fluidez_3_df_Escuela_ID_FL = u.cargar_csv(csv_path_df_Fluidez_3_df_Escuela_ID_FL)
lista_Fluidez_3_Escuela_IDs = Escuela_IDs.get_df_lista_de_Ecuela_ID(dataFrame_df_Fluidez_3_df_Escuela_ID_FL,'df_Fluidez_3')

# -Datos institucionales-
# leer los datos institucionales
PATH_file_df_nominal_df_datos_institucionales = 'data/processed/transformed/Nominal/2025_04/df_nominal_df_datos_institucionales.csv'
csv_path_df_nominal_df_datos_institucionales = os.path.join(project_root, PATH_file_df_nominal_df_datos_institucionales)
dataFrame_df_nominal_df_datos_institucionales = u.cargar_csv(csv_path_df_nominal_df_datos_institucionales)

# -Crear la tabla de datos por curso para cada escuela, la que muestra la cantidad de alumnos por curso
# por el operativo actual y la cantidad de alumnos filtrados (Incluidos = SI, alumnos con desemepño, alumnos con medición inconsistente)
# a-leer la cantidad de alumnos por escuela y curso
PATH_file_df_nominal_cantidad_de_alumnos_por_escuela_y_curso = 'data/processed/transformed/Nominal/2025_04/df_nominal_cantidad_de_alumnos_por_escuela_y_curso.csv'
csv_path_df_nominal_cantidad_de_alumnos_por_escuela_y_curso = os.path.join(project_root, PATH_file_df_nominal_cantidad_de_alumnos_por_escuela_y_curso)
dataFrame_df_nominal_cantidad_de_alumnos_por_escuela_y_curso = u.cargar_csv(csv_path_df_nominal_cantidad_de_alumnos_por_escuela_y_curso)

# -Leer los nominales de alumnos que tienen desempeño en los tres operativos
# -OPERATIVO 1 AÑO ANTERIOR MAYO APROX
# -OPERATIVO 2 ÚLTMO AÑO NOVIEMBRER APROX
# -OPERATIVO 3 AÑO ACTUAL MAYO APROX

#### OPERATIVO A - 1 AÑO ANTERIOR ABRIL-MAYO APROX #########################################################################
#### OPERATIVO A - 1 AÑO ANTERIOR ABRIL-MAYO APROX #########################################################################
#### OPERATIVO A - 1 AÑO ANTERIOR ABRIL-MAYO APROX #########################################################################
#### OPERATIVO A - 1 AÑO ANTERIOR ABRIL-MAYO APROX #########################################################################
# LEER -OPERATIVO 1 AÑO ANTERIOR MAYO APROX
PATH_file_df_Fluidez_1_alumnos_con_MÁXIMA_cant_palabras = 'data/processed/transformed/Fluidez/2025_04/df_Fluidez_1_alumnos_con_MÁXIMA_cant_palabras.csv'
csv_path_df_Fluidez_1_alumnos_con_MÁXIMA_cant_palabras = os.path.join(project_root, PATH_file_df_Fluidez_1_alumnos_con_MÁXIMA_cant_palabras)
dataFrame_df_Fluidez_1_alumnos_con_MÁXIMA_cant_palabras = u.cargar_csv(csv_path_df_Fluidez_1_alumnos_con_MÁXIMA_cant_palabras)




#### OPERATIVO B - 2 AÑO ANTERIOR (EL ÚLTIMO) NOVIEMBRER APROX #############################################################
#### OPERATIVO B - 2 AÑO ANTERIOR (EL ÚLTIMO) NOVIEMBRER APROX #############################################################
#### OPERATIVO B - 2 AÑO ANTERIOR (EL ÚLTIMO) NOVIEMBRER APROX #############################################################
#### OPERATIVO B - 2 AÑO ANTERIOR (EL ÚLTIMO) NOVIEMBRER APROX #############################################################
# LEER -OPERATIVO 2 ÚLTMO AÑO NOVIEMBRER APROX
PATH_file_df_Fluidez_2_alumnos_con_MÁXIMA_cant_palabras = 'data/processed/transformed/Fluidez/2025_04/df_Fluidez_2_alumnos_con_MÁXIMA_cant_palabras.csv'
csv_path_df_Fluidez_2_alumnos_con_MÁXIMA_cant_palabras = os.path.join(project_root, PATH_file_df_Fluidez_2_alumnos_con_MÁXIMA_cant_palabras)
dataFrame_df_Fluidez_2_alumnos_con_MÁXIMA_cant_palabras = u.cargar_csv(csv_path_df_Fluidez_2_alumnos_con_MÁXIMA_cant_palabras)




#### OPERATIVO C - 1 AÑO ACTUAL ABRIL-MAYO APROX ###########################################################################
#### OPERATIVO C - 1 AÑO ACTUAL ABRIL-MAYO APROX ###########################################################################
#### OPERATIVO C - 1 AÑO ACTUAL ABRIL-MAYO APROX ###########################################################################
#### OPERATIVO C - 1 AÑO ACTUAL ABRIL-MAYO APROX ###########################################################################
# LEER -OPERATIVO 3 AÑO ACTUAL MAYO APROX
PATH_file_df_Fluidez_3_alumnos_con_MÁXIMA_cant_palabras = 'data/processed/transformed/Fluidez/2025_04/df_Fluidez_3_alumnos_con_MÁXIMA_cant_palabras.csv'
csv_path_df_Fluidez_3_alumnos_con_MÁXIMA_cant_palabras = os.path.join(project_root, PATH_file_df_Fluidez_3_alumnos_con_MÁXIMA_cant_palabras)
dataFrame_df_Fluidez_3_alumnos_con_MÁXIMA_cant_palabras = u.cargar_csv(csv_path_df_Fluidez_3_alumnos_con_MÁXIMA_cant_palabras)
# -Leer la lista de cursos normalizados que se corresponde con los cursos en cuestión que van a ser mostrados
# es decir que debemos tener la lista de los cursos que intervinieron en el opearativo...
PATH_file_df_Fluidez_3_Escuela_ID_CURSO_NORMALIZADO_list = 'data/processed/transformed/Fluidez/2025_04/df_Fluidez_3_Escuela_ID_CURSO_NORMALIZADO_list.csv'
csv_path_df_Fluidez_3_Escuela_ID_CURSO_NORMALIZADO_list = os.path.join(project_root, PATH_file_df_Fluidez_3_Escuela_ID_CURSO_NORMALIZADO_list)
dataFrame_df_Fluidez_3_Escuela_ID_CURSO_NORMALIZADO_list = u.cargar_csv(csv_path_df_Fluidez_3_Escuela_ID_CURSO_NORMALIZADO_list)
# # -Leer la lista de cursos normalizados que se corresponde con los cursos en cuestión que van a ser mostrados
# # es decir que debemos tener la lista de los cursos que intervinieron en el opearativo...
# PATH_file_df_Fluidez_3_Escuela_ID_CURSO_NORMALIZADO_list = 'data/processed/transformed/Fluidez/df_Fluidez_3_Escuela_ID_CURSO_NORMALIZADO_list.csv'
# csv_path_df_Fluidez_3_Escuela_ID_CURSO_NORMALIZADO_list = os.path.join(project_root, PATH_file_df_Fluidez_3_Escuela_ID_CURSO_NORMALIZADO_list)
# dataFrame_df_Fluidez_3_Escuela_ID_CURSO_NORMALIZADO_list = u.cargar_csv(csv_path_df_Fluidez_3_Escuela_ID_CURSO_NORMALIZADO_list)

# b-leer la cantidad de alumnos por escuela y curso que sean inconsitentes (que hayan leído mas de 300 palabras por minuto)
PATH_file_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_curso_mayor_a_300_palabras = 'data/processed/transformed/Fluidez/2025_04/df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_curso_mayor_a_300_palabras.csv'
csv_path_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_curso_mayor_a_300_palabras = os.path.join(project_root, PATH_file_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_curso_mayor_a_300_palabras)
dataFrame_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_curso_mayor_a_300_palabras = u.cargar_csv(csv_path_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_curso_mayor_a_300_palabras)

# c-leer la cantidad de alumnos por escuela y curso que tengan desempeño (maxima cantidad de palabras leídas por minuto))
PATH_file_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_curso_con_MÁXIMA_cant_palabras = 'data/processed/transformed/Fluidez/2025_04/df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_curso_con_MÁXIMA_cant_palabras.csv'
csv_path_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_curso_con_MÁXIMA_cant_palabras = os.path.join(project_root, PATH_file_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_curso_con_MÁXIMA_cant_palabras)
dataFrame_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_curso_con_MÁXIMA_cant_palabras = u.cargar_csv(csv_path_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_curso_con_MÁXIMA_cant_palabras)

# d-leer la cantidad de alumnos por escuela y curso que no tengan desempeño (sin_DESEMPEÑO)
PATH_file_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_curso_sin_DESEMPEÑO = 'data/processed/transformed/Fluidez/2025_04/df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_curso_sin_DESEMPEÑO.csv'
csv_path_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_curso_sin_DESEMPEÑO = os.path.join(project_root, PATH_file_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_curso_sin_DESEMPEÑO)
dataFrame_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_curso_sin_DESEMPEÑO = u.cargar_csv(csv_path_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_curso_sin_DESEMPEÑO)

# e-leer la cantidad de alumnos por escuela y curso que sen incluidos = NO
PATH_file_df_Fluidez_3_cantidad_de_alumnos_incluidos_NO_por_escuela_y_curso = 'data/processed/transformed/Fluidez/2025_04/df_Fluidez_3_cantidad_de_alumnos_incluidos_NO_por_escuela_y_curso.csv'
csv_path_df_Fluidez_3_cantidad_de_alumnos_incluidos_NO_por_escuela_y_curso = os.path.join(project_root, PATH_file_df_Fluidez_3_cantidad_de_alumnos_incluidos_NO_por_escuela_y_curso)
dataFrame_df_Fluidez_3_cantidad_de_alumnos_incluidos_NO_por_escuela_y_curso = u.cargar_csv(csv_path_df_Fluidez_3_cantidad_de_alumnos_incluidos_NO_por_escuela_y_curso)

# f-leer la cantidad de alumnos por escuela y curso que sen incluidos = SI
PATH_file_df_Fluidez_3_cantidad_de_alumnos_incluidos_SI_por_escuela_y_curso = 'data/processed/transformed/Fluidez/2025_04/df_Fluidez_3_cantidad_de_alumnos_incluidos_SI_por_escuela_y_curso.csv'
csv_path_df_Fluidez_3_cantidad_de_alumnos_incluidos_SI_por_escuela_y_curso = os.path.join(project_root, PATH_file_df_Fluidez_3_cantidad_de_alumnos_incluidos_SI_por_escuela_y_curso)
dataFrame_df_Fluidez_3_cantidad_de_alumnos_incluidos_SI_por_escuela_y_curso = u.cargar_csv(csv_path_df_Fluidez_3_cantidad_de_alumnos_incluidos_SI_por_escuela_y_curso)

# -LEER LAS CANTIDADES DE ALUMNOS POR ESCUELA, CURSO Y DESEMPEÑO PARA CONSTRUIR LAS TABLAS  POR NIVEL DE DESEMPEÑO SEGÚN MEDICIÓN POR CURSO
# -OPERATIVO 1 AÑO ANTERIOR 2024
PATH_file_df_Fluidez_1_cantidad_de_alumnos_por_escuela_curso_y_desempeño = 'data/processed/transformed/Fluidez/2025_04/df_Fluidez_1_cantidad_de_alumnos_por_escuela_curso_y_desempeño.csv'
csv_path_df_Fluidez_1_cantidad_de_alumnos_por_escuela_curso_y_desempeño = os.path.join(project_root, PATH_file_df_Fluidez_1_cantidad_de_alumnos_por_escuela_curso_y_desempeño)
dataFrame_df_Fluidez_1_cantidad_de_alumnos_por_escuela_curso_y_desempeño = u.cargar_csv(csv_path_df_Fluidez_1_cantidad_de_alumnos_por_escuela_curso_y_desempeño)


# -LEER LAS CANTIDADES DE ALUMNOS POR ESCUELA, CURSO Y DESEMPEÑO PARA CONSTRUIR LAS TABLAS  POR NIVEL DE DESEMPEÑO SEGÚN MEDICIÓN POR CURSO
# -OPERATIVO 3 AÑO ACTUAL 2025
PATH_file_df_Fluidez_3_cantidad_de_alumnos_por_escuela_curso_y_desempeño = 'data/processed/transformed/Fluidez/2025_04/df_Fluidez_3_cantidad_de_alumnos_por_escuela_curso_y_desempeño.csv'
csv_path_df_Fluidez_3_cantidad_de_alumnos_por_escuela_curso_y_desempeño = os.path.join(project_root, PATH_file_df_Fluidez_3_cantidad_de_alumnos_por_escuela_curso_y_desempeño)
dataFrame_df_Fluidez_3_cantidad_de_alumnos_por_escuela_curso_y_desempeño = u.cargar_csv(csv_path_df_Fluidez_3_cantidad_de_alumnos_por_escuela_curso_y_desempeño)


# -LEER LOS PORCENTAJES DE ALUMNOS POR ESCUELA, CURSO Y DESEMPEÑO PARA CONSTRUIR LOS GRÁFICOS POR CURSO
# -OPERATIVO 1 AÑO ANTERIOR 2024
PATH_file_df_Fluidez_1_calcular_porcentaje_desempeno_por_escuela_y_curso = 'data/processed/transformed/Fluidez/2025_04/df_Fluidez_1_calcular_porcentaje_desempeno_por_escuela_y_curso.csv'
csv_path_df_Fluidez_1_calcular_porcentaje_desempeno_por_escuela_y_curso = os.path.join(project_root, PATH_file_df_Fluidez_1_calcular_porcentaje_desempeno_por_escuela_y_curso)
dataFrame_df_Fluidez_1_calcular_porcentaje_desempeno_por_escuela_y_curso = u.cargar_csv(csv_path_df_Fluidez_1_calcular_porcentaje_desempeno_por_escuela_y_curso)

# -LEER LOS PORCENTAJES DE ALUMNOS POR ESCUELA, CURSO Y DESEMPEÑO PARA CONSTRUIR LOS GRÁFICOS POR CURSO
# -OPERATIVO 3 AÑO ANTERIOR 2025
PATH_file_df_Fluidez_3_calcular_porcentaje_desempeno_por_escuela_y_curso = 'data/processed/transformed/Fluidez/2025_04/df_Fluidez_3_calcular_porcentaje_desempeno_por_escuela_y_curso.csv'
csv_path_df_Fluidez_3_calcular_porcentaje_desempeno_por_escuela_y_curso = os.path.join(project_root, PATH_file_df_Fluidez_3_calcular_porcentaje_desempeno_por_escuela_y_curso)
dataFrame_df_Fluidez_3_calcular_porcentaje_desempeno_por_escuela_y_curso = u.cargar_csv(csv_path_df_Fluidez_3_calcular_porcentaje_desempeno_por_escuela_y_curso)

# -LEER LOS ARCHIVOS NOMINALES DE LOS ALUMNOS DEL OPERATIVO DE FLUIDEZ LECTORA 3, QUE YA HAN SIDO TRATADOS EN EL PREPROCESO
# -ESTOS ARCHIVOS SON NOMINALES CON DATOS DE ALUMNOS Y SERÁN FILTRADOS POR LA ESCUELA Y EL CURSO NORMALIZADO
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# DATAFRAME DE LA MEDICIÓN ACTUAL
# PRIMERA DEL AÑO
# -LEER LOS ARCHIVOS NOMINALES DE LOS ALUMNOS DEL OPERATIVO DE FLUIDEZ LECTORA 3, QUE YA HAN SIDO TRATADOS EN EL PREPROCESO
# -ESTOS ARCHIVOS SON NOMINALES CON DATOS DE ALUMNOS Y SERÁN FILTRADOS POR LA ESCUELA Y EL CURSO NORMALIZADO
# 1- df_Fluidez_3_alumnos_con_DESEMPEÑO
PATH_file_df_Fluidez_3_alumnos_con_DESEMPEÑO = 'data/processed/transformed/Fluidez/2025_04/df_Fluidez_3_alumnos_con_DESEMPEÑO.csv'
csv_path_df_Fluidez_3_alumnos_con_DESEMPEÑO = os.path.join(project_root, PATH_file_df_Fluidez_3_alumnos_con_DESEMPEÑO)
dataFrame_df_Fluidez_3_alumnos_con_DESEMPEÑO = u.cargar_csv(csv_path_df_Fluidez_3_alumnos_con_DESEMPEÑO)

# 2- df_Fluidez_3_alumnos_con_MÁXIMA_cant_palabras
PATH_file_df_Fluidez_3_alumnos_con_MÁXIMA_cant_palabras = 'data/processed/transformed/Fluidez/2025_04/df_Fluidez_3_alumnos_con_MÁXIMA_cant_palabras.csv'
csv_path_df_Fluidez_3_alumnos_con_MÁXIMA_cant_palabras = os.path.join(project_root, PATH_file_df_Fluidez_3_alumnos_con_MÁXIMA_cant_palabras)
dataFrame_df_Fluidez_3_alumnos_con_MÁXIMA_cant_palabras = u.cargar_csv(csv_path_df_Fluidez_3_alumnos_con_MÁXIMA_cant_palabras)

# 3- df_Fluidez_3_alumnos_incluidos_NO
PATH_file_df_Fluidez_3_alumnos_incluidos_NO = 'data/processed/transformed/Fluidez/2025_04/df_Fluidez_3_alumnos_incluidos_NO.csv'
csv_path_df_Fluidez_3_alumnos_incluidos_NO = os.path.join(project_root, PATH_file_df_Fluidez_3_alumnos_incluidos_NO)
dataFrame_df_Fluidez_3_alumnos_incluidos_NO = u.cargar_csv(csv_path_df_Fluidez_3_alumnos_incluidos_NO)

# 4- df_Fluidez_3_alumnos_incluidos_SI
PATH_file_df_Fluidez_3_alumnos_incluidos_SI = 'data/processed/transformed/Fluidez/2025_04/df_Fluidez_3_alumnos_incluidos_SI.csv'
csv_path_df_Fluidez_3_alumnos_incluidos_SI = os.path.join(project_root, PATH_file_df_Fluidez_3_alumnos_incluidos_SI)
dataFrame_df_Fluidez_3_alumnos_incluidos_SI = u.cargar_csv(csv_path_df_Fluidez_3_alumnos_incluidos_SI)

# 5- df_Fluidez_3_alumnos_mayor_a_300_palabras
PATH_file_df_Fluidez_3_alumnos_mayor_a_300_palabras = 'data/processed/transformed/Fluidez/2025_04/df_Fluidez_3_alumnos_mayor_a_300_palabras.csv'
csv_path_df_Fluidez_3_alumnos_mayor_a_300_palabras = os.path.join(project_root, PATH_file_df_Fluidez_3_alumnos_mayor_a_300_palabras)
dataFrame_df_Fluidez_3_alumnos_mayor_a_300_palabras = u.cargar_csv(csv_path_df_Fluidez_3_alumnos_mayor_a_300_palabras)

# 6- df_Fluidez_3_alumnos_sin_DESEMPEÑO
PATH_file_df_Fluidez_3_alumnos_sin_DESEMPEÑO = 'data/processed/transformed/Fluidez/2025_04/df_Fluidez_3_alumnos_sin_DESEMPEÑO.csv'
csv_path_df_Fluidez_3_alumnos_sin_DESEMPEÑO = os.path.join(project_root, PATH_file_df_Fluidez_3_alumnos_sin_DESEMPEÑO)
dataFrame_df_Fluidez_3_alumnos_sin_DESEMPEÑO = u.cargar_csv(csv_path_df_Fluidez_3_alumnos_sin_DESEMPEÑO)



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------


# EL ARCHIVO UNIDO DE LOS TRES OPERATIVOS ÚLTIMOS DE LOS ALUMNOS QUE TIENEN DESEMPEÑO 
PATH_file_union_DFs_2024_1__2024_3__2025_1_CON_DESEMPEÑO = 'data/processed/transformed/Fluidez/2025_04/_union_DFs_2024_1__2024_3__2025_1_CON_DESEMPEÑO.csv'
csv_path_union_DFs_2024_1__2024_3__2025_1_CON_DESEMPEÑO = os.path.join(project_root, PATH_file_union_DFs_2024_1__2024_3__2025_1_CON_DESEMPEÑO)
_union_DFs_2024_1__2024_3__2025_1_CON_DESEMPEÑO = u.cargar_csv(csv_path_union_DFs_2024_1__2024_3__2025_1_CON_DESEMPEÑO)

# EL ARCHIVO UNIDO DE LOS TRES OPERATIVOS ÚLTIMOS DE LOS ALUMNOS QUE SON INCLUIDOS SI
PATH_file_union_DFs_2024_1__2024_3__2025_1_INCLUIDOS_SI = 'data/processed/transformed/Fluidez/2025_04/_union_DFs_2024_1__2024_3__2025_1_INCLUIDOS_SI.csv'
csv_path_union_DFs_2024_1__2024_3__2025_1_INCLUIDOS_SI = os.path.join(project_root, PATH_file_union_DFs_2024_1__2024_3__2025_1_INCLUIDOS_SI)
_union_DFs_2024_1__2024_3__2025_1_INCLUIDOS_SI = u.cargar_csv(csv_path_union_DFs_2024_1__2024_3__2025_1_INCLUIDOS_SI)


# VARIABLES GLOBALES
# -PARA DETERMINAR SI SE PONE GRADO O CURSO DEPENDIENDO DEL NIVEL DE LA ESCUELA
tipo_grado_o_curso = ''
# -PARA CALCULAR LA FECHA EN LA QUE SE HIZO EL INFORME
hoy = datetime.now()


def check_escuela_id_in_list(escuela_id, lista_escuela_ids):
    """
    Verifica si un escuela_id está en la lista de escuela_ids.
    """
    return escuela_id in lista_escuela_ids

# iterar por la cantidad de escuelas que participaron en el operativo 2 de fluidez pero tener en 
# MEJOR ES ITERAR POR TODAS LAS ESCUELAS Y AQUELLAS QUE NO TENGAN NADA EN EL OPERATIVO 3 DE FLUIDEZ LECTORA
# SE HACE UN JSON QUUE TENGA LOS DATOS DE LA ESCUELA PERO CON LA LEYENDA QUE NO TIENE NADA EN EL OPERATIVO 3 !

last_Escuela_ID = 0 # se cambia acá el escuela_id para que no se rompa el programa
lista_algunas_escuelas_ID = [
        2336,
        164,
        1403
        
        
        
        
        # 2018,
        # 2037,
        # 2681,
        # 2680,
        # 347,
        # 404,
        # 2379,
        # 186,
        # 506,
        # 1427,
        # 1408,
        # 1430,
        # 1431,
        # 1432,
        # 1438,
        # 1439,
        # 1402,
        # 1406,
        # 1407,
        # 1414,
        # 1436,
        # 1437,
        # 1411,
        # 1415,
        # 1416,
        # 1420,
        # 1421,
        # 1422,
        # 1423,
        # 1424,
        # 1426,
        # 1428,
        # 1435,
        # 1440,
        # 1404,
        # 1410,
        # 1433,
        # 1434,
        # 1405,
        # 1409,
        # 1412,
        # 1413,
        # 1418,
        # 1419,
        # 1425,
        # 1441,
        # 1417,
]
lista_una_escuela = [1193]
# modificación solamente algunas escuelas
for Escuela_ID in lista_algunas_escuelas_ID:
    
    #PARA CORREGIR EL PROBLEMA DEL CERRE DEL VISUAL STUDIO CODE
    if Escuela_ID >= last_Escuela_ID:
        # ejecutamos lo que sigue...
              
    
        # DEFINIMOS EL DICCIONARIO QUE CONTENDRÁ LOS DATOS DE TODO EL INFORME, O SEA DE LO QUE SIGUE A CONTINUACIÓN
        # LUEGO AL FINAL GRABAREMOS ESOS DATOS DENTRO DEL DIRECTORIO CORRESPONDIENTE EN FORMATO JSON
        # ESTE DICCIONARIO CONTENDRÁ LOS DATOS DE CADA ESCUELA
        dict_reporte_por_escuela = {}
        
        print('Escuela_ID ' , Escuela_ID)
        
        is_in_lista_Fluidez_3_Escuela_IDs = check_escuela_id_in_list(Escuela_ID, lista_Fluidez_3_Escuela_IDs)
        if is_in_lista_Fluidez_3_Escuela_IDs == False:
                # si no está en la lista de escuelas del operativo 3 de fluidez lectora
                # entonces no tiene nada para mostrar y se le pone un mensaje
                print('Escuela_ID : ' , Escuela_ID , ' ' , is_in_lista_Fluidez_3_Escuela_IDs)
                # en el json se le pone un mensaje que no tiene nada para mostrar
                dict_reporte_por_escuela[Escuela_ID] = {
                        'Escuela_ID' : Escuela_ID,
                        'datos_institucionales' : datos_institucionales.filter_datos_institucionales(Escuela_ID , dataFrame_df_nominal_df_datos_institucionales),
                        'mensaje' : 'Sin datos registrados para este Operativo de Fluidez Lectora',
                }
                pJ.pretty_print_json(dict_reporte_por_escuela)    
                # Aseguramos que `project_root` no tenga una barra final
                project_root = project_root.rstrip("\\/")
                # Construir la ruta correctamente
                ruta_json = os.path.join(
                        "\\","src", "_main_", "Fluidez_Lectora_medición_1", "2025", "05_mayo",
                        "reporte_por_escuela", "reporte_por_escuela_JSON",
                        f"{Escuela_ID}_{dict_reporte_por_escuela[Escuela_ID]['datos_institucionales']['Número']}_Fluidez_Lectora_Op_1_2025.json"
                )
                # Guardamos el JSON que no tiene nada para mostrar
                u.save_json(dict_reporte_por_escuela, ruta_json)

                # HAGO EL PDF QUE NO TIENE NADA PARA MOSTRAR
                Fluidez_Lectora_PDFs.hacer_reporte_PDF_sin_informe(dict_reporte_por_escuela,)
        else:
                #print('Escuela_ID : ' , Escuela_ID , ' ' , is_in_lista_Fluidez_3_Escuela_IDs)
        
                # print(json.dumps(
                #     datos_institucionales.filter_datos_institucionales(Escuela_ID , dataFrame_df_nominal_df_datos_institucionales),
                #     indent=4,
                #     ensure_ascii=False))
                
                # AGREGO LOS DATOS INSTITUCIONALES AL DICCIONARIO
                dict_reporte_por_escuela[Escuela_ID] = {
                        'Escuela_ID' : Escuela_ID,
                        'datos_institucionales' : datos_institucionales.filter_datos_institucionales(Escuela_ID , dataFrame_df_nominal_df_datos_institucionales),
                }    

                # Orden deseado para los cursos
                # pero debe leerse la lista de cursos normalizado para el operativo correspondiente
                lista_de_CURSOS_NORMALIZADOS = cursos.filter_df_lista_de_cursos_normalizados(Escuela_ID,dataFrame_df_nominal_df_Escuela_ID_CURSO_NORMALIZADO_list)  #['1°', '2°', '3°', '4°', '5°', '6°', '7°']
                lista_de_CURSOS_NORMALIZADOS_con_datos = cursos.filter_df_lista_de_cursos_normalizados(Escuela_ID,dataFrame_df_Fluidez_3_Escuela_ID_CURSO_NORMALIZADO_list)  #['1°', '2°', '3°', '4°', '5°', '6°', '7°']

                ###################################### ATENCIÓN ####################################################################
                # SI LA LONGITUD DE lista_de_CURSOS_NORMALIZADOS ES MENOR A LA LISTA lista_de_CURSOS_NORMALIZADOS_con_datos,
                # USAMOS LA LISTA lista_de_CURSOS_NORMALIZADOS_con_datos, PORUQ SI NO
                # EL PROGRAMA ROMPE LA EJECUCIÓN DEBIDO A QUE NO VA A ENCONTRAR LOS CURSOS CON INFORMACIÓN
                # EJEMPLO LA ESCUELA_ID = 257
                ###################################### ATENCIÓN ####################################################################

                if len(lista_de_CURSOS_NORMALIZADOS) < len(lista_de_CURSOS_NORMALIZADOS_con_datos):
                        # si la longitud de la lista de cursos normalizados es menor a la lista de cursos normalizados con datos
                        # entonces usamos la lista de cursos normalizados con datos
                        lista_de_CURSOS_NORMALIZADOS = lista_de_CURSOS_NORMALIZADOS_con_datos
                        dict_reporte_por_escuela[Escuela_ID]['lista_de_CURSOS_NORMALIZADOS_escuela_con_grado_múltiple'] = 'presenta error en los grados múltiples, se usa la lista de cursos normalizados con datos'

                ###################################### ATENCIÓN ####################################################################

                


                
                
                # AGREGO LA LISTA DE CURSOS NORMALIZADOS AL DICCIONARIO
                dict_reporte_por_escuela[Escuela_ID]['lista_de_CURSOS_NORMALIZADOS'] = lista_de_CURSOS_NORMALIZADOS
                # Y TAMBIÉN LOS CURSOS QUE APARECEN EN EL TOTAL LOS QUE CORRESPONDEN A LOS ANALIZADOS
                dict_reporte_por_escuela[Escuela_ID]['lista_de_CURSOS_NORMALIZADOS_con_datos'] = lista_de_CURSOS_NORMALIZADOS_con_datos

                # GUARDO EL TÍTULO DE LA TABLA
                dict_reporte_por_escuela[Escuela_ID]['Cantidad_de_estudiantes_censado_as'] = 'Cantidad de estudiantes censado/as en su establecimiento en primera medición ' + hoy.strftime("%Y")
                        
                
                # DESDE ACÁ SE CREAN LAS TABLAS DE DATOS QUE SE CORRESPONDE CON LA PRIMERA PARTE DEL INFORME
                # -TABLA DE CANTIDAD DE ESTUDIANTES POR CURSO
                data_dict_totalidad_de_estudiantes_por_curso = {
                        'Los_Cursos':[
                                pd.DataFrame({
                                        'Escuela_ID'                    :       [Escuela_ID] * len(lista_de_CURSOS_NORMALIZADOS),   
                                        'Curso '                        :       lista_de_CURSOS_NORMALIZADOS,                        
                                        'matricula_por_escuela_y_curso' :       [0] * len(lista_de_CURSOS_NORMALIZADOS)})  # dataframe vacío
                                ,
                                {'matricula_por_escuela_y_curso' :  ['Curso ' ,]}, # se renombra la columna
                        ]
                        ,
                        'Alumnos_por_curso':[
                                pd.DataFrame(contar_alumnos_por_escuela_y_curso.contar_alumnos_por_escuela_y_curso______filter(
                                        Escuela_ID, # la clave a buscar
                                        dataFrame_df_nominal_cantidad_de_alumnos_por_escuela_y_curso, # el dataframe
                                        True, # se resetea el índice ? 
                                        ['Escuela_ID' , 'Curso ', 'matricula_por_escuela_y_curso' , ], # qué columnas quiero mostrar 
                                        'list', # Opciones: 'dict', 'list', 'series', 'split', 'records', 'index'
                                        condiciones=None))
                                ,
                                {'matricula_por_escuela_y_curso' :  ['Alumnos_por_curso' ,]}, # se renombra la columna
                        ]
                        ,    
                        'Alumnos_inconsistentes':[            
                                pd.DataFrame(contar_alumnos_por_escuela_y_curso.contar_alumnos_por_escuela_y_curso______filter(
                                        Escuela_ID, # la clave a buscar
                                        dataFrame_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_curso_mayor_a_300_palabras, # el dataframe
                                        True, # se resetea el índice ? 
                                        ['Escuela_ID' , 'Curso ', 'matricula_por_escuela_y_curso' , ], # qué columnas quiero mostrar 
                                        'list', # Opciones: 'dict', 'list', 'series', 'split', 'records', 'index'
                                        condiciones=None))
                                ,
                                {'matricula_por_escuela_y_curso' :  ['Alumnos_inconsistentes' ,]}, # se renombra la columna
                        ]        
                        ,
                        'Alumnos_con_DESEMPEÑO':[
                                pd.DataFrame(contar_alumnos_por_escuela_y_curso.contar_alumnos_por_escuela_y_curso______filter(
                                        Escuela_ID, # la clave a buscar
                                        dataFrame_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_curso_con_MÁXIMA_cant_palabras, # el dataframe
                                        True, # se resetea el índice ? 
                                        ['Escuela_ID' , 'Curso ', 'matricula_por_escuela_y_curso' , ], # qué columnas quiero mostrar 
                                        'list', # Opciones: 'dict', 'list', 'series', 'split', 'records', 'index'
                                        condiciones=None))
                                ,
                                {'matricula_por_escuela_y_curso' :  ['Alumnos_con_DESEMPEÑO' ,]},   # se renombra la columna         
                        ] 
                        ,
                        'Alumnos_sin_DESEMPEÑO':[
                                pd.DataFrame(contar_alumnos_por_escuela_y_curso.contar_alumnos_por_escuela_y_curso______filter(
                                        Escuela_ID, # la clave a buscar
                                        dataFrame_df_Fluidez_3_cantidad_de_alumnos_por_escuela_y_curso_sin_DESEMPEÑO, # el dataframe
                                        True, # se resetea el índice ? 
                                        ['Escuela_ID' , 'Curso ', 'matricula_por_escuela_y_curso' , ], # qué columnas quiero mostrar 
                                        'list', # Opciones: 'dict', 'list', 'series', 'split', 'records', 'index'
                                        condiciones=None))
                                ,
                                {'matricula_por_escuela_y_curso' :  ['Alumnos_sin_DESEMPEÑO' ,]}, # se renombra la columna
                        ] 
                        ,
                        # 'Alumnos_incluidos_NO':[
                        #         pd.DataFrame(contar_alumnos_por_escuela_y_curso.contar_alumnos_por_escuela_y_curso______filter(
                        #                 Escuela_ID, # la clave a buscar
                        #                 dataFrame_df_Fluidez_3_cantidad_de_alumnos_incluidos_NO_por_escuela_y_curso, # el dataframe
                        #                 True, # se resetea el índice ? 
                        #                 ['Escuela_ID' , 'Curso ', 'matricula_por_escuela_y_curso' , ], # qué columnas quiero mostrar 
                        #                 'list', # Opciones: 'dict', 'list', 'series', 'split', 'records', 'index'
                        #                 condiciones=None))
                        #         ,
                        #         {'matricula_por_escuela_y_curso' :  ['Alumnos_incluidos_NO' ,]},   # se renombra la columna         
                        # ]
                        # ,
                        'Alumnos_incluidos_SI':[
                                pd.DataFrame(contar_alumnos_por_escuela_y_curso.contar_alumnos_por_escuela_y_curso______filter(
                                        Escuela_ID, # la clave a buscar
                                        dataFrame_df_Fluidez_3_cantidad_de_alumnos_incluidos_SI_por_escuela_y_curso, # el dataframe
                                        True, # se resetea el índice ? 
                                        ['Escuela_ID' , 'Curso ', 'matricula_por_escuela_y_curso' , ], # qué columnas quiero mostrar 
                                        'list', # Opciones: 'dict', 'list', 'series', 'split', 'records', 'index'
                                        condiciones=None))
                                ,
                                {'matricula_por_escuela_y_curso' :  ['Alumnos_incluidos_SI' ,]},   # se renombra la columna          
                        ]
                        ,
                }

                tabla_data_dict_totalidad_de_estudiantes_por_curso , cabecera_tabla_cursos, cuerpo_tabla_cursos, total_tabla_cursos= dT3.dataTable(
                        data_dict_totalidad_de_estudiantes_por_curso,         
                        common_column = 'Curso ',
                        show_columns = ['Curso ' , 'Alumnos_por_curso' , 'Alumnos_inconsistentes', 'Alumnos_con_DESEMPEÑO' , 'Alumnos_sin_DESEMPEÑO' , 'Alumnos_incluidos_SI' ,  ],
                        order_columns= ['Curso ' , 'Alumnos_por_curso' , 'Alumnos_inconsistentes', 'Alumnos_con_DESEMPEÑO' , 'Alumnos_sin_DESEMPEÑO' , 'Alumnos_incluidos_SI' ,  ],
                        order_rows      = {'Curso ' : lista_de_CURSOS_NORMALIZADOS},
                        operations_columns = {'Curso ' : 'Total' , 'Alumnos_por_curso' : 'sumar' , 'Alumnos_inconsistentes' : 'sumar' , 'Alumnos_con_DESEMPEÑO' : 'sumar' , 'Alumnos_sin_DESEMPEÑO' : 'sumar' ,  'Alumnos_incluidos_SI' : 'sumar' ,  },
                        column_types = {'Curso ' : str , 'Alumnos_por_curso' : int , 'Alumnos_inconsistentes' : int , 'Alumnos_con_DESEMPEÑO' : int , 'Alumnos_sin_DESEMPEÑO' : int ,  'Alumnos_incluidos_SI' : int ,  },
                        rename_columns=[{'Curso ':'Cursos' , 'Alumnos_por_curso' : 'Alumnos por curso' , 'Alumnos_inconsistentes' : 'Alumnos inconsistentes' , 'Alumnos_con_DESEMPEÑO' : 'Alumnos con DESEMPEÑO' , 'Alumnos_sin_DESEMPEÑO' : 'Alumnos sin DESEMPEÑO' ,  'Alumnos_incluidos_SI' : 'Alumnos incluidos SI' }],
                        show_total_row = True,
                        hide_zero_totals = True,
                )
                
                # Ver el resultado
                # printDF('Alumnos por curso ' , tabla_data_dict_totalidad_de_estudiantes_por_curso)
                # print('--' * 50)
                # print('--' * 50)    
                tabla_data_dict_totalidad_de_estudiantes_por_curso = tabla_data_dict_totalidad_de_estudiantes_por_curso.convert_dtypes()

                # Convertir el DataFrame a JSON asegurando los enteros
                json_data_tabla_data_dict_totalidad_de_estudiantes_por_curso = json.dumps(
                        tabla_data_dict_totalidad_de_estudiantes_por_curso.to_dict(orient='records'),
                        indent=4,
                        ensure_ascii=False
                )

                # print(json_data_tabla_data_dict_totalidad_de_estudiantes_por_curso)
                # AGREGO LA TABLA DE DATOS AL DICCIONARIO
                dict_reporte_por_escuela[Escuela_ID]['tabla_data_dict_totalidad_de_estudiantes_por_curso'] = json_data_tabla_data_dict_totalidad_de_estudiantes_por_curso

                ##### PARA HACER LA LISTA DE LOS ALUMNOS POR CURSO DEPENDIENDO DE LA TABLA tabla_data_dict_totalidad_de_estudiantes_por_curso; VER EL TOTAL Y PREGUNTAR POR LOS VALORES REQUERIDOS
                # buscamos las columnas de la tabla TOTAL y de ahí partimos para ver qué listado tenemos que imprimir
                total_cols_de_la_tabla_cursos = total_tabla_cursos.columns
                # print(total_cols)
                # descartamos lass dos primerass columnas porque lo que buscamos estpan desde la segunda en adelante..
                interested_columns_for_Student_reports = total_cols_de_la_tabla_cursos[2:]
                print('columnas interesadas : ' , interested_columns_for_Student_reports.to_list())
                # for col_interested in interested_columns_for_Student_reports:
                #     if not total[col_interested].empty:
                #             print(int(total[col_interested].iloc[0]))
                #             dict_reporte_por_escuela[Escuela_ID][col_interested] = int(total[col_interested].iloc[0])
                #     else:
                #            print("La serie está vacía.")
                
                
                
                # GENERO EL PORCENTAJE DE ALUMNOS CENSADOS RESPECTO A LA MATRÍCULA TOTAL DE LA ESCUELA
                carga_registrada_porcentaje = round(float(total_tabla_cursos['Alumnos con DESEMPEÑO'] / total_tabla_cursos['Alumnos por curso'] * 100) , 2)
                # print('carga_registrada_porcentaje : ' , carga_registrada_porcentaje)
                
                dict_reporte_por_escuela[Escuela_ID]['porcentaje_de_carga_registrada'] = 'Este informe se realizó el '+ hoy.strftime("%d/%m/%Y") +' en base al ' + str(round(carga_registrada_porcentaje)) + ' % de carga registrada en GEM.' 

                
                
                
                
                # SE RECORREN LOS CURSOS QUE HAN SIDO EVALUADOS
                for curso in lista_de_CURSOS_NORMALIZADOS:
                        if Escuela_ID not in dict_reporte_por_escuela:
                                dict_reporte_por_escuela[Escuela_ID] = {}

                        if curso not in dict_reporte_por_escuela[Escuela_ID]:
                                dict_reporte_por_escuela[Escuela_ID][curso] = {}

                        # PONGO EL TÍTULO DE LA HOJA         
                        if dict_reporte_por_escuela[Escuela_ID]['datos_institucionales']['Nivel_Unificado'] == 'Primario':
                                tipo_grado_o_curso = 'grado'
                        else:
                                # si no es primario entonces es secundario
                                # y el curso es el mismo que el grado
                                tipo_grado_o_curso = 'curso'
                        dict_reporte_por_escuela[Escuela_ID][curso]['Título_1_resultado_por_grado_curso'] = 'Resultados de '+ curso + ' ' +  tipo_grado_o_curso + ' de ' + dict_reporte_por_escuela[Escuela_ID]['datos_institucionales']['Nivel_Unificado']
                        dict_reporte_por_escuela[Escuela_ID][curso]['Título_2_porcentaje_por_grado_curso'] = 'Porcentaje de estudiantes del '+ tipo_grado_o_curso + ' por nivel de desempeño según medición' 

                        # print('curso : ' , curso)
                        # declaro algunas condiciones adicionales para el filtrado final
                        condiciones = {
                                "Curso ": [curso],  # irá cambiando según el curso
                                "DESEMPEÑO":  ['Avanzado' , 'Medio' , 'Básico' , 'Crítico'],  # solamente Avanzado y Crítico
                                "AND": True  # Lógica AND ,  "AND": False  # Lógica OR
                        }

                        # - TABLA DE PORCENTAJE DE ESTUDIANTES DEL GRADO O URSO POR NIVEL DE DESEMPEÑO SEGÚN MEDICIÓN
                        data_dict_porcentaje_de_estudiantes_por_curso_y_por_nivel_de_desempeño_según_medición = {
                                'DESEMPEÑOS':[
                                        pd.DataFrame({
                                        'Escuela_ID'                              :       [Escuela_ID,    Escuela_ID,     Escuela_ID,     Escuela_ID],
                                        'Curso '                                  :       [curso,         curso,          curso,          curso],
                                        'DESEMPEÑO'                               :       ['Avanzado',    'Medio',        'Básico',       'Crítico'], 
                                        'matricula_por_escuela_curso_y_desempeño' :       [ 0 ,  0 ,  0 , 0],
                                        'matricula_por_escuela_y_curso'           :       [ 0 ,  0 ,  0 , 0],
                                        'porcentaje_desempeno'                    :       [ 0 ,  0 ,  0 , 0],  })  # dataframe vacío
                                        
                                        ,
                                        {'porcentaje_desempeno' :  ['DESEMPEÑO' ,]},
                                ]
                                ,
                                '1°_Medición_2024':[
                                        pd.DataFrame(fL_alumnos_por_escuela_curso_y_desempeño.filtrar_alumnos_por_escuela_curso_y_desempeño_group(
                                        Escuela_ID, # la clave a buscar
                                        dataFrame_df_Fluidez_1_calcular_porcentaje_desempeno_por_escuela_y_curso, # el dataframe
                                        True, # se resetea el índice ? 
                                        ['Curso ' ,'Escuela_ID' ,  'DESEMPEÑO',  'porcentaje_desempeno', ], # qué columnas quiero mostrar 
                                        'list', # Opciones: 'dict', 'list', 'series', 'split', 'records', 'index'
                                        condiciones=condiciones))
                                        ,
                                        {'porcentaje_desempeno' :  ['Porcentaje_Primera_Medición_2024' ,]},                                       
                                ]
                                ,                
                                '1°_Medición_2025':[
                                        pd.DataFrame(fL_alumnos_por_escuela_curso_y_desempeño.filtrar_alumnos_por_escuela_curso_y_desempeño_group(
                                        Escuela_ID, # la clave a buscar
                                        dataFrame_df_Fluidez_3_calcular_porcentaje_desempeno_por_escuela_y_curso, # el dataframe
                                        True, # se resetea el índice ? 
                                        ['Curso ' ,'Escuela_ID' ,  'DESEMPEÑO',  'porcentaje_desempeno', ], # qué columnas quiero mostrar  
                                        'list', # Opciones: 'dict', 'list', 'series', 'split', 'records', 'index'
                                        condiciones=condiciones))
                                        ,
                                        {'porcentaje_desempeno' :  ['Porcentaje_Primera_Medición_2025' ,]},                                       
                                ]
                                ,
                        }

                        tabla_porcentaje_de_estudiantes_por_curso_y_por_nivel_de_desempeño_según_medición , cabecera_porcentaje, cuerpo_porcentaje, total_porcentaje = dT3.dataTable(
                        data_dict_porcentaje_de_estudiantes_por_curso_y_por_nivel_de_desempeño_según_medición,
                        common_column = 'DESEMPEÑO',
                        show_columns = ['DESEMPEÑO' , 'Porcentaje_Primera_Medición_2024' , 'Porcentaje_Primera_Medición_2025'],
                        order_columns= ['DESEMPEÑO' , 'Porcentaje_Primera_Medición_2024' , 'Porcentaje_Primera_Medición_2025'],
                        order_rows      = {'DESEMPEÑO' : ['Crítico' , 'Básico' , 'Medio' , 'Avanzado' , 'Total']}, # {'DESEMPEÑO' : ['Avanzado' , 'Medio' , 'Básico' , 'Crítico' , 'Total']},
                        operations_columns = {'DESEMPEÑO' : 'Total' , 'Porcentaje_Primera_Medición_2024' : 'sumar' , 'Porcentaje_Primera_Medición_2025' : 'sumar' ,   },
                        column_types = {'DESEMPEÑO' : str , 'Porcentaje_Primera_Medición_2024' : int , 'Porcentaje_Primera_Medición_2025' : int },
                        rename_columns=[{'DESEMPEÑO':'Niveles de Desempeño' , 'Porcentaje_Primera_Medición_2024' : 'Primera Medición 2024' , 'Porcentaje_Primera_Medición_2025' : 'Primera Medición 2025'   }],
                        show_total_row = False,
                        hide_zero_totals = False,
                        )

                        # Ver el resultado
                        # printDF('porcentajes de desempeño -- ', tabla_porcentaje_de_estudiantes_por_curso_y_por_nivel_de_desempeño_según_medición)
                        # print('--' * 50)
                        # print('--' * 50)        
                        # Forzar las columnas a enteros si no hay NaN
                        tabla_porcentaje_de_estudiantes_por_curso_y_por_nivel_de_desempeño_según_medición = tabla_porcentaje_de_estudiantes_por_curso_y_por_nivel_de_desempeño_según_medición.convert_dtypes()

                        # Convertir el DataFrame a JSON asegurando los enteros
                        json_data_tabla_porcentaje_de_estudiantes_por_curso_y_por_nivel_de_desempeño_según_medición = json.dumps(
                                tabla_porcentaje_de_estudiantes_por_curso_y_por_nivel_de_desempeño_según_medición.to_dict(orient='records'),
                                indent=4,
                                ensure_ascii=False
                        )

                        # print(json_data_tabla_porcentaje_de_estudiantes_por_curso_y_por_nivel_de_desempeño_según_medición)
                        dict_reporte_por_escuela[Escuela_ID][curso]['porcentaje_de_estudiantes_del_curso_por_nivel_de_desempeño_según_medición'] = json_data_tabla_porcentaje_de_estudiantes_por_curso_y_por_nivel_de_desempeño_según_medición




                        dict_reporte_por_escuela[Escuela_ID][curso]['Título_3_cantidad_por_grado_curso'] = 'Cantidad de estudiantes del '+ tipo_grado_o_curso + ' por nivel de desempeño según medición' 
                        # - TABLA DE CANTIDAD DE ESTUDIANTES DEL CURSO POR NIVEL DE DESEMPEÑO SEGÚN MEDICIÓN
                        # EL DICCIONARIO CON LOS DATOS CONTIENE LA CANTIDAD DE ALUMNOS POR NIVEL DE DESEMPEÑO DE LAS MEDICIONES
                        # DEL AÑO ANTERIOR Y LA DE ESTE AÑO, ES POR CADA CURSO POR LO TANTO SE DEBE ITERAR POR CURSO NORMALIZADO               
                        data_dict_cantidad_de_estudiantes_por_curso_y_por_nivel_de_desempeño_según_medición = {
                                'DESEMPEÑOS':[
                                        pd.DataFrame({
                                        'Escuela_ID'                              :       [Escuela_ID,    Escuela_ID,     Escuela_ID,     Escuela_ID],
                                        'Curso '                                   :       [curso,         curso,          curso,          curso],
                                        'DESEMPEÑO'                               :       ['Avanzado',    'Medio',        'Básico',       'Crítico'], 
                                        'matricula_por_escuela_curso_y_desempeño' :       [ 0 ,  0 ,  0 , 0]})  # dataframe vacío
                                        ,
                                        {'matricula_por_escuela_curso_y_desempeño' :  ['DESEMPEÑO' ,]},
                                ]
                                ,
                                '1°_Medición_2024':[
                                        pd.DataFrame(fL_alumnos_por_escuela_curso_y_desempeño.filtrar_alumnos_por_escuela_curso_y_desempeño_group(
                                        Escuela_ID, # la clave a buscar
                                        dataFrame_df_Fluidez_1_cantidad_de_alumnos_por_escuela_curso_y_desempeño, # el dataframe
                                        True, # se resetea el índice ? 
                                        ['Curso ' ,'Escuela_ID' ,  'DESEMPEÑO',  'matricula_por_escuela_curso_y_desempeño', ], # qué columnas quiero mostrar 
                                        'list', # Opciones: 'dict', 'list', 'series', 'split', 'records', 'index'
                                        condiciones=condiciones))
                                        ,
                                        {'matricula_por_escuela_curso_y_desempeño' :  ['Primera_Medición_2024' ,]},                                       
                                ]
                                ,                
                                '1°_Medición_2025':[
                                        pd.DataFrame(fL_alumnos_por_escuela_curso_y_desempeño.filtrar_alumnos_por_escuela_curso_y_desempeño_group(
                                        Escuela_ID, # la clave a buscar
                                        dataFrame_df_Fluidez_3_cantidad_de_alumnos_por_escuela_curso_y_desempeño, # el dataframe
                                        True, # se resetea el índice ? 
                                        ['Curso ' ,'Escuela_ID' ,  'DESEMPEÑO',  'matricula_por_escuela_curso_y_desempeño', ], # qué columnas quiero mostrar 
                                        'list', # Opciones: 'dict', 'list', 'series', 'split', 'records', 'index'
                                        condiciones=condiciones))
                                        ,
                                        {'matricula_por_escuela_curso_y_desempeño' :  ['Primera_Medición_2025' ,]},                                       
                                ]
                                ,
                        }

                        tabla_cantidad_de_estudiantes_por_curso_y_por_nivel_de_desempeño_según_medición , cabecera_cantidades, cuerpo_cantidades, total_cantidades= dT3.dataTable(
                                data_dict_cantidad_de_estudiantes_por_curso_y_por_nivel_de_desempeño_según_medición,
                                common_column = 'DESEMPEÑO',
                                show_columns = ['DESEMPEÑO' , 'Primera_Medición_2024' , 'Primera_Medición_2025'],
                                order_columns= ['DESEMPEÑO' , 'Primera_Medición_2024' , 'Primera_Medición_2025'],
                                order_rows      = {'DESEMPEÑO' : ['Avanzado' , 'Medio' , 'Básico' , 'Crítico' , 'Total']},
                                operations_columns = {'DESEMPEÑO' : 'Total' , 'Primera_Medición_2024' : 'sumar' , 'Primera_Medición_2025' : 'sumar' ,   },
                                column_types = {'DESEMPEÑO' : str , 'Primera_Medición_2024' : int , 'Primera_Medición_2025' : int },
                                rename_columns=[{'DESEMPEÑO':'Niveles de Desempeño' , 'Primera_Medición_2024' : 'Primera Medición 2024' , 'Primera_Medición_2025' : 'Primera Medición 2025'   }],
                                show_total_row = True,
                                hide_zero_totals = False,
                        )

                        # Ver el resultado
                        # printDF('cantidades de alumnos por operativo -- ', tabla_cantidad_de_estudiantes_por_curso_y_por_nivel_de_desempeño_según_medición)
                        # print('--' * 50)
                        # print('--' * 50)        
                        # Forzar las columnas a enteros si no hay NaN
                        tabla_cantidad_de_estudiantes_por_curso_y_por_nivel_de_desempeño_según_medición = tabla_cantidad_de_estudiantes_por_curso_y_por_nivel_de_desempeño_según_medición.convert_dtypes()

                        # Convertir el DataFrame a JSON asegurando los enteros
                        json_data_tabla_cantidad_de_estudiantes_por_curso_y_por_nivel_de_desempeño_según_medición = json.dumps(
                                tabla_cantidad_de_estudiantes_por_curso_y_por_nivel_de_desempeño_según_medición.to_dict(orient='records'),
                                indent=4,
                                ensure_ascii=False
                        )
                        dict_reporte_por_escuela[Escuela_ID][curso]['cantidad_de_estudiantes_del_curso_por_nivel_de_desempeño_según_medición'] = json_data_tabla_cantidad_de_estudiantes_por_curso_y_por_nivel_de_desempeño_según_medición

                        # print(json_data_tabla_cantidad_de_estudiantes_por_curso_y_por_nivel_de_desempeño_según_medición)        
                        # print('---'* 150)

                        # Escuela_ID;CURSO_NORMALIZADO;DESEMPEÑO;matricula_por_escuela_curso_y_desempeño;matricula_por_escuela_y_curso;porcentaje_desempeno
                        
                        

                        # Iteramos sobre cada columna de interés
                        #print(interested_columns_for_Student_reports)
                        # Iteramos por cada columna de interés

                        # Diccionario que relaciona las columnas con los DataFrames correspondientes
                        # esto se usa para poder iterar por los dataframes y hacer las tablas de los alumnos por curso
                        # de acuerdo a los criterios de desempeño y de  lectura inconsistente e inclussión
                        dataframes_por_categoria = {
                                "Alumnos inconsistentes"                :       [dataFrame_df_Fluidez_3_alumnos_mayor_a_300_palabras ,  ['DNI' , 'Apellido', 'Nombre', 'Curso ', 'División', 'Cant. palabras' ,]],
                                "Alumnos con DESEMPEÑO"                 :       [_union_DFs_2024_1__2024_3__2025_1_CON_DESEMPEÑO , ['DNI' , 'Apellido', 'Nombre',  'Curso ', 'División', 'Cant. palabras 1° med. 2024' , 'Cant. palabras 3° med. 2024' ,  'Cant. palabras 1° med. 2025' , 'Desemp. prim. med. 2025' ],],
                                'Alumnos sin DESEMPEÑO'                 :       [dataFrame_df_Fluidez_3_alumnos_sin_DESEMPEÑO , ['DNI' , 'Apellido', 'Nombre', 'Curso ', 'División', ]],
                                #"Alumnos incluidos NO"                  :       [dataFrame_df_Fluidez_3_alumnos_incluidos_NO, ['DNI' , 'Apellido', 'Nombre', 'Curso ', 'División', ]],
                                "Alumnos incluidos SI"                  :       [_union_DFs_2024_1__2024_3__2025_1_INCLUIDOS_SI ,  [ 'DNI' , 'Apellido', 'Nombre',  'Curso ', 'División', 'Cant. palabras 1° med. 2024' , 'Cant. palabras 3° med. 2024' ,  'Cant. palabras 1° med. 2025' ,]],
                        }

                        # Orden de desempeño para filtrar
                        orden_desempeño = ["Avanzado", "Medio", "Básico", "Crítico"]

                        # Iteramos por cada columna de interés
                        for col_interested in interested_columns_for_Student_reports:
                                if not total_tabla_cursos[col_interested].empty:
                                        total_value = int(total_tabla_cursos[col_interested].iloc[0])

                                        if total_value > 0:
                                                # Inicializamos la estructura si no existe
                                                dict_reporte_por_escuela.setdefault(Escuela_ID, {}).setdefault(curso, {})

                                                # Determinar qué DataFrame usar y las columnas correspondientes
                                                df_data = dataframes_por_categoria.get(col_interested, None)

                                                if df_data:
                                                        df_to_filter, columnas_a_mostrar = df_data  # Desempaquetamos la lista

                                                        if col_interested == "Alumnos con DESEMPEÑO":
                                                                # Guardaremos los listados agrupados por desempeño
                                                                dict_reporte_por_escuela[Escuela_ID][curso][f"Listado {col_interested} de " +  curso + ' ' +  tipo_grado_o_curso] = {}

                                                                for nivel_de_DESEMPEÑO in orden_desempeño:
                                                                        condiciones = {"Desemp. prim. med. 2025": [nivel_de_DESEMPEÑO]}  # Filtrar por nivel actual                                                        

                                                                        # Obtener los alumnos que cumplen la condición
                                                                        listado_alumnos = filtrar_dataframe_nominal_alumnos.filtrar_dataframe_nominal_por_escuela_y_curso(
                                                                                df=df_to_filter, 
                                                                                Escuela_ID=Escuela_ID, 
                                                                                CURSO_NORMALIZADO=curso,
                                                                                show_index=False,  
                                                                                columns=columnas_a_mostrar,  
                                                                                orientacion="records",
                                                                                condiciones=condiciones  
                                                                        )

                                                                        # Solo agregar la entrada si hay alumnos en ese nivel de desempeño
                                                                        if listado_alumnos:
                                                                                dict_reporte_por_escuela[Escuela_ID][curso][f"Listado {col_interested} de " +  curso + ' ' +  tipo_grado_o_curso][nivel_de_DESEMPEÑO] = listado_alumnos
                                                                                        
                                                        
                                                        else:
                                                                # Para otras categorías, se usa la lógica original
                                                                listado_alumnos = filtrar_dataframe_nominal_alumnos.filtrar_dataframe_nominal_por_escuela_y_curso(
                                                                        df=df_to_filter, 
                                                                        Escuela_ID=Escuela_ID, 
                                                                        CURSO_NORMALIZADO=curso,
                                                                        show_index=False,  
                                                                        columns=columnas_a_mostrar,  
                                                                        orientacion="records",
                                                                        condiciones=None  
                                                                )

                                                                # Guardamos el listado en el reporte
                                                                dict_reporte_por_escuela[Escuela_ID][curso][f"Listado {col_interested}"] = listado_alumnos
                                                else:
                                                        print(f"No se encontró DataFrame para la categoría: {col_interested}")
                                        else:
                                                print(f"Total en {col_interested} es 0, no se generará un listado.")
                        else:
                                print("La serie está vacía.")
                
                
                
                
                pJ.pretty_print_json(dict_reporte_por_escuela)
                
                # Aseguramos que `project_root` no tenga una barra final
                project_root = project_root.rstrip("\\/")
                        #     ruta_json = os.path.join(
                        #           '\\','src', '_main_', 'Fluidez_Lectora_medición_1', '2025', '05_mayo', 'reporte_por_escuela', 'reporte_por_escuela_JSON', f'{Escuela_ID}_{dict_reporte_por_escuela[Escuela_ID]['datos_institucionales']['Número']}_Fluidez_Lectora_Op_1_2025.json'
                        #     )
                        # Construir la ruta correctamente
                ruta_json = os.path.join(
                        "\\","src", "_main_", "Fluidez_Lectora_medición_1", "Año_2025", "mes_05_mayo",
                        "reporte_por_escuela", "reporte_por_escuela_JSON",
                        f"{Escuela_ID}_{dict_reporte_por_escuela[Escuela_ID]['datos_institucionales']['Número']}_Fluidez_Lectora_Op_1_2025.json"
                )

                # Guardamos el JSON
                u.save_json(dict_reporte_por_escuela, ruta_json)
                #exit()
                #'os.path.join(project_root,'

                # HAGO EL PDF
                Fluidez_Lectora_PDFs.hacer_reporte_PDF(dict_reporte_por_escuela,)

print('...fin..!')

# # ESTA TABLA SE HACE A NIVEL DE ESCUELA Y CURSO ASÍ QUE DEBE IR EN EL BUCLE DE CURSOS    
        # # EN ESTA PARTE CREAMOS EL LISTADO DE ALUMNOS CON DESEMPEÑO DE LAS TRES MEDCIONES
        # # LA QUE SE CORRESPONDE CON LA PRIMERA MEDICIPON DEL AÑO ANTERIOR
        # # CON LA QUE SE CORRESPONDE CON LA ÚLTIMA MEDICIÓN DEL AÑO ANTERIOR
        # # Y LA QUE SE CORRESPONDE CON LA PRIMERA MEDICIÓN DEL AÑO ACTUAL
        # # ES UNA TABLA NOMINAL QUE SE USARÁ PARA MOSTRAR LOS ALUMNOS QUE TIENEN DESEMPEÑO EN LAS TRES MEDICIONES
        # # EN CASO DE NO TENER DESEMPEÑO EN LAS MEDICIONES ANTERIORES SE COLOCARÁ UN '-' EN EL LUGAR CORRESPONDIENTE

        # # PARA EL LISTADO DE ALUMNOS CON DESEMPEÑO DE LAS TRES MEDICIONES
        # data_dict_Listado_de_estudiantes_tres_ultimas_mediciones = {
        #         'Sin_Medición':[
        #                 pd.DataFrame({
        #                         'Alumno_ID'             :       [0],
        #                         'Apellido_Alumno'       :       ['Sin_Medición'],    
        #                         'Nombre_Alumno'         :       ['Sin_Medición'],    
        #                         'Escuela_ID'            :       [Escuela_ID],   
        #                         'CURSO_NORMALIZADO'     :       None,
        #                         'División'              :       None,
        #                         'Cantidad_de_palabras': 0
        #                 })  # dataframe vacío
        #                 ,
        #                 {'Cantidad_de_palabras' :  ['Sin_Medición' ,]},                                        
        #         ]
        #         ,
        #         'Primera_Medición_Año_Anterior':[
        #                 pd.DataFrame(filtrar_dataframe_nominal_alumnos.filtrar_dataframe_nominal_por_escuela_y_curso(
        #                         df=dataFrame_df_Fluidez_1_alumnos_con_MÁXIMA_cant_palabras, 
        #                         Escuela_ID=Escuela_ID, 
        #                         CURSO_NORMALIZADO=None,
        #                         show_index=False,  
        #                         columns=['Alumno_ID', 'Apellido_Alumno', 'Nombre_Alumno', 'Escuela_ID', 'CURSO_NORMALIZADO', 'División', 'Cantidad_de_palabras'], 
        #                         orientacion="records",
        #                         condiciones=condiciones
        #                 ))
        #                 ,
        #                 {'Cantidad_de_palabras' :  ['Cant. palabras 1° med. 2024' ,]},
        #         ]
        #         ,
        #         'ültima_Medición_Año_Anterior':[
        #                 pd.DataFrame(filtrar_dataframe_nominal_alumnos.filtrar_dataframe_nominal_por_escuela_y_curso(
        #                         df=dataFrame_df_Fluidez_2_alumnos_con_MÁXIMA_cant_palabras, 
        #                         Escuela_ID=Escuela_ID, 
        #                         CURSO_NORMALIZADO=None,
        #                         show_index=False,  
        #                         columns=['Alumno_ID', 'Apellido_Alumno', 'Nombre_Alumno', 'Escuela_ID', 'CURSO_NORMALIZADO', 'División', 'Cantidad_de_palabras'], 
        #                         orientacion="records",
        #                         condiciones=condiciones
        #                 ))
        #                 ,
        #                 {'Cantidad_de_palabras' :  ['Cant. palabras 3° med. 2024' ,]},
        #         ]
        #         ,
        #         'Primera_Medición_Año_Actual':[
        #                 pd.DataFrame(filtrar_dataframe_nominal_alumnos.filtrar_dataframe_nominal_por_escuela_y_curso(
        #                         df=dataFrame_df_Fluidez_3_alumnos_con_MÁXIMA_cant_palabras, 
        #                         Escuela_ID=Escuela_ID, 
        #                         CURSO_NORMALIZADO=curso,
        #                         show_index=False,  
        #                         columns=['Alumno_ID', 'Apellido_Alumno', 'Nombre_Alumno', 'Escuela_ID', 'CURSO_NORMALIZADO', 'División', 'Cantidad_de_palabras'], 
        #                         orientacion="records",
        #                         condiciones=condiciones
        #                 ))
        #                 ,
        #                 {'Cantidad_de_palabras' :  ['Cant. palabras 1° med. 2025' ,]},
        #         ]
        #         ,
        # }

        # para aprovechar que estamos recorriendo la lista de cursos y no repetir nuevamente el bucle, en est aparte agregaremos el listado de alumnos
        # hay que ver los resultados de las columnas de la tabla la cual nos va a decir qué listado corresponde mostrar
        # LISTADO DE ALUMNOS.... Alumnos inconsistentes
        # LISTADO DE ALUMNOS.... Alumnos con DESEMPEÑO (ORDENARLOS POR DESEMPEÑO SEGÚN EL ORDEN YA SABIDO)
        # LISTADO DE ALUMNOS.... Alumnos sin DESEMPEÑO
        # LISTADO DE ALUMNOS.... Alumnos incluidos_NO
        # LISTADO DE ALUMNOS.... Alumnos incluidos_SI

        # columnas de los listados : 
        # Alumno_ID;
        # DNI;
        # DESEMPEÑO;
        # Operativo;
        # Fluidez_ID;
        # f_a.fluidez_escuela_id;
        # Persona_ID;
        # Apellido_Alumno;
        # Nombre_Alumno;
        # Sexo;
        # Fecha_Nacimiento;
        # Edad;
        # CURSO_NORMALIZADO;
        # Curso;
        # Curso_ID;
        # División;
        # División_ID;
        # Alumno_División;
        # Ausente;
        # Cantidad_de_palabras;
        # Prosodia;
        # Incluido;
        # Turno;
        # Modalidad;
        # Nivel_ID;
        # Nivel;
        # Gestión;
        # Supervisión;
        # escuela seleccionada;
        # Escuela_ID;
        # CUE;
        # subcue;
        # Número_escuela;
        # Nombre_Escuela;
        # Departamento;
        # Localidad;
        # zona;
        # Regional;
        # ciclo_lectivo;
        # separador;
        # Nivel_Unificado