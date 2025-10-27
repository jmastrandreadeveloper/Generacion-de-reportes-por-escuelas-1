# ESTE ES EL MODELO ORIGINAL EL QUE SE USÓ PARA CONSTRUIR LA FUNCIÓN,
# NO BORRAR, DEJARLO ASÍ, USAR OTROS ARCHIVOS PARA PROBAR

# esta función hace que un dataframe que está en forma de sábana se convierta en uno que está en forma de tabla
# y viceversa, es decir, que se convierta en uno que está en forma de sábana
# en este caso, el dataframe que se pasa como parámetro es el que tiene la forma de sábana y se convierte en uno que tiene  
# la forma de tabla, es decir, que tiene una fila por cada alumno y una columna por cada pregunta

import pandas as pd
import os
import sys
import json

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..' , '..' , '..' , ))
sys.path.append(project_root)

print(project_root)

import src.tools.utils as u
from src.tools.print_dataframe import print_dataframe as printDF

# def pivotear_dataframe(df, index_column, columns_column, values_column, 
#                        filtro_col=None, filtro_valores=None, 
#                        orden_columnas=None):
#     """
#     Pivotear un DataFrame largo a formato ancho, soporta múltiples columnas índice.

#     Parámetros:
#     - df: DataFrame original.
#     - index_column: str o list. Columnas a usar como índice (ej: 'Escuela_ID' o ['Escuela_ID', 'Curso']).
#     - columns_column: str. Columna que se convierte en las nuevas columnas (ej: 'DESEMPEÑO').
#     - values_column: str. Columna con los valores.
#     - filtro_col: str. Columna para filtrar (opcional).
#     - filtro_valores: list. Valores a filtrar (opcional).
#     - orden_columnas: list. Orden personalizado de columnas después del pivot (opcional).

#     Retorna:
#     - DataFrame pivotado.
#     """
#     df_filtrado = df.copy()

#     # Filtrado
#     if filtro_col and filtro_valores:
#         df_filtrado = df_filtrado[df_filtrado[filtro_col].isin(filtro_valores)]

#     # Pivot con múltiples índices si es necesario
#     df_pivot = df_filtrado.pivot(index=index_column, columns=columns_column, values=values_column)

#     # Ordenar columnas si se pide
#     if orden_columnas:
#         columnas_existentes = [col for col in orden_columnas if col in df_pivot.columns]
#         otras = [col for col in df_pivot.columns if col not in columnas_existentes]
#         df_pivot = df_pivot[columnas_existentes + otras]

#     df_pivot = df_pivot.reset_index()
#     return df_pivot

# def pivotear_dataframe(
#     df,
#     index,
#     columns,
#     values,
#     filtro_id_columnas=None,
#     filtro_ids=None,
#     orden_columnas=None
# ):
#     """
#     Convierte un DataFrame largo en formato ancho (pivot table).

#     Parámetros:
#     - df (DataFrame): El DataFrame en formato largo.
#     - index (str o list): Columnas a usar como índice en el resultado (ej: ['Escuela_ID', 'Curso']).
#     - columns (str): Columna cuyos valores se convertirán en encabezados.
#     - values (str): Columna que contiene los valores a llenar.
#     - filtro_id_columnas (list): (Opcional) Lista de columnas para filtrar antes del pivot.
#     - filtro_ids (list): (Opcional) Lista de listas con los valores a mantener en cada columna.
#     - orden_columnas (list): (Opcional) Orden deseado de las columnas (categorías del eje horizontal).

#     Retorna:
#     - DataFrame pivotado.
#     """
#     if isinstance(index, str):
#         index = [index]

#     # Filtrado previo al pivot
#     if filtro_id_columnas and filtro_ids:
#         for col, valores in zip(filtro_id_columnas, filtro_ids):
#             df = df[df[col].isin(valores)]

#     # Ordenar valores de la columna pivot si se especifica
#     if orden_columnas:
#         df[columns] = pd.Categorical(df[columns], categories=orden_columnas, ordered=True)

#     df_pivot = df.pivot_table(
#         index=index,
#         columns=columns,
#         values=values,
#         aggfunc='first'  # Podés cambiar a 'sum', 'mean', etc., según tus necesidades
#     )

