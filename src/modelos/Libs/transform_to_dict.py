def transform_to_dict(data):
    """
    Convierte una lista de diccionarios en un formato donde cada clave tiene una lista de valores.

    Args:
    data (list of dict): Lista de diccionarios con las mismas claves.

    Returns:
    dict: Diccionario con claves como nombres de columnas y valores como listas.
    """
    if not data:
        return {}

    transformed_dict = {key: [] for key in data[0].keys()}

    for entry in data:
        for key, value in entry.items():
            transformed_dict[key].append(value)

    return transformed_dict