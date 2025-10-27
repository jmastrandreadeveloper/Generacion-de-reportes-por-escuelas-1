# esta utilidad sirve para leer un archivo JSON para poder generar un reporte PDF

# Importar librerías
import os
import sys
import json
import ast  # Para convertir strings en diccionarios

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'  ))
sys.path.append(project_root)

import json
import src.tools.prettyJSON as pJ

def leer_JSON(ruta_archivo_JSON):    

    # Leer el archivo JSON
    with open(ruta_archivo_JSON , encoding="utf-8" )  as file:
        data = json.load(file)

    # Retornar el contenido del archivo JSON
    return data


# Llamar a la función de prueba si el script se ejecuta directamente
if __name__ == '__main__':
    print("Este script no se puede ejecutar directamente")   

    file_JSON = leer_JSON("C:/Users/w10-21h2/Documents/GitHub/python_data_analysis_v3/src/_main_/Fluidez_Lectora_medición_1/2025/05_mayo/reporte_por_escuela/reporte_por_escuela_JSON/4_Fluidez_Lectora.json")
    pJ.pretty_print_json(file_JSON)
    
    exit(1)