# eta función filtra un archivo nominal de alumnos dependiendo de los criterios que se pasen,
# estos dataframe no han sido agrupadoss, on el reultado del preproceso de loss archivos nominale o de fluidez
# usaremos el mecanismo de criterios desarrollado en los otros tipos de filtrado

import pandas as pd
import os
import sys
import json

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..' ))
sys.path.append(project_root)
import src.tools.utils as u
import src.modelos.Libs.validar_columna as valCols
from  src.modelos.Libs.filtrado_condicional import aplicar_condiciones_avanzadas

def test_(nombre):
    print('Hola este es el test de filtrar_dataframe_nominal_por_escuela_y_curso...  ', nombre)

def filtrar_dataframe_nominal_por_escuela_y_curso(df, Escuela_ID, CURSO_NORMALIZADO, show_index=True, columns=None, orientacion='records', condiciones=None):
    """
    Esta función filtra un DataFrame nominal de alumnos en base a 'Escuela_ID' y 'CURSO_NORMALIZADO'.
    No realiza agrupamientos, solo filtra y devuelve los datos en el formato especificado.

    Parámetros:
    - df (DataFrame): El DataFrame con los datos de alumnos.
    - Escuela_ID (int o str): El ID de la escuela que se quiere filtrar.
    - CURSO_NORMALIZADO (str): El curso específico a filtrar.
    - show_index (bool, opcional): Si es False, se eliminará el índice en el resultado. Por defecto es True.
    - columns (list, opcional): Lista de columnas a conservar en el DataFrame filtrado. Si es None, se mantienen todas.
    - orientacion (str, opcional): El formato en el que se devolverá el resultado (`'records'`, `'dict'`, `'list'`, etc.). 
      Por defecto es `'records'`.
    - condiciones (dict, opcional): Diccionario con condiciones adicionales para aplicar filtros más avanzados.

    Retorna:
    - dict o lista, según el formato especificado en `orientacion`.

    Explicación de la lógica:
    Verificar si hay datos
    Antes de filtrar, se revisa si Escuela_ID y CURSO_NORMALIZADO están en el DataFrame. Si no existen, retorna una lista vacía [].
    Filtrar por Escuela_ID y CURSO_NORMALIZADO
    Se seleccionan las filas que cumplen con ambos criterios.
    Aplicar condiciones adicionales (si existen)
    Si se pasa un diccionario de condiciones (condiciones), se usa la función aplicar_condiciones_avanzadas() para filtrar aún más los datos.
    Seleccionar columnas específicas (si se especifican)
    Se revisa que las columnas indicadas existan en el DataFrame. Si alguna falta, se lanza un error.
    Opcional: Quitar el índice
    Si show_index es False, se elimina el índice para que el resultado sea más limpio.
    Convertir al formato solicitado
    Se usa .to_dict(orient=orientacion) para devolver los datos en el formato deseado ('records', 'dict', etc.).
    """
    try:
        # Paso 1: Verificar si existen registros con el 'Escuela_ID' y 'CURSO_NORMALIZADO' especificados
        if (Escuela_ID not in df['Escuela_ID'].unique()) or (CURSO_NORMALIZADO not in df['Curso '].unique()):
            return []  # Si no existen coincidencias, devuelve una lista vacía
        
        # Paso 2: Filtrar el DataFrame según los valores de 'Escuela_ID' y 'CURSO_NORMALIZADO'
        dFrame_filtrado = df[(df['Escuela_ID'] == Escuela_ID) & (df['Curso '] == CURSO_NORMALIZADO)]

        # Paso 3: Aplicar filtros adicionales si se especificaron en 'condiciones'
        if condiciones:
            dFrame_filtrado = aplicar_condiciones_avanzadas(dFrame_filtrado, condiciones)

        # Paso 4: Si se especifican columnas, validar que existan en el DataFrame y filtrar
        if columns:
            missing_columns = set(columns) - set(dFrame_filtrado.columns)
            if missing_columns:
                raise ValueError(f'Columnas faltantes en el DataFrame filtrado: {missing_columns}')
            dFrame_filtrado = dFrame_filtrado[columns]

        # Paso 5: Resetear el índice si 'show_index' es False
        if not show_index:
            dFrame_filtrado = dFrame_filtrado.reset_index(drop=True)

        # Paso 6: Convertir el DataFrame al formato especificado en 'orientacion' y retornarlo
        return dFrame_filtrado.to_dict(orient=orientacion)

    except Exception as e:
        # Capturar cualquier error y lanzar un ValueError con un mensaje descriptivo
        raise ValueError(f'Error al filtrar el DataFrame: {e}')
