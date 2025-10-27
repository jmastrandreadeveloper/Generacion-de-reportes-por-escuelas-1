
import os
import sys
import json

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..' ))
sys.path.append(project_root)

import numpy as np
import src.tools.utils as u

def generar_condiciones_personalizadas_extendido(dataframe, reglas=None, max_categorias=10, rango_percentil=(0.05, 0.95)):
    """
    Genera un diccionario de condiciones avanzadas basado en las columnas y datos del DataFrame,
    con soporte extendido para múltiples tipos y reglas dinámicas.
    """
    condiciones = {}

    for columna in dataframe.columns:
        regla = reglas.get(columna, {}) if reglas else {}
        tipo_dato = regla.get("tipo", None)
        dtype = dataframe[columna].dtype

        if not tipo_dato:
            if dtype in ['object', 'category', 'bool']:
                tipo_dato = "categorico"
            elif np.issubdtype(dtype, np.number):
                tipo_dato = "numerico"
            elif np.issubdtype(dtype, np.datetime64):
                tipo_dato = "fecha"

        # Configuración de reglas extendidas por tipo
        if tipo_dato == "categorico":
            valores_unicos = dataframe[columna].dropna().unique()
            condiciones[columna] = {
                "in": regla.get("in", list(valores_unicos)),
                "not_in": regla.get("not_in", []),
                "contiene": regla.get("contiene", None),
                "no_contiene": regla.get("no_contiene", None),
                "empieza_con": regla.get("empieza_con", None),
                "termina_con": regla.get("termina_con", None),
            }

        elif tipo_dato == "numerico":
            percentiles = regla.get("percentiles", rango_percentil)
            min_val = dataframe[columna].quantile(percentiles[0])
            max_val = dataframe[columna].quantile(percentiles[1])
            condiciones[columna] = {
                "range": regla.get("rango_personalizado", [min_val, max_val]),
                "not_in": regla.get("excluir", [])
            }

        elif tipo_dato == "fecha":
            min_date = dataframe[columna].min()
            max_date = dataframe[columna].max()
            condiciones[columna] = {
                "range": regla.get("rango_personalizado", [min_date, max_date]),
            }

        elif tipo_dato == "booleano":
            condiciones[columna] = {
                "is_true": regla.get("is_true", True),
                "is_false": regla.get("is_false", False),
            }

        condiciones[columna]["is_null"] = regla.get("incluir_nulos", False)
        condiciones[columna]["not_null"] = regla.get("excluir_nulos", True)

    condiciones["AND"] = True
    return condiciones


def aplicar_filtro_avanzado_extendido(dataframe, condiciones):
    """
    Aplica condiciones avanzadas extendidas de filtrado en un DataFrame.

    Args:
        dataframe (pd.DataFrame): DataFrame de entrada.
        condiciones (dict): Diccionario con las condiciones a aplicar.

    Returns:
        pd.DataFrame: DataFrame filtrado.
    """
    logic_and = condiciones.pop("AND", True)
    filtros = []

    for columna, criterio in condiciones.items():
        if columna not in dataframe.columns:
            raise ValueError(f"La columna '{columna}' no existe en el DataFrame.")

        if "in" in criterio:
            filtros.append(dataframe[columna].isin(criterio["in"]))
        if "not_in" in criterio:
            filtros.append(~dataframe[columna].isin(criterio["not_in"]))
        if "range" in criterio:
            min_val, max_val = criterio["range"]
            filtros.append(dataframe[columna].between(min_val, max_val))
        if "contiene" in criterio and criterio["contiene"]:
            filtros.append(dataframe[columna].str.contains(criterio["contiene"], na=False))
        if "no_contiene" in criterio and criterio["no_contiene"]:
            filtros.append(~dataframe[columna].str.contains(criterio["no_contiene"], na=False))
        if "empieza_con" in criterio and criterio["empieza_con"]:
            filtros.append(dataframe[columna].str.startswith(criterio["empieza_con"], na=False))
        if "termina_con" in criterio and criterio["termina_con"]:
            filtros.append(dataframe[columna].str.endswith(criterio["termina_con"], na=False))
        if criterio.get("is_true"):
            filtros.append(dataframe[columna] == True)
        if criterio.get("is_false"):
            filtros.append(dataframe[columna] == False)
        if criterio.get("is_null"):
            filtros.append(dataframe[columna].isnull())
        if criterio.get("not_null"):
            filtros.append(dataframe[columna].notnull())

    if logic_and:
        return dataframe[np.logical_and.reduce(filtros)]
    else:
        return dataframe[np.logical_or.reduce(filtros)]


if __name__ == '__main__':    
    PATH_file_contar_alumnos_por_escuela_group = 'data/processed/transformed/Fluidez/dataframe_FL_1_contar_alumnos_por_escuela_y_curso_group.csv'
    csv_path = os.path.join(project_root, PATH_file_contar_alumnos_por_escuela_group)
    alumnos_por_escuela_y_curso = u.cargar_csv(csv_path)

    # reglas_personalizadas = generar_reglas_interactivas(alumnos_por_escuela_y_curso)
    # condiciones = generar_condiciones_personalizadas(alumnos_por_escuela_y_curso, reglas=reglas_personalizadas)

    reglas_personalizadas = {
        "CURSO_NORMALIZADO": {
            "in": ["4°", "5°"],
            "contiene": "°"
        },
        "matricula_por_curso": {
            "range": [50, 200]
        },
        "activo": {
            "is_true": True
        }
    }

    # Generar condiciones avanzadas
    condiciones = generar_condiciones_personalizadas_extendido(alumnos_por_escuela_y_curso, reglas=reglas_personalizadas)

    # Filtrar DataFrame
    df_filtrado = aplicar_filtro_avanzado_extendido(alumnos_por_escuela_y_curso, condiciones)
    print(df_filtrado)

    print(json.dumps(
        condiciones,
        indent=4,
        ensure_ascii=False))
    
    print('...fin..!')
