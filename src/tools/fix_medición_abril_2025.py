import data_loading as u 
import utils as u

import pandas as pd

import numpy as np
import csv

# función para arreglar la escuela S132
# debe cambiar el 
# sep_            = ';'
# encoding_       = "UTF-8"
# lineterminator_ = '\n'


df_fluidez_3 = u.cargar_csv('3-FLUIDEZ_LECTORA_PRIMERA_MEDICIÓN_ABRIL_38_39_40_41.csv')


# arreglar el subcue
def convert_to_int_or_str_(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return 0
    
# for col in ['subcue']:
#     df_fluidez_3[col] = pd.to_numeric(df_fluidez_3[col], errors='coerce').fillna('-').apply(convert_to_int_or_str_)

# Función para actualizar una fila específica sin alterar otras columnas
def actualizar_fila(df, escuela_id, valor_actual, nuevo_valor):
    # Actualizar solo la columna 'Incluido'
    df.loc[(df['Escuela_ID'] == escuela_id) & (df['Incluido'] == valor_actual), 'Incluido'] = nuevo_valor
    return df


lista_de_Escuela_ID_a_cambiar = [502 , 1923 , 1957 , 4866 , ]

# Actualizar las filas relacionadas con el Escuela_ID = 2037 (S132)
for Escuela_ID in lista_de_Escuela_ID_a_cambiar:
    df_actualizado = actualizar_fila(df_fluidez_3, Escuela_ID , 'Si', 'No')  

# Verificar que los valores no se pierdan después de la modificación
print("Datos después de la modificación:", df_actualizado[['subcue', 'Número_escuela']].head())

# Guardar el DataFrame actualizado
u.guardar_dataframe_a_csv(df_fluidez_3  ,   '/data/raw/_3-fixed-FLUIDEZ_LECTORA_PRIMERA_MEDICIÓN_ABRIL_38_39_40_41.csv')