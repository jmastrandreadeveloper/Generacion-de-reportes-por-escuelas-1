def convertir_a_lista_de_listas(data_dict, key):
    """
    Convierte un diccionario con listas de diccionarios en una lista de listas.
    :param data_dict: Diccionario que contiene la clave con los datos.
    :param key: Clave del diccionario que contiene la lista de diccionarios.
    :return: Lista de listas donde la primera sublista es el encabezado.
    """
    # Extraer la lista de diccionarios
    data_list = data_dict.get(key, [])
    
    if not data_list:
        return []  # Retorna lista vacía si no hay datos
    
    # Obtener los nombres de las columnas (las claves del primer diccionario)
    columnas = list(data_list[0].keys())
    
    # Crear la lista de listas
    resultado = [columnas]  # Primera fila con los nombres de las columnas
    resultado.extend([list(fila.values()) for fila in data_list])
    
    return resultado

def view_table(resultado):
    for fila in resultado:
        print(fila)
    return

def extraer_todas_las_columnas(lista_diccionarios):
    if not lista_diccionarios:
        return []

    # Detecta todas las claves presentes en el primer diccionario
    claves = list(lista_diccionarios[0].keys())

    # Genera una lista por cada clave con sus respectivos valores
    resultado = []
    for clave in claves:
        valores = [dic.get(clave, None) for dic in lista_diccionarios]
        resultado.append(valores)

    return resultado

# Llamar a la función de prueba si el script se ejecuta directamente
if __name__ == '__main__':   

    # Ejemplo de uso
    data_dict = {
        "tabla_data_dict_totalidad_de_estudiantes_por_curso": [
            {"Cursos": "2°", "Alumnos por curso": 107, "Alumnos con DESEMPEÑO": 122, "Alumnos sin DESEMPEÑO": 1, "Alumnos incluidos NO": 123, "Alumnos incluidos SI": 5},
            {"Cursos": "3°", "Alumnos por curso": 137, "Alumnos con DESEMPEÑO": 114, "Alumnos sin DESEMPEÑO": 1, "Alumnos incluidos NO": 115, "Alumnos incluidos SI": 4},
            {"Cursos": "4°", "Alumnos por curso": 115, "Alumnos con DESEMPEÑO": 112, "Alumnos sin DESEMPEÑO": 2, "Alumnos incluidos NO": 114, "Alumnos incluidos SI": 6},
            {"Cursos": "5°", "Alumnos por curso": 122, "Alumnos con DESEMPEÑO": 111, "Alumnos sin DESEMPEÑO": 5, "Alumnos incluidos NO": 116, "Alumnos incluidos SI": 1},
            {"Cursos": "6°", "Alumnos por curso": 119, "Alumnos con DESEMPEÑO": 117, "Alumnos sin DESEMPEÑO": 4, "Alumnos incluidos NO": 121, "Alumnos incluidos SI": 2},
            {"Cursos": "7°", "Alumnos por curso": 125, "Alumnos con DESEMPEÑO": 114, "Alumnos sin DESEMPEÑO": 6, "Alumnos incluidos NO": 120, "Alumnos incluidos SI": 1},
            {"Cursos": "Total", "Alumnos por curso": 725, "Alumnos con DESEMPEÑO": 690, "Alumnos sin DESEMPEÑO": 19, "Alumnos incluidos NO": 709, "Alumnos incluidos SI": 19}
        ]
    }

    resultado = convertir_a_lista_de_listas(data_dict, "tabla_data_dict_totalidad_de_estudiantes_por_curso")
    view_table(resultado)