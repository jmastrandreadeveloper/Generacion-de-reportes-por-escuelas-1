# ESTE PROGRAMA LO QUE HACE ES GENERAR EL REPORTE PDF 
# PARA CADA UNA DE LA SUPERVISIONES, LEYENDO LOS ARCHIVOS JSON CORRESPONDIENTES
import pandas as pd
import os
import sys
import json
import ast  # Para convertir strings en diccionarios
from PyPDF2 import PdfReader
import io
import re

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..' , '..' , '..'))
sys.path.append(project_root)
print('project_root : ', project_root)


import src.tools.load_JSON as lJ
import src.modelos.Libs.dict_List_To_List_of_list as dictList
import TABLE_STYLES as estilo
import src.tools.prettyJSON as pJ

import src.modelos.Libs.Libs_PDF.PDFEditor as PDF
import src.modelos.Libs.Libs_GRÁFICAS.PLOTLY.barChart as barChart
import src.modelos.Libs.transform_to_dict as to_Dict 

PATH_FILE_TO_FINAL_PDFs_buffer = 'src/_main_/Fluidez_Lectora_medición_1/Año_2025/mes_05_mayo/reporte_por_supervisión/reportes_PDFs/reportes_PDFs_buffer/'
PATH_FILE_TO_FINAL_PDFs = 'src/_main_/Fluidez_Lectora_medición_1/Año_2025/mes_05_mayo/reporte_por_supervisión/reportes_PDFs/'
PATH_files_template = 'src/_main_/Fluidez_Lectora_medición_1/Año_2025/mes_05_mayo/reporte_por_supervisión/PDFs_templates_por_Supervisión/Template-Vertical.pdf'

def hacer_carátula(supervisión , supervision_data):    
    PATH_files_templates_por_Supervisión_0_Carátula_Template_Vertical = 'src/_main_/Fluidez_Lectora_medición_1/Año_2025/mes_05_mayo/reporte_por_supervisión/PDFs_templates_por_Supervisión/0-Carátula-Template-Vertical.pdf'
    pdf_archivo_0_Carátula_Template_Vertical = PDF.PDFEditor(PATH_files_templates_por_Supervisión_0_Carátula_Template_Vertical , supervision_data)     

    pdf_archivo_0_Carátula_Template_Vertical.add_text_to_page(
        'Supervisión : ' + supervisión,
        (30, 80), 
        0, 
        "REM-Black", 20,
        color=(0, 15, 159),
        align='center'
    )

    # import re
    # nombre_archivo_seguro = re.sub(r'[^\w\-_. ]', '_', supervisión.replace(' ', '_'))
    # pdfFile = PATH_FILE_TO_FINAL_PDFs_buffer + nombre_archivo_seguro + '_0_CARÁTULA_Fluidez_Lectora_Op_1_2025.pdf'

    pdfFile = PATH_FILE_TO_FINAL_PDFs_buffer + supervisión + '_0_CARÁTULA_Fluidez_Lectora_Op_1_2025.pdf'
    pdf_archivo_0_Carátula_Template_Vertical.save_pdf(pdfFile,)
    print('...Carátula guardada en : ' , pdfFile)
    
    return pdf_archivo_0_Carátula_Template_Vertical

