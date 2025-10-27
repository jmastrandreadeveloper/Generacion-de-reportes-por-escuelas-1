"""
import pandas as pd
import os
import sys
import json

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..' ))
sys.path.append(project_root)
import src.tools.utils as u
import src.modelos.Libs.validar_columna as valCols
from  src.modelos.Libs.filtrado_condicional import aplicar_condiciones_avanzadas

# Llamar a la función de prueba si el script se ejecuta directamente
if __name__ == '__main__':
    Escuela_ID = 9  # Reemplaza con un ID de escuela válido
    PATH_file_contar_alumnos_por_escuela_group = 'data/processed/transformed/Fluidez/df_Fluidez_1_contar_alumnos_por_escuela_y_curso_group.csv'
    csv_path = os.path.join(project_root, PATH_file_contar_alumnos_por_escuela_group)
    alumnos_por_escuela_y_curso = u.cargar_csv(csv_path)
    
    # declaro algunas condiciones adicionales para el filtrado final
    condiciones = {
        "CURSO_NORMALIZADO": ["2°", "5°"],  # Cursos 4° o 5°
        "matricula_por_curso": {"range": [130, 140]},  # Entre 130 y 140
        "AND": False  # Lógica AND ,  "AND": False  # Lógica OR
    }

    data = ___group_contar_alumnos_por_escuela_y_curso______filter(
        Escuela_ID, # la clave a buscar
        alumnos_por_escuela_y_curso, # el dataframe
        True, # se resetea el índice ? 
        ['CURSO_NORMALIZADO', 'matricula_por_curso' , ], # qué columnas quiero mostrar 
        'records', # Opciones: 'dict', 'list', 'series', 'split', 'records', 'index'
        condiciones=condiciones # le paso condiciones adicionales al resultado final
    )
    
    print(json.dumps(
        data,
        indent=4,
        ensure_ascii=False))
    
    print('...fin..!')
"""