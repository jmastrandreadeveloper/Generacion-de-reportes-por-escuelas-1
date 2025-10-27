# tabla genérica es una función que me permite a partir de uno o varios
# dataframe, genera una tabla, uniendo por una columna en común con esos dataframes
# y teniendo en cuenta que cuando falte algún elemento, deberá poner un cero en su lugar,
# que pueda ser ordenada de diferentes formas y que además totalice las cantidades en caso 
# que hayan valores numéricos que puedan ser sumados
# v tomar un diccionario que contenga dataframes

import pandas as pd
import json
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..' ,  ))
sys.path.append(project_root)
import src.tools.print_dataframe as printDFrame



def tabla_generica_v1(data_dict, common_column, order=None):
    """
    Une los DataFrames del diccionario 'data_dict' usando 'common_column' como clave común.
    Permite ordenar los datos de acuerdo con una lista dada en 'order'.

    Parámetros:
        data_dict (dict): Diccionario donde cada clave tiene un DataFrame con 'common_column'.
        common_column (str): Nombre de la columna común para unir los DataFrames.
        order (list, opcional): Lista con el orden deseado de los valores en 'common_column'.

    Retorna:
        pd.DataFrame: DataFrame final con valores combinados, sin NaN, en enteros y con una fila de totales.
    """
    df_final = None

    for key, df in data_dict.items():
        if isinstance(df, pd.DataFrame):
            # Buscar la columna de valores (excluyendo la columna común y posibles identificadores)
            value_cols = [col for col in df.columns if col not in [common_column, 'Escuela_ID']]
            if value_cols:
                df = df.rename(columns={value_cols[0]: key})  # Renombrar la primera columna de datos

            # Eliminar 'Escuela_ID' para evitar duplicaciones
            df = df.drop(columns=['Escuela_ID'], errors='ignore')

            # Unir los DataFrames sucesivamente
            if df_final is None:
                df_final = df
            else:
                df_final = pd.merge(df_final, df, on=common_column, how='outer')

    # Reemplazar NaN con 0 y convertir todas las columnas numéricas a enteros
    df_final = df_final.fillna(0).astype({col: int for col in df_final.columns if col != common_column})

    # Aplicar orden si se proporciona
    if order:
        df_final = df_final.set_index(common_column).reindex(order).reset_index()

    # Agregar fila con los totales
    total_row = df_final.drop(columns=[common_column]).sum(numeric_only=True)
    total_row[common_column] = 'TOTAL'
    df_final = pd.concat([df_final, pd.DataFrame([total_row])], ignore_index=True)

    return df_final

import pandas as pd

def tabla_generica_v2(data_dict, common_column, order=None):
    """
    Une los DataFrames del diccionario 'data_dict' usando 'common_column' como clave común.
    Si alguna clave en 'data_dict' no tiene datos, se asegura de incluirla con valores en cero.
    Se reemplazan NaN con 0 y se convierten los valores numéricos a enteros.

    Parámetros:
        data_dict (dict): Diccionario donde cada clave tiene un DataFrame con 'common_column'.
        common_column (str): Nombre de la columna común para unir los DataFrames.
        order (list, opcional): Lista con el orden deseado de los valores en 'common_column'.

    Retorna:
        pd.DataFrame: DataFrame final con valores combinados, sin NaN, en enteros y con una fila de totales.
    """
    df_final = None
    valores_existentes = set()  # Almacena los valores de la columna común para asegurar consistencia

    for key, df in data_dict.items():
        if isinstance(df, pd.DataFrame) and not df.empty:
            value_cols = [col for col in df.columns if col not in [common_column, 'Escuela_ID']]

            if value_cols:
                df = df.rename(columns={value_cols[0]: key})

            df = df.drop(columns=['Escuela_ID'], errors='ignore')

            valores_existentes.update(df[common_column].unique())  # Almacenar valores únicos de common_column
        else:
            # Si el DataFrame está vacío, crear uno con 'common_column' y la clave con 0
            df = pd.DataFrame({common_column: ['TOTAL'], key: [0]})

        df_final = df if df_final is None else pd.merge(df_final, df, on=common_column, how='outer').fillna(0)

    # Si df_final sigue siendo None, devolver un DataFrame vacío con la columna común
    if df_final is None or df_final.empty:
        print("Advertencia: No se encontraron datos válidos en 'data_dict'. Se devuelve un DataFrame vacío.")
        return pd.DataFrame(columns=[common_column])

    # Asegurar que todas las claves en data_dict aparecen en cada fila
    for key in data_dict.keys():
        if key not in df_final.columns:
            df_final[key] = 0  # Agregar columna faltante con ceros

    # Aplicar orden si se proporciona
    if order:
        df_final = df_final.set_index(common_column).reindex(order).reset_index()
    else:
        # Mantener el orden de aparición de los valores en common_column
        df_final = df_final.set_index(common_column).reindex(sorted(valores_existentes)).reset_index()

    # ===================== 🔹 BLOQUE DESTACADO: Convertir a enteros y eliminar NaN 🔹 =====================
    numeric_cols = [col for col in df_final.columns if col != common_column]  # Columnas numéricas
    
    # Reemplazar NaN con 0 en todas las columnas numéricas
    df_final[numeric_cols] = df_final[numeric_cols].fillna(0)
    
    # Convertir todas las columnas numéricas a enteros
    df_final[numeric_cols] = df_final[numeric_cols].astype(int)
    # =====================================================================================================

    # Agregar fila con los totales si hay columnas numéricas
    if numeric_cols:
        total_row = df_final[numeric_cols].sum(numeric_only=True).astype(int)  # Convertir total a int
        total_row[common_column] = 'TOTAL'
        df_final = pd.concat([df_final, pd.DataFrame([total_row])], ignore_index=True)

    return df_final

import pandas as pd

def tabla_generica_v3(data_dict, common_column, exclude_columns=None, order=None):
    """
    Une los DataFrames del diccionario 'data_dict' usando 'common_column' como clave común.
    - Se eliminan las columnas especificadas en 'exclude_columns' para evitar duplicados.
    - Se reemplazan NaN con 0 y se convierten los valores numéricos a enteros.

    Parámetros:
        data_dict (dict): Diccionario donde cada clave tiene un DataFrame con 'common_column'.
        common_column (str): Nombre de la columna común para unir los DataFrames.
        exclude_columns (list, opcional): Lista de columnas que deben excluirse (ej. IDs).
        order (list, opcional): Lista con el orden deseado de los valores en 'common_column'.

    Retorna:
        pd.DataFrame: DataFrame final con valores combinados, sin NaN, en enteros y con una fila de totales.
    """
    df_final = None
    valores_existentes = set()  # Almacena valores únicos de la columna común

    exclude_columns = set(exclude_columns or [])  # Convertir en conjunto para búsqueda rápida

    for key, df in data_dict.items():
        if isinstance(df, pd.DataFrame) and not df.empty:
            value_cols = [col for col in df.columns if col not in exclude_columns and col != common_column]

            if value_cols:
                df = df.rename(columns={value_cols[0]: key})

            # Eliminar columnas especificadas en exclude_columns
            df = df.drop(columns=exclude_columns, errors='ignore')

            valores_existentes.update(df[common_column].unique())  # Guardar valores de common_column
        else:
            # Si el DataFrame está vacío, crear uno con 'common_column' y la clave con 0
            df = pd.DataFrame({common_column: ['TOTAL'], key: [0]})

        df_final = df if df_final is None else pd.merge(df_final, df, on=common_column, how='outer').fillna(0)

    # Si df_final sigue siendo None, devolver un DataFrame vacío con la columna común
    if df_final is None or df_final.empty:
        print("Advertencia: No se encontraron datos válidos en 'data_dict'. Se devuelve un DataFrame vacío.")
        return pd.DataFrame(columns=[common_column])

    # Asegurar que todas las claves en data_dict aparecen en cada fila
    for key in data_dict.keys():
        if key not in df_final.columns:
            df_final[key] = 0  # Agregar columna faltante con ceros

    # Aplicar orden si se proporciona
    if order:
        df_final = df_final.set_index(common_column).reindex(order).reset_index()
    else:
        df_final = df_final.set_index(common_column).reindex(sorted(valores_existentes)).reset_index()

    # ===================== 🔹 BLOQUE DESTACADO: Convertir a enteros y eliminar NaN 🔹 =====================
    numeric_cols = [col for col in df_final.columns if col != common_column]  # Columnas numéricas
    
    # Reemplazar NaN con 0 en todas las columnas numéricas
    df_final[numeric_cols] = df_final[numeric_cols].fillna(0)
    
    # Convertir todas las columnas numéricas a enteros
    df_final[numeric_cols] = df_final[numeric_cols].astype(int)
    # =====================================================================================================

    # Agregar fila con los totales si hay columnas numéricas
    if numeric_cols:
        total_row = df_final[numeric_cols].sum(numeric_only=True).astype(int)  # Convertir total a int
        total_row[common_column] = 'TOTAL'
        df_final = pd.concat([df_final, pd.DataFrame([total_row])], ignore_index=True)

    return df_final

import numpy as np