def hacer_primera_hoja(supervisión , supervision_data):
    PATH_files_templates_por_escuela_1_Primera_Hoja_Presentación_Template_Vertical = 'src/_main_/Fluidez_Lectora_medición_1/Año_2025/mes_05_mayo/reporte_por_supervisión/PDFs_templates_por_Supervisión/1-Primera-Hoja-Presentación-Template-Vertical.pdf'
    pdf_archivo_1_Primera_Hoja_Presentación_Template_Vertical = PDF.PDFEditor(PATH_files_templates_por_escuela_1_Primera_Hoja_Presentación_Template_Vertical , supervision_data)

    # OBTENGO EL TÍTULO DE LA TABLA
    título_tabla_uno = supervision_data['título_tabala_uno']
    # IMPRIMO EN LA HOJA
    pdf_archivo_1_Primera_Hoja_Presentación_Template_Vertical.add_text_to_page(
        título_tabla_uno, 
        (210, 170),  
        0,
        "REM-Regular", 10,
        color=(0, 0 , 0),
        align='center'
    )
    
    # OBTENGO LA TABLA DE LAS CANTIDADES DE ALUMNOS
    tabla_data_dict_primera_tabla_del_informe_Supervisores = dictList.convertir_a_lista_de_listas(supervision_data , 'tabla_data_dict_primera_tabla_del_informe_Supervisores')    
    
    # IMPRIMO LA TABLA EN LA HOJA
    pdf_archivo_1_Primera_Hoja_Presentación_Template_Vertical.add_table_to_page_v2(        
        tabla_data_dict_primera_tabla_del_informe_Supervisores,
        130,
        0,
        estilo.tableStyle_8
    )

    pdfFile = PATH_FILE_TO_FINAL_PDFs_buffer + supervisión +  '_1_PRIMERA_HOJA_Fluidez_Lectora_Op_1_2025.pdf'
    pdf_archivo_1_Primera_Hoja_Presentación_Template_Vertical.save_pdf(pdfFile,)
    print('...Primera hoja guardada en : ' , pdfFile)
    
    return pdf_archivo_1_Primera_Hoja_Presentación_Template_Vertical

def hacer_segunda_hoja(supervisión , supervision_data):
    # no hace nada mas que leer el archivo
    PATH_files_templates_por_Supervisión_2_Segunda_Hoja_Desempeños_Template_Vertical = 'src/_main_/Fluidez_Lectora_medición_1/Año_2025/mes_05_mayo/reporte_por_supervisión/PDFs_templates_por_Supervisión/2-Segunda-Hoja-Desempeños-Template-Vertical.pdf'
    pdf_archivo_2_Segunda_Hoja_Desempeños_Template_Vertical = PDF.PDFEditor(PATH_files_templates_por_Supervisión_2_Segunda_Hoja_Desempeños_Template_Vertical , supervision_data)
    
    pdfFile = PATH_FILE_TO_FINAL_PDFs_buffer + supervisión +  '_2_SEGUNDA_HOJA_Fluidez_Lectora_Op_1_2025.pdf'
    pdf_archivo_2_Segunda_Hoja_Desempeños_Template_Vertical.save_pdf(pdfFile,)
    print('...Segunda hoja guardada en : ' , pdfFile)

    return pdf_archivo_2_Segunda_Hoja_Desempeños_Template_Vertical

def hacer_tercera_hoja(supervisión , supervision_data):
    # la tercera hoja es la de los enlaces a los informes
    PATH_files_templates_por_Supervisión_3_Tercera_Hoja_Enlaces_a_escuelas_Template_Vertical = 'src/_main_/Fluidez_Lectora_medición_1/Año_2025/mes_05_mayo/reporte_por_supervisión/PDFs_templates_por_Supervisión/3-Terccera-Hoja-Resultados-Por-Curso-Template-Vertical.pdf'
    pdf_archivo_3_Tercera_Hoja_Enlaces_a_escuelas_Template_Vertical = PDF.PDFEditor(PATH_files_templates_por_Supervisión_3_Tercera_Hoja_Enlaces_a_escuelas_Template_Vertical , supervision_data)

    # OBTENGO EL TÍTULO DE LA TABLA
    título_tabla_enlaces = supervision_data['título_tabla_enlaces']
    # IMPRIMO EN LA HOJA
    pdf_archivo_3_Tercera_Hoja_Enlaces_a_escuelas_Template_Vertical.add_text_to_page(
        título_tabla_enlaces, 
        (210, 260),  
        0,
        "REM-Regular", 10,
        color=(0, 0 , 0),
        align='center'
    )
    
    
    # OBTENGO LA TABLA DE LOS ENLACES
    tabla_Escuelas_con_enlace = dictList.convertir_a_lista_de_listas(supervision_data , 'Escuelas_con_enlace')
    
    # IMPRIMO LA TABLA DE LOS ENLACES EN LA HOJA
    pdf_archivo_3_Tercera_Hoja_Enlaces_a_escuelas_Template_Vertical.add_table_to_page_v2(        
        tabla_Escuelas_con_enlace,
        40,
        0,
        estilo.tableStyle_9
    )
    
    pdfFile = PATH_FILE_TO_FINAL_PDFs_buffer + supervisión +  '_3_TERCERA_HOJA_Fluidez_Lectora_Op_1_2025.pdf'
    pdf_archivo_3_Tercera_Hoja_Enlaces_a_escuelas_Template_Vertical.save_pdf(pdfFile,)
    print('...Tercera hoja guardada en : ' , pdfFile)

    return PATH_FILE_TO_FINAL_PDFs_buffer

