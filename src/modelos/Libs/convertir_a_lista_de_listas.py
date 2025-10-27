def convertir_a_lista_de_listas(data):
    """
    Convierte una lista de diccionarios a una lista de listas,
    donde la primera fila contiene los encabezados.
    """
    if not data:
        return []

    encabezados = list(data[0].keys())
    filas = [encabezados]

    for fila in data:
        filas.append([fila.get(col, '') for col in encabezados])

    return filas
