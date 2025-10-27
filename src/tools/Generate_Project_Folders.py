# esta utilidad sirve para crear la estructura de carpetas de un proyecto para análisis de datos
# la estructura de carpetas es la siguiente:
# src
# ├── _main_
# │   ├── *X*
# │   │   ├── Año_YYYY
# │   │   │   ├── mes_MM
# │   │   │   │   ├── data
# │   │   │   │   │   ├── raw
# │   │   │   │   ├──rerporte_**X**
# │   │   │   │   │   ├── PDFs_templates_**X**
# │   │   │   │   │   ├── reporte_por_**X**_JSON
# │   │   │   │   │   ├── reportes_PDFs
# │   │   │   │   │   │     ├── reportes_PDFs_buffer
# │   │   │   │   │   ├── reporte_por_**X**_JSON.py
# │   │   │   │   │   ├── reporte_por_**X**_PDFs.py
# │   │   │   │   ├──rerporte_**Y**
# │   │   │   │   │   ├── PDFs_templates_**Y**
# │   │   │   │   │   ├── reporte_por_**Y**_JSON
# │   │   │   │   │   ├── reportes_PDFs
# │   │   │   │   │   │     ├── reportes_PDFs_buffer
# │   │   │   │   │   ├── reporte_por_**Y**_JSON.py
# │   │   │   │   │   ├── reporte_por_**Y**_PDFs.py
# │   │   │   │   ├── main.py

import os

def crear_estructura_directorios(dict_definition, anio, mes):
    base_dir = os.path.dirname(os.path.abspath(__file__))  # src/_main_
    nombre_proyecto = dict_definition['*X*']
    reporte_X = dict_definition['**X**']
    reporte_Y = dict_definition['**Y**']

    # Rutas clave
    raiz_proyecto = os.path.join(base_dir, nombre_proyecto, f"Año_{anio}", f"mes_{mes}")
    data_raw = os.path.join(raiz_proyecto, "data", "raw")

    def crear_reporte_ruta(nombre_reporte):
        path_base = os.path.join(raiz_proyecto, f"rerporte_{nombre_reporte}")
        subdirs = [
            f"PDFs_templates_{nombre_reporte}",
            f"reporte_por_{nombre_reporte}_JSON",
            os.path.join("reportes_PDFs", "reportes_PDFs_buffer")
        ]
        archivos = [
            f"reporte_por_{nombre_reporte}_JSON.py",
            f"reporte_por_{nombre_reporte}_PDFs.py"
        ]
        for subdir in subdirs:
            os.makedirs(os.path.join(path_base, subdir), exist_ok=True)
        for archivo in archivos:
            ruta_archivo = os.path.join(path_base, archivo)
            with open(ruta_archivo, 'w', encoding='utf-8') as f:
                f.write("# Archivo generado automáticamente\n")

    # Crear carpetas generales
    os.makedirs(data_raw, exist_ok=True)
    crear_reporte_ruta(reporte_X)
    crear_reporte_ruta(reporte_Y)

    # Crear archivo main.py
    ruta_main_py = os.path.join(raiz_proyecto, "main.py")
    with open(ruta_main_py, 'w', encoding='utf-8') as f:
        f.write("# main.py generado automáticamente\n")

    print("✅ Estructura creada con éxito.")

# --------------------
# LLAMADA A LA FUNCIÓN
# --------------------

if __name__ == "__main__":
    dict_definition = {
        '*X*': 'Proyecto_1',
        '**X**': 'reporte_Proyecto_1_a',
        '**Y**': 'reporte_Proyecto_1_b',
    }
    anio = "2025"
    mes = "05_mayo"

    crear_estructura_directorios(dict_definition, anio, mes)



# dict_definition = {
#     "": {
#         "Año_YYYY": {
#             "mes_MM": {
#                 "data": {
#                     "raw": None
#                 },
#                 "rerporte_**X**": {
#                     "PDFs_templates_**X**": None,
#                     "reporte_por_**X**_JSON": None,
#                     "reportes_PDFs": {
#                         "reportes_PDFs_buffer": None
#                     },
#                     "reporte_por_**X**_JSON.py": None,
#                     "reporte_por_**X**_PDFs.py": None
#                 },
#                 "rerporte_**Y**": {
#                     "PDFs_templates_**Y**": None,
#                     "reporte_por_**Y**_JSON": None,
#                     "reportes_PDFs": {
#                         "reportes_PDFs_buffer": None
#                     },
#                     "reporte_por_**Y**_JSON.py": None,
#                     "reporte_por_**Y**_PDFs.py": None
#                 },
#                 "main.py": None
#             }
#         }
#     }
# }

# dict_definition = {
#     '*X*' : 'Proyecto_1',
#     '**X**' : 'reporte_Proyecto_1_a',
#     '**Y**' : 'reporte_Proyecto_1_b',
# }
