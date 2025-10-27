import pandas as pd
from collections import defaultdict

def generar_diccionario_divisiones(df, col_escuela="Escuela_ID", col_curso="Curso ",
                                    col_division_id="División_ID", col_division="División"):
    """
    Genera un diccionario anidado con la estructura:
    {Escuela_ID: {Curso: {División_ID: Nombre_División}}}

    :param df: DataFrame de entrada.
    :param col_escuela: Nombre de la columna que identifica la escuela.
    :param col_curso: Nombre de la columna que identifica el curso.
    :param col_division_id: Nombre de la columna que identifica la división de forma única.
    :param col_division: Nombre de la columna que contiene el nombre de la división.
    :return: Diccionario anidado.
    """
    diccionario = {}

    # Ordenar para que el diccionario salga consistente
    df_ordenado = df.sort_values(by=[col_escuela, col_curso, col_division_id])

    for _, fila in df_ordenado.iterrows():
        escuela = fila[col_escuela]
        curso = fila[col_curso]
        division_id = fila[col_division_id]
        nombre_division = fila[col_division]

        diccionario.setdefault(escuela, {}).setdefault(curso, {})[division_id] = nombre_division

    return diccionario