def tabla_generica_v4(data_dict, common_column, exclude_columns=None, order=None):
    """
    Une los DataFrames del diccionario 'data_dict' usando 'common_column' como clave común.
    - Permite especificar una operación de agregación para cada conjunto de datos (suma, promedio, etc.).
    - Se eliminan las columnas especificadas en 'exclude_columns' para evitar duplicados.
    - Se reemplazan NaN con 0 y se convierten los valores numéricos a enteros.

    Parámetros:
        data_dict (dict): Diccionario donde cada clave es el nombre de la columna final y el valor es una tupla (DataFrame, operación).
        common_column (str): Nombre de la columna común para unir los DataFrames.
        exclude_columns (list, opcional): Lista de columnas que deben excluirse (ej. IDs).
        order (list, opcional): Lista con el orden deseado de los valores en 'common_column'.

    Retorna:
        pd.DataFrame: DataFrame final con valores combinados, sin NaN, en enteros y con una fila de totales.
    """
    df_final = None
    valores_existentes = set()

    exclude_columns = set(exclude_columns or [])  # Convertir en conjunto para búsqueda rápida

    operaciones_validas = {
        'sumar': np.sum,
        'promedio': np.mean,
        'minimo': np.min,
        'maximo': np.max,
        'mediana': np.median,
        'desviacion': np.std
    }

    for key, (df, operacion) in data_dict.items():
        if operacion not in operaciones_validas:
            raise ValueError(f"Operación '{operacion}' no válida. Opciones: {list(operaciones_validas.keys())}")

        if isinstance(df, pd.DataFrame) and not df.empty:
            value_cols = [col for col in df.columns if col not in exclude_columns and col != common_column]

            if value_cols:
                df = df.rename(columns={value_cols[0]: key})

            # Eliminar columnas no deseadas
            df = df.drop(columns=exclude_columns, errors='ignore')

            valores_existentes.update(df[common_column].unique())  # Guardar valores de common_column
        else:
            # Si el DataFrame está vacío, crear uno con 'common_column' y la clave con 0
            df = pd.DataFrame({common_column: ['TOTAL'], key: [0]})

        df_final = df if df_final is None else pd.merge(df_final, df, on=common_column, how='outer').fillna(0)

    # Si df_final sigue siendo None, devolver un DataFrame vacío con la columna común
    if df_final is None or df_final.empty:
        print("Advertencia: No se encontraron datos válidos en 'data_dict'. Se devuelve un DataFrame vacío.")
        return pd.DataFrame(columns=[common_column])

    # Asegurar que todas las claves en data_dict aparecen en cada fila
    for key in data_dict.keys():
        if key not in df_final.columns:
            df_final[key] = 0

    # Aplicar orden si se proporciona
    if order:
        df_final = df_final.set_index(common_column).reindex(order).reset_index()
    else:
        df_final = df_final.set_index(common_column).reindex(sorted(valores_existentes)).reset_index()

    # ===================== 🔹 BLOQUE DESTACADO: Convertir a enteros y eliminar NaN 🔹 =====================
    numeric_cols = [col for col in df_final.columns if col != common_column]  # Columnas numéricas
    
    # Reemplazar NaN con 0 en todas las columnas numéricas
    df_final[numeric_cols] = df_final[numeric_cols].fillna(0)
    
    # Convertir todas las columnas numéricas a enteros
    df_final[numeric_cols] = df_final[numeric_cols].astype(int)
    # =====================================================================================================

    # Agregar fila con los resultados de agregación si hay columnas numéricas
    if numeric_cols:
        total_row = {}
        for key, (_, operacion) in data_dict.items():
            if key in df_final.columns:
                if operacion == 'promedio':
                    count_nonzero = (df_final[key] != 0).sum()  # Contar solo los valores diferentes de 0
                    total_row[key] = df_final[key].sum() / count_nonzero if count_nonzero > 0 else 0
                else:
                    total_row[key] = operaciones_validas[operacion](df_final[key])
        
        total_row[common_column] = 'TOTAL'
        df_final = pd.concat([df_final, pd.DataFrame([total_row])], ignore_index=True)

    return df_final

import numpy as np
import pandas as pd

def tabla_generica_v5(data_dict, common_column, exclude_columns=None, order=None):
    """
    Une los DataFrames del diccionario 'data_dict' usando 'common_column' como clave común.
    Permite especificar múltiples operaciones de agregación para cada conjunto de datos.
    Se eliminan las columnas especificadas en 'exclude_columns' para evitar duplicados.
    Se reemplazan NaN con 0 y se convierten los valores numéricos a enteros.

    Parámetros:
        data_dict (dict): Diccionario donde cada clave es el nombre de la columna final y el valor es una tupla (DataFrame, operación).
        common_column (str): Nombre de la columna común para unir los DataFrames.
        exclude_columns (list, opcional): Lista de columnas que deben excluirse (ej. IDs).
        order (list, opcional): Lista con el orden deseado de los valores en 'common_column'.

    Retorna:
        pd.DataFrame: DataFrame final con valores combinados, sin NaN, en enteros y con una fila de totales.
    """
    df_final = None
    valores_existentes = set()

    exclude_columns = set(exclude_columns or [])  # Convertir en conjunto para búsqueda rápida

    operaciones_validas = {
        'sumar': np.sum,
        'promedio': np.mean,
        'minimo': np.min,
        'maximo': np.max,
        'mediana': np.median,
        'desviacion': np.std,
        'varianza': np.var,
        'moda': lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan,
        'coef_var': lambda x: np.std(x) / np.mean(x) if np.mean(x) != 0 else np.nan,
        'iqr': lambda x: np.percentile(x, 75) - np.percentile(x, 25),
        'percentil_25': lambda x: np.percentile(x, 25),
        'percentil_75': lambda x: np.percentile(x, 75),
        'conteo': len,
        'frecuencia_relativa': lambda x: x.value_counts(normalize=True).to_dict(),
        'crecimiento_porcentual': lambda x: x.pct_change().mean(),
        'tendencia_movil': lambda x: x.rolling(window=2).mean().iloc[-1] if len(x) > 1 else np.nan
    }

    for key, (df, operacion) in data_dict.items():
        if operacion not in operaciones_validas:
            raise ValueError(f"Operación '{operacion}' no válida. Opciones: {list(operaciones_validas.keys())}")

        if isinstance(df, pd.DataFrame) and not df.empty:
            value_cols = [col for col in df.columns if col not in exclude_columns and col != common_column]

            if value_cols:
                df = df.rename(columns={value_cols[0]: key})

            # Eliminar columnas no deseadas
            df = df.drop(columns=exclude_columns, errors='ignore')

            valores_existentes.update(df[common_column].unique())  # Guardar valores de common_column
        else:
            # Si el DataFrame está vacío, crear uno con 'common_column' y la clave con 0
            df = pd.DataFrame({common_column: ['TOTAL'], key: [0]})

        df_final = df if df_final is None else pd.merge(df_final, df, on=common_column, how='outer').fillna(0)

    # Si df_final sigue siendo None, devolver un DataFrame vacío con la columna común
    if df_final is None or df_final.empty:
        print("Advertencia: No se encontraron datos válidos en 'data_dict'. Se devuelve un DataFrame vacío.")
        return pd.DataFrame(columns=[common_column])

    # Asegurar que todas las claves en data_dict aparecen en cada fila
    for key in data_dict.keys():
        if key not in df_final.columns:
            df_final[key] = 0

    # Aplicar orden si se proporciona
    if order:
        df_final = df_final.set_index(common_column).reindex(order).reset_index()
    else:
        df_final = df_final.set_index(common_column).reindex(sorted(valores_existentes)).reset_index()

    # ===================== 🔹 BLOQUE DESTACADO: Convertir a enteros y eliminar NaN 🔹 =====================
    numeric_cols = [col for col in df_final.columns if col != common_column]  # Columnas numéricas
    
    # Reemplazar NaN con 0 en todas las columnas numéricas
    df_final[numeric_cols] = df_final[numeric_cols].fillna(0)
    
    # Convertir todas las columnas numéricas a enteros
    df_final[numeric_cols] = df_final[numeric_cols].astype(int)
    # =====================================================================================================

    # Agregar fila con los resultados de agregación si hay columnas numéricas
    if numeric_cols:
        total_row = {}
        for key, (_, operacion) in data_dict.items():
            if key in df_final.columns:
                total_row[key] = operaciones_validas[operacion](df_final[key])
        
        total_row[common_column] = 'TOTAL'
        df_final = pd.concat([df_final, pd.DataFrame([total_row])], ignore_index=True)

    return df_final

import numpy as np
import pandas as pd

def tabla_generica_v6(data_dict, common_column, exclude_columns=None, order=None):
    """
    Combina múltiples DataFrames basados en una columna común y aplica agregaciones definidas.
    - Permite ocultar columnas basadas en condiciones específicas.
    - Elimina columnas no deseadas y gestiona valores NaN.
    - Agrega una fila con totales calculados según la operación especificada.

    Parámetros:
        data_dict (dict): Diccionario con nombre de columna final como clave y una tupla (DataFrame, operación, condiciones) como valor.
        common_column (str): Nombre de la columna clave usada para unir los DataFrames.
        exclude_columns (list, opcional): Columnas a excluir de la fusión para evitar duplicados.
        order (list, opcional): Orden específico para la columna común.

    Retorna:
        pd.DataFrame: DataFrame fusionado con las transformaciones aplicadas.
    """
    df_final = None  # DataFrame resultante
    valores_existentes = set()  # Almacena valores únicos de 'common_column'
    exclude_columns = set(exclude_columns or [])  # Convierte en conjunto para búsqueda rápida

    # Diccionario de operaciones de agregación permitidas
    # operaciones_validas = {
    #     'sumar': np.sum,
    #     'promedio': np.mean,
    #     'minimo': np.min,
    #     'maximo': np.max,
    #     'mediana': np.median,
    #     'desviacion': np.std
    # }
    operaciones_validas = {
        'sumar': np.sum,
        'promedio': np.mean,
        'minimo': np.min,
        'maximo': np.max,
        'mediana': np.median,
        'desviacion': np.std,
        'varianza': np.var,
        'moda': lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan,
        'coef_var': lambda x: np.std(x) / np.mean(x) if np.mean(x) != 0 else np.nan,
        'iqr': lambda x: np.percentile(x, 75) - np.percentile(x, 25),
        'percentil_25': lambda x: np.percentile(x, 25),
        'percentil_75': lambda x: np.percentile(x, 75),
        'conteo': len,
        'frecuencia_relativa': lambda x: x.value_counts(normalize=True).to_dict(),
        'crecimiento_porcentual': lambda x: x.pct_change().mean(),
        'tendencia_movil': lambda x: x.rolling(window=2).mean().iloc[-1] if len(x) > 1 else np.nan
    }

    condiciones_columnas = {}  # Almacena condiciones de ocultación por columna

    # Itera sobre cada entrada en el diccionario de datos
    for key, value in data_dict.items():
        # Manejo de casos con y sin condiciones
        if len(value) == 2:
            df, operacion = value
            condiciones = {}
        else:
            df, operacion, condiciones = value

        # Validar que la operación sea permitida
        if operacion not in operaciones_validas:
            raise ValueError(f"Operación '{operacion}' no válida. Opciones: {list(operaciones_validas.keys())}")

        # Almacenar condiciones asociadas a la columna
        condiciones_columnas[key] = condiciones

        # Verificar si el DataFrame es válido
        if isinstance(df, pd.DataFrame) and not df.empty:
            # Filtrar columnas excluidas y renombrar la primera columna de valores
            value_cols = [col for col in df.columns if col not in exclude_columns and col != common_column]
            
            if value_cols:
                df = df.rename(columns={value_cols[0]: key})

            # Eliminar columnas excluidas
            df = df.drop(columns=exclude_columns, errors='ignore')
            
            # Almacenar valores únicos de la columna común
            valores_existentes.update(df[common_column].unique())
        else:
            # Si el DataFrame está vacío, agregar fila con total 0
            df = pd.DataFrame({common_column: ['TOTAL'], key: [0]})

        # Fusionar DataFrames usando la columna común
        df_final = df if df_final is None else pd.merge(df_final, df, on=common_column, how='outer').fillna(0)

    # Si no hay datos válidos, retornar un DataFrame vacío
    if df_final is None or df_final.empty:
        print("Advertencia: No se encontraron datos válidos en 'data_dict'. Se devuelve un DataFrame vacío.")
        return pd.DataFrame(columns=[common_column])

    # Asegurar que todas las claves del diccionario existan en el DataFrame final
    for key in data_dict.keys():
        if key not in df_final.columns:
            df_final[key] = 0

    # Ordenar DataFrame si se especifica un orden
    if order:
        df_final = df_final.set_index(common_column).reindex(order).reset_index()
    else:
        df_final = df_final.set_index(common_column).reindex(sorted(valores_existentes)).reset_index()

    # Convertir columnas numéricas y reemplazar NaN con 0
    numeric_cols = [col for col in df_final.columns if col != common_column]
    df_final[numeric_cols] = df_final[numeric_cols].fillna(0).astype(int)

    # Agregar fila de totales si hay columnas numéricas
    if numeric_cols:
        total_row = {}
        for key, (_, operacion, *_) in data_dict.items():
            if key in df_final.columns:
                total_row[key] = operaciones_validas[operacion](df_final[key])
        total_row[common_column] = 'TOTAL'
        df_final = pd.concat([df_final, pd.DataFrame([total_row])], ignore_index=True)

    # Aplicar condiciones para ocultar columnas
    columnas_a_eliminar = []
    for col, condiciones in condiciones_columnas.items():
        if 'ocultar_si' in condiciones:
            condicion = condiciones['ocultar_si']
            valor_umbral = condiciones.get('valor', 0)
            
            if condicion == 'es_cero' and (df_final[col] == 0).all():
                columnas_a_eliminar.append(col)
            elif condicion == 'mayor_a' and (df_final[col] > valor_umbral).all():
                columnas_a_eliminar.append(col)
            elif condicion == 'menor_a' and (df_final[col] < valor_umbral).all():
                columnas_a_eliminar.append(col)

    # Eliminar columnas que cumplen las condiciones
    df_final = df_final.drop(columns=columnas_a_eliminar, errors='ignore')
    
    return df_final

