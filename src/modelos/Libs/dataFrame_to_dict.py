# esta función convierte un dataframe en un diccionario para luego
# ser usado dentro de un json
import src.modelos.Libs.validar_columna as valCols

def dataframe_to_dict(dataframe, orient='records', show_index=True, columns=None):
    """
    Convierte un DataFrame a un diccionario o JSON con opciones avanzadas.

    Args:
        dataframe (pd.DataFrame): DataFrame a convertir.
        orient (str): Orientación del diccionario ('records', 'index', etc.).
        show_index (bool): Incluir el índice en la salida.
        columns (list): Columnas a incluir. Si es None, incluye todas.

    Returns:
        dict/list: Datos convertidos a dict o lista.
    """
    try:
        # Validar columnas si se especifican
        if columns:
            missing_columns = valCols.validar_columnas(dataframe, columns)
            if missing_columns:
                raise ValueError(f"Columnas faltantes en el DataFrame: {missing_columns}")
            dataframe = dataframe[columns]

        # Eliminar índice si no se requiere
        if not show_index:
            dataframe = dataframe.reset_index(drop=True)

        # Convertir a diccionario
        return dataframe.to_dict(orient=orient)
    except Exception as e:
        raise ValueError(f"Error al convertir el DataFrame a dict: {e}")


