# esta función usa el json de divisiones que se genera en el preprocesamiento de nominal
# para poder usarlo en el preprocesamiento de matemática
# y así evitar errores en el procesamiento posterior
import pandas as pd

def aplicar_diccionario_divisiones(df, diccionario, col_escuela="Escuela_ID", col_curso="Curso", col_division_id="División_ID", col_division="División"):
    """
    Reemplaza los nombres de las divisiones en un DataFrame según un diccionario
    que mapea (Escuela_ID, Curso, División_ID) -> Nombre de División.
    
    :param df: DataFrame sobre el que se aplicarán los cambios
    :param diccionario: Diccionario generado por generar_diccionario_divisiones
    :param col_escuela: Nombre de la columna de ID de escuela
    :param col_curso: Nombre de la columna de curso
    :param col_division_id: Nombre de la columna ID de división
    :param col_division: Nombre de la columna con el nombre de la división
    :return: DataFrame con las divisiones renombradas
    """
    df = df.copy()

    def obtener_nombre(row):
        clave = (row[col_escuela], row[col_curso], row[col_division_id])
        return diccionario.get(clave, row[col_division])  # si no está, deja el valor original

    df[col_division] = df.apply(obtener_nombre, axis=1)

    return df

def aplicar_nombres_divisiones(df, mapping_dict, 
                                col_escuela="Escuela_ID", 
                                col_curso="Curso ", 
                                col_division_id="División_ID", 
                                col_division_nombre="División", 
                                nueva_columna=False):
    """
    Aplica los nombres de divisiones a un DataFrame usando un diccionario de mapeo.

    Optimización:
    - Convierte mapping_dict en un DataFrame auxiliar y hace un merge para mayor velocidad.
    - Evita el uso de .apply fila por fila.
    """
    # Paso 1: Convertir el mapping_dict a una lista de tuplas para DataFrame
    registros = []
    for escuela_id, cursos in mapping_dict.items():
        for curso, divisiones in cursos.items():
            for division_id, nombre in divisiones.items():
                registros.append({
                    col_escuela: str(escuela_id),
                    col_curso: str(curso),
                    col_division_id: str(division_id),
                    col_division_nombre: nombre
                })

    # Paso 2: Crear DataFrame auxiliar de mapeo
    df_mapeo = pd.DataFrame(registros)

    # Paso 3: Convertir columnas clave en el df original a string para que coincidan
    df[col_escuela] = df[col_escuela].astype(str)
    df[col_curso] = df[col_curso].astype(str)
    df[col_division_id] = df[col_division_id].astype(str)

    # Paso 4: Merge
    if nueva_columna:
        nuevo_nombre = col_division_nombre + "_Nuevo"
        df = df.merge(df_mapeo, on=[col_escuela, col_curso, col_division_id], how="left", suffixes=("", "_map"))
        df[nuevo_nombre] = df[col_division_nombre + "_map"]
        df.drop(columns=[col_division_nombre + "_map"], inplace=True)
    else:
        df = df.merge(df_mapeo, on=[col_escuela, col_curso, col_division_id], how="left", suffixes=("", "_map"))
        df[col_division_nombre] = df[col_division_nombre + "_map"]
        df.drop(columns=[col_division_nombre + "_map"], inplace=True)

    return df