def hacer_cuarta_hoja(supervisión , supervision_data):
    # la cuata hoja es la de los desempeños de todas las escuelas 
    # RESULTADOS DE TODOS LOS CURSOS CENSADOS
    # Proporción de estudiantes por escuela según nivel de desempeño en fluidez lectora
    # se usa el mismo template que la tercera hoja pero con otro contenido
    PATH_files_templates_por_Supervisión_4_Cuarta_Desempeño_Escuela_Template_Vertical = 'src/_main_/Fluidez_Lectora_medición_1/Año_2025/mes_05_mayo/reporte_por_supervisión/PDFs_templates_por_Supervisión/3-Terccera-Hoja-Resultados-Por-Curso-Template-Vertical.pdf'
    pdf_archivo_4_Cuarta_Desempeño_Escuela_Template_Vertical = PDF.PDFEditor(PATH_files_templates_por_Supervisión_4_Cuarta_Desempeño_Escuela_Template_Vertical , supervision_data)

    título_tabala_dos = supervision_data['título_tabala_dos']
    # IMPRIMO EN LA HOJA EL PRIMER TÍTULO
    pdf_archivo_4_Cuarta_Desempeño_Escuela_Template_Vertical.add_text_to_page(
        título_tabala_dos, 
        (20, 270), 
        0,
        "REM-Black", 12,
        color=(60, 180 , 229),
        align='left'
    )
    
    sub_título_tabala_dos = supervision_data['sub_título_tabala_dos']
    # IMPRIMO EN LA HOJA EL SEGUNDO TÍTULO
    pdf_archivo_4_Cuarta_Desempeño_Escuela_Template_Vertical.add_text_to_page(
        sub_título_tabala_dos, 
        (210, 260), 
        0,
        "REM-Regular", 12,
        color=(60, 180 , 229),
        align='center'
    )

    # CARGO LOS PORCENTAJES
    desempeños_por_escuelas_de_la_supervision = supervision_data['desempeños_por_escuelas_de_la_supervision']

    gráfico = barChart.Matplotlib_stacked_bar_chart_2(
        to_Dict.transform_to_dict(desempeños_por_escuelas_de_la_supervision) , 
        ["#205159", "#307A8A", "#4AACAE", "#9DDEDC"] , 
    )
    # inserto el gráfico de los porcentajes de desempeño por escuela
    pdf_archivo_4_Cuarta_Desempeño_Escuela_Template_Vertical.add_matplotlib_figure_to_pdf(
        gráfico, 
        (0,155), # 80 
        0 , 
        width_mm=200, # 120 
        height_mm=100
    )

    TÏTULO_Cantidad_de_estudiantes_censados_por_establecimiento_SEGÚN_NIVEL_DE_DESEMPEÑO = supervision_data['TÏTULO_Cantidad_de_estudiantes_censados_por_establecimiento_SEGÚN_NIVEL_DE_DESEMPEÑO']

    # IMPRIMO LA TABLA Cantidad de estudiantes censados por escuela según nivel de desempeño
    pdf_archivo_4_Cuarta_Desempeño_Escuela_Template_Vertical.add_text_to_page(
        TÏTULO_Cantidad_de_estudiantes_censados_por_establecimiento_SEGÚN_NIVEL_DE_DESEMPEÑO, 
        (210, 150), 
        0,
        "REM-Regular", 10,
        color=(0, 0 , 0),
        align='center'
    )

    # cargo lo datoss de la tabla Cantidad_de_estudiantes_censados_por_establecimiento_SEGÚN_NIVEL_DE_DESEMPEÑO
    # t = supervision_data['tabla_data_dict_Cantidad_de_estudiantes_censados_por_establecimiento_SEGÚN_NIVEL_DE_DESEMPEÑO']
    # print(t)
    # exit()

    # OBTENGO LA TABLA DE LOS datos
    tabla_data_dict_Cantidad_de_estudiantes_censados_por_establecimiento_SEGÚN_NIVEL_DE_DESEMPEÑO = dictList.convertir_a_lista_de_listas(supervision_data , 'tabla_data_dict_Cantidad_de_estudiantes_censados_por_establecimiento_SEGÚN_NIVEL_DE_DESEMPEÑO')    
    
    # IMPRIMO LA TABLA DE LOS ENLACES EN LA HOJA
    pdf_archivo_4_Cuarta_Desempeño_Escuela_Template_Vertical.add_table_to_page_v2(        
        tabla_data_dict_Cantidad_de_estudiantes_censados_por_establecimiento_SEGÚN_NIVEL_DE_DESEMPEÑO,
        155,
        0,
        estilo.tableStyle_8
    )


    pdfFile = PATH_FILE_TO_FINAL_PDFs_buffer + supervisión +  '_4_CUARTA_HOJA_Fluidez_Lectora_Op_1_2025.pdf'
    pdf_archivo_4_Cuarta_Desempeño_Escuela_Template_Vertical.save_pdf(pdfFile,)
    print('...Cuarta hoja guardada en : ' , pdfFile)

    return PATH_FILE_TO_FINAL_PDFs_buffer


