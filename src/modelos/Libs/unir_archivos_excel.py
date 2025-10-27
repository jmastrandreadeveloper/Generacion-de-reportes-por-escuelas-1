import os
import pandas as pd

def unir_excels(directorio, archivo_salida="consolidado.xlsx"):
    """
    Une todos los archivos Excel de un directorio en un solo archivo.

    Parámetros:
        directorio (str): Ruta de la carpeta que contiene los archivos Excel.
        archivo_salida (str): Nombre del archivo de salida (xlsx).
    
    Retorna:
        str: Ruta del archivo consolidado generado.
    """
    archivos = [f for f in os.listdir(directorio) if f.endswith((".xlsx", ".xls"))]
    
    if not archivos:
        raise FileNotFoundError("No se encontraron archivos Excel en el directorio especificado.")

    lista_df = []

    for archivo in archivos:
        ruta_archivo = os.path.join(directorio, archivo)
        print(f"📂 Leyendo: {ruta_archivo}")
        df = pd.read_excel(ruta_archivo)
        df["Archivo_Origen"] = archivo  # opcional: para identificar el origen
        lista_df.append(df)

    # Concatenar todos los DataFrames
    df_final = pd.concat(lista_df, ignore_index=True)

    # Guardar en un único archivo Excel
    ruta_salida = os.path.join(directorio, archivo_salida)
    df_final.to_excel(ruta_salida, index=False)

    print(f"✅ Archivo consolidado creado: {ruta_salida}")
    return ruta_salida

def unir_hojas_excel(ruta_archivo, archivo_salida="consolidado_hojas.xlsx"):
    """
    Une todas las hojas de un archivo Excel en una sola hoja consolidada.

    Parámetros:
        ruta_archivo (str): Ruta del archivo Excel de origen.
        archivo_salida (str): Nombre del archivo de salida (xlsx).
    
    Retorna:
        str: Ruta del archivo consolidado generado.
    """
    # Leer todas las hojas en un diccionario {nombre_hoja: DataFrame}
    hojas = pd.read_excel(ruta_archivo, sheet_name=None)

    if not hojas:
        raise ValueError("El archivo no contiene hojas.")

    lista_df = []

    for nombre_hoja, df in hojas.items():
        print(f"📄 Leyendo hoja: {nombre_hoja}")
        df["Hoja_Origen"] = nombre_hoja  # opcional: para identificar de qué hoja viene
        lista_df.append(df)

    # Concatenar todos los DataFrames
    df_final = pd.concat(lista_df, ignore_index=True)

    # Generar ruta de salida en el mismo directorio
    directorio = os.path.dirname(ruta_archivo)
    ruta_salida = os.path.join(directorio, archivo_salida)

    # Guardar en un único archivo Excel
    df_final.to_excel(ruta_salida, index=False)

    print(f"✅ Archivo consolidado creado: {ruta_salida}")
    return ruta_salida