def tabla_generica_v7(data_dict, common_column, exclude_columns=None, order=None):
    """
    Combina múltiples DataFrames basados en una columna común y aplica agregaciones definidas.
    - Permite ocultar columnas basadas en condiciones específicas.
    - Elimina columnas no deseadas y gestiona valores NaN.
    - Agrega una fila con totales calculados según la operación especificada.

    Parámetros:
        data_dict (dict): Diccionario con nombre de columna final como clave y una tupla 
                          (DataFrame, operación, condiciones, nombre_columna) como valor.
        common_column (str): Nombre de la columna clave usada para unir los DataFrames.
        exclude_columns (list, opcional): Columnas a excluir de la fusión para evitar duplicados.
        order (list, opcional): Orden específico para la columna común.

    Retorna:
        pd.DataFrame: DataFrame fusionado con las transformaciones aplicadas.
    """
    df_final = None  # DataFrame resultante
    valores_existentes = set()  # Almacena valores únicos de 'common_column'
    exclude_columns = set(exclude_columns or [])  # Convierte en conjunto para búsqueda rápida

    # Diccionario de operaciones de agregación permitidas
    operaciones_validas = {
        'sumar': np.sum,
        'promedio': np.mean,
        'minimo': np.min,
        'maximo': np.max,
        'mediana': np.median,
        'desviacion': np.std,
        'varianza': np.var,
        'moda': lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan,
        'coef_var': lambda x: np.std(x) / np.mean(x) if np.mean(x) != 0 else np.nan,
        'iqr': lambda x: np.percentile(x, 75) - np.percentile(x, 25),
        'percentil_25': lambda x: np.percentile(x, 25),
        'percentil_75': lambda x: np.percentile(x, 75),
        'conteo': len,
        'frecuencia_relativa': lambda x: x.value_counts(normalize=True).to_dict(),
        'crecimiento_porcentual': lambda x: x.pct_change().mean(),
        'tendencia_movil': lambda x: x.rolling(window=2).mean().iloc[-1] if len(x) > 1 else np.nan
    }

    condiciones_columnas = {}  # Almacena condiciones de ocultación por columna

    # Itera sobre cada entrada en el diccionario de datos
    for key, value in data_dict.items():
        # Manejo de casos con y sin condiciones y nombre de columna
        if len(value) == 2:
            df, operacion = value
            condiciones = {}
            nombre_columna = key
        elif len(value) == 3:
            df, operacion, condiciones = value
            nombre_columna = key
        else:
            df, operacion, condiciones, nombre_columna = value

        # Validar que la operación sea permitida
        if operacion not in operaciones_validas:
            raise ValueError(f"Operación '{operacion}' no válida. Opciones: {list(operaciones_validas.keys())}")

        # Almacenar condiciones asociadas a la columna
        condiciones_columnas[key] = condiciones

        # Verificar si el DataFrame es válido
        if isinstance(df, pd.DataFrame) and not df.empty:
            # Filtrar columnas excluidas y renombrar la primera columna de valores
            value_cols = [col for col in df.columns if col not in exclude_columns and col != common_column]

            if value_cols:
                df = df.rename(columns={value_cols[0]: nombre_columna})

            # Eliminar columnas excluidas
            df = df.drop(columns=exclude_columns, errors='ignore')

            # Almacenar valores únicos de la columna común
            valores_existentes.update(df[common_column].unique())
        else:
            # Si el DataFrame está vacío, agregar fila con total 0
            df = pd.DataFrame({common_column: ['TOTAL'], nombre_columna: [0]})

        # Fusionar DataFrames usando la columna común
        df_final = df if df_final is None else pd.merge(df_final, df, on=common_column, how='outer').fillna(0)

    # Si no hay datos válidos, retornar un DataFrame vacío
    if df_final is None or df_final.empty:
        print("Advertencia: No se encontraron datos válidos en 'data_dict'. Se devuelve un DataFrame vacío.")
        return pd.DataFrame(columns=[common_column])

    # Asegurar que todas las claves del diccionario existan en el DataFrame final
    for key, value in data_dict.items():
        nombre_columna = value[3] if len(value) > 3 else key
        if nombre_columna not in df_final.columns:
            df_final[nombre_columna] = 0

    # Ordenar DataFrame si se especifica un orden
    if order:
        df_final = df_final.set_index(common_column).reindex(order).reset_index()
    else:
        df_final = df_final.set_index(common_column).reindex(sorted(valores_existentes)).reset_index()

    # Convertir columnas numéricas y reemplazar NaN con 0
    numeric_cols = [col for col in df_final.columns if col != common_column]
    df_final[numeric_cols] = df_final[numeric_cols].fillna(0).astype(int)

    # Agregar fila de totales si hay columnas numéricas
    if numeric_cols:
        total_row = {}
        for key, (_, operacion, *_) in data_dict.items():
            nombre_columna = data_dict[key][3] if len(data_dict[key]) > 3 else key
            if nombre_columna in df_final.columns:
                total_row[nombre_columna] = operaciones_validas[operacion](df_final[nombre_columna])
        total_row[common_column] = 'TOTAL'
        df_final = pd.concat([df_final, pd.DataFrame([total_row])], ignore_index=True)

    # Aplicar condiciones para ocultar columnas
    columnas_a_eliminar = []
    for col, condiciones in condiciones_columnas.items():
        if 'ocultar_si' in condiciones:
            condicion = condiciones['ocultar_si']
            valor_umbral = condiciones.get('valor', 0)

            if condicion == 'es_cero' and (df_final[col] == 0).all():
                columnas_a_eliminar.append(col)
            elif condicion == 'mayor_a' and (df_final[col] > valor_umbral).all():
                columnas_a_eliminar.append(col)
            elif condicion == 'menor_a' and (df_final[col] < valor_umbral).all():
                columnas_a_eliminar.append(col)

    # Eliminar columnas que cumplen las condiciones
    df_final = df_final.drop(columns=columnas_a_eliminar, errors='ignore')

    return df_final

