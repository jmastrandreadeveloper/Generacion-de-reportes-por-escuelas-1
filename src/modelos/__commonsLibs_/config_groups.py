# ESTA FUNCIÓN SE DEBE EJECUTAR DENTRO DE LAS CARPETAS PREPARADAS PARA PODER CONTENER LAS CARPETAS CON LOS AGRUPAMIENTOS 
# Y FILTROS NECESARIOS, NO EJECUTARLA EN CUALQUIER PARTE PORQUE VA A DEJAR LA CARPETA RESULTANTE EN CUALQUIER LADO

import os
import sys

# Añadir el directorio raíz del proyecto al sys.path para poder importar módulos desde 'src'
# Asume que este archivo está en 'src/modelos/Libs_GroupAgg_And_Filterring/' y que 'src' está en el directorio raíz.
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(project_root)
from src.tools.generate_group_V2 import generate_group_aggregation_functions_V2

# Crear el diccionario de parámetros de agrupación
group_params_dict = {
    'contar_alumnos_por_escuela_____': (
        ['Escuela_ID', 'Alumno_ID'],
        {'count': 'Alumno_ID'},
        {"rename_columns": {"Alumno_ID": "matricula_por_escuela"}},
        {"filter": ['Escuela_ID']}  
    ),
    'contar_alumnos_por_escuela_y_curso_____': (
        ['Escuela_ID', 'CURSO_NORMALIZADO', 'Alumno_ID'],
        {'count': 'Alumno_ID'},
        {"rename_columns": {"Alumno_ID": "matricula_por_escuela_y_curso"}},
        {"filter": ['Escuela_ID']}
    ),
    'contar_alumnos_por_escuela_curso_y_division_____': (
        ['Escuela_ID', 'CURSO_NORMALIZADO' , 'División', 'Alumno_ID'],
        {'count': 'Alumno_ID'},
        {"rename_columns": {"Alumno_ID": "matricula_por_escuela_curso_y_division"}},
        {"filter": ['Escuela_ID']}
     ),
    'contar_alumnos_por_nivel_y_curso_____':(
        ['Nivel_Unificado', 'CURSO_NORMALIZADO', 'Alumno_ID'],
        {'count': 'Alumno_ID'},
        {"rename_columns": {"Alumno_ID": "matricula_por_nivel_y_curso"}},
        {"filter": ['CURSO_NORMALIZADO']}         
     ),
    'contar_alumnos_por_supervisión_y_curso_____':(
        ['Supervisión', 'CURSO_NORMALIZADO', 'Alumno_ID'],
        {'count': 'Alumno_ID'},
        {"rename_columns": {"Alumno_ID": "matricula_por_supervisión_y_curso"}},
        {"filter": ['CURSO_NORMALIZADO']}         
     )
}
generate_group_aggregation_functions_V2(group_params_dict, os.path.dirname(os.path.abspath(__file__)))