import pandas as pd
import json
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..' ,  ))
sys.path.append(project_root)
import src.tools.print_dataframe as printDFrame

import pandas as pd
from functools import reduce

def test_(message = ''):
    print('hello dataTable..!!! ' , message)

def expand_columns(data_dict):
    """
    Añade columnas a cada DataFrame según los nombres especificados en el diccionario.
    Si un DataFrame está vacío, se usa la estructura del primer DataFrame del diccionario.
    """
    updated_data_dict = {}
    
    # Obtener el primer DataFrame del diccionario como referencia
    first_key = next(iter(data_dict))  # Obtener la primera clave
    first_df = data_dict[first_key][0].copy()  # Obtener la estructura del primer DataFrame
    
    for key, (df, column_map) in data_dict.items():
        # Si el DataFrame está vacío, usa la estructura del primer DataFrame
        df_copy = df.copy() if not df.empty else first_df.copy()
        
        # Agregar las columnas nuevas especificadas en column_map
        for col, new_names in column_map.items():
            if col in df_copy.columns:  # Verifica que la columna exista antes de replicarla
                for new_col in new_names:
                    df_copy[new_col] = df_copy[col]
        
        updated_data_dict[key] = df_copy
    
    return updated_data_dict


def join_dataframes(data_dict, common_column):
    #print('join_dataframes ' , common_column)
    """
    Une todos los DataFrames en data_dict usando la columna en común.
    Convierte la columna clave a str para evitar errores de tipo.
    Maneja conflictos de nombres de columnas con sufijos personalizados.
    """
    df_list = []

    for key, df in data_dict.items():
        df = df.copy()
        df[common_column] = df[common_column].astype(str)  # 🔹 Asegurar que la clave es string
        df_list.append(df)

    # Inicializar con el primer DataFrame
    df_final = df_list[0]

    # Merge sucesivos con sufijos personalizados
    for i, df in enumerate(df_list[1:], start=1):
        df_final = df_final.merge(df, on=common_column, how='outer', suffixes=('', f'_dup{i}'))

    #printDFrame.print_dataframe('df_final ' , df_final , numfilas=70)
    return df_final

def replace_nan_with_zero(df):
    #print('replace_nan_with_zero')
    
    """
    Reemplaza los valores NaN en un DataFrame con ceros.
    
    :param df: DataFrame de entrada.
    :return: DataFrame con NaN reemplazados por 0.
    """
    #print(df)
    return df.fillna(0)

def show_columns_df(df, show_columns, order_columns=None , verbose = False):
    #print('show_columns_df')
    #print(df)
    """
    Función que devuelve un DataFrame con solo las columnas especificadas,
    agregando las faltantes con valores de cero.
    
    :param df: El DataFrame original.
    :param show_columns: Lista de columnas que se desean mostrar.
    :param order_columns: (Opcional) Lista de las columnas en el orden deseado.
    
    :return: DataFrame con las columnas seleccionadas.
    """
    if verbose :
        print(df.columns)

    # Agregar columnas faltantes con valores de cero
    for col in show_columns:
        if col not in df.columns:
            df[col] = 0

    # Filtrar las columnas deseadas
    df_filtered = df[show_columns]

    # Ordenar las columnas si se proporciona el parámetro order
    if order_columns:
        df_filtered = df_filtered[order_columns]

    # # Imprimir el resultado para depuración (opcional)
    # if verbose :
    #     printDFrame.print_dataframe('show_columns_df -- ', df_filtered)
    #     #print(df_filtered)

    #print(df_filtered)
    return df_filtered

def reorder_rows(df, order_dict):
    #print(df)
    """
    Reordena las filas del DataFrame según un orden específico basado en un diccionario.

    :param df: DataFrame original.
    :param order_dict: Diccionario donde la clave es el nombre de la columna y el valor es la lista con el orden deseado.
    :return: DataFrame con las filas reorganizadas.
    """
    for column, order_list in order_dict.items():
        if column in df.columns:
            # Convertimos tanto la columna como el orden a string
            df[column] = df[column].astype(str)
            order_list_str = list(dict.fromkeys([str(i) for i in order_list]))  # Elimina duplicados manteniendo el orden

            # Convertimos a tipo categórico con el orden deseado
            df[column] = pd.Categorical(df[column], categories=order_list_str, ordered=True)

            # Ordenamos
            df = df.sort_values(by=column).reset_index(drop=True)
        else:
            raise KeyError(f"La columna '{column}' no existe en el DataFrame.")

    #print(df)
    return df