def tabla_generica_v8(data_dict, common_column, exclude_columns=None, order=None, rename_columns=None):
    df_final = None  # DataFrame resultante
    valores_existentes = set()  # Almacena valores únicos de 'common_column'
    exclude_columns = set(exclude_columns or [])  # Convierte en conjunto para búsqueda rápida
    rename_columns = rename_columns or []
    
    operaciones_validas = {
        'sumar': np.sum,
        'promedio': np.mean,
        'minimo': np.min,
        'maximo': np.max,
        'mediana': np.median,
        'desviacion': np.std,
        'varianza': np.var,
        'moda': lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan,
        'coef_var': lambda x: np.std(x) / np.mean(x) if np.mean(x) != 0 else np.nan,
        'iqr': lambda x: np.percentile(x, 75) - np.percentile(x, 25),
        'percentil_25': lambda x: np.percentile(x, 25),
        'percentil_75': lambda x: np.percentile(x, 75),
        'conteo': len,
        'frecuencia_relativa': lambda x: x.value_counts(normalize=True).to_dict(),
        'crecimiento_porcentual': lambda x: x.pct_change().mean(),
        'tendencia_movil': lambda x: x.rolling(window=2).mean().iloc[-1] if len(x) > 1 else np.nan
    }
    
    condiciones_columnas = {}  # Almacena condiciones de ocultación por columna
    
    for key, value in data_dict.items():
        if len(value) == 2:
            df, operacion = value
            condiciones = {}
            nombre_columna = key
        elif len(value) == 3:
            df, operacion, condiciones = value
            nombre_columna = key
        else:
            df, operacion, condiciones, nombre_columna = value

        if operacion not in operaciones_validas:
            raise ValueError(f"Operación '{operacion}' no válida. Opciones: {list(operaciones_validas.keys())}")

        condiciones_columnas[key] = condiciones

        if isinstance(df, pd.DataFrame) and not df.empty:
            value_cols = [col for col in df.columns if col not in exclude_columns and col != common_column]
            if value_cols:
                df = df.rename(columns={value_cols[0]: nombre_columna})
            df = df.drop(columns=exclude_columns, errors='ignore')
            valores_existentes.update(df[common_column].unique())
        else:
            df = pd.DataFrame({common_column: ['TOTAL'], nombre_columna: [0]})

        df_final = df if df_final is None else pd.merge(df_final, df, on=common_column, how='outer').fillna(0)

    if df_final is None or df_final.empty:
        print("Advertencia: No se encontraron datos válidos en 'data_dict'. Se devuelve un DataFrame vacío.")
        return pd.DataFrame(columns=[common_column])

    for key, value in data_dict.items():
        nombre_columna = value[3] if len(value) > 3 else key
        if nombre_columna not in df_final.columns:
            df_final[nombre_columna] = 0

    if order:
        df_final = df_final.set_index(common_column).reindex(order).reset_index()
    else:
        df_final = df_final.set_index(common_column).reindex(sorted(valores_existentes)).reset_index()

    numeric_cols = [col for col in df_final.columns if col != common_column]
    df_final[numeric_cols] = df_final[numeric_cols].fillna(0).astype(int)

    if numeric_cols:
        total_row = {common_column: 'TOTAL'}
        for key, (_, operacion, *_) in data_dict.items():
            nombre_columna = data_dict[key][3] if len(data_dict[key]) > 3 else key
            if nombre_columna in df_final.columns:
                total_row[nombre_columna] = operaciones_validas[operacion](df_final[nombre_columna])
        df_final = pd.concat([df_final, pd.DataFrame([total_row])], ignore_index=True)

    columnas_a_eliminar = []
    for col, condiciones in condiciones_columnas.items():
        if 'ocultar_si' in condiciones:
            condicion = condiciones['ocultar_si']
            valor_umbral = condiciones.get('valor', 0)
            if condicion == 'es_cero' and (df_final[col] == 0).all():
                columnas_a_eliminar.append(col)
            elif condicion == 'mayor_a' and (df_final[col] > valor_umbral).all():
                columnas_a_eliminar.append(col)
            elif condicion == 'menor_a' and (df_final[col] < valor_umbral).all():
                columnas_a_eliminar.append(col)

    df_final = df_final.drop(columns=columnas_a_eliminar, errors='ignore')
    
    rename_dict = {list(rename.keys())[0]: list(rename.values())[0] for rename in rename_columns}
    df_final = df_final.rename(columns=rename_dict)
    
    return df_final

def tabla_generica_v9(data_dict, common_column, exclude_columns=None, include_columns=None, order=None, rename_columns=None):
    df_final = None  # DataFrame resultante
    valores_existentes = set()  # Almacena valores únicos de 'common_column'
    exclude_columns = set(exclude_columns or [])  # Convierte en conjunto para búsqueda rápida
    include_columns = set(include_columns or [])  # Columnas que solo deben mostrarse
    rename_columns = rename_columns or []
    
    operaciones_validas = {
        'sumar': np.sum,
        'promedio': np.mean,
        'minimo': np.min,
        'maximo': np.max,
        'mediana': np.median,
        'desviacion': np.std,
        'varianza': np.var,
        'moda': lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan,
        'coef_var': lambda x: np.std(x) / np.mean(x) if np.mean(x) != 0 else np.nan,
        'iqr': lambda x: np.percentile(x, 75) - np.percentile(x, 25),
        'percentil_25': lambda x: np.percentile(x, 25),
        'percentil_75': lambda x: np.percentile(x, 75),
        'conteo': len,
        'frecuencia_relativa': lambda x: x.value_counts(normalize=True).to_dict(),
        'crecimiento_porcentual': lambda x: x.pct_change().mean(),
        'tendencia_movil': lambda x: x.rolling(window=2).mean().iloc[-1] if len(x) > 1 else np.nan
    }
    
    condiciones_columnas = {}  # Almacena condiciones de ocultación por columna
    
    for key, value in data_dict.items():
        if len(value) == 2:
            df, operacion = value
            condiciones = {}
            nombre_columna = key
        elif len(value) == 3:
            df, operacion, condiciones = value
            nombre_columna = key
        else:
            df, operacion, condiciones, nombre_columna = value

        if operacion not in operaciones_validas and nombre_columna not in include_columns:
            raise ValueError(f"Operación '{operacion}' no válida. Opciones: {list(operaciones_validas.keys())}")

        condiciones_columnas[key] = condiciones

        if isinstance(df, pd.DataFrame) and not df.empty:
            value_cols = [col for col in df.columns if col not in exclude_columns and col != common_column]
            if value_cols:
                df = df.rename(columns={value_cols[0]: nombre_columna})
            df = df.drop(columns=exclude_columns, errors='ignore')
            valores_existentes.update(df[common_column].unique())
        else:
            df = pd.DataFrame({common_column: ['TOTAL'], nombre_columna: [0]})

        df_final = df if df_final is None else pd.merge(df_final, df, on=common_column, how='outer').fillna(0)

    if df_final is None or df_final.empty:
        print("Advertencia: No se encontraron datos válidos en 'data_dict'. Se devuelve un DataFrame vacío.")
        return pd.DataFrame(columns=[common_column])

    for key, value in data_dict.items():
        nombre_columna = value[3] if len(value) > 3 else key
        if nombre_columna not in df_final.columns:
            df_final[nombre_columna] = 0

    if order:
        df_final = df_final.set_index(common_column).reindex(order).reset_index()
    else:
        df_final = df_final.set_index(common_column).reindex(sorted(valores_existentes)).reset_index()

    numeric_cols = [col for col in df_final.columns if col != common_column and col not in include_columns]
    df_final[numeric_cols] = df_final[numeric_cols].fillna(0).astype(int)

    if numeric_cols:
        total_row = {common_column: 'TOTAL'}
        for key, (_, operacion, *_) in data_dict.items():
            nombre_columna = data_dict[key][3] if len(data_dict[key]) > 3 else key
            if nombre_columna in df_final.columns and nombre_columna not in include_columns:
                total_row[nombre_columna] = operaciones_validas[operacion](df_final[nombre_columna])
        df_final = pd.concat([df_final, pd.DataFrame([total_row])], ignore_index=True)

    columnas_a_eliminar = []
    for col, condiciones in condiciones_columnas.items():
        if 'ocultar_si' in condiciones:
            condicion = condiciones['ocultar_si']
            valor_umbral = condiciones.get('valor', 0)
            if condicion == 'es_cero' and (df_final[col] == 0).all():
                columnas_a_eliminar.append(col)
            elif condicion == 'mayor_a' and (df_final[col] > valor_umbral).all():
                columnas_a_eliminar.append(col)
            elif condicion == 'menor_a' and (df_final[col] < valor_umbral).all():
                columnas_a_eliminar.append(col)

    df_final = df_final.drop(columns=columnas_a_eliminar, errors='ignore')
    
    rename_dict = {list(rename.keys())[0]: list(rename.values())[0] for rename in rename_columns}
    df_final = df_final.rename(columns=rename_dict)
    
    return df_final


import pandas as pd
import numpy as np

def tabla_generica_v10__(data_dict, common_column, exclude_columns=None, include_columns=None, order=None, rename_columns=None):
    # Inicialización de variables
    df_final = None  # DataFrame resultante
    valores_existentes = set()  # Almacena valores únicos de 'common_column'
    exclude_columns = set(exclude_columns or [])  # Convierte en conjunto para búsqueda rápida
    include_columns = set(include_columns or [])  # Columnas que solo deben mostrarse
    rename_columns = rename_columns or []

    # Definición de operaciones válidas
    operaciones_validas = {
        'sumar': np.sum,
        'promedio': np.mean,
        'minimo': np.min,
        'maximo': np.max,
        'mediana': np.median,
        'desviacion': np.std,
        'varianza': np.var,
        'moda': lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan,
        'coef_var': lambda x: np.std(x) / np.mean(x) if np.mean(x) != 0 else np.nan,
        'iqr': lambda x: np.percentile(x, 75) - np.percentile(x, 25),
        'percentil_25': lambda x: np.percentile(x, 25),
        'percentil_75': lambda x: np.percentile(x, 75),
        'conteo': len,
        'frecuencia_relativa': lambda x: x.value_counts(normalize=True).to_dict(),
        'crecimiento_porcentual': lambda x: x.pct_change().mean(),
        'tendencia_movil': lambda x: x.rolling(window=2).mean().iloc[-1] if len(x) > 1 else np.nan
    }

    condiciones_columnas = {}  # Almacena condiciones de ocultación por columna

    # Función interna para procesar cada DataFrame
    def procesar_df(df, operacion, nombre_columna):
        if isinstance(df, pd.DataFrame) and not df.empty:
            value_cols = [col for col in df.columns if col not in exclude_columns and col != common_column]
            if value_cols:
                df = df.rename(columns={value_cols[0]: nombre_columna})
            df = df.drop(columns=exclude_columns, errors='ignore')
            valores_existentes.update(df[common_column].unique())
        else:
            df = pd.DataFrame({common_column: ['TOTAL'], nombre_columna: [0]})
        return df

    # Procesar los DataFrames del data_dict
    for key, value in data_dict.items():
        if len(value) == 2:
            df, operacion = value
            condiciones = {}
            nombre_columna = key
        elif len(value) == 3:
            df, operacion, condiciones = value
            nombre_columna = key
        else:
            df, operacion, condiciones, nombre_columna = value
        
        # Validar operación
        if operacion not in operaciones_validas and nombre_columna not in include_columns:
            raise ValueError(f"Operación '{operacion}' no válida. Opciones: {list(operaciones_validas.keys())}")
        
        condiciones_columnas[key] = condiciones

        df = procesar_df(df, operacion, nombre_columna)

        df_final = df if df_final is None else pd.merge(df_final, df, on=common_column, how='outer').fillna(0)

    # Si no se encontraron datos válidos, retornar un DataFrame vacío
    if df_final is None or df_final.empty:
        print("Advertencia: No se encontraron datos válidos en 'data_dict'. Se devuelve un DataFrame vacío.")
        return pd.DataFrame(columns=[common_column])

    # Eliminar las columnas duplicadas que puedan haber quedado después de la fusión
    df_final = df_final.loc[:, ~df_final.columns.duplicated()]

    # Ordenar los datos por el valor de 'common_column' si se proporciona 'order'
    if order:
        df_final = df_final.set_index(common_column).reindex(order).reset_index()
    else:
        df_final = df_final.set_index(common_column).reindex(sorted(valores_existentes)).reset_index()

    # Rellenar las columnas numéricas con valores por defecto
    numeric_cols = [col for col in df_final.columns if col != common_column and col not in include_columns]
    df_final[numeric_cols] = df_final[numeric_cols].fillna(0).astype(int)

    # Agregar una fila con los totales calculados por operación
    total_row = {common_column: 'TOTAL'}
    for key, (_, operacion, *_) in data_dict.items():
        nombre_columna = data_dict[key][3] if len(data_dict[key]) > 3 else key
        if nombre_columna in df_final.columns and nombre_columna not in include_columns:
            total_row[nombre_columna] = operaciones_validas[operacion](df_final[nombre_columna])
    df_final = pd.concat([df_final, pd.DataFrame([total_row])], ignore_index=True)

    # Eliminar columnas según condiciones de ocultación
    columnas_a_eliminar = []
    for col, condiciones in condiciones_columnas.items():
        if 'ocultar_si' in condiciones:
            condicion = condiciones['ocultar_si']
            valor_umbral = condiciones.get('valor', 0)
            if condicion == 'es_cero' and (df_final[col] == 0).all():
                columnas_a_eliminar.append(col)
            elif condicion == 'mayor_a' and (df_final[col] > valor_umbral).all():
                columnas_a_eliminar.append(col)
            elif condicion == 'menor_a' and (df_final[col] < valor_umbral).all():
                columnas_a_eliminar.append(col)

    df_final = df_final.drop(columns=columnas_a_eliminar, errors='ignore')

    # Renombrar las columnas si se proporcionan nuevos nombres
    if rename_columns:
        rename_dict = {list(rename.keys())[0]: list(rename.values())[0] for rename in rename_columns}
        df_final = df_final.rename(columns=rename_dict)

    return df_final

