# esta función genera las conclusiones por alumno en base a los valores de las respuestas de la columna respuesta

def generar_conclusiones_por_alumno(df, col_alumno='Alumno_ID', col_resultado='resultado', total_preguntas=16):
    """
    Genera un DataFrame con una conclusión del examen por alumno, incluyendo datos descriptivos.

    Parámetros:
    - df: DataFrame con respuestas de los alumnos.
    - col_alumno: nombre de la columna de identificación del alumno.
    - col_resultado: nombre de la columna que contiene 'Verdadero', 'Falso' o 'Sin respuesta'.
    - total_preguntas: cantidad total de preguntas que debe responder cada alumno.

    Retorna:
    - DataFrame con una fila por alumno, incluyendo columnas descriptivas y la Conclusión.
    """
    
    # Copia para evitar modificar el DataFrame original
    df = df.copy()

    columnas_deseadas = [
        'Alumno_ID', 'DNI', 'Persona_ID', 'Apellido', 'Nombre',
        'Curso ', 'Curso ', 'Curso_ID', 'División', 'Nivel', 'Gestión',
        'Supervisión', 'Escuela_ID', 'CUE', 'subcue', 'Número',
        'Nombre_Escuela', 'Anexo', 'Departamento', 'Localidad', 'zona',
        'Regional', 'ciclo_lectivo'
    ]

    def clasificar(porcentaje, sin_respuestas, total):
        if sin_respuestas == total:
            return "Examen no respondido"
        elif porcentaje == 0:
            return "Sin respuestas correctas"
        elif porcentaje >= 90:
            return "Excelente desempeño"
        elif porcentaje >= 70:
            return "Buen desempeño"
        elif porcentaje >= 50:
            return "Desempeño aceptable"
        elif porcentaje >= 30:
            return "Bajo desempeño"
        else:
            return "Desempeño deficiente"

    # Contar respuestas por tipo por alumno
    resumen = df.groupby(col_alumno)[col_resultado].value_counts().unstack(fill_value=0).reset_index()

    # Calcular % de respuestas correctas
    resumen['%_correctas'] = 100 * resumen.get('Correcto', 0) / total_preguntas

    # Clasificar según criterios
    resumen['Conclusión'] = resumen.apply(
        lambda row: clasificar(row['%_correctas'], row.get('Sin respuesta', 0), total_preguntas),
        axis=1
    )

    # Datos únicos por alumno (solo una fila con datos personales)
    datos_alumno = df.drop_duplicates(subset=[col_alumno])[columnas_deseadas]

    # Combinar datos personales con la conclusión
    resultado_final = datos_alumno.merge(resumen[[col_alumno, 'Conclusión']], on=col_alumno, how='left')

    return resultado_final


# la diferencia con la de arriba es que pueden ser más de 16 respuestas o preguntas por alumno
def generar_conclusiones_por_alumno_dinamica(df, col_alumno='Alumno_ID', col_resultado='resultado'):
    """
    Genera un DataFrame con una conclusión del examen por alumno, sin asumir una cantidad fija de preguntas.

    Parámetros:
    - df: DataFrame con respuestas de los alumnos.
    - col_alumno: nombre de la columna de identificación del alumno.
    - col_resultado: nombre de la columna que contiene 'Verdadero', 'Falso' o 'Sin respuesta'.

    Retorna:
    - DataFrame con columnas: Alumno_ID, Conclusión.
    """
    def clasificar(porcentaje, sin_respuestas, total):
        if sin_respuestas == total:
            return "Examen no respondido"
        elif porcentaje == 0:
            return "Sin respuestas correctas"
        elif porcentaje >= 90:
            return "Excelente desempeño"
        elif porcentaje >= 70:
            return "Buen desempeño"
        elif porcentaje >= 50:
            return "Desempeño aceptable"
        elif porcentaje >= 30:
            return "Bajo desempeño"
        else:
            return "Desempeño deficiente"

    # Contar por tipo de respuesta por alumno
    resumen = df.groupby(col_alumno)[col_resultado].value_counts().unstack(fill_value=0).reset_index()

    # Calcular total de respuestas por alumno
    resumen['total_respuestas'] = resumen.sum(axis=1, numeric_only=True)

    # Calcular % correctas
    resumen['%_correctas'] = 100 * resumen.get('Correcto', 0) / resumen['total_respuestas']

    # Clasificar según criterios
    resumen['Conclusión'] = resumen.apply(
        lambda row: clasificar(row['%_correctas'], row.get('Sin respuesta', 0), row['total_respuestas']),
        axis=1
    )

    return resumen[[col_alumno, 'Conclusión']]

def generar_conclusiones_df(df, col_alumno='Alumno_ID', col_resultado='resultado'):
    """
    Devuelve un DataFrame con una fila por alumno, incluyendo datos generales y una conclusión según su desempeño.

    Parámetros:
    - df: DataFrame que contiene una fila por respuesta del alumno.
    - col_alumno: nombre de la columna identificadora del alumno.
    - col_resultado: nombre de la columna con los resultados (Verdadero, Falso, Sin respuesta).

    Retorna:
    - DataFrame con una fila por alumno y la conclusión de su examen.
    """

    columnas_deseadas = [
        'Alumno_ID', 'DNI', 'Persona_ID', 'Apellido_Alumno', 'Nombre_Alumno',
        'CURSO_NORMALIZADO', 'Curso ', 'Curso_ID', 'División', 'Nivel', 'Gestión',
        'Supervisión', 'Escuela_ID', 'CUE', 'subcue', 'mero_escuela',
        'Nombre_Escuela', 'Anexo', 'Departamento', 'Localidad', 'zona',
        'Regional', 'ciclo_lectivo'
    ]

    def clasificar(porcentaje, sin_respuestas, total):
        if sin_respuestas == total:
            return "Examen no respondido"
        elif porcentaje == 0:
            return "Sin respuestas correctas"
        elif porcentaje >= 90:
            return "Excelente desempeño"
        elif porcentaje >= 70:
            return "Buen desempeño"
        elif porcentaje >= 50:
            return "Desempeño aceptable"
        elif porcentaje >= 30:
            return "Bajo desempeño"
        else:
            return "Desempeño deficiente"

    # Resumen de resultados por alumno
    resumen = df.groupby(col_alumno)[col_resultado].value_counts().unstack(fill_value=0).reset_index()
    resumen['total_respuestas'] = resumen.sum(axis=1, numeric_only=True)
    resumen['%_correctas'] = 100 * resumen.get('Correcto', 0) / resumen['total_respuestas']
    resumen['Conclusión'] = resumen.apply(
        lambda row: clasificar(row['%_correctas'], row.get('Sin respuesta', 0), row['total_respuestas']),
        axis=1
    )

    # Datos únicos por alumno (para columnas descriptivas)
    datos_alumno = df.drop_duplicates(subset=[col_alumno])[columnas_deseadas]

    # Unimos los datos descriptivos con la conclusión
    resultado_final = datos_alumno.merge(resumen[[col_alumno, 'Conclusión']], on=col_alumno, how='left')

    return resultado_final


