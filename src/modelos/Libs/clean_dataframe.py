# def clean_dataframe(dataframe, int_columns, float_columns):
    

#     for col in int_columns:
#         dataframe[col] = dataframe[col].astype(int).round(0).fillna(0)
#     for col in float_columns:
#         dataframe[col] = dataframe[col].round(2).fillna(0)
        
#     return dataframe

import pandas as pd
import numpy as np

# def clean_dataframe(dataframe, int_columns, float_columns):
#     df = dataframe.copy()  # Trabaja sobre una copia
    
#     # Limpieza de columnas enteras
#     for col in int_columns:
#         df[col] = pd.to_numeric(df[col], errors='coerce')       # Convierte a numérico
#         df[col] = df[col].fillna(0).replace([np.inf, -np.inf], 0)  # Reemplaza NaN e Inf
#         #df[col] = df[col].round(0).astype(int)                  # Redondea y convierte a int
    
#     # Limpieza de columnas flotantes
#     for col in float_columns:
#         df[col] = pd.to_numeric(df[col], errors='coerce')       # Convierte a numérico
#         df[col] = df[col].fillna(0).replace([np.inf, -np.inf], 0)  # Reemplaza NaN e Inf
#         #df[col] = df[col].round(2)                              # Redondea a 2 decimales
    
#     return df


def clean_dataframe(
    dataframe, 
    int_columns=None, 
    float_columns=None,
    round_int=False, 
    round_float=False
):
    df = dataframe.copy()
    
    int_columns = int_columns or []
    float_columns = float_columns or []

    ignored_columns = []

    for col in int_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            df[col] = df[col].fillna(0).replace([np.inf, -np.inf], 0)
            
            if round_int:
                df[col] = df[col].round(0).astype(int)
            else:
                if (df[col] % 1 == 0).all():  # solo convierte si ya son enteros
                    df[col] = df[col].astype(int)
                else:
                    print(f"⚠️ Columna '{col}' no convertida a entero para evitar pérdida de decimales.")
        else:
            ignored_columns.append(col)

    for col in float_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            df[col] = df[col].fillna(0).replace([np.inf, -np.inf], 0)
            if round_float:
                df[col] = df[col].round(2)
        else:
            ignored_columns.append(col)

    if ignored_columns:
        print(f"🔍 Columnas ignoradas (no existen en el DataFrame): {ignored_columns}")
    
    return df


# import pandas as pd
# import numpy as np

# def clean_dataframe(
#     dataframe, 
#     int_columns=None, 
#     float_columns=None,
#     round_int=False, 
#     round_float=False
# ):
#     df = dataframe.copy()
    
#     int_columns = int_columns or []
#     float_columns = float_columns or []

#     ignored_columns = []

#     for col in int_columns:
#         if col in df.columns:
#             df[col] = pd.to_numeric(df[col], errors='coerce')
#             df[col] = df[col].fillna(0).replace([np.inf, -np.inf], 0)
#             if round_int:
#                 df[col] = df[col].round(0)
#             try:
#                 df[col] = df[col].astype(int)
#             except ValueError:
#                 print(f"⚠️ No se pudo convertir a entero la columna '{col}'.")
#         else:
#             ignored_columns.append(col)

#     for col in float_columns:
#         if col in df.columns:
#             df[col] = pd.to_numeric(df[col], errors='coerce')
#             df[col] = df[col].fillna(0).replace([np.inf, -np.inf], 0)
#             if round_float:
#                 df[col] = df[col].round(2)
#         else:
#             ignored_columns.append(col)

#     if ignored_columns:
#         print(f"🔍 Columnas ignoradas (no existen en el DataFrame): {ignored_columns}")
    
#     return df