import pandas as pd
import numpy as np

def tabla_generica_v10(data_dict, common_column, exclude_columns=None, include_columns=None, order=None, rename_columns=None):
    # Inicialización de variables
    df_final = None  # DataFrame resultante
    valores_existentes = set()  # Almacena valores únicos de 'common_column'
    exclude_columns = set(exclude_columns or [])  # Convierte en conjunto para búsqueda rápida
    include_columns = set(include_columns or [])  # Columnas que solo deben mostrarse
    rename_columns = rename_columns or []

    # Definición de operaciones válidas
    operaciones_validas = {
        'sumar': np.sum,
        'promedio': np.mean,
        'minimo': np.min,
        'maximo': np.max,
        'mediana': np.median,
        'desviacion': np.std,
        'varianza': np.var,
        'moda': lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan,
        'coef_var': lambda x: np.std(x) / np.mean(x) if np.mean(x) != 0 else np.nan,
        'iqr': lambda x: np.percentile(x, 75) - np.percentile(x, 25),
        'percentil_25': lambda x: np.percentile(x, 25),
        'percentil_75': lambda x: np.percentile(x, 75),
        'conteo': len,
        'frecuencia_relativa': lambda x: x.value_counts(normalize=True).to_dict(),
        'crecimiento_porcentual': lambda x: x.pct_change().mean(),
        'tendencia_movil': lambda x: x.rolling(window=2).mean().iloc[-1] if len(x) > 1 else np.nan
    }

    condiciones_columnas = {}  # Almacena condiciones de ocultación por columna

    # Función interna para procesar cada DataFrame
    def procesar_df(df, operacion, nombre_columna):
        if isinstance(df, pd.DataFrame) and not df.empty:
            value_cols = [col for col in df.columns if col not in exclude_columns and col != common_column]
            if value_cols:
                df = df.rename(columns={value_cols[0]: nombre_columna})
            df = df.drop(columns=exclude_columns, errors='ignore')
            valores_existentes.update(df[common_column].unique())
        else:
            df = pd.DataFrame({common_column: ['TOTAL'], nombre_columna: [0]})
        return df

    # Procesar los DataFrames del data_dict
    for key, value in data_dict.items():
        if len(value) == 2:
            df, operacion = value
            condiciones = {}
            nombre_columna = key
        elif len(value) == 3:
            df, operacion, condiciones = value
            nombre_columna = key
        else:
            df, operacion, condiciones, nombre_columna = value
        
        # Validar operación
        if operacion not in operaciones_validas and nombre_columna not in include_columns:
            raise ValueError(f"Operación '{operacion}' no válida. Opciones: {list(operaciones_validas.keys())}")
        
        condiciones_columnas[key] = condiciones

        df = procesar_df(df, operacion, nombre_columna)

        df_final = df if df_final is None else pd.merge(df_final, df, on=common_column, how='outer').fillna(0)

    # Si no se encontraron datos válidos, retornar un DataFrame vacío
    if df_final is None or df_final.empty:
        print("Advertencia: No se encontraron datos válidos en 'data_dict'. Se devuelve un DataFrame vacío.")
        return pd.DataFrame(columns=[common_column])

    # Eliminar las columnas duplicadas que puedan haber quedado después de la fusión
    df_final = df_final.loc[:, ~df_final.columns.str.contains('_x|_y')]

    # Si todavía hay una columna 'Escuela_ID_x', tomarla y eliminar las columnas duplicadas
    if 'Escuela_ID_x' in df_final.columns:
        df_final['Escuela_ID'] = df_final['Escuela_ID_x']
        df_final = df_final.drop(columns=['Escuela_ID_x', 'Escuela_ID_y'], errors='ignore')

    # Ordenar los datos por el valor de 'common_column' si se proporciona 'order'
    if order:
        df_final = df_final.set_index(common_column).reindex(order).reset_index()
    else:
        df_final = df_final.set_index(common_column).reindex(sorted(valores_existentes)).reset_index()

    # Rellenar las columnas numéricas con valores por defecto
    numeric_cols = [col for col in df_final.columns if col != common_column and col not in include_columns]
    df_final[numeric_cols] = df_final[numeric_cols].fillna(0).astype(int)

    # Agregar una fila con los totales calculados por operación
    total_row = {common_column: 'TOTAL'}
    for key, (_, operacion, *_) in data_dict.items():
        nombre_columna = data_dict[key][3] if len(data_dict[key]) > 3 else key
        if nombre_columna in df_final.columns and nombre_columna not in include_columns:
            total_row[nombre_columna] = operaciones_validas[operacion](df_final[nombre_columna])
    df_final = pd.concat([df_final, pd.DataFrame([total_row])], ignore_index=True)

    # Eliminar columnas según condiciones de ocultación
    columnas_a_eliminar = []
    for col, condiciones in condiciones_columnas.items():
        if 'ocultar_si' in condiciones:
            condicion = condiciones['ocultar_si']
            valor_umbral = condiciones.get('valor', 0)
            if condicion == 'es_cero' and (df_final[col] == 0).all():
                columnas_a_eliminar.append(col)
            elif condicion == 'mayor_a' and (df_final[col] > valor_umbral).all():
                columnas_a_eliminar.append(col)
            elif condicion == 'menor_a' and (df_final[col] < valor_umbral).all():
                columnas_a_eliminar.append(col)

    df_final = df_final.drop(columns=columnas_a_eliminar, errors='ignore')

    # Renombrar las columnas si se proporcionan nuevos nombres
    if rename_columns:
        rename_dict = {list(rename.keys())[0]: list(rename.values())[0] for rename in rename_columns}
        df_final = df_final.rename(columns=rename_dict)

    return df_final

