import os
import sys
import json

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..' ))
sys.path.append(project_root)

import numpy as np
import src.tools.utils as u

def generar_condiciones_personalizadas(dataframe, reglas=None, max_categorias=10, rango_percentil=(0.05, 0.95)):
    """
    Genera un diccionario de condiciones avanzadas basado en las columnas y datos del DataFrame,
    con opciones de personalización por columna.

    Args:
        dataframe (pd.DataFrame): DataFrame de entrada.
        reglas (dict): Diccionario que define reglas específicas por columna. Ejemplo:
            {
                "CURSO_NORMALIZADO": {"tipo": "categorico", "incluir_todo": True},
                "matricula_por_curso": {"tipo": "numerico", "percentiles": [0.1, 0.9]},
                "fecha_ingreso": {"tipo": "fecha", "rango_personalizado": ["2023-01-01", "2023-06-30"]}
            }
        max_categorias (int): Número máximo de categorías únicas para considerar una columna como categórica.
        rango_percentil (tuple): Percentiles (mínimo y máximo) para calcular el rango por defecto de condiciones numéricas.

    Returns:
        dict: Diccionario de condiciones avanzadas basado en el contenido del DataFrame.
    """
    condiciones = {}

    for columna in dataframe.columns:
        # Obtener reglas específicas para la columna
        regla = reglas.get(columna, {}) if reglas else {}
        tipo_dato = regla.get("tipo", None)
        dtype = dataframe[columna].dtype

        # Si no se especifica el tipo, deducirlo automáticamente
        if not tipo_dato:
            if dtype in ['object', 'category', 'bool']:
                tipo_dato = "categorico"
            elif np.issubdtype(dtype, np.number):
                tipo_dato = "numerico"
            elif np.issubdtype(dtype, np.datetime64):
                tipo_dato = "fecha"

        # Generar condiciones según el tipo de columna
        if tipo_dato == "categorico":
            incluir_todo = regla.get("incluir_todo", False)
            valores_unicos = dataframe[columna].dropna().unique()
            if incluir_todo or len(valores_unicos) <= max_categorias:
                condiciones[columna] = {
                    "in": list(valores_unicos),
                    "not_in": regla.get("excluir", [])  # Valores excluidos personalizados
                }

        elif tipo_dato == "numerico":
            percentiles = regla.get("percentiles", rango_percentil)
            min_val = dataframe[columna].quantile(percentiles[0])
            max_val = dataframe[columna].quantile(percentiles[1])
            condiciones[columna] = {
                "range": regla.get("rango_personalizado", [min_val, max_val]),  # Rango personalizado o calculado
                "not_in": regla.get("excluir", [])
            }

        elif tipo_dato == "fecha":
            min_date = dataframe[columna].min()
            max_date = dataframe[columna].max()
            condiciones[columna] = {
                "range": regla.get("rango_personalizado", [min_date, max_date]),
                "not_in": regla.get("excluir", [])
            }

        # Valores faltantes (si no está configurado, se incluyen por defecto)
        condiciones[columna]["is_null"] = regla.get("incluir_nulos", False)
        condiciones[columna]["not_null"] = regla.get("excluir_nulos", True)

    # Lógica combinada por defecto
    condiciones["AND"] = True
    return condiciones

if __name__ == '__main__':    
    PATH_file_contar_alumnos_por_escuela_group = 'data/processed/transformed/Fluidez/dataframe_FL_1_contar_alumnos_por_escuela_y_curso_group.csv'
    csv_path = os.path.join(project_root, PATH_file_contar_alumnos_por_escuela_group)
    alumnos_por_escuela_y_curso = u.cargar_csv(csv_path)

    data = generar_condiciones_personalizadas(alumnos_por_escuela_y_curso)
    
    print(json.dumps(
        data,
        indent=4,
        ensure_ascii=False))
    
    print('...fin..!')