# def reorder_rows(df, order_dict):
#     print('reorder_rows')
#     print(df)
#     """
#     Reordena las filas del DataFrame según un orden específico basado en un diccionario.
    
#     :param df: DataFrame original.
#     :param order_dict: Diccionario donde la clave es el nombre de la columna y el valor es la lista con el orden deseado.
#     :return: DataFrame con las filas reorganizadas.
#     """
#     for column, order_list in order_dict.items():
#         print(column)
#         print(order_list)
#         print(df['Escuela_ID'].dtype)
#         print(order_list)
#         print([type(i) for i in order_list])
#         print(df['Escuela_ID'].unique())
#         exit()
        
#         if column in df.columns:
#             print('la columna ' , column , ' existe en el dataframe')
#             # Convertimos la columna a tipo categórico con el orden deseado
#             df[column] = pd.Categorical(df[column], categories=order_list, ordered=True)
#             #df[column] = pd.DataFrame({column : order_list})
#             print('dentro del for')
#             print(df)
#             df = df.sort_values(by=column).reset_index(drop=True)
#             #print(df)
#         else:
#             raise KeyError(f"La columna '{column}' no existe en el DataFrame.")
#     print('after reorder_rows')
#     print(df)
#     return df
# def reorder_rows(df, order_dict):
#     # print('reorder_rows')
#     # print(df)

#     for column, order_list in order_dict.items():
#         if column in df.columns:
#             # Armamos una lista completa: primero los del orden deseado, luego el resto
#             all_values = df[column].unique().tolist()
#             full_order = [v for v in order_list if v in all_values] + [v for v in all_values if v not in order_list]

#             # Creamos una columna auxiliar con el orden
#             df['__sort_order__'] = df[column].apply(lambda x: full_order.index(x) if x in full_order else -1)

#             # Ordenamos y limpiamos
#             df = df.sort_values(by='__sort_order__').drop(columns='__sort_order__').reset_index(drop=True)
#         else:
#             raise KeyError(f"La columna '{column}' no existe en el DataFrame.")

#     # print('after reorder_rows')
#     # print(df)
#     return df

def rename_columns_in_dataframe(df, rename_columns , ):
    """
    Renombra las columnas de un DataFrame según un diccionario proporcionado.
    
    :param df: DataFrame al que se le cambiarán los nombres de columnas.
    :param rename_columns: Lista de diccionarios con los cambios de nombres.
    :return: DataFrame con columnas renombradas.
    """
    if not rename_columns:
        return df  # Si no hay renombramiento, devolver el DF original
    
    rename_dict = {}
    for rename_map in rename_columns:
        rename_dict.update(rename_map)  # Unimos todos los diccionarios de renombramiento

    df = df.rename(columns=rename_dict)  # Aplicamos los cambios
      
    
    return df

# def apply_operations(df, operations_columns):
#     #print(df)   
#     """
#     Aplica las operaciones especificadas en operations_columns sobre el DataFrame df.
    
#     - Si el valor es 'Total', agrega una fila con 'Total' en esa columna.
#     - Si el valor es 'sumar', calcula la suma de la columna y la coloca en la fila 'Total'.
#     """
#     df_copy = df.copy()
    
#     # Agregar la fila 'Total' si está especificado en alguna columna
#     if 'Total' in operations_columns.values():
#         total_row = {col: 'Total' if col == list(operations_columns.keys())[0] else 0 for col in df.columns}
#         df_copy = pd.concat([df_copy, pd.DataFrame([total_row])], ignore_index=True)
    