#     # Si se usó orden_columnas, asegurar orden en las columnas
#     if orden_columnas:
#         df_pivot = df_pivot[orden_columnas]

#     # Restaurar columnas como parte del índice si es necesario
#     df_pivot.reset_index(inplace=True)

#     return df_pivot

# def pivotear_por_grupo(df, grupo_columna, index_column, columns_column, values_column,
#                        filtro_col=None, filtro_valores=None, orden_columnas=None):
#     """
#     Pivotear por grupo, devolviendo un diccionario de DataFrames separados.

#     Retorna:
#     - dict: {valor_grupo: DataFrame pivotado}
#     """
#     df_filtrado = df.copy()
#     if filtro_col and filtro_valores:
#         df_filtrado = df_filtrado[df_filtrado[filtro_col].isin(filtro_valores)]

#     dataframes_por_grupo = {}
#     for valor, grupo in df_filtrado.groupby(grupo_columna):
#         df_pivot = pivotear_dataframe(
#             grupo,
#             index_column=index_column,
#             columns_column=columns_column,
#             values_column=values_column,
#             orden_columnas=orden_columnas
#         )
#         dataframes_por_grupo[valor] = df_pivot
#     return dataframes_por_grupo


# def despivotear_dataframe(df, id_vars, var_name='variable', value_name='value', filtro_col=None, filtro_valores=None):
#     """
#     Convierte un DataFrame ancho en formato largo (unpivot o melt).

#     Parámetros:
#     - df (DataFrame): El DataFrame ancho.
#     - id_vars (str o list): Columnas que deben mantenerse fijas (por ejemplo, 'Escuela_ID').
#     - var_name (str): Nombre de la columna que tendrá los nombres originales de las columnas.
#     - value_name (str): Nombre de la columna que tendrá los valores.
#     - filtro_col (str): (Opcional) Nombre de la columna para filtrar.
#     - filtro_valores (list): (Opcional) Lista de valores para filtrar en esa columna.

#     Retorna:
#     - DataFrame despivotado.
#     """
#     if isinstance(id_vars, str):
#         id_vars = [id_vars]

#     df_long = pd.melt(df, 
#                       id_vars=id_vars,
#                       var_name=var_name,
#                       value_name=value_name)
    
#     if filtro_col and filtro_valores:
#         df_long = df_long[df_long[filtro_col].isin(filtro_valores)]
    
#     return df_long
# def despivotear_dataframe(
#     df,
#     id_vars,
#     var_name='variable',
#     value_name='value',
#     filtro_col=None,
#     filtro_valores=None,
#     filtro_id_columnas=None,
#     filtro_ids=None,
#     orden_columnas=None
# ):
#     """
#     Convierte un DataFrame ancho en formato largo (unpivot o melt).

#     Parámetros:
#     - df (DataFrame): El DataFrame ancho.
#     - id_vars (str o list): Columnas que deben mantenerse fijas (por ejemplo, 'Escuela_ID').
#     - var_name (str): Nombre de la columna que tendrá los nombres originales de las columnas.
#     - value_name (str): Nombre de la columna que tendrá los valores.
#     - filtro_col (str): (Opcional) Nombre de la columna para filtrar (luego del melt).
#     - filtro_valores (list): (Opcional) Lista de valores para filtrar en esa columna.
#     - filtro_id_columnas (list): (Opcional) Lista de columnas para filtrar antes del melt.
#     - filtro_ids (list): (Opcional) Lista de listas con los valores a mantener en cada columna.
#     - orden_columnas (list): (Opcional) Orden deseado de las categorías en la columna var_name.

#     Retorna:
#     - DataFrame despivotado.
#     """
#     if isinstance(id_vars, str):
#         id_vars = [id_vars]

#     # Filtrado previo (antes del melt)
#     if filtro_id_columnas and filtro_ids:
#         for col, valores in zip(filtro_id_columnas, filtro_ids):
#             df = df[df[col].isin(valores)]

#     # Melt
#     df_long = pd.melt(
#         df,
#         id_vars=id_vars,
#         var_name=var_name,
#         value_name=value_name
#     )