def hacer_quinta_hoja(supervisión , supervision_data):
    # la quinta hoja es similar a la cuarta pero se itera por curso
    # RESULTADOS DE TODOS LOS CURSOS CENSADOS
    # Proporción de estudiantes por escuela según nivel de desempeño en fluidez lectora
    # DEBEMOS ITERAR SOBRE LOS CURSOS!
    # debo saber qué tipo de supervisión es si es primaria o secundaria
    Supervisión_tipo = supervision_data['Supervisión_tipo']
    Tipo_curso = supervision_data['Tipo_curso']

    lista_de_hojas = []
    
    for curso in supervision_data['lista_de_Cursos_de_la_Supervisión']:
        PATH_files_templates_por_Supervisión_5_Quinta_Desempeño_Escuela_Curso_Template_Vertical = 'src/_main_/Fluidez_Lectora_medición_1/Año_2025/mes_05_mayo/reporte_por_supervisión/PDFs_templates_por_Supervisión/3-Terccera-Hoja-Resultados-Por-Curso-Template-Vertical.pdf'
        pdf_archivo_5_Quinta_Desempeño_Escuela_Curso_Template_Vertical = PDF.PDFEditor(PATH_files_templates_por_Supervisión_5_Quinta_Desempeño_Escuela_Curso_Template_Vertical , supervision_data)

        título_ = 'RESULTADOS DE ' + curso + ' ' + Tipo_curso + ' ' + Supervisión_tipo
        # IMPRIMO EN LA HOJA EL PRIMER TÍTULO
        pdf_archivo_5_Quinta_Desempeño_Escuela_Curso_Template_Vertical.add_text_to_page(
            título_, 
            (20, 270), 
            0,
            "REM-Black", 12,
            color=(60, 180 , 229),
            align='left'
        )
        
        sub_título = 'Proporción de estudiantes por escuela según nivel de desempeño en fluidez lectora'
        # IMPRIMO EN LA HOJA EL SEGUNDO TÍTULO
        pdf_archivo_5_Quinta_Desempeño_Escuela_Curso_Template_Vertical.add_text_to_page(
            sub_título, 
            (210, 260), 
            0,
            "REM-Regular", 12,
            color=(60, 180 , 229),
            align='center'
        )

        # acá saco los datos de los porcentajes para ser graficados
        el_value_de_los_porcentajes = supervision_data['tabla_data_dict_Porcentajes_de_estudiantes_censados_por_curso_SEGÚN_NIVEL_DE_DESEMPEÑO'][curso]
        
        #print(curso)
        #print(el_value_de_los_porcentajes)
        #print('-----------------------------------')

        gráfico = barChart.Matplotlib_stacked_bar_chart_2(
            to_Dict.transform_to_dict(el_value_de_los_porcentajes) , 
            ["#205159", "#307A8A", "#4AACAE", "#9DDEDC"] , 
        )
        # inserto el gráfico de los porcentajes de desempeño por escuela
        pdf_archivo_5_Quinta_Desempeño_Escuela_Curso_Template_Vertical.add_matplotlib_figure_to_pdf(
            gráfico, 
            (0,155), # 80 
            0 , 
            width_mm=200, # 120 
            height_mm=100
        )        
        
        
        TÏTULO_Cantidad_de_estudiantes_censados_por_establecimiento_SEGÚN_NIVEL_DE_DESEMPEÑO = 'Cantidad de estudiantes censados por escuela y ' + Tipo_curso +  ' según nivel de desempeño'

        # IMPRIMO el título de la tabla 
        pdf_archivo_5_Quinta_Desempeño_Escuela_Curso_Template_Vertical.add_text_to_page(
            TÏTULO_Cantidad_de_estudiantes_censados_por_establecimiento_SEGÚN_NIVEL_DE_DESEMPEÑO, 
            (210, 150), 
            0,
            "REM-Regular", 10,
            color=(0, 0 , 0),
            align='center'
        )

        # esto es para poder crear el diccionario que necesita la función para poder convertirlo en lista de listas
        el_value_de_las_cantidades = supervision_data['tabla_data_dict_Cantidad_de_estudiantes_censados_por_curso_SEGÚN_NIVEL_DE_DESEMPEÑO'][curso]
        el_dict_de_las_cantidades = {
            curso : el_value_de_las_cantidades
        }

        # IMPRIMO LA TABLA DE LOS ENLACES EN LA HOJA
        pdf_archivo_5_Quinta_Desempeño_Escuela_Curso_Template_Vertical.add_table_to_page_v2(        
            dictList.convertir_a_lista_de_listas(el_dict_de_las_cantidades , curso),
            155,
            0,
            estilo.tableStyle_8
        )

        lista_de_hojas.append(pdf_archivo_5_Quinta_Desempeño_Escuela_Curso_Template_Vertical)    
    
    
    # Unir todos los PDFs en memoria
    pdf_final = pdf_archivo_5_Quinta_Desempeño_Escuela_Curso_Template_Vertical.merge_pdfs_in_memory(lista_de_hojas, additional_pdfs = None) # additional_pdfs=[pdf_extra_1, pdf_extra_2])
        
    pdfFile = PATH_FILE_TO_FINAL_PDFs_buffer + supervisión +  '_5_QUINTA_UNIDA_HOJA_Fluidez_Lectora_Op_1_2025.pdf'
    pdf_archivo_5_Quinta_Desempeño_Escuela_Curso_Template_Vertical.save_multiples_pdf_to_disk(pdf_final , pdfFile)
    
    return pdf_archivo_5_Quinta_Desempeño_Escuela_Curso_Template_Vertical


