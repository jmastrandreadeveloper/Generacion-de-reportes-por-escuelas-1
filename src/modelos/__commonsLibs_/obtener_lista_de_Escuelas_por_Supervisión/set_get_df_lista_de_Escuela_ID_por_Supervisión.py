import pandas as pd
import os
import sys
import json

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..' ))
sys.path.append(project_root)
import src.tools.utils as u

PATH_file_lista_de_Escuelas_ID_nominal = 'data/processed/transformed/Nominal/df_nominal_df_datos_institucionales.csv'
"""
Escuela_ID;Número;Escuela;Nivel;Nivel_Unificado;Gestión;Supervisión;Departamento;Localidad;zona;AMBITO;Regional
4;1003;JUSTO JOSÉ DE URQUIZA;Primario;Primario;Pública;13 - Primario;MAIPÚ;MAIPÚ;10%;Urbano;CENTRO
"""

# Agrupa las escuelas por Supervisión, mostrando la lista de Escuela_ID
def set_df_lista_de_Escuela_ID_por_Supervisión(dataFrame):
    if 'Supervisión' not in dataFrame.columns or 'Escuela_ID' not in dataFrame.columns:
        raise ValueError("El DataFrame debe contener las columnas 'Supervisión' y 'Escuela_ID'.")

    # Agrupa por Supervisión y agrega una lista de Escuela_ID por cada una
    result_df = dataFrame.groupby('Supervisión')['Escuela_ID'].apply(list).reset_index()
    result_df.columns = ['Supervisión', 'Lista_Escuela_ID']
    return result_df

# Devuelve la lista de Escuela_ID para una Supervisión específica
def get_df_escuelas_por_supervision_con_datos(dataFrame, supervision):
    """
    Devuelve una lista de diccionarios con todos los datos de las escuelas que pertenecen a una supervisión específica.
    """
    if 'Supervisión' not in dataFrame.columns:
        raise ValueError("El DataFrame debe contener la columna 'Supervisión'.")

    # Filtrar las filas que coinciden con la supervisión indicada
    filtro = dataFrame[dataFrame['Supervisión'] == supervision]

    # Convertir el resultado a una lista de diccionarios
    return filtro.to_dict(orient='records')


# Llamar a la función de prueba si el script se ejecuta directamente
if __name__ == '__main__':
    # Ruta relativa al archivo CSV
    PATH_file_lista_de_Escuelas_ID_nominal = 'data/processed/transformed/Nominal/df_nominal_df_datos_institucionales.csv'

    # Asumo que tenés una variable definida `project_root` y una función `u.cargar_csv()`
    csv_path = os.path.join(project_root, PATH_file_lista_de_Escuelas_ID_nominal)
    dataFrame = u.cargar_csv(csv_path)

    # Supervisión a consultar (por ejemplo)
    Supervisión = '16 - Primario'

    # ✅ PRUEBA 1: Agrupar todas las supervisiones
    df_por_supervision = set_df_lista_de_Escuela_ID_por_Supervisión(dataFrame)
    print("✅ Agrupación por Supervisión:")
    print(df_por_supervision.head())

    # ✅ PRUEBA 2: Obtener lista de escuelas de una supervisión
    lista_escuelas = get_df_escuelas_por_supervision_con_datos(dataFrame, Supervisión)

    print(f"\n✅ Lista de escuelas de la supervisión '{Supervisión}':")
    print(json.dumps(lista_escuelas, indent=4, ensure_ascii=False))

    print('...fin..!')