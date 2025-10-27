def recorrer_diccionario_a_lista(d, prefijo=""):
    resultados = []
    for clave, valor in d.items():
        ruta = f"{prefijo}/{clave}" if prefijo else clave
        if isinstance(valor, dict):
            resultados.extend(recorrer_diccionario_a_lista(valor, ruta))
        else:
            resultados.append((ruta, valor))
    return resultados


def recorrer_diccionario_descompuesto(d, prefijo=None):
    """
    Recorre un diccionario anidado y devuelve una lista de tuplas con:
    - partes de la clave como lista
    - el valor final
    """
    if prefijo is None:
        prefijo = []

    resultados = []
    for clave, valor in d.items():
        nueva_ruta = prefijo + [clave]
        if isinstance(valor, dict):
            resultados.extend(recorrer_diccionario_descompuesto(valor, nueva_ruta))
        else:
            resultados.append((nueva_ruta, valor))
    return resultados