def tabla_generica_v10_funciona_en_DGE(data_dict, common_column, exclude_columns=None, include_columns=None, order=None, rename_columns=None):
    # Inicialización de variables
    df_final = None  # DataFrame resultante
    valores_existentes = set()  # Almacena valores únicos de 'common_column'
    exclude_columns = set(exclude_columns or [])  # Convierte en conjunto para búsqueda rápida
    include_columns = set(include_columns or [])  # Columnas que solo deben mostrarse
    rename_columns = rename_columns or []

    # Definición de operaciones válidas
    operaciones_validas = {
        'sumar': np.sum,
        'promedio': np.mean,
        'minimo': np.min,
        'maximo': np.max,
        'mediana': np.median,
        'desviacion': np.std,
        'varianza': np.var,
        'moda': lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan,
        'coef_var': lambda x: np.std(x) / np.mean(x) if np.mean(x) != 0 else np.nan,
        'iqr': lambda x: np.percentile(x, 75) - np.percentile(x, 25),
        'percentil_25': lambda x: np.percentile(x, 25),
        'percentil_75': lambda x: np.percentile(x, 75),
        'conteo': len,
        'frecuencia_relativa': lambda x: x.value_counts(normalize=True).to_dict(),
        'crecimiento_porcentual': lambda x: x.pct_change().mean(),
        'tendencia_movil': lambda x: x.rolling(window=2).mean().iloc[-1] if len(x) > 1 else np.nan
    }

    condiciones_columnas = {}  # Almacena condiciones de ocultación por columna

    # Función interna para procesar cada DataFrame
    def procesar_df(df, operacion, nombre_columna):
        if isinstance(df, pd.DataFrame) and not df.empty:
            value_cols = [col for col in df.columns if col not in exclude_columns and col != common_column]
            if value_cols:
                df = df.rename(columns={value_cols[0]: nombre_columna})
            df = df.drop(columns=exclude_columns, errors='ignore')
            valores_existentes.update(df[common_column].unique())
        else:
            df = pd.DataFrame({common_column: ['TOTAL'], nombre_columna: [0]})
        return df

    # Procesar los DataFrames del data_dict
    for key, value in data_dict.items():
        if len(value) == 2:
            df, operacion = value
            condiciones = {}
            nombre_columna = key
        elif len(value) == 3:
            df, operacion, condiciones = value
            nombre_columna = key
        else:
            df, operacion, condiciones, nombre_columna = value
        
        # Validar operación
        if operacion not in operaciones_validas and nombre_columna not in include_columns:
            raise ValueError(f"Operación '{operacion}' no válida. Opciones: {list(operaciones_validas.keys())}")
        
        condiciones_columnas[key] = condiciones

        df = procesar_df(df, operacion, nombre_columna)

        df_final = df if df_final is None else pd.merge(df_final, df, on=common_column, how='outer').fillna(0)

    # Si no se encontraron datos válidos, retornar un DataFrame vacío
    if df_final is None or df_final.empty:
        print("Advertencia: No se encontraron datos válidos en 'data_dict'. Se devuelve un DataFrame vacío.")
        return pd.DataFrame(columns=[common_column])

    # Eliminar las columnas duplicadas que puedan haber quedado después de la fusión
    df_final = df_final.loc[:, ~df_final.columns.str.contains('_x|_y')]

    # Si todavía hay una columna 'Escuela_ID_x', tomarla y eliminar las columnas duplicadas
    if 'Escuela_ID_x' in df_final.columns:
        df_final['Escuela_ID'] = df_final['Escuela_ID_x']
        df_final = df_final.drop(columns=['Escuela_ID_x', 'Escuela_ID_y'], errors='ignore')

    # Ordenar los datos por el valor de 'common_column' si se proporciona 'order'
    if order:
        df_final = df_final.set_index(common_column).reindex(order).reset_index()
    else:
        df_final = df_final.set_index(common_column).reindex(sorted(valores_existentes)).reset_index()

    # Rellenar las columnas numéricas con valores por defecto
    numeric_cols = [col for col in df_final.columns if col != common_column and col not in include_columns]
    df_final[numeric_cols] = df_final[numeric_cols].fillna(0).astype(int)

    # Agregar una fila con los totales calculados por operación
    total_row = {common_column: 'TOTAL'}
    for key, (_, operacion, *_) in data_dict.items():
        nombre_columna = data_dict[key][3] if len(data_dict[key]) > 3 else key
        if nombre_columna in df_final.columns and nombre_columna not in include_columns:
            total_row[nombre_columna] = operaciones_validas[operacion](df_final[nombre_columna])
    df_final = pd.concat([df_final, pd.DataFrame([total_row])], ignore_index=True)

    # Eliminar columnas según condiciones de ocultación
    columnas_a_eliminar = []
    for col, condiciones in condiciones_columnas.items():
        if 'ocultar_si' in condiciones:
            condicion = condiciones['ocultar_si']
            valor_umbral = condiciones.get('valor', 0)
            if condicion == 'es_cero' and (df_final[col] == 0).all():
                columnas_a_eliminar.append(col)
            elif condicion == 'mayor_a' and (df_final[col] > valor_umbral).all():
                columnas_a_eliminar.append(col)
            elif condicion == 'menor_a' and (df_final[col] < valor_umbral).all():
                columnas_a_eliminar.append(col)

    df_final = df_final.drop(columns=columnas_a_eliminar, errors='ignore')

    # Renombrar las columnas si se proporcionan nuevos nombres
    if rename_columns:
        rename_dict = {list(rename.keys())[0]: list(rename.values())[0] for rename in rename_columns}
        df_final = df_final.rename(columns=rename_dict)

    return df_final


import pandas as pd
import numpy as np

def tabla_generica_v10_v2(data_dict, common_column, exclude_columns=None, include_columns=None, order=None, rename_columns=None):
    # Inicialización de variables
    df_final = None  # DataFrame resultante
    valores_existentes = set()  # Almacena valores únicos de 'common_column'
    exclude_columns = set(exclude_columns or [])  # Convierte en conjunto para búsqueda rápida
    include_columns = set(include_columns or [])  # Columnas que solo deben mostrarse
    rename_columns = rename_columns or []
    tipos_originales = {}  # Almacena los tipos de datos originales antes de la unión

    # Definición de operaciones válidas
    operaciones_validas = {
        'sumar': np.sum,
        'promedio': np.mean,
        'minimo': np.min,
        'maximo': np.max,
        'mediana': np.median,
        'desviacion': np.std,
        'varianza': np.var,
        'moda': lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan,
        'coef_var': lambda x: np.std(x) / np.mean(x) if np.mean(x) != 0 else np.nan,
        'iqr': lambda x: np.percentile(x, 75) - np.percentile(x, 25),
        'percentil_25': lambda x: np.percentile(x, 25),
        'percentil_75': lambda x: np.percentile(x, 75),
        'conteo': len,
        'frecuencia_relativa': lambda x: x.value_counts(normalize=True).to_dict(),
        'crecimiento_porcentual': lambda x: x.pct_change().mean(),
        'tendencia_movil': lambda x: x.rolling(window=2).mean().iloc[-1] if len(x) > 1 else np.nan,
        'ninguna': lambda x: x  # No se aplica ninguna operación
    }

    condiciones_columnas = {}  # Almacena condiciones de ocultación por columna

    # Función interna para procesar cada DataFrame
    def procesar_df(df, operacion, nombre_columna):
        if isinstance(df, pd.DataFrame) and not df.empty:
            value_cols = [col for col in df.columns if col not in exclude_columns and col != common_column]
            if value_cols:
                df = df.rename(columns={value_cols[0]: nombre_columna})
            df = df.drop(columns=exclude_columns, errors='ignore')
            valores_existentes.update(df[common_column].unique())
            tipos_originales.update(df.dtypes.to_dict())  # Guardar los tipos originales
        else:
            df = pd.DataFrame({common_column: ['TOTAL'], nombre_columna: [0]})
        return df

    # Procesar los DataFrames del data_dict
    for key, value in data_dict.items():
        if len(value) == 2:
            df, operacion = value
            condiciones = {}
            nombre_columna = key
        elif len(value) == 3:
            df, operacion, condiciones = value
            nombre_columna = key
        else:
            df, operacion, condiciones, nombre_columna = value
        
        # Validar operación
        if operacion not in operaciones_validas and nombre_columna not in include_columns:
            raise ValueError(f"Operación '{operacion}' no válida. Opciones: {list(operaciones_validas.keys())}")
        
        condiciones_columnas[key] = condiciones

        df = procesar_df(df, operacion, nombre_columna)

        df_final = df if df_final is None else pd.merge(df_final, df, on=common_column, how='outer', suffixes=('', '_dup')).fillna(0)

    # Si no se encontraron datos válidos, retornar un DataFrame vacío
    if df_final is None or df_final.empty:
        print("Advertencia: No se encontraron datos válidos en 'data_dict'. Se devuelve un DataFrame vacío.")
        return pd.DataFrame(columns=[common_column])

    # Eliminar las columnas con sufijo '_dup'
    df_final = df_final[[col for col in df_final.columns if not col.endswith('_dup')]]

    # Ordenar los datos por el valor de 'common_column' si se proporciona 'order'
    if order:
        df_final = df_final.set_index(common_column).reindex(order).reset_index()
    else:
        df_final = df_final.set_index(common_column).reindex(sorted(valores_existentes)).reset_index()

    # Restaurar los tipos originales
    for col, tipo in tipos_originales.items():
        if col in df_final.columns and not col.endswith('_dup'):
            df_final[col] = df_final[col].astype(tipo)

    # Agregar una fila con los totales calculados por operación
    total_row = {common_column: 'TOTAL'}
    for key, (_, operacion, *_) in data_dict.items():
        nombre_columna = data_dict[key][3] if len(data_dict[key]) > 3 else key
        if nombre_columna in df_final.columns and nombre_columna not in include_columns:
            total_row[nombre_columna] = operaciones_validas[operacion](df_final[nombre_columna])
    df_final = pd.concat([df_final, pd.DataFrame([total_row])], ignore_index=True)

    # Eliminar columnas según condiciones de ocultación
    columnas_a_eliminar = []
    for col, condiciones in condiciones_columnas.items():
        if 'ocultar_si' in condiciones:
            condicion = condiciones['ocultar_si']
            valor_umbral = condiciones.get('valor', 0)
            if condicion == 'es_cero' and (df_final[col] == 0).all():
                columnas_a_eliminar.append(col)
            elif condicion == 'mayor_a' and (df_final[col] > valor_umbral).all():
                columnas_a_eliminar.append(col)
            elif condicion == 'menor_a' and (df_final[col] < valor_umbral).all():
                columnas_a_eliminar.append(col)

    df_final = df_final.drop(columns=columnas_a_eliminar, errors='ignore')

    # Renombrar las columnas si se proporcionan nuevos nombres
    if rename_columns:
        rename_dict = {list(rename.keys())[0]: list(rename.values())[0] for rename in rename_columns}
        df_final = df_final.rename(columns=rename_dict)

    return df_final


import pandas as pd
import numpy as np


# def tabla_generica_v10_v3_(data_dict, common_column, exclude_columns=None, include_columns=None, order=None, rename_columns=None):
#     # Inicialización de variables
#     df_final = None  # DataFrame resultante
#     valores_existentes = set()  # Almacena valores únicos de 'common_column'
#     exclude_columns = set(exclude_columns or [])  # Convierte en conjunto para búsqueda rápida
#     include_columns = set(include_columns or [])  # Columnas que solo deben mostrarse
#     rename_columns = rename_columns or []

#     # Definición de operaciones válidas
#     operaciones_validas = {
#         'sumar': np.sum,
#         'promedio': np.mean,
#         'minimo': np.min,
#         'maximo': np.max,
#         'mediana': np.median,
#         'desviacion': np.std,
#         'varianza': np.var,
#         'moda': lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan,
#         'coef_var': lambda x: np.std(x) / np.mean(x) if np.mean(x) != 0 else np.nan,
#         'iqr': lambda x: np.percentile(x, 75) - np.percentile(x, 25),
#         'percentil_25': lambda x: np.percentile(x, 25),
#         'percentil_75': lambda x: np.percentile(x, 75),
#         'conteo': len,
#         'frecuencia_relativa': lambda x: x.value_counts(normalize=True).to_dict(),
#         'crecimiento_porcentual': lambda x: x.pct_change().mean(),
#         'tendencia_movil': lambda x: x.rolling(window=2).mean().iloc[-1] if len(x) > 1 else np.nan
#     }

