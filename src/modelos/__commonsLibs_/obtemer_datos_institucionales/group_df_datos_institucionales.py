import os
import sys
import json
import pandas as pd

# Añadir el directorio raíz del proyecto al sys.path para poder importar módulos desde 'src'
# Asume que este archivo está en 'src/modelos/Libs_GroupAgg_And_Filterring/' y que 'src' está en el directorio raíz.
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..' ))
sys.path.append(project_root)


# Ahora que el directorio raíz está en el path, intenta importar el módulo
#import src.tools.data_loading as u
import src.tools.utils as u

def group_df_datos_institucionales(dataframe, as_json=True):
    """
    Agrupa el DataFrame por 'Escuela_ID' y devuelve los datos institucionales en dos formatos:

    - Si as_json=True: Devuelve 'datos_institucionales' como un JSON en formato string (con comillas dobles).
    - Si as_json=False: Devuelve un DataFrame filtrado sin convertirlo a JSON.

    Parámetros:
        dataframe (pd.DataFrame): DataFrame con la información de las escuelas.
        as_json (bool, opcional): Indica si se desea devolver el resultado como JSON (True) o como DataFrame normal (False).

    Retorna:
        pd.DataFrame: DataFrame con 'Escuela_ID' y 'datos_institucionales' (si as_json=True) 
                      o un DataFrame filtrado con las columnas originales (si as_json=False).
    """
    columnas_datos = [
        'Número',
        'Escuela',
        'Nivel', 
        'Nivel_Unificado', 
        'Gestión', 
        'Supervisión', 
        'Departamento', 
        'Localidad', 
        'zona', 
        'AMBITO', 
        'Regional'
    ]

    # Si se requiere como JSON
    if as_json:
        processed_data = []

        for escuela_id, group in dataframe.groupby('Escuela_ID'):
            datos_institucionales = group[columnas_datos].iloc[0].to_dict()  # Convertir a diccionario
            datos_institucionales_json = json.dumps(datos_institucionales, ensure_ascii=False)  # Convertir a JSON string
            
            processed_data.append({
                'Escuela_ID': int(escuela_id),
                'datos_institucionales': datos_institucionales_json
            })
        
        return pd.DataFrame(processed_data)

    # Si no se requiere como JSON, devolver el DataFrame filtrado
    return dataframe[['Escuela_ID'] + columnas_datos].drop_duplicates()

def filter_datos_institucionales(Escuela_ID, df_nominal_datos_institucionales):
    """
    Filtra el DataFrame por el ID de la escuela proporcionado y devuelve los datos institucionales
    en un diccionario, ya sea que estén en formato JSON o en un DataFrame normal.

    Parámetros:
        Escuela_ID (int): ID de la escuela a buscar.
        df_nominal_datos_institucionales (pd.DataFrame): DataFrame con los datos institucionales.

    Retorna:
        dict | None: Diccionario con los datos institucionales de la escuela o None si no se encuentra.
    """
    # Filtrar el DataFrame por el ID de la escuela
    df_filtrado = df_nominal_datos_institucionales[df_nominal_datos_institucionales['Escuela_ID'] == Escuela_ID]

    # Verificar si hay datos
    if df_filtrado.empty:
        print(f"No se encontraron datos para la escuela con ID '{Escuela_ID}'.")
        return None

    # Verificar si la columna 'datos_institucionales' existe (modo JSON)
    if 'datos_institucionales' in df_filtrado.columns:
        datos_institucionales = df_filtrado.iloc[0]['datos_institucionales']

        # Intentar convertir de JSON a diccionario
        try:
            return json.loads(datos_institucionales) if isinstance(datos_institucionales, str) else datos_institucionales
        except json.JSONDecodeError:
            print(f"Error al decodificar JSON para la escuela con ID '{Escuela_ID}'.")
            return None

    # Si no existe 'datos_institucionales', devolver los datos en formato de diccionario
    return df_filtrado.iloc[0].drop('Escuela_ID').to_dict()

# Llamar a la función de prueba si el script se ejecuta directamente
if __name__ == '__main__':
    Escuela_ID = 9  # Reemplaza con un ID de escuela válido
    csv_path = os.path.join(project_root, 'data/processed/transformed/Nominal/df_nominal_df_datos_institucionales.csv')
    dataFrame = u.cargar_csv_2(csv_path)
    data = filter_datos_institucionales(Escuela_ID , dataFrame)
    
    print(json.dumps(
        data,
        indent=4,
        ensure_ascii=False))
    
    print('...fin..!')