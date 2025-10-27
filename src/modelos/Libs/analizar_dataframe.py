
import os
import sys
import json

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..' ))
sys.path.append(project_root)

import numpy as np
import src.tools.utils as u

def generar_condiciones_avanzadas_desde_dataframe(dataframe, max_categorias=10, rango_percentil=(0.05, 0.95)):
    """
    Genera un diccionario de condiciones avanzadas basado en las columnas y datos del DataFrame.

    Args:
        dataframe (pd.DataFrame): DataFrame de entrada.
        max_categorias (int): Número máximo de categorías únicas para considerar una columna como categórica.
        rango_percentil (tuple): Percentiles (mínimo y máximo) para calcular el rango de condiciones numéricas.

    Returns:
        dict: Diccionario de condiciones avanzadas basado en el contenido del DataFrame.
    """
    condiciones = {}

    for columna in dataframe.columns:
        dtype = dataframe[columna].dtype
        
        # Condiciones para columnas categóricas o de texto
        if dtype in ['object', 'category', 'bool']:
            valores_unicos = dataframe[columna].dropna().unique()
            if len(valores_unicos) <= max_categorias:
                condiciones[columna] = {
                    "in": list(valores_unicos),  # Valores permitidos
                    "not_in": []                # Valores excluidos
                }
        
        # Condiciones para columnas numéricas
        elif np.issubdtype(dtype, np.number):
            min_val = dataframe[columna].quantile(rango_percentil[0])
            max_val = dataframe[columna].quantile(rango_percentil[1])
            condiciones[columna] = {
                "range": [min_val, max_val],  # Rango de valores
                "not_in": []                 # Valores excluidos
            }
        
        # Condiciones para columnas de fecha
        elif np.issubdtype(dtype, np.datetime64):
            min_date = dataframe[columna].min()
            max_date = dataframe[columna].max()
            condiciones[columna] = {
                "range": [min_date, max_date],  # Rango de fechas
                "not_in": []                   # Fechas excluidas
            }
        
        # Valores faltantes
        condiciones[columna]["is_null"] = False  # Incluir valores nulos
        condiciones[columna]["not_null"] = True  # Excluir valores nulos

    # Lógica combinada por defecto
    condiciones["AND"] = True
    return condiciones

if __name__ == '__main__':    
    PATH_file_contar_alumnos_por_escuela_group = 'data/processed/transformed/Fluidez/dataframe_FL_1_contar_alumnos_por_escuela_y_curso_group.csv'
    csv_path = os.path.join(project_root, PATH_file_contar_alumnos_por_escuela_group)
    alumnos_por_escuela_y_curso = u.cargar_csv(csv_path)

    data = generar_condiciones_avanzadas_desde_dataframe(alumnos_por_escuela_y_curso)
    
    print(json.dumps(
        data,
        indent=4,
        ensure_ascii=False))
    
    print('...fin..!')

    

