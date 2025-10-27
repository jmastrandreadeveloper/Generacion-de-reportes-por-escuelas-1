import pandas as pd
import os
import sys
import json

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..' ))
sys.path.append(project_root)
import src.tools.utils as u

PATH_file_lista_de_Escuelas_ID_nominal = 'data/processed/transformed/Nominal/2025_04/df_nominal_datos_institucionales_Escuela_ID.csv'

def set_df_lista_de_Ecuela_ID(processed_dataframe, nombre_operativo):
    # Verificar si la columna 'Escuela_ID' existe en el DataFrame
    if 'Escuela_ID' not in processed_dataframe.columns:
        raise ValueError("La columna 'Escuela_ID' no existe en el dataframe.")
    
    # Agrupar los 'Escuela_ID' en una lista única
    escuelas_participantes = sorted(set(processed_dataframe['Escuela_ID']))
    
    # Crear un nuevo DataFrame con las columnas solicitadas
    result_df = pd.DataFrame({
        'Operativo': [nombre_operativo],
        'Escuela_ID': [escuelas_participantes]
    })
    
    return result_df

def get_df_lista_de_Ecuela_ID(df, nombre_operativo):
    # Filtrar el DataFrame por el nombre del operativo
    df_filtrado = df[df['Operativo'] == nombre_operativo]
    
    # Asegurarse de que el valor sea una lista
    if not df_filtrado.empty:
        lista_escuelas = df_filtrado['Escuela_ID'].values[0]
        # Si es una cadena (por error de carga), convierte a lista
        if isinstance(lista_escuelas, str):
            lista_escuelas = eval(lista_escuelas)
        return lista_escuelas
    else:
        raise ValueError(f"No se encontró el operativo '{nombre_operativo}' en el DataFrame.")


# Llamar a la función de prueba si el script se ejecuta directamente
if __name__ == '__main__':
    nombre_operativo = 'df_nominal'    
    csv_path = os.path.join(project_root, PATH_file_lista_de_Escuelas_ID_nominal)
    dataFrame = u.cargar_csv(csv_path)
    data = get_df_lista_de_Ecuela_ID(
        dataFrame, 
        nombre_operativo, 
    )
    
    print(json.dumps(
        data,
        indent=4,
        ensure_ascii=False))
    
    print('...fin..!')

