import os
import pandas as pd
import sys
# Agregar la ruta base al sys.path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)
import src.tools.utils as u

def cargar_csv(filename):
    filepath = os.path.join(os.path.dirname(__file__), '..' , 'data', 'raw', filename)
    filepath = clean_path(filepath)
    # Verifica que el archivo exista
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"No se encontró el archivo: {filepath}")        
    return u.quitar_retorno_de_columnas(pd.read_csv(filepath , header=0 , delimiter=";" , encoding = "UTF-8" , lineterminator = '\n'))

def load_excel(filename):
    filepath = os.path.join(os.path.dirname(__file__), '..' , 'data', 'raw', filename)
    filepath = clean_path(filepath)
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"No se encontró el archivo: {filepath}")
    return pd.read_excel(filepath)

def clean_path(path):
    # Divide la ruta en componentes
    parts = path.split(os.sep)    
    # Elimina cualquier componente que sea 'tools'
    cleaned_parts = [part for part in parts if part != 'tools']    
    # Vuelve a ensamblar la ruta
    cleaned_path = os.sep.join(cleaned_parts)    
    return cleaned_path