#     # Filtro posterior (después del melt)
#     if filtro_col and filtro_valores:
#         df_long = df_long[df_long[filtro_col].isin(filtro_valores)]

#     # Reordenar si se especificó un orden para la columna var_name
#     if orden_columnas:
#         df_long[var_name] = pd.Categorical(
#             df_long[var_name],
#             categories=orden_columnas,
#             ordered=True
#         )
#         df_long = df_long.sort_values(by=var_name)

#     return df_long

####################################################################################################################################################
# def pivotear_dataframe(
#     df,
#     index,
#     columns,
#     values,
#     filtro_id_columnas=None,
#     filtro_ids=None,
#     orden_columnas=None
# ):
#     """
#     Convierte un DataFrame largo en formato ancho (pivot table).

#     Parámetros:
#     - df (DataFrame): El DataFrame en formato largo.
#     - index (str o list): Columnas a usar como índice.
#     - columns (str): Columna cuyos valores se convertirán en encabezados.
#     - values (str): Columna que contiene los valores a llenar.
#     - filtro_id_columnas (list): (Opcional) Columnas para filtrar antes del pivot.
#     - filtro_ids (list): (Opcional) Lista de listas con los valores a mantener por columna.
#     - orden_columnas (list): (Opcional) Orden deseado de las columnas pivotadas.

#     Retorna:
#     - DataFrame pivotado.
#     """
#     if isinstance(index, str):
#         index = [index]

#     if filtro_id_columnas and filtro_ids:
#         for col, valores in zip(filtro_id_columnas, filtro_ids):
#             df = df[df[col].isin(valores)]

#     if orden_columnas:
#         df[columns] = pd.Categorical(df[columns], categories=orden_columnas, ordered=True)

#     df_pivot = df.pivot_table(
#         index=index,
#         columns=columns,
#         values=values,
#         aggfunc='first'
#     )

#     if orden_columnas:
#         df_pivot = df_pivot[orden_columnas]

#     df_pivot.reset_index(inplace=True)

#     return df_pivot

# def pivotear_por_grupo(
#     df,
#     grupo_columna,
#     index,
#     columns,
#     values,
#     filtro_id_columnas=None,
#     filtro_ids=None,
#     orden_columnas=None
# ):
#     """
#     Pivotear por grupo, devolviendo un diccionario de DataFrames separados.

#     Parámetros:
#     - df (DataFrame): DataFrame original.
#     - grupo_columna (str): Columna para agrupar.
#     - index (str o list): Columnas a usar como índice en cada grupo.
#     - columns (str): Columna que se convertirá en encabezados.
#     - values (str): Columna que contiene los valores.
#     - filtro_id_columnas (list): (Opcional) Columnas para filtrar antes del pivot.
#     - filtro_ids (list): (Opcional) Lista de listas con los valores a mantener por columna.
#     - orden_columnas (list): (Opcional) Orden deseado de las columnas pivotadas.

#     Retorna:
#     - dict: {valor_grupo: DataFrame pivotado}
#     """
#     df_filtrado = df.copy()

#     if filtro_id_columnas and filtro_ids:
#         for col, valores in zip(filtro_id_columnas, filtro_ids):
#             df_filtrado = df_filtrado[df_filtrado[col].isin(valores)]

#     dataframes_por_grupo = {}
#     for valor, grupo in df_filtrado.groupby(grupo_columna):
#         df_pivot = pivotear_dataframe(
#             grupo,
#             index=index,
#             columns=columns,
#             values=values,
#             orden_columnas=orden_columnas
#         )
#         dataframes_por_grupo[valor] = df_pivot

#     return dataframes_por_grupo


# def despivotear_dataframe(
#     df,
#     id_vars,
#     var_name='variable',
#     value_name='value',
#     filtro_col=None,
#     filtro_valores=None,
#     filtro_id_columnas=None,
#     filtro_ids=None,
#     orden_columnas=None
# ):
#     """
#     Convierte un DataFrame ancho en formato largo (unpivot o melt).

