import json
import pandas as pd

def group_df(dataframe, id_col, columnas_datos=None, output_col='datos_agrupados', as_json=True):
    """
    Agrupa el DataFrame por una columna ID dada y devuelve los datos agrupados en dos formatos:

    - Si as_json=True: Devuelve la columna de datos agrupados como JSON string.
    - Si as_json=False: Devuelve un DataFrame filtrado.

    Parámetros:
        dataframe (pd.DataFrame): El DataFrame de entrada.
        id_col (str): Nombre de la columna a usar como ID para agrupar.
        columnas_datos (list, opcional): Lista de columnas a incluir. Si no se especifica, usa todas menos la columna ID.
        output_col (str, opcional): Nombre de la columna que contendrá los datos agrupados.
        as_json (bool, opcional): Indica si se desea devolver como JSON (True) o como DataFrame normal (False).

    Retorna:
        pd.DataFrame: DataFrame agrupado.
    """

    if columnas_datos is None:
        columnas_datos = [col for col in dataframe.columns if col != id_col]

    dataframe = dataframe.copy()

    if as_json:
        processed_data = []

        for id_value, group in dataframe.groupby(id_col):
            datos = group[columnas_datos].iloc[0].to_dict()
            datos_json = json.dumps(datos, ensure_ascii=False)
            
            processed_data.append({
                id_col: id_value,
                output_col: datos_json
            })
        
        return pd.DataFrame(processed_data)

    return dataframe[[id_col] + columnas_datos].drop_duplicates()

def filter_datos(id_value, dataframe, id_col, output_col='datos_agrupados'):
    """
    Filtra el DataFrame por un valor de ID y devuelve los datos agrupados en formato diccionario.

    Parámetros:
        id_value (any): Valor de ID a buscar.
        dataframe (pd.DataFrame): DataFrame a filtrar.
        id_col (str): Nombre de la columna ID.
        output_col (str, opcional): Nombre de la columna de datos agrupados (cuando está en formato JSON).

    Retorna:
        dict | None: Diccionario con los datos agrupados o None si no se encuentra.
    """

    df_filtrado = dataframe[dataframe[id_col] == id_value]

    if df_filtrado.empty:
        print(f"No se encontraron datos para el ID '{id_value}'.")
        return None

    if output_col in df_filtrado.columns:
        datos = df_filtrado.iloc[0][output_col]
        try:
            return json.loads(datos) if isinstance(datos, str) else datos
        except json.JSONDecodeError:
            print(f"Error al decodificar JSON para el ID '{id_value}'.")
            return None