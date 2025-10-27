# esta función toma el archivo de Matemática y obtiene la última carga por fecha
# es decir considera como última carga válida la que tiene la fecha más reciente
# la nueva manera de escribir el código será utilizando menos archivos intermedios 
# como por ejemplo los GroupAggregation, estos se harán directamente 
# llamando funciones desde el main

import pandas as pd


def obtener_última_carga_por_fecha(df, fecha_columna=None, columnas_clave=None):
    """
    Elimina duplicados dejando solo la fila más reciente según una columna de fecha.

    Parámetros:
    - df: DataFrame con los datos a limpiar.
    - fecha_columna: str. Nombre de la columna que contiene la fecha y hora de carga.
    - columnas_clave: list of str. Lista de columnas que identifican un registro único 
      (por ejemplo, ['alumno_id', 'pregunta_id']).

    Retorna:
    - DataFrame limpio con los registros más recientes según la clave definida.
    """
    
    # Copia para evitar modificar el DataFrame original
    df = df.copy()

    if fecha_columna is None:
        raise ValueError("Debes especificar el nombre de la columna de fecha.")

    if fecha_columna not in df.columns:
        raise ValueError(f"La columna '{fecha_columna}' no existe en el DataFrame.")

    if columnas_clave is None:
        raise ValueError("Debes especificar una lista de columnas clave para identificar duplicados.")

    for col in columnas_clave:
        if col not in df.columns:
            raise ValueError(f"La columna clave '{col}' no existe en el DataFrame.")

    # Convertir la columna de fecha a tipo datetime (por si acaso)
    df[fecha_columna] = pd.to_datetime(df[fecha_columna], errors='coerce')

    # Ordenar por la columna de fecha descendente (más reciente primero)
    df_ordenado = df.sort_values(by=fecha_columna, ascending=False)

    # Eliminar duplicados dejando el más reciente por combinación de columnas clave
    df_filtrado = df_ordenado.drop_duplicates(subset=columnas_clave, keep='first')

    # Ordenar por las columnas clave para una mejor presentación
    df_ordenado_final = df_filtrado.sort_values(by=columnas_clave)

    return df_ordenado_final