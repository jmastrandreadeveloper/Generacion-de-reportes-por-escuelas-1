import pandas as pd
import os
import sys
import json

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..' ))
sys.path.append(project_root)
import src.tools.utils as u

PATH_file_lista_de_Escuelas_ID_nominal = 'data/processed/transformed/Nominal/df_nominal_df_datos_institucionales.csv'

def set_df_lista_de_Supervisiones(processed_dataframe, nombre_operativo):
    # Verificar si la columna 'Supervisión' existe en el DataFrame
    if 'Supervisión' not in processed_dataframe.columns:
        raise ValueError("La columna 'Supervisión' no existe en el DataFrame.")
    
    # Agrupar las 'Supervisión' en una lista única, ordenada alfabéticamente
    lista_supervisiones = sorted(set(processed_dataframe['Supervisión']))

    # Crear un nuevo DataFrame con las columnas solicitadas
    result_df = pd.DataFrame({
        'Operativo': [nombre_operativo],
        'Supervisión': [lista_supervisiones]
    })

    return result_df

def get_df_lista_de_Supervisiones(df, nombre_operativo):
    # Filtrar el DataFrame por el nombre del operativo
    df_filtrado = df[df['Operativo'] == nombre_operativo]
    
    if not df_filtrado.empty:
        lista_superv = df_filtrado['Supervisión'].values[0]
        # Asegurarse de que el valor sea una lista
        if isinstance(lista_superv, str):
            lista_superv = eval(lista_superv)
        return lista_superv
    else:
        raise ValueError(f"No se encontró el operativo '{nombre_operativo}' en el DataFrame.")


# Llamar a la función de prueba si el script se ejecuta directamente
if __name__ == '__main__':
    # Ruta relativa al archivo CSV
    PATH_file_lista_de_Escuelas_ID_nominal = 'data/processed/transformed/Nominal/df_nominal_datos_institucionales_Lista_de_Supervisiones.csv'

    # Asumo que tenés una variable definida `project_root` y una función `u.cargar_csv()`
    csv_path = os.path.join(project_root, PATH_file_lista_de_Escuelas_ID_nominal)
    dataFrame = u.cargar_csv(csv_path)

    # Generar el dataframe con supervisiones
    df_supervisiones = set_df_lista_de_Supervisiones(dataFrame, "df_nominal")

    # Recuperar la lista
    lista = get_df_lista_de_Supervisiones(df_supervisiones, "df_nominal")
    print(lista[0])

    print('...fin..!')



# # Cargar tu DataFrame desde CSV si es necesario:
# df = pd.read_csv("tu_archivo.csv", sep=';')  # asumiendo que está separado por punto y coma

# # Generar el dataframe con supervisiones
# df_supervisiones = set_df_lista_de_Supervisiones(df, "Operativo_2024")

# # Recuperar la lista
# lista = get_df_lista_de_Supervisiones(df_supervisiones, "Operativo_2024")
# print(lista)