#     # Aplicar operaciones (sumar)
#     for col, operation in operations_columns.items():
#         if operation == 'sumar' and col in df_copy.columns:
#             df_copy.loc[df_copy[df_copy.iloc[:, 0] == 'Total'].index, col] = df_copy[col].sum()
    
#     return df_copy

import pandas as pd
import numpy as np

# def apply_operations_funcionabien(df, operations_columns):
#     """
#     Aplica operaciones de suma y agrega fila Total con valores apropiados.
    
#     - Coloca 'Total' en la columna indicada.
#     - Suma las columnas numéricas especificadas.
#     - Deja celdas vacías ('') en columnas no involucradas en sumas.
#     """
#     df_copy = df.copy()
    
#     # Identificar columna que llevará la etiqueta 'Total'
#     columna_total = next((col for col, op in operations_columns.items() if op == 'Total'), None)
    
#     if columna_total:
#         total_row = {}
#         for col in df.columns:
#             if col == columna_total:
#                 total_row[col] = 'Total'
#             elif operations_columns.get(col) == 'sumar':
#                 total_row[col] = 0  # Inicializa en 0 para permitir suma
#             else:
#                 total_row[col] = ''  # Estético: vacío para las no numéricas

#         df_copy = pd.concat([df_copy, pd.DataFrame([total_row])], ignore_index=True)

#         # Sumar las columnas indicadas
#         for col, op in operations_columns.items():
#             if op == 'sumar' and col in df_copy.columns:
#                 try:
#                     total_value = pd.to_numeric(df_copy[col], errors='coerce').sum()
#                     df_copy.loc[df_copy[columna_total] == 'Total', col] = total_value
#                 except Exception as e:
#                     print(f"Error al sumar la columna {col}: {e}")
    
#     return df_copy

def apply_operations(df, operations_columns, total_label='Total'):
    """
    Aplica operaciones de suma y agrega una fila con un total personalizado.

    Parámetros:
    - df: DataFrame original.
    - operations_columns: dict con columnas y operación ('sumar' o 'Total').
    - total_label: texto a mostrar en la fila total (por defecto: 'Total').

    Ejemplo:
        operations_columns = {
            'Escuela': 'Total',
            'Censados': 'sumar',
            'Matrícula': 'sumar'
        }
    """
    df_copy = df.copy()

    # Identificar la columna donde se coloca el total_label (ej. 'Escuela')
    columna_total = next((col for col, op in operations_columns.items() if op == 'Total'), None)

    if columna_total:
        # Construir la fila total
        total_row = {}
        for col in df.columns:
            if col == columna_total:
                total_row[col] = total_label
            elif operations_columns.get(col) == 'sumar':
                total_row[col] = 0  # inicializa para suma
            else:
                total_row[col] = ''  # estético

        # Agregar la fila vacía
        df_copy = pd.concat([df_copy, pd.DataFrame([total_row])], ignore_index=True)

        # Aplicar sumas donde corresponda
        for col, op in operations_columns.items():
            if op == 'sumar' and col in df_copy.columns:
                try:
                    total_value = pd.to_numeric(df_copy[col], errors='coerce').sum()
                    df_copy.loc[df_copy[columna_total] == total_label, col] = total_value
                except Exception as e:
                    print(f"Error al sumar la columna {col}: {e}")

    return df_copy



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

def drop_rows_with_nan(df):
    """
    Elimina las filas que contienen al menos un valor NaN en cualquier columna.
    
    :param df: DataFrame de Pandas
    :return: DataFrame sin filas con NaN
    """
    return df.dropna(how="any").reset_index(drop=True)

def show_total_row_df(df, show_total_row=True):
    """
    Elimina filas con el valor 'Total' en cualquier columna si show_total_row=False.

    Args:
        df (pd.DataFrame): DataFrame de entrada.
        show_total_row (bool): Si False, elimina filas que contengan 'Total' en cualquier columna.

    Returns:
        pd.DataFrame: DataFrame sin las filas que contienen 'Total' si show_total_row es False.
    """
    df_copy = df.copy()

    if not show_total_row:
        mask = ~(df_copy == 'Total').any(axis=1)  # Filtrar filas donde no haya 'Total'
        df_copy = df_copy[mask]

    return df_copy