#     Parámetros:
#     - df (DataFrame): El DataFrame ancho.
#     - id_vars (str o list): Columnas a mantener fijas (por ejemplo, 'Escuela_ID').
#     - var_name (str): Nombre de la columna con los nombres originales.
#     - value_name (str): Nombre de la columna con los valores.
#     - filtro_col (str): (Opcional) Columna para filtrar después del melt.
#     - filtro_valores (list): (Opcional) Valores para filtrar después del melt.
#     - filtro_id_columnas (list): (Opcional) Columnas para filtrar antes del melt.
#     - filtro_ids (list): (Opcional) Lista de listas con los valores a mantener por columna.
#     - orden_columnas (list): (Opcional) Orden deseado en la columna `var_name`.

#     Retorna:
#     - DataFrame despivotado.
#     """
#     if isinstance(id_vars, str):
#         id_vars = [id_vars]

#     # Filtrado previo
#     if filtro_id_columnas and filtro_ids:
#         for col, valores in zip(filtro_id_columnas, filtro_ids):
#             df = df[df[col].isin(valores)]

#     # Melt
#     df_long = pd.melt(
#         df,
#         id_vars=id_vars,
#         var_name=var_name,
#         value_name=value_name
#     )

#     # Filtro posterior
#     if filtro_col and filtro_valores:
#         df_long = df_long[df_long[filtro_col].isin(filtro_valores)]

#     # Reordenar categorías si se especifica
#     if orden_columnas:
#         df_long[var_name] = pd.Categorical(df_long[var_name], categories=orden_columnas, ordered=True)
#         df_long = df_long.sort_values(by=var_name)

#     return df_long
###################################################################################################################
# Función: Pivotear un DataFrame (de largo a ancho)
def pivotear_dataframe(
    df,
    index,
    columns,
    values,
    filtro_id_columnas=None,
    filtro_ids=None,
    orden_columnas=None
):
    """
    Convierte un DataFrame largo en formato ancho (pivot table).

    Parámetros:
    - df (DataFrame): El DataFrame en formato largo.
    - index (str o list): Columnas a usar como índice.
    - columns (str): Columna cuyos valores se convertirán en encabezados.
    - values (str): Columna que contiene los valores a llenar.
    - filtro_id_columnas (list): (Opcional) Columnas para filtrar antes del pivot.
    - filtro_ids (list): (Opcional) Lista de listas con los valores a mantener por columna.
    - orden_columnas (list): (Opcional) Orden deseado de las columnas pivotadas.

    Retorna:
    - DataFrame pivotado.
    """
    if isinstance(index, str):
        index = [index]

    if filtro_id_columnas and filtro_ids:
        for col, valores in zip(filtro_id_columnas, filtro_ids):
            df = df[df[col].isin(valores)]

    if orden_columnas:
        df[columns] = pd.Categorical(df[columns], categories=orden_columnas, ordered=True)

    df_pivot = df.pivot_table(
        index=index,
        columns=columns,
        values=values,
        aggfunc='first'
    )

    if orden_columnas:
        df_pivot = df_pivot[orden_columnas]

    df_pivot.reset_index(inplace=True)

    return df_pivot


# Función: Pivotear por grupo, devolviendo un diccionario de DataFrames separados
def pivotear_por_grupo(
    df,
    grupo_columna,
    index,
    columns,
    values,
    filtro_id_columnas=None,
    filtro_ids=None,
    orden_columnas=None
):
    """
    Pivotear por grupo, devolviendo un diccionario de DataFrames separados.

    Parámetros:
    - df (DataFrame): DataFrame original.
    - grupo_columna (str): Columna para agrupar.
    - index (str o list): Columnas a usar como índice en cada grupo.
    - columns (str): Columna que se convertirá en encabezados.
    - values (str): Columna que contiene los valores.
    - filtro_id_columnas (list): (Opcional) Columnas para filtrar antes del pivot.
    - filtro_ids (list): (Opcional) Lista de listas con los valores a mantener por columna.
    - orden_columnas (list): (Opcional) Orden deseado de las columnas pivotadas.

    Retorna:
    - dict: {valor_grupo: DataFrame pivotado}
    """
    df_filtrado = df.copy()

    if filtro_id_columnas and filtro_ids:
        for col, valores in zip(filtro_id_columnas, filtro_ids):
            df_filtrado = df_filtrado[df_filtrado[col].isin(valores)]

    dataframes_por_grupo = {}
    for valor, grupo in df_filtrado.groupby(grupo_columna):
        df_pivot = pivotear_dataframe(
            grupo,
            index=index,
            columns=columns,
            values=values,
            orden_columnas=orden_columnas
        )
        dataframes_por_grupo[valor] = df_pivot

    return dataframes_por_grupo


