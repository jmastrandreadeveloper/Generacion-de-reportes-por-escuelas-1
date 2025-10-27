import pandas as pd
import sys
import os
# Añadir la raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.tools.utils import cargar_csv

print('\n')
# Creación de un DataFrame desde un archivo CSV
# Los archivos CSV son una fuente común de datos. Puedes crear un DataFrame leyendo un archivo CSV.
print('Leer un archivo CSV para crear un DataFrame')
# Carga de datos
df = cargar_csv('demo_data_000.csv')
# Mostrar el DataFrame
print(df,'\n')