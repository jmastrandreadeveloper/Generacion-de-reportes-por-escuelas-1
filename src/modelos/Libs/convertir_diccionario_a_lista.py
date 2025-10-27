def convertir_diccionario_a_lista(diccionario):
    # Extraer las claves y la longitud de los valores (asumiendo que todas las listas tienen la misma longitud)
    claves = list(diccionario.keys())
    longitud = len(diccionario[claves[0]])

    # Construir la lista de diccionarios
    lista_de_diccionarios = [
        {clave: diccionario[clave][i] for clave in claves}
        for i in range(longitud)
    ]

    return lista_de_diccionarios