# este sería el que realiza el PDF completo
def hacer_reporte_PDF(json_data):
    # Desomponer el json_data en partes
    # escuela_id = list(json_data.keys())[0]
    # escuela_data = json_data[escuela_id]
    # Obtener el nombre de la supervisón
    supervisión = json_data["Supervisión"]  # ✅ Esto da "01 - Primario Privada"
    supervisión_data = json_data  # ✅ El JSON completo ya es el contenido que querés

    hacer_carátula(supervisión, supervisión_data)
    hacer_primera_hoja(supervisión, supervisión_data)
    hacer_segunda_hoja(supervisión, supervisión_data)
    hacer_tercera_hoja(supervisión, supervisión_data)
    hacer_cuarta_hoja(supervisión, supervisión_data)
    hacer_quinta_hoja(supervisión, supervisión_data)

    # Obtener lista de PDFEditor desde un directorio
    print( 'Obtener lista de PDFEditor desde un directorio : ')
    lista_pdfs_en_directorio = PDF.PDFEditor.leer_pdfs_en_directorio(PATH_FILE_TO_FINAL_PDFs_buffer, supervisión_data)    

    # Contar páginas de cada PDF en la lista
    print('Contar páginas de cada PDF en la lista : ')
    paginas_por_pdf = PDF.PDFEditor.contar_paginas_pdf_editors(lista_pdfs_en_directorio)
    print(paginas_por_pdf)   

    # Unir los PDFs en memoria
    pdf_unido = PDF.PDFEditor.final_union_PDFs(lista_pdfs_en_directorio)

    # Guardar el PDF final en disco    
    pdfFile = PATH_FILE_TO_FINAL_PDFs + supervisión +  '_Fluidez_Lectora_Op_1_2025.pdf'
    PDF.PDFEditor(PATH_files_template, supervisión_data).save_multiples_pdf_to_disk(pdf_unido, pdfFile)    

    PDF.PDFEditor.eliminar_pdfs_en_directorio(PATH_FILE_TO_FINAL_PDFs_buffer)
    print('...Reporte PDF generado y guardado en : ' , pdfFile)
    print('...PDFs temporales eliminados de : ' , PATH_FILE_TO_FINAL_PDFs_buffer)
    return


