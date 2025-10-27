# esta función genera un resultado en base a los resultados de un cuestionario
# se pasa un diccionario donde el primer valor es la pregunta o item y una tupla
# como valor, el primer valor de la tupla es la respuesta correcta y el segundo valor
# es la respuesta equivalente a Sin Respuesta

import pandas as pd
import numpy as np


def clasificar_respuestas(df, respuestas_dict, col_pregunta='pregunta_id', col_opcion='opcion_id', col_resultado='resultado'):
    """
    Clasifica cada respuesta como 'Verdadero', 'Falso' o 'Sin respuesta'.

    Inserta la columna resultado justo antes de la última columna del DataFrame.

    Parámetros:
    - df: DataFrame con las columnas de preguntas y opciones seleccionadas.
    - respuestas_dict: dict con la forma {pregunta_id: (opcion_correcta, opcion_sin_respuesta)}.
    - col_pregunta: str, nombre de la columna de preguntas.
    - col_opcion: str, nombre de la columna con la opción seleccionada.
    - col_resultado: str, nombre de la nueva columna resultado a crear.

    Retorna:
    - DataFrame con la nueva columna `resultado`.
    """
    
    # Copia para evitar modificar el DataFrame original
    df = df.copy()
    
    def evaluar_respuesta(row):
        pregunta = row[col_pregunta]
        opcion = row[col_opcion]
        correcta, sin_respuesta = respuestas_dict.get(pregunta, (None, None))
        
        if opcion == correcta:
            return 'Correcto'
        elif opcion == sin_respuesta:
            return 'Sin respuesta'
        else:
            return 'Incorrecto'

    # Crear la nueva columna de resultados
    resultado = df.apply(evaluar_respuesta, axis=1)

    # Insertar antes de la última columna
    insert_index = len(df.columns) - 1
    df.insert(insert_index, col_resultado, resultado)

    return df