def hide_zero_total_columns(df, hide_zero_totals=True):
    """
    Elimina las columnas cuyo total es igual a cero si la opción está activada.
    
    :param df: DataFrame a procesar
    :param hide_zero_totals: Booleano, si es True elimina las columnas con total 0
    :return: DataFrame con las columnas filtradas
    """
    if hide_zero_totals:
        total_values = df.sum(numeric_only=True)  # Sumar solo columnas numéricas
        zero_total_columns = total_values[total_values == 0].index  # Columnas con total 0
        df = df.drop(columns=zero_total_columns)  # Eliminar columnas con total 0
    
    return df

def completar_rows(df_agrupado, columna_categoria, columna_valor, valores_esperados, valor_por_defecto=0):
    """
    Asegura que en el DataFrame estén presentes todos los valores esperados en una columna específica.

    Parámetros:
    - df_agrupado: DataFrame con los datos agrupados.
    - columna_categoria: Nombre de la columna con los valores categóricos.
    - columna_valor: Nombre de la columna con los valores numéricos.
    - valores_esperados: Lista con los valores que deben estar siempre presentes.
    - valor_por_defecto: Valor a asignar si falta una categoría (por defecto 0).

    Retorna:
    - DataFrame con todas las categorías aseguradas.
    """

    # Convertimos el DataFrame en un diccionario para acceso rápido
    datos_existentes = dict(zip(df_agrupado[columna_categoria], df_agrupado[columna_valor]))

    # Completamos los valores que falten con el valor por defecto
    datos_completos = {valor: datos_existentes.get(valor, valor_por_defecto) for valor in valores_esperados}

    # Convertimos de nuevo en DataFrame
    df_completo = pd.DataFrame(list(datos_completos.items()), columns=[columna_categoria, columna_valor])

    return df_completo

def dividir_dataframe(df):
    """
    Divide un DataFrame en tres partes: cabecera, cuerpo y total.

    Parámetros:
        df (pd.DataFrame): El DataFrame a dividir.

    Retorna:
        tuple: (cabecera, cuerpo, total) como DataFrames separados.
    """
    if df.empty or len(df) < 2:
        raise ValueError("El DataFrame debe tener al menos dos filas para dividirse correctamente.")

    cabecera = df.iloc[:1]  # Primera fila
    cuerpo = df.iloc[1:-1]  # Todas las filas intermedias
    total = df.iloc[-1:]  # Última fila

    return cabecera, cuerpo, total



def dataTable(data_dict, common_column , show_columns , order_columns , order_rows ,  operations_columns , column_types , rename_columns , show_total_row , hide_zero_totals):
    """Expande columnas y luego une los DataFrames en base a una columna común."""
    expanded_dict = expand_columns(data_dict)
    joined_df = join_dataframes(expanded_dict , common_column ,  )
    cleaned_df = replace_nan_with_zero(joined_df)
    filtered_df = show_columns_df(cleaned_df, show_columns, order_columns , )
    reordered_df = reorder_rows(filtered_df , order_rows)
    # hay qye hacer que se garanticen todas las filas del dataframe para el caso de que se muestren los desempeño, tienen que estar todos
    # pedirle a chat que columna_valor acepte una lista de columnas a las cuales se les colocará el cero si no hay alguna de los niveles_necesarios
    # niveles_necesarios = ['Avanzado', 'Medio', 'Básico', 'Crítico']
    # df_completo = completar_niveles(df_original, columna_categoria='Desempeño', columna_valor='Cantidad', valores_esperados=niveles_necesarios)
    # completed_df = completar_rows(reordered_df , columna_categoria , )
    
    totalized_df = apply_operations(reordered_df , operations_columns)
    renamed_df = rename_columns_in_dataframe(totalized_df, rename_columns, )
    typed_df = enforce_column_types(renamed_df, column_types)
    no_NaN_df = drop_rows_with_nan(typed_df)
    show_total_df = show_total_row_df(no_NaN_df , show_total_row)
    no_zero_total = hide_zero_total_columns(show_total_df , hide_zero_totals )       

    # cabecera, cuerpo, total = dividir_dataframe(no_zero_total)

    
    # renamed_df = rename_columns_in_dataframe(reordered_df, rename_columns, )

    # typed_df = enforce_column_types(renamed_df, column_types)

    # totalized_df = apply_operations(typed_df , operations_columns)

    # no_NaN_df = drop_rows_with_nan(totalized_df)

    # show_total_df = show_total_row_df(no_NaN_df , show_total_row)
    
    # no_zero_total = hide_zero_total_columns(show_total_df , hide_zero_totals )       

    cabecera, cuerpo, total = dividir_dataframe(no_zero_total)

    return no_zero_total , cabecera, cuerpo, total



