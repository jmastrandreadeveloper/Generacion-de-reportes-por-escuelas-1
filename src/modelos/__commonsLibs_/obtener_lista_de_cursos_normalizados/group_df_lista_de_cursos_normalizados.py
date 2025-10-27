import os
import sys
import numpy
import json

# Añadir el directorio raíz del proyecto al sys.path para poder importar módulos desde 'src'
# Asume que este archivo está en 'src/modelos/Libs_GroupAgg_And_Filterring/' y que 'src' está en el directorio raíz.
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(project_root)

# Ahora que el directorio raíz está en el path, intenta importar el módulo
import src.tools.utils as u
import pandas as pd

def group_df_lista_de_cursos_normalizados(processed_dataframe):
    required_columns = ['Escuela_ID', 'Curso ']
    missing_columns = [col for col in required_columns if col not in processed_dataframe.columns]
    if not missing_columns:
        result = processed_dataframe.groupby('Escuela_ID')['Curso '].agg(lambda x: sorted(set(x)))
        return result.reset_index()
    else:
        raise ValueError(f'Las columnas especificadas no existen en el dataframe. Columnas faltantes: {missing_columns}')
    
def filter_df_lista_de_cursos_normalizados(Escuela_ID, dFrame):
    # Filtrar el DataFrame por el Escuela_ID especificado
    df_filtrado = dFrame[dFrame['Escuela_ID'] == Escuela_ID]

    # Verificar si se encontró algún resultado
    if not df_filtrado.empty:
        # Extraer el valor de la columna 'matricula_por_curso_y_division'
        lista_de_cursos_por_Escuela_ID = df_filtrado.iloc[0]['Curso ']        
        # Si es una cadena (por error de carga), convierte a lista
        if isinstance(lista_de_cursos_por_Escuela_ID, str):
            lista_de_cursos_por_Escuela_ID = eval(lista_de_cursos_por_Escuela_ID)
        return lista_de_cursos_por_Escuela_ID
    else:
        raise ValueError(f"No se encontraron datos para la escuela con ID '{Escuela_ID}' en el DataFrame.")

def test_df_lista_de_cursos_normalizados(Escuela_ID , PATH_file):
    csv_path = os.path.join(project_root, PATH_file)
    df_matricula_por_escuela_curso_y_division = u.cargar_csv_2(csv_path)       
    # Ejecutar una prueba llamando a la función con un ID de escuela de ejemplo
    resultado = filter_df_lista_de_cursos_normalizados(Escuela_ID , df_matricula_por_escuela_curso_y_division)# , listaDeCursos.lista_de_cursos_escuela(Escuela_ID , df_lista_de_cursos_normalizados))
    print(json.dumps(resultado, indent=4, ensure_ascii=False))


# Llamar a la función de prueba si el script se ejecuta directamente
if __name__ == '__main__':
    Escuela_ID = 18  # Reemplaza con un ID de escuela válido    
    PATH_file = 'data/processed/transformed/Nominal/df_nominal_df_Escuela_ID_CURSO_NORMALIZADO_list.csv'
    test_df_lista_de_cursos_normalizados(Escuela_ID , PATH_file)