# para hacer el análisis de los alumnos con discapacidades
# el archivo princcipal del análsisi de matemáticas
import os
import sys


#'C:\Users\w10-21h2\Documents\GitHub\python_data_analysis_v3\src\_main_\Fluidez_Lectora_medición_1\Año_2025\mes_05_mayo\data\raw\_NOMINAL_AL_13_04_2025_PARA_FL_2025_ABRIL.csv'

# el project_root tiene una profundidad de carpetas medidas por los '..', eso es lo que dice la linea de abajo
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..' , '..' )) # E:\GitHub\python_data_analysis_v3\src
sys.path.append(project_root)
# obligatorio para poder acceder a todas las funcionalidades de las librerias para el proyecto y todo lo demas
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))
# en esta parte le digo que los datos van a estar dentro de dos subcarpetas acá mismo
raw_data = os.path.join(os.path.dirname(__file__),'data','raw')

import pandas as pd
import src.tools.utils as u

from src.tools.print_dataframe import print_dataframe as printDF


# cargo el archivo
df_ = u.cargar_csv_2(raw_data + '/' +  '_df_nominal_alumnos_con_discapacidades.csv')

import pandas as pd


# Cargar tu DataFrame
# df = pd.read_csv('ruta_a_tu_archivo.csv')  # si el archivo está en CSV



# Cargar el DataFrame
# df = pd.read_csv("archivo.csv")

# Columnas de discapacidad
discapacidad_cols = [
    'Intelectual', 'Mental', 'Visual', 'Auditiva', 'Motriz',
    'Docente_Acompañante', 'Otra_Discapacidad', 'Múltiple',
    'CUD_Certificado', 'Tiene_PPI'
]

# Columnas por las que se va a agrupar
grupo_cols = ['ID_escuela', 'Nivel' , 'Numero_escuela' ,	'Anexo' , 	'Número_Anexo' ,	'Escuela'  , 'CURSO_NORMALIZADO', 'Division', 'Sexo']

# Normalizar: pasar a string, quitar espacios, convertir a minúsculas
for col in discapacidad_cols:
    df_[col] = df_[col].astype(str).str.strip().str.lower()

# Función que devuelve 1 si hay alguna discapacidad informada (no "0", "", "nan")
def discapacidad_presente(valor):
    return 0 if valor in ['0', '', 'nan', 'no', '0.0'] else 1

# Aplicar la función a todas las columnas de discapacidad
for col in discapacidad_cols:
    df_[col] = df_[col].apply(discapacidad_presente)

# Eliminar duplicados si es necesario (por Alumno_ID)
df = df_.drop_duplicates(subset=['Alumno_ID'] + grupo_cols)

# Agrupar y sumar
df_grouped = df.groupby(grupo_cols)[discapacidad_cols].sum().reset_index()

print(df_grouped.head())


u.guardar_dataframe_a_csv(df_grouped,'/src/_main_/ALumnos_con_discapacidades/Año_2025/mes_06_junio/data/raw/_df_grouped_nominal_alumnos_con_discapacidades.csv')

print(df_grouped.head())