# Llamar a la función de prueba si el script se ejecuta directamente
if __name__ == '__main__':

    data_dict_1 = {
        'DESEMPEÑOS'            :   [
                                        pd.DataFrame({'DESEMPEÑO' : ['Avanzado' , 'Medio' , 'Básico' , 'Crítico']    , 'Matrícula'   : [ 0 ,  0 ,  0 , 0]})  , # dataframe
                                        {'Matrícula' :  ['Matrícula_DESEMPEÑOS_Suma' , 'Matrícula_DESEMPEÑOS_Promedio']
                                        },                                        
                                    ]
        ,
        'primera_medición_2024' :   [
                                        pd.DataFrame({'DESEMPEÑO' : ['Avanzado' , 'Medio' , 'Básico' , 'Crítico']    , 'Matrícula'   : [ 10 ,  20 ,  30 , 40]})  , # dataframe
                                        {'Matrícula' :  ['Matrícula_primera_medición_2024_Suma' , 'Matrícula_primera_medición_2024_Promedio']
                                        },                                        
                                    ]
        ,
        'primera_medición_2025' :   [
                                        pd.DataFrame({'DESEMPEÑO' : ['Avanzado' , 'Medio' , 'Básico' , 'Crítico']    , 'Matrícula'   : [ 50 ,  60 ,  70 , 80]})  , # dataframe
                                        {'Matrícula' :  ['Matrícula_primera_medición_2025_Suma' , 'Matrícula_primera_medición_2025_Promedio']
                                        },                                        
                                    ]
        ,        
    }

    

    tabla_final_data_dict_1 , cabecera, cuerpo, total = dataTable(
        data_dict_1, 
        common_column = 'DESEMPEÑO',
        show_columns = ['DESEMPEÑO' , 'Matrícula_primera_medición_2024_Suma' , 'Matrícula_primera_medición_2025_Suma',],
        order_columns= ['DESEMPEÑO' , 'Matrícula_primera_medición_2024_Suma' , 'Matrícula_primera_medición_2025_Suma',] ,
        order_rows = {'DESEMPEÑO' : ['Avanzado' , 'Medio' , 'Básico' , 'Crítico', ]},
        operations_columns = {'DESEMPEÑO' : 'Total' , 'Matrícula_primera_medición_2024_Suma' : 'sumar' , 'Matrícula_primera_medición_2025_Suma' : 'sumar' },
        column_types = {'DESEMPEÑO': str, 'Matrícula_primera_medición_2024_Suma': int, 'Matrícula_primera_medición_2025_Suma': int, },
        rename_columns=[{'DESEMPEÑO':'Niveles de Desempeño' , 'Matrícula_primera_medición_2024_Suma' : 'Primera Medición 2024' , 'Matrícula_primera_medición_2025_Suma' : 'Primera Medición 2025'   }],
        show_total_row = True,
        hide_zero_totals = False
    )

    # Convertir el DataFrame a JSON asegurando los enteros
    json_data = json.dumps(
            tabla_final_data_dict_1.to_dict(orient='records'),
            indent=4,
            ensure_ascii=False
    )

    print('cabecera -- \n' , cabecera )
    print('cuerpo -- \n' , cuerpo )
    print('total -- \n' , total )
    print(json_data)
    print(tabla_final_data_dict_1)
    exit()