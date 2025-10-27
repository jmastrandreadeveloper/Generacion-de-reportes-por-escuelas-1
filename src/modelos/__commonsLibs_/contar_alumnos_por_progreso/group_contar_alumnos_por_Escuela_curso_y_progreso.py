# esta función cuenta la cantidad de alumnos por escuela, curso y progreso
# se usa para generar el reporte por escuela en formato JSON
import pandas as pd
import os
import sys
import json

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..' ))
sys.path.append(project_root)
import src.tools.utils as u
import src.modelos.Libs.validar_columna as valCols
from  src.modelos.Libs.filtrado_condicional import aplicar_condiciones_avanzadas

def contar_alumnos_por_escuela_curso_y_progreso_group(dataframe):
    required_columns = ['Escuela_ID', 'Curso ', 'compara', 'Alumno_ID']
    # Validar las columnas requeridas
    missing_columns = valCols.validar_columnas(dataframe, required_columns)
    missing_columns = [col for col in required_columns if col not in dataframe.columns]
    if not missing_columns:
        result = dataframe.groupby(['Escuela_ID', 'Curso ', 'compara']).agg({'Alumno_ID': 'count'})
        # renombrar todo acá !!
        result.rename(columns={'Alumno_ID':'matricula_por_escuela_curso_y_progreso'},inplace = True) 
        result.reset_index(inplace=True)
        #### renombra las columnas aquí..!!!!
        #print(df_key + 'contar_alumnos_por_escuela_y_desempeño_group.csv')
        #print(result)
        #u.guardar_dataframe_a_csv(result , PATH + df_key +'_contar_alumnos_por_escuela_y_desempeño_group.csv')
        return result
    else:
        raise ValueError(f'Las columnas especificadas no existen en el dataframe. Columnas faltantes: {missing_columns}')
    
def filtrar_alumnos_por_escuela_curso_y_progreso_group(
    Escuela_ID,
    dataframe,
    show_index,
    columns,
    orientacion='records',
    condiciones=None
):
    try:
        # Verificar si Escuela_ID existe en el DataFrame
        if Escuela_ID not in dataframe['Escuela_ID'].unique():
            # Si no existe, devolver una fila única con ceros en todas las columnas solicitadas
            return pd.DataFrame([{col: 0 for col in columns}]).to_dict(orient=orientacion)

        # Filtrar por Escuela_ID
        dFrame_filtrado = dataframe[dataframe['Escuela_ID'] == Escuela_ID]

        # Aplicar condiciones avanzadas
        if condiciones:
            dFrame_filtrado = aplicar_condiciones_avanzadas(dFrame_filtrado, condiciones)

        # Si el resultado filtrado está vacío, devolver una fila con ceros
        if dFrame_filtrado.empty:
            return pd.DataFrame([{col: 0 for col in columns}]).to_dict(orient=orientacion)

        # Validar columnas requeridas y agregar las faltantes con valor 0
        for col in columns:
            if col not in dFrame_filtrado.columns:
                dFrame_filtrado[col] = 0

        # Seleccionar solo las columnas deseadas
        dFrame_filtrado = dFrame_filtrado[columns]

        # Eliminar índice si no es requerido
        if not show_index:
            dFrame_filtrado = dFrame_filtrado.reset_index(drop=True)

        # Convertir a JSON/diccionario
        return dFrame_filtrado.to_dict(orient=orientacion)

    except Exception as e:
        raise ValueError(f"Error al filtrar el DataFrame: {e}")
    
# Llamar a la función de prueba si el script se ejecuta directamente
if __name__ == '__main__':
    Escuela_ID = 4  # Reemplaza con un ID de escuela válido
    PATH_file_contar_alumnos_por_escuela_curso_y_progreso_group = 'data/processed/transformed/Fluidez/2025_12/_df_Cantidad_de_alumnos_por_escuela_curso_y_progreso.csv'
    csv_path = os.path.join(project_root, PATH_file_contar_alumnos_por_escuela_curso_y_progreso_group)
    alumnos_por_escuela_y_curso_y_progreso = u.cargar_csv(csv_path)
    
    # declaro algunas condiciones adicionales para el filtrado final
    condiciones = {
        "Curso ": ["5°"],  # "2°", "5°"
        "compara":  ["Bajó de nivel", "Se mantuvo" , "Subió de nivel" ,],  # solamente esos valores
        "AND": True  # Lógica AND ,  "AND": False  # Lógica OR
    }

    data = filtrar_alumnos_por_escuela_curso_y_progreso_group(
        Escuela_ID, # la clave a buscar
        alumnos_por_escuela_y_curso_y_progreso, # el dataframe
        True, # se resetea el índice ? 
        ['Escuela_ID','Curso ','compara','matricula_por_escuela_curso_y_progreso', ], # qué columnas quiero mostrar 
        'records', # Opciones: 'dict', 'list', 'series', 'split', 'records', 'index'
        condiciones=condiciones # le paso condiciones adicionales al resultado final
    )

    print(pd.DataFrame(data))
    
    print(json.dumps(
        data,
        indent=4,
        ensure_ascii=False))
    
    print('...fin..!')