#     condiciones_columnas = {}  # Almacena condiciones de ocultación por columna
#     tipos_columnas_originales = {}  # Almacena los tipos de datos originales

#     # Función interna para procesar cada DataFrame
#     def procesar_df(df, operacion, nombre_columna):
#         if isinstance(df, pd.DataFrame) and not df.empty:
#             print(f"Columnas y tipos antes de la unión para {nombre_columna}:\n{df.dtypes}\n")
#             tipos_columnas_originales.update(df.dtypes.to_dict())
#             value_cols = [col for col in df.columns if col not in exclude_columns and col != common_column]
#             if value_cols:
#                 df = df.rename(columns={value_cols[0]: nombre_columna})
#             df = df.drop(columns=exclude_columns, errors='ignore')
#             valores_existentes.update(df[common_column].unique())
#         else:
#             df = pd.DataFrame({common_column: ['TOTAL'], nombre_columna: [0]})
#         return df

#     # Procesar los DataFrames del data_dict
#     for key, value in data_dict.items():
#         if len(value) == 2:
#             df, operacion = value
#             condiciones = {}
#             nombre_columna = key
#         elif len(value) == 3:
#             df, operacion, condiciones = value
#             nombre_columna = key
#         else:
#             df, operacion, condiciones, nombre_columna = value
        
#         # Validar operación
#         if operacion not in operaciones_validas and nombre_columna not in include_columns:
#             raise ValueError(f"Operación '{operacion}' no válida. Opciones: {list(operaciones_validas.keys())}")
        
#         condiciones_columnas[key] = condiciones

#         df = procesar_df(df, operacion, nombre_columna)

#         df_final = df if df_final is None else pd.merge(df_final, df, on=common_column, how='outer', suffixes=('', '_dup')).fillna(0)

#     # Si no se encontraron datos válidos, retornar un DataFrame vacío
#     if df_final is None or df_final.empty:
#         print("Advertencia: No se encontraron datos válidos en 'data_dict'. Se devuelve un DataFrame vacío.")
#         return pd.DataFrame(columns=[common_column])

#     # Eliminar columnas duplicadas que puedan haber quedado después de la fusión    
#     df_final = df_final.loc[:, ~df_final.columns.duplicated()]

#     print(f"Columnas y tipos después de la unión:\n{df_final.dtypes}\n")

#     # Restaurar los tipos de datos originales
#     for col, tipo in tipos_columnas_originales.items():
#         if col in df_final.columns and not col.endswith("_dup"):
#             df_final[col] = df_final[col].astype(tipo)

#     # Ordenar los datos por el valor de 'common_column' si se proporciona 'order'
#     if order:
#         df_final = df_final.set_index(common_column).reindex(order).reset_index()
#     else:
#         df_final = df_final.set_index(common_column).reindex(sorted(valores_existentes)).reset_index()

#     # Rellenar las columnas numéricas con valores por defecto
#     numeric_cols = [col for col in df_final.columns if col != common_column and col not in include_columns]
#     df_final[numeric_cols] = df_final[numeric_cols].fillna(0)

#     # Agregar una fila con los totales calculados por operación
#     total_row = {common_column: 'TOTAL'}
#     for key, (_, operacion, *_) in data_dict.items():
#         nombre_columna = data_dict[key][3] if len(data_dict[key]) > 3 else key
#         if nombre_columna in df_final.columns and nombre_columna not in include_columns:
#             total_row[nombre_columna] = operaciones_validas[operacion](df_final[nombre_columna])
#     df_final = pd.concat([df_final, pd.DataFrame([total_row])], ignore_index=True)

#     # Eliminar columnas según condiciones de ocultación
#     columnas_a_eliminar = []
#     for col, condiciones in condiciones_columnas.items():
#         if 'ocultar_si' in condiciones:
#             condicion = condiciones['ocultar_si']
#             valor_umbral = condiciones.get('valor', 0)
#             if condicion == 'es_cero' and (df_final[col] == 0).all():
#                 columnas_a_eliminar.append(col)
#             elif condicion == 'mayor_a' and (df_final[col] > valor_umbral).all():
#                 columnas_a_eliminar.append(col)
#             elif condicion == 'menor_a' and (df_final[col] < valor_umbral).all():
#                 columnas_a_eliminar.append(col)

#     df_final = df_final.drop(columns=columnas_a_eliminar, errors='ignore')

#     # Renombrar las columnas si se proporcionan nuevos nombres
#     if rename_columns:
#         rename_dict = {list(rename.keys())[0]: list(rename.values())[0] for rename in rename_columns}
#         df_final = df_final.rename(columns=rename_dict)

#     return df_final


# def tabla_generica_v10_v4_(data_dict, common_column, include_columns=None, order=None, rename_columns=None):
#     # Inicialización de variables
#     df_final = None  # DataFrame resultante
#     valores_existentes = set()  # Almacena valores únicos de 'common_column'
#     include_columns = set(include_columns or [])  # Columnas que solo deben mostrarse
#     rename_columns = rename_columns or []

#     # Definición de operaciones válidas
#     operaciones_validas = {
#         'sumar': np.sum,
#         'promedio': np.mean,
#         'minimo': np.min,
#         'maximo': np.max,
#         'mediana': np.median,
#         'desviacion': np.std,
#         'varianza': np.var,
#         'moda': lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan,
#         'coef_var': lambda x: np.std(x) / np.mean(x) if np.mean(x) != 0 else np.nan,
#         'iqr': lambda x: np.percentile(x, 75) - np.percentile(x, 25),
#         'percentil_25': lambda x: np.percentile(x, 25),
#         'percentil_75': lambda x: np.percentile(x, 75),
#         'conteo': len,
#         'frecuencia_relativa': lambda x: x.value_counts(normalize=True).to_dict(),
#         'crecimiento_porcentual': lambda x: x.pct_change().mean(),
#         'tendencia_movil': lambda x: x.rolling(window=2).mean().iloc[-1] if len(x) > 1 else np.nan
#     }

#     condiciones_columnas = {}  # Almacena condiciones de ocultación por columna
#     tipos_columnas_originales = {}  # Almacena los tipos de datos originales

#     # Función interna para procesar cada DataFrame
#     def procesar_df(df, operacion, nombre_columna):
#         if isinstance(df, pd.DataFrame) and not df.empty:
#             print(f"Columnas y tipos antes de la unión para {nombre_columna}:\n{df.dtypes}\n")
#             tipos_columnas_originales.update(df.dtypes.to_dict())
#             value_cols = [col for col in df.columns if col != common_column]
#             if value_cols:
#                 df = df.rename(columns={value_cols[0]: nombre_columna})
#             valores_existentes.update(df[common_column].unique())
#         else:
#             df = pd.DataFrame({common_column: ['TOTAL'], nombre_columna: [0]})
#         return df

#     # Procesar los DataFrames del data_dict
#     for key, value in data_dict.items():
#         if len(value) == 2:
#             df, operacion = value
#             condiciones = {}
#             nombre_columna = key
#         elif len(value) == 3:
#             df, operacion, condiciones = value
#             nombre_columna = key
#         else:
#             df, operacion, condiciones, nombre_columna = value
        
#         # Validar operación
#         if operacion not in operaciones_validas and nombre_columna not in include_columns:
#             raise ValueError(f"Operación '{operacion}' no válida. Opciones: {list(operaciones_validas.keys())}")
        
#         condiciones_columnas[key] = condiciones

#         df = procesar_df(df, operacion, nombre_columna)

#         df_final = df if df_final is None else pd.merge(df_final, df, on=common_column, how='outer', suffixes=('', '_dup')).fillna(0)

#     # Si no se encontraron datos válidos, retornar un DataFrame vacío
#     if df_final is None or df_final.empty:
#         print("Advertencia: No se encontraron datos válidos en 'data_dict'. Se devuelve un DataFrame vacío.")
#         return pd.DataFrame(columns=[common_column])

#     # Eliminar columnas duplicadas que puedan haber quedado después de la fusión    
#     df_final = df_final.loc[:, ~df_final.columns.duplicated()]

#     print(f"Columnas y tipos después de la unión:\n{df_final.dtypes}\n")

#     # Restaurar los tipos de datos originales
#     for col, tipo in tipos_columnas_originales.items():
#         if col in df_final.columns and not col.endswith("_dup"):
#             df_final[col] = df_final[col].astype(tipo)

#     # Ordenar los datos por el valor de 'common_column' si se proporciona 'order'
#     if order:
#         df_final = df_final.set_index(common_column).reindex(order).reset_index()
#     else:
#         df_final = df_final.set_index(common_column).reindex(sorted(valores_existentes)).reset_index()

#     # Rellenar las columnas numéricas con valores por defecto
#     numeric_cols = [col for col in df_final.columns if col != common_column and col not in include_columns]
#     df_final[numeric_cols] = df_final[numeric_cols].fillna(0)

#     # Agregar una fila con los totales calculados por operación
#     total_row = {common_column: 'TOTAL'}
#     for key, (_, operacion, *_) in data_dict.items():
#         nombre_columna = data_dict[key][3] if len(data_dict[key]) > 3 else key
#         if nombre_columna in df_final.columns and nombre_columna not in include_columns:
#             total_row[nombre_columna] = operaciones_validas[operacion](df_final[nombre_columna])
#     df_final = pd.concat([df_final, pd.DataFrame([total_row])], ignore_index=True)

#     # Eliminar columnas según condiciones de ocultación
#     columnas_a_eliminar = []
#     for col, condiciones in condiciones_columnas.items():
#         if 'ocultar_si' in condiciones:
#             condicion = condiciones['ocultar_si']
#             valor_umbral = condiciones.get('valor', 0)
#             if condicion == 'es_cero' and (df_final[col] == 0).all():
#                 columnas_a_eliminar.append(col)
#             elif condicion == 'mayor_a' and (df_final[col] > valor_umbral).all():
#                 columnas_a_eliminar.append(col)
#             elif condicion == 'menor_a' and (df_final[col] < valor_umbral).all():
#                 columnas_a_eliminar.append(col)

#     df_final = df_final.drop(columns=columnas_a_eliminar, errors='ignore')

