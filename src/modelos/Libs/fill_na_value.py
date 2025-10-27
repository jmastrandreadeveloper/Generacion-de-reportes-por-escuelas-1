import pandas as pd

def fill_na_value_in_column(dataframe, column, value):
    # Validación del DataFrame
    if dataframe is None or not isinstance(dataframe, pd.DataFrame):
        raise ValueError("❌ El argumento 'dataframe' debe ser un DataFrame válido.")
    
    # Validación del nombre de columna
    if column not in dataframe.columns:
        raise KeyError(f"❌ La columna '{column}' no existe en el DataFrame.")

    # Validación del valor
    if value is None:
        raise ValueError("❌ El valor de reemplazo no puede ser None.")

    # Operación segura sobre una copia
    df = dataframe.copy()
    df[column] = df[column].fillna(value)

    return df
