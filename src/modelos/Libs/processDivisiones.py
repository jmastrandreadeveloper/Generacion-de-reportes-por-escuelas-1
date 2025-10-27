# esta función procesa los nombres de las divisiones para estandarizarlas 
# se realiza con el fin de evitar errores en el procesamiento posterior
# y para que los nombres de las divisiones sean consistentes en todo el sistema

# ingresa un dataframe y devuelve un dataframe con las divisiones estandarizadas   
# el reemplazo es por curso o sea que cambia los nombres de las divisiones por curso  


# La idea sería:

# Agrupar por curso.
# Dentro de cada curso, identificar todas las divisiones únicas.
# Asignarles nombres normalizados "1°", "2°", "3°", ... según su orden.
# Devolver el mismo DataFrame pero con la columna División remapeada.


import pandas as pd
import json

# def remapear_divisiones_por_escuela_curso(
#     df,
#     col_escuela="Escuela_ID",
#     col_curso="Curso ",
#     col_division="División",
#     col_alumno_id="Alumno_ID"
# ):
#     """
#     Reordena por Escuela, Curso, Alumno_ID y División,
#     y reasigna nombres de divisiones por cada grupo (Escuela + Curso)
#     siguiendo el orden de aparición.
#     """
#     df = df.copy()

#     # Ordenar para consistencia
#     df = df.sort_values(
#         by=[col_escuela, col_curso, col_alumno_id, col_division],
#         ascending=[True, True, True, True]
#     )

#     nueva_division = pd.Series(index=df.index, dtype="object")

#     # Agrupar por Escuela y Curso
#     for (escuela, curso), grupo in df.groupby([col_escuela, col_curso], sort=False):
#         divisiones_unicas = list(dict.fromkeys(grupo[col_division]))  # Orden de aparición
#         mapping = {old: f"{i+1}°" for i, old in enumerate(divisiones_unicas)}
#         nueva_division.loc[grupo.index] = grupo[col_division].map(mapping)

#     df[col_division] = nueva_division
#     return df

def remapear_divisiones_por_escuela_curso(
    df,
    col_escuela="Escuela_ID",
    col_curso="Curso ",
    col_division="División",    
    col_division_id="División_ID"  # Se agrega el nombre de la columna para el ID
):
    """
    Reasigna los nombres de las divisiones por cada grupo (Escuela + Curso)
    basándose en el orden ascendente de la División_ID, reemplazándolos
    por números (1, 2, 3, etc.).
    """
    df = df.copy()
    
    # Se agrega la columna de División_ID para el ordenamiento
    nueva_division = pd.Series(index=df.index, dtype="object")

    # Agrupar por Escuela y Curso
    for (escuela, curso), grupo in df.groupby([col_escuela, col_curso]):
        # Obtener las divisiones únicas y ordenarlas por su ID de forma ascendente
        divisiones_unicas_y_ordenadas = grupo[[col_division, col_division_id]].drop_duplicates().sort_values(by=col_division_id)
        
        # Crear el diccionario de mapeo
        mapping = {old_name: str(i + 1) for i, old_name in enumerate(divisiones_unicas_y_ordenadas[col_division])}
        
        # Aplicar el mapeo al grupo
        nueva_division.loc[grupo.index] = grupo[col_division].map(mapping)
        
    df[col_division] = nueva_division
    return df

def mapear_divisiones(df, json_data):
    """
    Actualiza la columna 'División' en un DataFrame usando los IDs de 'División_ID'
    y un diccionario JSON de referencia.

    Args:
        df (pd.DataFrame): El DataFrame de pandas con las columnas 'División_ID' y 'División'.
        json_data (dict): El diccionario que contiene la estructura del JSON.

    Returns:
        pd.DataFrame: El DataFrame con la columna 'División' actualizada.
                      Devuelve None si el JSON no tiene la estructura esperada
                      o si el DataFrame no tiene las columnas necesarias.
    """
    try:
        # Verificar que existan las columnas necesarias
        if 'División_ID' not in df.columns or 'División' not in df.columns:
            print("❌ Error: El DataFrame debe contener las columnas 'División_ID' y 'División'.")
            return None

        # Unir todos los mapeos de todas las escuelas y cursos en un solo dict
        mapeo_divisiones = {}
        for escuela, cursos in json_data.get("escuela_id_curso_división_id", {}).items():
            for curso, divisiones in cursos.items():
                mapeo_divisiones.update(divisiones)

        # Si no encontramos nada en el JSON
        if not mapeo_divisiones:
            print("❌ Error: La estructura del JSON no es la esperada o no se encontraron divisiones.")
            return None

        # Usar 'División_ID' como referencia para actualizar la columna 'División'
        df['División'] = df['División_ID'].astype(str).map(mapeo_divisiones).fillna(df['División'])

        return df

    except Exception as e:
        print(f"❌ Ocurrió un error inesperado: {e}")
        return None