#     # Renombrar las columnas si se proporcionan nuevos nombres
#     if rename_columns:
#         rename_dict = {list(rename.keys())[0]: list(rename.values())[0] for rename in rename_columns}
#         df_final = df_final.rename(columns=rename_dict)

#     return df_final

def tabla_generica_v10_v2_1_previo(data_dict, common_column,  include_columns=None, order=None, rename_columns=None):
    # Inicialización de variables
    df_final = None  # DataFrame resultante
    valores_existentes = set()  # Almacena valores únicos de 'common_column'    
    #include_columns = set(include_columns or [])  # Columnas que solo deben mostrarse
    include_columns = include_columns or []
    rename_columns = rename_columns or []
    tipos_originales = {}  # Almacena los tipos de datos originales antes de la unión

    

    # Definición de operaciones válidas
    operaciones_validas = {
        'sumar': np.sum,
        'promedio': np.mean,
        'minimo': np.min,
        'maximo': np.max,
        'mediana': np.median,
        'desviacion': np.std,
        'varianza': np.var,
        'moda': lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan,
        'coef_var': lambda x: np.std(x) / np.mean(x) if np.mean(x) != 0 else np.nan,
        'iqr': lambda x: np.percentile(x, 75) - np.percentile(x, 25),
        'percentil_25': lambda x: np.percentile(x, 25),
        'percentil_75': lambda x: np.percentile(x, 75),
        'conteo': len,
        'frecuencia_relativa': lambda x: x.value_counts(normalize=True).to_dict(),
        'crecimiento_porcentual': lambda x: x.pct_change().mean(),
        'tendencia_movil': lambda x: x.rolling(window=2).mean().iloc[-1] if len(x) > 1 else np.nan,
        'ninguna': lambda x: x  # No se aplica ninguna operación
    }

    condiciones_columnas = {}  # Almacena condiciones de ocultación por columna

    # Función interna para procesar cada DataFrame
    def procesar_df(df, operacion, nombre_columna):
        if isinstance(df, pd.DataFrame) and not df.empty:
            #value_cols = [col for col in df.columns if col not in exclude_columns and col != common_column]
            value_cols = [col for col in df.columns if col != common_column]
            if value_cols:
                df = df.rename(columns={value_cols[0]: nombre_columna})            
            valores_existentes.update(df[common_column].unique())
            tipos_originales.update(df.dtypes.to_dict())  # Guardar los tipos originales
        else:
            df = pd.DataFrame({common_column: ['TOTAL'], nombre_columna: [0]})
        return df

    # Procesar los DataFrames del data_dict
    for key, value in data_dict.items():
        if len(value) == 2:
            df, operacion = value
            condiciones = {}
            nombre_columna = key
        elif len(value) == 3:
            df, operacion, condiciones = value
            nombre_columna = key
        else:
            df, operacion, condiciones, nombre_columna = value
        
        # Validar operación
        if operacion not in operaciones_validas and nombre_columna not in include_columns:
            raise ValueError(f"Operación '{operacion}' no válida. Opciones: {list(operaciones_validas.keys())}")
        
        condiciones_columnas[key] = condiciones

        df = procesar_df(df, operacion, nombre_columna)

        print('... obtengo los tipos de datos del dataframe... ' )
        for col in df.columns:
            print(col , ' ' , type(col))

        df_final = df if df_final is None else pd.merge(df_final, df, on=common_column, how='outer', suffixes=('', '_dup')).fillna(0)

    print('..imprimir las columnas resultantes... ' , )
    for col in df_final.columns:
        print(col , ' ' , type(col))
    print('----------------------------------------------')
    print('..verificar las columnas que tengo con las que debería tener... ')
    print(data_dict.keys())    
    print(common_column)
    print(include_columns)
    columnas_finales = []
    for col_ in data_dict.keys():
        if col_ != common_column:
            columnas_finales.append(col_)
    for col_ in include_columns:
        columnas_finales.append(col_)
    columnas_finales.append(common_column)
    for col_ in rename_columns:
        columnas_finales.append(list(col_.values())[0]) 
    print('columnas finales..')
    print(columnas_finales)        
    print('----------------------------------------------')
    

    def eliminar_columnas_df(df, columnas_finales, df_final_columns):
        return df[[col for col in df.columns if col in columnas_finales and col in df_final_columns]]
    
    # Si no se encontraron datos válidos, retornar un DataFrame vacío
    if df_final is None or df_final.empty:
        print("Advertencia: No se encontraron datos válidos en 'data_dict'. Se devuelve un DataFrame vacío.")
        return pd.DataFrame(columns=[common_column])

    # Eliminar las columnas con sufijo '_dup'
    df_final = df_final[[col for col in df_final.columns if not col.endswith('_dup')]]

    # Ordenar los datos por el valor de 'common_column' si se proporciona 'order'
    if order:
        df_final = df_final.set_index(common_column).reindex(order).reset_index()
    else:
        df_final = df_final.set_index(common_column).reindex(sorted(valores_existentes)).reset_index()

    # Restaurar los tipos originales
    for col, tipo in tipos_originales.items():
        if col in df_final.columns and not col.endswith('_dup'):
            df_final[col] = df_final[col].astype(tipo)

    # Agregar una fila con los totales calculados por operación
    total_row = {common_column: 'TOTAL'}
    for key, (_, operacion, *_) in data_dict.items():
        nombre_columna = data_dict[key][3] if len(data_dict[key]) > 3 else key
        if nombre_columna in df_final.columns and nombre_columna not in include_columns:
            total_row[nombre_columna] = operaciones_validas[operacion](df_final[nombre_columna])
    df_final = pd.concat([df_final, pd.DataFrame([total_row])], ignore_index=True)

    # Eliminar columnas según condiciones de ocultación
    columnas_a_eliminar = []
    for col, condiciones in condiciones_columnas.items():
        if 'ocultar_si' in condiciones:
            condicion = condiciones['ocultar_si']
            valor_umbral = condiciones.get('valor', 0)
            if condicion == 'es_cero' and (df_final[col] == 0).all():
                columnas_a_eliminar.append(col)
            elif condicion == 'mayor_a' and (df_final[col] > valor_umbral).all():
                columnas_a_eliminar.append(col)
            elif condicion == 'menor_a' and (df_final[col] < valor_umbral).all():
                columnas_a_eliminar.append(col)

    df_final = df_final.drop(columns=columnas_a_eliminar, errors='ignore')

    # Renombrar las columnas si se proporcionan nuevos nombres
    if rename_columns:
        rename_dict = {list(rename.keys())[0]: list(rename.values())[0] for rename in rename_columns}
        df_final = df_final.rename(columns=rename_dict)

    print('...columnas del dataframe final...')
    for col__ in df_final.columns:
        print(col__)

    print('----------------------------final--------------------------')        
    the_final_dataframe = eliminar_columnas_df(df_final, columnas_finales, df_final.columns)

    return the_final_dataframe

import pandas as pd
import numpy as np

import pandas as pd
import numpy as np






# Llamar a la función de prueba si el script se ejecuta directamente
if __name__ == '__main__':    

    data_dict_2 = {
        'DESEMPEÑOS'            : (pd.DataFrame({'DESEMPEÑO' : ['Avanzado' , 'Medio' , 'Básico' , 'Crítico']    , 'Matrícula'   : [ 0 ,  0 ,  0 , 0]})  , 'sumar'   ,   {'ocultar_si': 'es_cero'}) ,
        'primera medición 2024' : (pd.DataFrame({'DESEMPEÑO' : ['Avanzado' , 'Medio' , 'Básico' , 'Crítico']    , 'Matrícula'   : [ 7 , 17 , 37 , 62]}) , 'sumar'   ,   {'ocultar_si': 'es_cero'}),
        'primera medición 2025' : (pd.DataFrame({'DESEMPEÑO' : ['Avanzado' , 'Medio' , 'Básico' , 'Crítico']    , 'Matrícula'   : [16 , 18 , 47 , 47]}) , 'sumar'   ,   {'ocultar_si': 'es_cero'}),
    }

     # Orden deseado para los cursos
    order = ['Avanzado' , 'Medio' , 'Básico' , 'Crítico']
    tabla_final_data_dict_2 = tabla_generica_v10_v2_1_previo(
        data_dict_2, 
        common_column = 'DESEMPEÑO',        
        include_columns = ['Matrícula'], 
        order=order,
        rename_columns=[{'DESEMPEÑO':'Niveles de Desempeño'}]        
    )
    # print('--'*50)

    # print(type(tabla_final_data_dict_2))
    # caca = tabla_final_data_dict_2.to_dict(orient='records')
    # print(caca)

    # printDFrame('- ', tabla_final_data_dict_2)

    # print(tabla_final_data_dict_2)
    # print(tabla_final_data_dict_2.columns)
    # for col in tabla_final_data_dict_2.columns:
    #     print(col , ' ' , type(col))
    
    
    # Ver el resultado
    print(json.dumps(tabla_final_data_dict_2.to_dict(orient='records'), #'records', # Opciones: 'dict', 'list', 'series', 'split', 'records', 'index'
                     indent=4,
                     ensure_ascii=False)
    ) 


    # data_dict_1 = {        
    #     'Alumnos con Desempeño': pd.DataFrame({'CURSO_NORMALIZADO': ['2°', '3°'], 'Matricula': [129, 116]}),
    #     'Alumnos incluidos SI': pd.DataFrame({'CURSO_NORMALIZADO': ['2°', '3°'], 'Matricula': [90, 85]}),
    #     'Alumnos incluidos NO': pd.DataFrame({'CURSO_NORMALIZADO': ['2°', '3°'], 'Matricula': [39, None]})  # Contiene un NaN
    # }

    # # print('modelo a seguir... ')
    # # print(data_dict_1.get('Alumnos con Desempeño'))
    # # print('------------------------')

    #  # Orden deseado para los cursos
    # order = ['3°', '2°']
    # tabla_final_data_dict_1 = tabla_generica_v2(data_dict_1, common_column='CURSO_NORMALIZADO', order=order)
    # # Ver el resultado
    # # Ver el resultado
    # print(json.dumps(tabla_final_data_dict_1.to_dict(orient='records'), #'records', # Opciones: 'dict', 'list', 'series', 'split', 'records', 'index'
    #                  indent=4,
    #                  ensure_ascii=False)
    # )

    # print('-'*50)
    print('fin..')