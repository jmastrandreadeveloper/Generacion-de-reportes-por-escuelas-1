
def validar_columnas(dataframe, required_columns):
    """
    Valida si las columnas requeridas están presentes en un DataFrame.

    Args:
        dataframe (pd.DataFrame): DataFrame a validar.
        required_columns (list): Lista de nombres de columnas requeridas.

    Returns:
        list: Columnas faltantes. Vacío si no falta ninguna.
    """
    return [col for col in required_columns if col not in dataframe.columns]