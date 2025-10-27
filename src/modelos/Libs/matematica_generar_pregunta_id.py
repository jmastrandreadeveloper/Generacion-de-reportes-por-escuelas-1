def generar_pregunta_id_string(Nivel_ID, Curso, numero_pregunta):
    """
    Genera un código único de tipo string para identificar preguntas.
    
    Parámetros:
    - Nivel_ID (int): ID del nivel educativo (2: Primaria, 3: Secundaria, 4: Secundaria)
    - Curso (str): Curso con formato '1°', '2°', etc.
    - numero_pregunta (int): Número de la pregunta
    
    Retorna:
    - str: Código único para pregunta_id en formato 'Nivel_Curso_NumeroPregunta'
    
    Ejemplo:
    >>> generar_pregunta_id_string(2, '1°', 1)
    'Prim_1°_1'
    >>> generar_pregunta_id_string(3, '6°', 2)
    'Sec_6°_2'
    """
    dict_niveles = {
        2: "Prim",
        3: "Sec",
        4: "Sec",
    }
    
    # Obtener el nombre del nivel
    nivel_nombre = dict_niveles.get(Nivel_ID)
    
    if nivel_nombre is None:
        raise ValueError(f"Nivel_ID {Nivel_ID} no válido. Debe ser 2, 3 o 4.")
    
    # Limpiar espacios del curso si los tiene
    curso_limpio = str(Curso).strip()
    
    # Generar el código concatenado
    pregunta_id = f"{nivel_nombre}_{curso_limpio}_{numero_pregunta}"
    
    return pregunta_id


# Ejemplos de uso
if __name__ == "__main__":
        
    print('-------------------------------------------------------------------------------------------------------------------')
    
    # Ejemplos individuales
    print("Ejemplos individuales:")
    print(f"Ejemplo 1: {generar_pregunta_id_string(2, '1°', 1)}")
    print(f"Ejemplo 2: {generar_pregunta_id_string(4, '5°', 2)}")
    print(f"Ejemplo 3: {generar_pregunta_id_string(3, '6°', 1)}")
    
    # Ejemplo con un DataFrame de pandas
    try:
        import pandas as pd
        
        # Crear un DataFrame de ejemplo
        df = pd.DataFrame({
            'Nivel_ID': [2, 4, 2, 3, 2],
            'Curso ': ['1°', '5°', '4°', '6°', '7°'],
            'numero_pregunta': [1, 2, 18, 2, 20]
        })
        
        # Aplicar la función para generar pregunta_id
        df['pregunta_id'] = df.apply(
            lambda row: generar_pregunta_id_string(row['Nivel_ID'], row['Curso '], row['numero_pregunta']), 
            axis=1
        )
        
        print("\nDataFrame con pregunta_id:")
        print(df)
        
    except ImportError:
        print("\nPandas no está instalado. Instálalo con: pip install pandas")
        
        
def generar_pregunta_id_por_diccionario(DICT_NIVEL_CURSO_CANT_PREGUNTAS_CON_RESPUESTA_CORRECTA):
    PRIMARIA = 2
    SECUNDARIA_OR = 3
    SECUNDARIA_TEC = 4
    
    return


    # DICT_NIVEL_CURSO_CANT_PREGUNTAS = {
    #     'PRIMARIA': {
    #         '1°': 5 ,
    #         '2°': 7 , 
    #         '3°': 8 , 
    #         '4°': 9 , 
    #         '5°': 10 , 
    #         '6°': 10 , 
    #         '7°': 11 , 
    #     },
    #     'SECUNDARIA_OR': {
    #         '1°': 6 , 
    #         '2°': 8 , 
    #         '3°': 9 , 
    #         '4°': 10 , 
    #         '5°': 11 , 
    #     },
    # }
    
    #generar_pregunta_id_por_diccionario(DICT_NIVEL_CURSO_CANT_PREGUNTAS)
    
    #exit()
    
    
    # # Ejemplo 1: Nivel 1, Curso 5, Pregunta 23
    # print(f"Ejemplo 1: {generar_pregunta_id(1, 5, 23)}")
    
    # # Ejemplo 2: Nivel 3, Curso 12, Pregunta 150
    # print(f"Ejemplo 2: {generar_pregunta_id(3, 12, 150)}")
    
    # # Ejemplo 3: Nivel 10, Curso 1, Pregunta 1
    # print(f"Ejemplo 3: {generar_pregunta_id(10, 1, 1)}")
    
    # # Ejemplo con un DataFrame de pandas
    # try:
    #     import pandas as pd
        
    #     # Crear un DataFrame de ejemplo
    #     df = pd.DataFrame({
    #         'Nivel_ID': [2 , 4 , 2 , 3 , 2],
    #         'Curso ': ['1°' , '5°' , '4°' , '6°' , '7°'],
    #         'numero_pregunta': [1 , 2 , 1 , 2 , 1]
    #     })
        
    #     # Aplicar la función para generar pregunta_id
    #     df['pregunta_id'] = df.apply(
    #         lambda row: generar_pregunta_id(row['Nivel_ID'], row['Curso '], row['numero_pregunta']), 
    #         axis=1
    #     )
        
    #     print("\nDataFrame con pregunta_id:")
    #     print(df)
        
    # except ImportError:
    #     print("\nPandas no está instalado. Instálalo con: pip install pandas")
    
    
    
    
# def generar_pregunta_id(Nivel_ID, Curso, numero_pregunta):
#     """
#     Genera un código único de tipo int para identificar preguntas.
    
#     Parámetros:
#     - nivel (int): Nivel educativo (ej: 1, 2, 3, etc.)
#     - curso (int): Número de curso (ej: 1, 2, 3, etc.)
#     - numero_pregunta (int): Número de la pregunta (ej: 1, 2, 3, etc.)
    
#     Retorna:
#     - int: Código único para pregunta_id
    
#     Formato del código: NNCCCPPPP
#     - NN: Nivel (2 dígitos)
#     - CCC: Curso (3 dígitos)
#     - PPPP: Número de pregunta (4 dígitos)
    
#     Ejemplo:
#     >>> generar_pregunta_id(1, 5, 23)
#     10050023
#     """
#     # Validar que los valores sean positivos
#     if Nivel_ID < 0 or Curso < 0 or numero_pregunta < 0:
#         raise ValueError("Los valores deben ser positivos")
    
#     # Validar rangos máximos
#     if Nivel_ID > 99:
#         raise ValueError("El nivel no puede ser mayor a 99")
#     if Curso > 999:
#         raise ValueError("El curso no puede ser mayor a 999")
#     if numero_pregunta > 999999:
#         raise ValueError("El número de pregunta no puede ser mayor a 999999")
    
#     # Generar el código
#     pregunta_id = (Nivel_ID * 10000000) + (Curso * 10000) + numero_pregunta
    
#     return pregunta_id