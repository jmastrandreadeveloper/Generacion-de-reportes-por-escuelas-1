# ESTE PROGRAMA LO QUE HACE ES MIRAR EL ARCHIVO JSON DE CADA UNA DE LAS ESCUELAS
# Y MUETRA LOS DATOS CONTENIDOS EN EL ARCHIVO, LO DESEMPAQUETA

import pandas as pd
import os
import sys
import json
import ast  # Para convertir strings en diccionarios

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..' , '..' , '..', '..'))
sys.path.append(project_root)
print('project_root : ', project_root)

import src.tools.utils as u
import src.tools.prettyJSON as pJ
import src.tools.load_JSON as lJ

def obtener_listados_alumnos(datos_escuela):
    listados_alumnos = {}

    for curso, datos in datos_escuela.items():
        if isinstance(datos, dict):  # Aseguramos que sea un diccionario
            for clave, valor in datos.items():
                if clave.startswith("Listado "):  # Detectamos claves directas que comiencen con "Listado "
                    listados_alumnos.setdefault(curso, {})[clave] = valor
                
                # Caso especial: "Listado Alumnos con DESEMPEÑO"
                if clave == "Listado Alumnos con DESEMPEÑO" and isinstance(valor, dict):
                    for desempeno, alumnos in valor.items():  # Extraemos los desempeños
                        listados_alumnos.setdefault(curso, {}).setdefault(clave, {})[desempeno] = alumnos

    return listados_alumnos

# Llamar a la función de prueba si el script se ejecuta directamente
if __name__ == '__main__':    

    # leo el archivo JSON
    PATH_files_JSON = 'src/_main_/Fluidez_Lectora_medición_1/2025/05_mayo/reporte_por_escuela/reporte_por_escuela_JSON/4_1003_Fluidez_Lectora_Op_1_2025.json'
    file_JSON = lJ.leer_JSON(os.path.join(project_root, PATH_files_JSON))

    # desempaquetar el archivo JSON    
    #pJ.pretty_print_json(file_JSON)
    # Obtener el ID de la escuela (es la única clave en el JSON)
    escuela_id = list(file_JSON.keys())[0]
    escuela_data = file_JSON[escuela_id]

    # Datos Institucionales
    print(f"\n🔹 Escuela ID: {escuela_id}")
    print(f"Número: {escuela_data['datos_institucionales']['Número']}")
    print(f"Nombre: {escuela_data['datos_institucionales']['Escuela']}")
    print(f"Nivel: {escuela_data['datos_institucionales']['Nivel']}")
    print(f"Gestión: {escuela_data['datos_institucionales']['Gestión']}")
    print(f"Localidad: {escuela_data['datos_institucionales']['Localidad']}")
    print(f"Supervisión: {escuela_data['datos_institucionales']['Supervisión']}")    
    

    # Listado de cursos normalizados
    print("\n📌 Cursos Normalizados:")
    for curso in escuela_data["lista_de_CURSOS_NORMALIZADOS"]:
        print(f"- {curso}")

    # Listado de cursos analizados
    print("\n📌 Cursos Con Dato:")
    for curso in escuela_data["lista_de_CURSOS_NORMALIZADOS_con_datos"]:
        print(f"- {curso}")

    # Tabla de datos de estudiantes por curso
    print("\n📊 Datos de alumnos por curso:")
    for curso_data in escuela_data["tabla_data_dict_totalidad_de_estudiantes_por_curso"]:
        print(f"\nCurso: {curso_data['Cursos']}")
        print(f"  - Alumnos por curso: {curso_data['Alumnos por curso']}")
        print(f"  - Con desempeño: {curso_data['Alumnos con DESEMPEÑO']}")
        print(f"  - Sin desempeño: {curso_data['Alumnos sin DESEMPEÑO']}")
        print(f"  - Alumnos incluidos NO: {curso_data['Alumnos incluidos NO']}")
        print(f"  - Alumnos incluidos SI: {curso_data['Alumnos incluidos SI']}")

    
    # Porcentaje de carga regitrada
    print("\n📌 Porcentaje de carga regitrada:")
    print(f"Porcentaje de carga regitrada: {escuela_data['porcentaje_de_carga_registrada']}")
    
    # Datos de desempeño por curso (si existen)
    print("\n📈 Desempeño por curso:")
    for curso in escuela_data["lista_de_CURSOS_NORMALIZADOS"]:
        if curso in escuela_data:
            print(f"\n🔸 Curso: {curso}")
            print(escuela_data[curso]['Título_1_resultado_por_grado_curso'])
            print(escuela_data[curso]['Título_2_porcentaje_por_grado_curso'])
            # los porcentajes de estudiantes del curso por nivel de desempeño según medición
            for nivel in escuela_data[curso]["porcentaje_de_estudiantes_del_curso_por_nivel_de_desempeño_según_medición"]:
                print(f"  - {nivel['Niveles de Desempeño']}:")
                print(f"    Primera Medición 2024: {nivel['Primera Medición 2024']}")
                print(f"    Primera Medición 2025: {nivel['Primera Medición 2025']}")
            # las cantidad de estudiantes del curso por nivel de desempeño según medición
            print(escuela_data[curso]['Título_3_cantidad_por_grado_curso'])
            for nivel in escuela_data[curso]["cantidad_de_estudiantes_del_curso_por_nivel_de_desempeño_según_medición"]:
                print(f"  - {nivel['Niveles de Desempeño']}:")
                print(f"    Primera Medición 2024: {nivel['Primera Medición 2024']}")
                print(f"    Primera Medición 2025: {nivel['Primera Medición 2025']}")
    
    
    # Los listados de alumnos
    print("\n📌 Listados de alumnos:")    
    listados = obtener_listados_alumnos(escuela_data)
    # Mostrar los listados encontrados
    for curso, listados_curso in listados.items():
        print(f"Curso: {curso}")
        for tipo_listado, alumnos in listados_curso.items():
            if isinstance(alumnos, dict):  # Para los desempeños dentro de "Listado Alumnos con DESEMPEÑO"
                print(f"  {tipo_listado}:")
                for desempeno, lista in alumnos.items():
                    print(f"    {desempeno}: ")
                    for alumno in lista:
                        print(f"      - {alumno}")
            else:
                print(f"  {tipo_listado}: ")
                for alumno in alumnos:
                    print(f"    - {alumno}")
    
    
    

    exit(1)