# ultima versión
# Función: Despivotear (unpivot o melt) un DataFrame
def despivotear_dataframe(
    df,
    id_vars,
    var_name='variable',
    value_name='value',
    filtro_col=None,
    filtro_valores=None,
    filtro_id_columnas=None,
    filtro_ids=None,
    orden_columnas=None
):
    """
    Convierte un DataFrame ancho en formato largo (unpivot o melt).

    Parámetros:
    - df (DataFrame): El DataFrame ancho.
    - id_vars (str o list): Columnas que deben mantenerse fijas (por ejemplo, 'Escuela_ID').
    - var_name (str): Nombre de la columna que tendrá los nombres originales de las columnas.
    - value_name (str): Nombre de la columna que tendrá los valores.
    - filtro_col (str): (Opcional) Nombre de la columna para filtrar (luego del melt).
    - filtro_valores (list): (Opcional) Lista de valores para filtrar en esa columna.
    - filtro_id_columnas (list): (Opcional) Lista de columnas para filtrar antes del melt.
    - filtro_ids (list): (Opcional) Lista de listas con los valores a mantener en cada columna.
    - orden_columnas (list): (Opcional) Orden deseado de las categorías en la columna var_name.

    Retorna:
    - DataFrame despivotado.
    """
    if isinstance(id_vars, str):
        id_vars = [id_vars]

    # Filtrado previo (antes del melt)
    if filtro_id_columnas and filtro_ids:
        for col, valores in zip(filtro_id_columnas, filtro_ids):
            df = df[df[col].isin(valores)]

    # Melt (despivotar)
    df_long = pd.melt(
        df,
        id_vars=id_vars,
        var_name=var_name,
        value_name=value_name
    )

    # Filtro posterior (después del melt)
    if filtro_col and filtro_valores:
        df_long = df_long[df_long[filtro_col].isin(filtro_valores)]

    # Reordenar si se especificó un orden para la columna var_name
    if orden_columnas:
        df_long[var_name] = pd.Categorical(
            df_long[var_name],
            categories=orden_columnas,
            ordered=True
        )
        df_long = df_long.sort_values(by=var_name)

    return df_long

