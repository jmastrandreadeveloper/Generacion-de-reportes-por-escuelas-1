import os
#from PIL import Image
import csv
import pandas       as pd
import csv
import json
import numpy
import sys


#BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')) #os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')) #os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
#print('----- : ' , BASE_DIR)
#BASE_DIR = os.path.normpath(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')))

BASE_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', ))

# Agregar la ruta base al sys.path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
print('BASE_DIR -------------> ', BASE_DIR)

if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

#BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', ))
#BASE_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', ))
#BASE_DIR = BASE_DIR.replace("\\", "/")
        

def quitar_retorno_de_columnas(dataframe):
    # Quitar '\r' de los nombres de las columnas
    dataframe.columns = [c.replace('\r', '') for c in dataframe.columns]    
    # Obtener el nombre de la última columna
    ultima_columna = dataframe.columns[-1]    
    # Quitar '\r' de los datos de la última columna
    dataframe[ultima_columna] = dataframe[ultima_columna].apply(lambda x: x.replace('\r', '') if isinstance(x, str) else x)    
    return dataframe

def guardar_lista_bidimensional_en_csv(lista, nombre_archivo):
    with open(BASE_DIR + nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
        writer = csv.writer(archivo_csv)
        # Escribe cada sublista como una fila
        writer.writerows(lista)

def guardar_lista_simple_en_csv(lista, nombre_archivo):
    with open(BASE_DIR + nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
        writer = csv.writer(archivo_csv)
        # Escribe cada elemento en una fila
        for item in lista:
            writer.writerow([item])

def leer_lista_simple_desde_csv(nombre_archivo):
    lista = []
    with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as archivo_csv:
        reader = csv.reader(archivo_csv)
        for row in reader:
            # Agrega solo el primer elemento de cada fila a la lista
            lista.append(row[0])
    return lista

def leer_lista_bidimensional_desde_csv(nombre_archivo):
    lista = []
    with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as archivo_csv:
        reader = csv.reader(archivo_csv)
        for row in reader:
            # Agrega cada fila como una lista
            lista.append(row)
    return lista

def guardar_dataframe_a_csv_(dataframe, filepath):
    try:
        dict = {
            'sep' : ';' ,
            'encoding' : 'UTF-8' , 
            'lineterminator' : '' # 'lineterminator' : '\n'
        }
        dataframe = quitar_retorno_de_columnas(dataframe)
        
        # dataframe.to_csv(
        #     f'{filepath}',
        #     sep = dict.get('sep') , encoding = dict.get('encoding') , lineterminator=dict.get('lineterminator'),            
        #     #quoting=csv.QUOTE_ALL,
        #     index=False,
        #     header=True
        # )
        dataframe.to_csv(
            f'{BASE_DIR+filepath}',
            sep = dict.get('sep') , encoding = dict.get('encoding') ,#, line_terminator = dict.get('lineterminator'),
            #quoting=csv.QUOTE_ALL,
            index=False,
            header=True
        )
    except:
        print('..check nombre de archivo o espacio en disco..!' , f'{BASE_DIR+filepath}')
    else:        
        print('..archivo ', f'{BASE_DIR+filepath}' ,' grabado..!')
    return

# def guardar_dataframe_a_csv(dataframe, filepath):
#     try:
#         config = {
#             'sep': ';',
#             'encoding': 'UTF-8'
#         }
        
#         dataframe = quitar_retorno_de_columnas(dataframe)
#         full_path = os.path.join(BASE_DIR, filepath)
        
#         # Guardar el DataFrame en CSV
#         dataframe.to_csv(
#             f'{BASE_DIR+filepath}',
#             sep=config.get('sep'),
#             encoding=config.get('encoding'),
#             index=False,
#             header=True
#         )
        
#         # Eliminar última línea vacía si está presente
#         with open(f'{BASE_DIR+filepath}', "r", encoding=config.get('encoding')) as f:
#             lines = f.readlines()
        
#         if lines and lines[-1].strip() == "":  # Verifica si la última línea está vacía
#             with open(f'{BASE_DIR+filepath}', "w", encoding=config.get('encoding')) as f:
#                 f.writelines(lines[:-1])
        
#     except Exception as e:
#         #print(f'..check nombre de archivo o espacio en disco..! {f'{BASE_DIR+filepath}'} | Error: {e}')
#         print(f'..check nombre de archivo o espacio en disco..! {BASE_DIR+filepath} | Error: {e}')
#     else:
#         #print(f'..archivo {f'{BASE_DIR+filepath}'} grabado..!')
#         print(f'..check nombre de archivo o espacio en disco..! {BASE_DIR+filepath} | Error: {e}')

    
#     return

def guardar_dataframe_a_csv(dataframe, filepath):
    try:
        config = {
            'sep': ';',
            #'encoding': 'UTF-8'
            'encoding': 'utf-8-sig'
        }
        
        dataframe = quitar_retorno_de_columnas(dataframe)
        full_path = os.path.join(BASE_DIR, filepath)
        
        # Guardar el DataFrame en CSV
        dataframe.to_csv(
            f'{BASE_DIR+filepath}',
            sep=config.get('sep'),
            encoding=config.get('encoding'),
            index=False,
            header=True
        )
        
        # Eliminar última línea vacía si está presente
        with open(f'{BASE_DIR+filepath}', "r", encoding=config.get('encoding')) as f:
            lines = f.readlines()
        
        if lines and lines[-1].strip() == "":  # Verifica si la última línea está vacía
            with open(f'{BASE_DIR+filepath}', "w", encoding=config.get('encoding')) as f:
                f.writelines(lines[:-1])
        
    except Exception as e:
        print(f'..check nombre de archivo o espacio en disco..! {BASE_DIR+filepath} | Error: {e}')
    
    # Mensaje de éxito fuera del bloque try-except
    else:
        print(f'..archivo {BASE_DIR+filepath} grabado correctamente..!')

    return

import os

def guardar_dataframe_a_csv_2(dataframe, filepath, sep=';', encoding='utf-8-sig'):
    """
    Guarda un DataFrame como archivo CSV con opciones de codificación y separador configurables.

    Parámetros:
    - dataframe: DataFrame de pandas a guardar.
    - filepath: Ruta relativa del archivo CSV.
    - sep: Separador de columnas en el CSV. Default: ';'
    - encoding: Codificación del archivo. Default: 'utf-8-sig' (recomendado para Excel).
    """
    try:
        dataframe = quitar_retorno_de_columnas(dataframe)
        full_path = os.path.join(BASE_DIR, filepath)

        # Guardar el DataFrame en CSV
        dataframe.to_csv(
            full_path,
            sep=sep,
            encoding=encoding,
            index=False,
            header=True
        )

        # Eliminar última línea vacía si está presente
        
        with open(f'{BASE_DIR+filepath}', "r", encoding=encoding) as f:
            lines = f.readlines()

        if lines and lines[-1].strip() == "":
            with open(f'{BASE_DIR+filepath}', "w", encoding=encoding) as f:
                f.writelines(lines[:-1])

    except Exception as e:
        print(f'..check nombre de archivo o espacio en disco..! {BASE_DIR+filepath} | Error: {e}')
    else:
        print(f'..archivo {BASE_DIR+filepath} grabado correctamente..!')

    return

import os

def guardar_dataframe_a_csv_3(dataframe, filepath, sep=';', encoding='utf-8-sig'):
    """
    Guarda un DataFrame como archivo CSV con opciones de codificación y separador configurables.

    Parámetros:
    - dataframe: DataFrame de pandas a guardar.
    - filepath: Ruta relativa del archivo CSV.
    - sep: Separador de columnas en el CSV. Default: ';'
    - encoding: Codificación del archivo. Default: 'utf-8-sig' (recomendado para Excel).
    """
    try:
        dataframe = quitar_retorno_de_columnas(dataframe)
        full_path = os.path.join(BASE_DIR, filepath)

        # Guardar el DataFrame en CSV
        dataframe.to_csv(
            full_path,
            sep=sep,
            encoding=encoding,
            index=False,
            header=True
        )

        # Eliminar última línea vacía si está presente
        with open(full_path, "r", encoding=encoding) as f:
            lines = f.readlines()

        if lines and lines[-1].strip() == "":
            with open(full_path, "w", encoding=encoding) as f:
                f.writelines(lines[:-1])

    except Exception as e:
        print(f'..check nombre de archivo o espacio en disco..! {full_path} | Error: {e}')
    else:
        print(f'..archivo {full_path} grabado correctamente..!')

    return

def verificar_archivo(filename):
    """
    Verifica si un archivo existe en disco dentro de la carpeta 'data/raw'.
    
    Parámetros:
        filename (str): Nombre del archivo a verificar.
    
    Retorna:
        bool: True si el archivo existe, False en caso contrario.
    """
    # Construir ruta completa como en cargar_csv
    filepath = os.path.join(os.path.dirname(__file__), 'data', 'raw', filename)
    filepath = clean_path(filepath)

    print('filepath -------------> ', filepath)
    print('   ')

    # Quitar "src\" de la cadena de texto (igual que en cargar_csv)
    ruta_modificada = filepath.replace("src\\", "")

    # Verificar existencia
    if os.path.exists(ruta_modificada):
        print(f"✅ El archivo existe: {ruta_modificada}")
        return True
    else:
        print(f"❌ El archivo NO existe: {ruta_modificada}")
        return False


def cargar_csv(filename):
    filepath = os.path.join(os.path.dirname(__file__),   'data', 'raw', filename)
    filepath = clean_path(filepath)
    print('filepath -------------> ' , filepath)
    print('   ')
    # quito el src de la cadena de texto del filepath
    ruta_modificada = filepath.replace("src\\", "")
    # Verifica que el archivo exista
    if not os.path.exists(ruta_modificada):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_modificada}")        
    return quitar_retorno_de_columnas(pd.read_csv(ruta_modificada , header=0 , delimiter=";" , encoding = "UTF-8" , lineterminator = '\n'))

def cargar_csv_2(filename):
    #filepath = filename # os.path.join(os.path.dirname(__file__),   'data', 'raw', filename)
    #filepath = clean_path(filepath)
    print('filepath -------------> ' , filename)
    print('   ')
    # Verifica que el archivo exista
    if not os.path.exists(filename):
        raise FileNotFoundError(f"No se encontró el archivo: {filename}")        
    return quitar_retorno_de_columnas(pd.read_csv(filename , header=0 , delimiter=";" , encoding = "UTF-8" , lineterminator = '\n'))

def load_excel(filename):
    filepath = os.path.join(os.path.dirname(__file__),  'data', 'raw', filename)
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


def default_converter(o):
    if isinstance(o, numpy.int64): return int(o)  
    raise TypeError

def save_json(diccionario, filepath):
    """
    Función para grabar un diccionario en un archivo JSON.

    :param diccionario: Diccionario a grabar.
    :param nombre_archivo: Nombre del archivo de destino.
    """
    try:
        # Abriendo el archivo en modo escritura.
        with open(BASE_DIR+filepath, 'w', encoding='utf-8') as archivo:
            # Serializando el diccionario y escribiéndolo en el archivo.
            json.dump(diccionario, archivo, indent=4, ensure_ascii=False, default=default_converter)
        print(f"Archivo '{BASE_DIR+filepath}' grabado con éxito.")
    except TypeError as e:
        # Manejo de errores si hay algún problema durante la serialización.
        print(f"Error al grabar el archivo: {e}")
    except Exception as e:
        # Manejo de cualquier otro error.
        print(f"Ocurrió un error: {e}")


def load_json(filepath):
    """
    Función para leer un archivo JSON y devolverlo como diccionario.

    :param filepath: Ruta del archivo JSON a leer (relativa a BASE_DIR).
    :return: Diccionario con los datos del archivo JSON.
    """
    try:
        full_path = os.path.join(BASE_DIR, filepath)

        with open(full_path, 'r', encoding='utf-8') as archivo:
            data = json.load(archivo)

        print(f"Archivo '{full_path}' cargado con éxito.")
        return data

    except FileNotFoundError:
        print(f"Error: El archivo '{full_path}' no existe.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error al decodificar el archivo JSON: {e}")
        return None
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None