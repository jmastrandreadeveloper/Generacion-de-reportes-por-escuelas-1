def totalizar_columnas(lista_de_diccionarios):
    if not lista_de_diccionarios:
        return []  # Retorna una lista vacía si la entrada está vacía

    # Inicializar diccionario para almacenar los totales
    totales = {}

    # Iterar sobre las claves del primer diccionario
    for clave in lista_de_diccionarios[0].keys():
        # Si todos los valores de la columna son numéricos, se totaliza
        if all(isinstance(fila[clave], (int, float)) for fila in lista_de_diccionarios):
            totales[clave] = sum(fila[clave] for fila in lista_de_diccionarios)
        else:
            totales[clave] = "Total"  # Para la columna no numérica

    # Agregar la fila de totales a la lista original
    lista_de_diccionarios.append(totales)

    return lista_de_diccionarios