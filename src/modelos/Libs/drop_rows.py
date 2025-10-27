import pandas as pd

def drop_rows(dataframe: pd.DataFrame, column, valores_a_eliminar):
    """
    Elimina filas de un DataFrame si el valor en la columna especificada está en `valores_a_eliminar`.
    
    :param dataframe: DataFrame de pandas.
    :param column: Nombre de la columna donde se buscarán los valores a eliminar.
    :param valores_a_eliminar: Lista o conjunto de valores (numéricos o strings) a eliminar.
    :return: DataFrame sin las filas que contienen los valores a eliminar.
    """
    return dataframe.loc[~dataframe[column].astype(str).isin(map(str, valores_a_eliminar))]

def drop_rows_advanced(dataframe: pd.DataFrame, conditions: dict, logic: str = "AND"):
    """
    Elimina filas de un DataFrame según condiciones avanzadas.

    :param dataframe: DataFrame de pandas.
    :param conditions: Diccionario con las condiciones a aplicar. 
                       Formato: {'columna': ('operador', valor)}
                       Operadores admitidos: '==', '!=', '<', '>', '<=', '>=', 'in', 'not in'.
    :param logic: Tipo de lógica entre condiciones. Puede ser "AND" (todas deben cumplirse) o "OR" (cualquiera puede cumplirse).
    :return: DataFrame sin las filas que cumplen las condiciones.
    """
    
    if logic not in ["AND", "OR"]:
        raise ValueError("El parámetro 'logic' debe ser 'AND' o 'OR'.")

    filtros = []  # Lista de filtros para cada condición
    
    for column, (operator, value) in conditions.items():
        if column not in dataframe.columns:
            raise ValueError(f"La columna '{column}' no existe en el DataFrame.")
        
        if operator == "==":
            filtros.append(dataframe[column] == value)
        elif operator == "!=":
            filtros.append(dataframe[column] != value)
        elif operator == "<":
            filtros.append(dataframe[column] < value)
        elif operator == ">":
            filtros.append(dataframe[column] > value)
        elif operator == "<=":
            filtros.append(dataframe[column] <= value)
        elif operator == ">=":
            filtros.append(dataframe[column] >= value)
        elif operator == "in":
            filtros.append(dataframe[column].isin(value))
        elif operator == "not in":
            filtros.append(~dataframe[column].isin(value))
        else:
            raise ValueError(f"Operador no soportado: {operator}")

    # Combinar condiciones con AND (&) o OR (|)
    filtro_final = filtros[0]
    for f in filtros[1:]:
        filtro_final = filtro_final & f if logic == "AND" else filtro_final | f

    return dataframe.loc[~filtro_final]  # Se eliminan las filas que cumplen la condición