# Llamar a la función de prueba si el script se ejecuta directamente
if __name__ == '__main__':    

    # leo el archivo JSON    
    PATH_files_JSON = 'src/_main_/Fluidez_Lectora_medición_1/Año_2025/mes_05_mayo/reporte_por_supervisión/reporte_por_supervisión_JSON/01 - Primario Privada_Fluidez_Lectora_Op_1_2025.json'    
    file_JSON = lJ.leer_JSON(os.path.join(project_root, PATH_files_JSON))

    

    # desempaquetar el archivo JSON    
    #pJ.pretty_print_json(file_JSON)
    # Obtener el nombre de la supervisón
    supervisión = file_JSON["Supervisión"]  # ✅ Esto da "01 - Primario Privada"
    supervisión_data = file_JSON  # ✅ El JSON completo ya es el contenido que querés

    Carátula_Template_Vertical = hacer_carátula(supervisión, supervisión_data)
    Primera_Hoja_Presentación_Template_Vertical = hacer_primera_hoja(supervisión, supervisión_data)
    Segunda_Hoja_Template_Vertical = hacer_segunda_hoja(supervisión, supervisión_data)
    Tercera_Hoja_Template_Vertical = hacer_tercera_hoja(supervisión, supervisión_data)
    Cuarta_Hoja_Template_Vertical = hacer_cuarta_hoja(supervisión, supervisión_data)
    Quinta_Hoja_Template_Vertical = hacer_quinta_hoja(supervisión, supervisión_data)

    # Obtener lista de PDFEditor desde un directorio
    print( 'Obtener lista de PDFEditor desde un directorio : ')
    lista_pdfs_en_directorio = PDF.PDFEditor.leer_pdfs_en_directorio(PATH_FILE_TO_FINAL_PDFs_buffer, supervisión_data)    

    # Contar páginas de cada PDF en la lista
    print('Contar páginas de cada PDF en la lista : ')
    paginas_por_pdf = PDF.PDFEditor.contar_paginas_pdf_editors(lista_pdfs_en_directorio)
    print(paginas_por_pdf)   

    # Unir los PDFs en memoria
    pdf_unido = PDF.PDFEditor.final_union_PDFs(lista_pdfs_en_directorio)

    # Guardar el PDF final en disco    
    pdfFile = PATH_FILE_TO_FINAL_PDFs + supervisión +  '_Fluidez_Lectora_Op_1_2025.pdf'
    PDF.PDFEditor(PATH_files_template, supervisión_data).save_multiples_pdf_to_disk(pdf_unido, pdfFile)    

    resultado = PDF.PDFEditor.eliminar_pdfs_en_directorio(PATH_FILE_TO_FINAL_PDFs_buffer)   


    print('...fin')