# Llamar a la función de prueba si el script se ejecuta directamente
if __name__ == '__main__':
    Escuela_ID = 4  # Reemplaza con un ID de escuela válido 

    # PATH_file_df_Fluidez_1_calcular_porcentaje_desempeno_por_escuela = 'data/processed/transformed/Fluidez/df_Fluidez_1_calcular_porcentaje_desempeno_por_escuela.csv'    
    # csv_path = os.path.join(project_root, PATH_file_df_Fluidez_1_calcular_porcentaje_desempeno_por_escuela)
    # df_Fluidez_1_calcular_porcentaje_desempeno_por_escuela = u.cargar_csv_2(csv_path)

    PATH_file_df_Fluidez_1_calcular_porcentaje_desempeno_por_escuela_y_curso = 'data/processed/transformed/Fluidez/df_Fluidez_1_calcular_porcentaje_desempeno_por_escuela_y_curso.csv'    
    csv_path = os.path.join(project_root, PATH_file_df_Fluidez_1_calcular_porcentaje_desempeno_por_escuela_y_curso)
    df_Fluidez_1_calcular_porcentaje_desempeno_por_escuela_y_curso = u.cargar_csv_2(csv_path)

    
    # df_pivotado = pivotear_dataframe(
    #     df=df_Fluidez_1_calcular_porcentaje_desempeno_por_escuela_y_curso,
    #     index_column=['Escuela_ID', 'Curso '],
    #     columns_column='DESEMPEÑO',
    #     values_column='matricula_por_escuela_curso_y_desempeño',
    #     filtro_col='Escuela_ID',
    #     filtro_valores=[4, 5, 6],
    #     orden_columnas=['Avanzado', 'Medio', 'Básico', 'Crítico']
    # )
    # df_pivotado = pivotear_dataframe(
    #     df=df_Fluidez_1_calcular_porcentaje_desempeno_por_escuela_y_curso,
    #     index=['Escuela_ID', 'Curso '],
    #     columns='DESEMPEÑO',
    #     values='matricula_por_escuela_curso_y_desempeño',
    #     filtro_id_columnas=['Escuela_ID', 'Curso '],
    #     filtro_ids=[[4, 5, 6], ['2°', '3°']],
    #     orden_columnas=['Avanzado', 'Medio', 'Básico', 'Crítico']
    # )
    
    # printDF('df_pivotado ',df_pivotado)
    # print('-'*100)


    
    # df_dict = pivotear_por_grupo(
    #     df=df_Fluidez_1_calcular_porcentaje_desempeno_por_escuela_y_curso,
    #     grupo_columna='Escuela_ID',                      # Se agrupará un DataFrame por cada Escuela_ID
    #     index_column='Curso ',                            # Por cada curso dentro de cada escuela
    #     columns_column='DESEMPEÑO',                      # Los valores únicos de DESEMPEÑO serán las columnas
    #     values_column='matricula_por_escuela_curso_y_desempeño',
    #     orden_columnas=['Avanzado', 'Medio', 'Básico', 'Crítico']  # Orden personalizado
    # )
    # df = df_dict[4]
    
    # printDF('df_pivotado_por_grupo ',df)
    # print('-'*100)      

    # # df_despivotado = despivotear_dataframe(
    # #     df=df_pivotado,
    # #     id_vars='Escuela_ID',
    # #     var_name='DESEMPEÑO',
    # #     value_name='matricula_por_escuela_y_desempeño',
    # #     filtro_col='Escuela_ID',
    # #     filtro_valores=[4, 5, 6]
    # # )
    # df_largo = despivotear_dataframe(
    #     df=df_pivotado,
    #     id_vars=['Escuela_ID', 'Curso '],
    #     var_name='DESEMPEÑO',
    #     value_name='matricula',
    #     filtro_id_columnas=['Escuela_ID', 'Curso '],
    #     filtro_ids=[[4, 5], ['2°', '3°']],
    #     orden_columnas=['Avanzado', 'Medio', 'Básico', 'Crítico']
    # )

    # printDF('df_despivotado ',df_largo)
    # print('-'*100)

    df_pivot = pivotear_dataframe(
        df=df_Fluidez_1_calcular_porcentaje_desempeno_por_escuela_y_curso,
        index=['Escuela_ID', 'Curso '],
        columns='DESEMPEÑO',
        values='matricula_por_escuela_curso_y_desempeño',
        filtro_id_columnas=['Escuela_ID'],    # opcional
        filtro_ids=[[4]],                     # solo la escuela 4
        orden_columnas=['Avanzado','Medio','Básico','Crítico']
    )
    
    printDF('pivotear_dataframe ',df_pivot)

    dfs_por_escuela = pivotear_por_grupo(
        df=df_Fluidez_1_calcular_porcentaje_desempeno_por_escuela_y_curso,
        grupo_columna='Escuela_ID',
        index=['Curso '],
        columns='DESEMPEÑO',
        values='matricula_por_escuela_curso_y_desempeño',
        orden_columnas=['Avanzado','Medio','Básico','Crítico']
    )

    # Accedés a la escuela 4 así:    
    printDF('pivotear_por_grupo ',dfs_por_escuela[4])

    df_largo_de_nuevo = despivotear_dataframe(
        df=df_pivot,
        id_vars=['Escuela_ID', 'Curso '],  # Aquí incluyes 'Curso' para mantenerla
        var_name='DESEMPEÑO',
        value_name='matricula',
        filtro_col=None,
        filtro_valores=None,
        filtro_id_columnas=['Escuela_ID'],  # Ejemplo de filtro por Escuela_ID
        filtro_ids=[[4]],  # Solo para la escuela 4
        orden_columnas=['Avanzado','Medio','Básico','Crítico']
    )
    
    printDF('despivotear_dataframe ',df_largo_de_nuevo)


    print('...fin...!')