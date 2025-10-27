import pandas as pd

def aplicar_condiciones_avanzadas(dataframe, condiciones):
    """
    Aplica condiciones avanzadas de filtrado a un DataFrame usando pandas SQL (`query`).
    
    Args:
        dataframe (pd.DataFrame): DataFrame al que se aplicarán las condiciones.
        condiciones (dict): Diccionario con condiciones avanzadas.

    Returns:
        pd.DataFrame: DataFrame filtrado.
    """
    if condiciones is True or not isinstance(condiciones, dict):
        raise ValueError(f"Se esperaba un diccionario de condiciones, pero se recibió {type(condiciones).__name__}")
    
    logic_and = condiciones.pop("AND", True)  # Por defecto, lógica AND
    filtros = []
    
    for columna, criterio in condiciones.items():
        if columna not in dataframe.columns:
            raise ValueError(f"La columna '{columna}' no existe en el DataFrame.")
        
        if isinstance(criterio, list):  # Filtrar por lista de valores
            filtros.append(f"`{columna}` in {criterio}")
        elif isinstance(criterio, dict) and "range" in criterio:  # Filtrar por rango
            rango = criterio["range"]
            if len(rango) != 2:
                raise ValueError(f"El rango especificado para '{columna}' debe contener exactamente 2 valores.")
            filtros.append(f"`{columna}` >= {rango[0]} and `{columna}` <= {rango[1]}")
        else:  # Filtrar por valor exacto
            filtros.append(f"`{columna}` == {repr(criterio)}")
    
    if not filtros:
        return dataframe  # Si no hay filtros, devolver el DataFrame sin cambios
    
    query_str = (" and " if logic_and else " or ").join(filtros)
    
    try:
        return dataframe.query(query_str)
    except Exception as e:
        raise ValueError(f"Error al aplicar los filtros con query: {e}")

# import numpy as np


# def aplicar_condiciones_avanzadas(dataframe, condiciones):
#     """
#     Aplica condiciones avanzadas de filtrado a un DataFrame.

#     Args:
#         dataframe (pd.DataFrame): DataFrame al que se aplicarán las condiciones.
#         condiciones (dict): Diccionario con condiciones avanzadas.

#     Returns:
#         pd.DataFrame: DataFrame filtrado.
#     """

#     # Si condiciones es True (o cualquier otro valor no diccionario), lanzar un error
#     if condiciones is True or not isinstance(condiciones, dict):
#         raise ValueError(f"Se esperaba un diccionario de condiciones, pero se recibió {type(condiciones).__name__}")

#     logic_and = condiciones.pop("AND", True)  # Por defecto, lógica AND
    
#     filtros = []
#     for columna, criterio in condiciones.items():
#         if columna not in dataframe.columns:
#             raise ValueError(f"La columna '{columna}' no existe en el DataFrame.")

#         if isinstance(criterio, list):  # Filtrar por lista de valores
#             filtros.append(dataframe[columna].isin(criterio))
#         elif isinstance(criterio, dict) and "range" in criterio:  # Filtrar por rango
#             rango = criterio["range"]
#             if len(rango) != 2:
#                 raise ValueError(f"El rango especificado para '{columna}' debe contener exactamente 2 valores.")
#             filtros.append(dataframe[columna].between(rango[0], rango[1]))
#         else:  # Filtrar por valor exacto
#             filtros.append(dataframe[columna] == criterio)

#     # Combinar los filtros según lógica AND/OR
#     if logic_and:
#         return dataframe[np.logical_and.reduce(filtros)]
#     else:
#         return dataframe[np.logical_or.reduce(filtros)]

##################################################################################################################################

# def aplicar_condiciones_avanzadas(dataframe, condiciones):
#     """
#     Aplica condiciones avanzadas de filtrado a un DataFrame.

#     Args:
#         dataframe (pd.DataFrame): DataFrame al que se aplicarán las condiciones.
#         condiciones (dict): Diccionario con condiciones avanzadas. Ejemplo:
#             {
#                 "CURSO_NORMALIZADO": ["4°", "5°"],  # CURSO_NORMALIZADO en '4°' o '5°'
#                 "matricula_por_curso": {"range": [100, 200]},  # Entre 100 y 200 (inclusive)
#                 "AND": True  # Usar lógica AND (por defecto); OR para lógica alternativa.
#             }

#     Returns:
#         pd.DataFrame: DataFrame filtrado.
#     """
#     logic_and = condiciones.pop("AND", True)  # Por defecto, lógica AND
    
#     filtros = []
#     for columna, criterio in condiciones.items():
#         if columna not in dataframe.columns:
#             raise ValueError(f"La columna '{columna}' no existe en el DataFrame.")

#         if isinstance(criterio, list):  # Filtrar por lista de valores
#             filtros.append(dataframe[columna].isin(criterio))
#         elif isinstance(criterio, dict) and "range" in criterio:  # Filtrar por rango
#             rango = criterio["range"]
#             if len(rango) != 2:
#                 raise ValueError(f"El rango especificado para '{columna}' debe contener exactamente 2 valores.")
#             filtros.append(dataframe[columna].between(rango[0], rango[1]))
#         else:  # Filtrar por valor exacto
#             filtros.append(dataframe[columna] == criterio)

#     # Combinar los filtros según lógica AND/OR
#     if logic_and:
#         return dataframe[np.logical_and.reduce(filtros)]
#     else:
#         return dataframe[np.logical_or.reduce(filtros)]
