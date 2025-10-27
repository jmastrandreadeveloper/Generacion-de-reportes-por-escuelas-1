# ESTE PROGRAMA LO QUE HACE ES CREAR EL ARCHIVO PDF DE CADA UNA DE LAS ESCUELAS
# LEE EL ARCHIVO JSON Y LO CONVIERTE EN UN PDF USANDO PLANTILLAS PREVIAMENTE CREADAS
# O CREANDO HOJAS COMPLETAMENTE DESDE CERO
import pandas as pd
import os
import sys
import json
import ast  # Para convertir strings en diccionarios
from PyPDF2 import PdfReader
import io

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..' , '..' , '..'))
sys.path.append(project_root)
print('project_root : ', project_root)


import src.tools.load_JSON as lJ
import src.modelos.Libs.dict_List_To_List_of_list as dictList
import TABLE_STYLES as estilo

import src.modelos.Libs.Libs_PDF.PDFEditor as PDF
import src.modelos.Libs.Libs_GRÁFICAS.PLOTLY.barChart as barChart
import src.modelos.Libs.transform_to_dict as to_Dict 



PATH_FILE_TO_FINAL_PDFs_buffer = 'src/_main_/Fluidez_Lectora_medición_1/Año_2025/mes_05_mayo/reporte_por_escuela/reportes_PDFs/reportes_PDFs_buffer/'
PATH_FILE_TO_FINAL_PDFs = 'src/_main_/Fluidez_Lectora_medición_1/Año_2025/mes_05_mayo/reporte_por_escuela/reportes_PDFs/'
PATH_files_template = 'src/_main_/Fluidez_Lectora_medición_1/Año_2025/mes_05_mayo/reporte_por_escuela/PDFs_templates_por_escuela/Template-Vertical.pdf'

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

def hacer_carátula(escuela_id , escuela_data):
    PATH_files_templates_por_escuela_0_Carátula_Template_Vertical = 'src/_main_/Fluidez_Lectora_medición_1/Año_2025/mes_05_mayo/reporte_por_escuela/PDFs_templates_por_escuela/0-Carátula-Template-Vertical.pdf'
    pdf_archivo_0_Carátula_Template_Vertical = PDF.PDFEditor(PATH_files_templates_por_escuela_0_Carátula_Template_Vertical , escuela_data) 

    pdf_archivo_0_Carátula_Template_Vertical.add_text_to_page(
        'Escuela N° : ' + str(escuela_data['datos_institucionales']['Número']), 
        (30, 80), 
        0, 
        "REM-Regular", 25,
        color=(0, 15, 159),
        align='left'
    )

    pdf_archivo_0_Carátula_Template_Vertical.add_text_to_page(
        escuela_data['datos_institucionales']['Escuela'][:31], #escuela_data.Nombre_Escuela[:31], 
        (30, 70), 
        0,
        "REM-Black", 25,
        color=(0, 15, 159),
        align='left'
    )    

    pdfFile = PATH_FILE_TO_FINAL_PDFs_buffer +  str(escuela_id) + '_'  + str(escuela_data['datos_institucionales']['Número']) +  '_0_CARÁTULA_Fluidez_Lectora_Op_1_2025.pdf'
    pdf_archivo_0_Carátula_Template_Vertical.save_pdf(pdfFile,)
    print('...Carátula guardada en : ' , pdfFile)
    
    return pdfFile # pdf_archivo_0_Carátula_Template_Vertical

def hacer_primera_hoja(escuela_id , escuela_data):
    PATH_files_templates_por_escuela_1_Primera_Hoja_Presentación_Template_Vertical = 'src/_main_/Fluidez_Lectora_medición_1/Año_2025/mes_05_mayo/reporte_por_escuela/PDFs_templates_por_escuela/1-Primera-Hoja-Presentación-Template-Vertical.pdf'
    pdf_archivo_1_Primera_Hoja_Presentación_Template_Vertical = PDF.PDFEditor(PATH_files_templates_por_escuela_1_Primera_Hoja_Presentación_Template_Vertical , escuela_data) 

    # OBTENGO EL TÍTULO DE LA TABLA
    titulo_tabla_data_dict_totalidad_de_estudiantes_por_curso = escuela_data['Cantidad_de_estudiantes_censado_as']
    # IMPRIMO EN LA HOJA
    pdf_archivo_1_Primera_Hoja_Presentación_Template_Vertical.add_text_to_page(
        titulo_tabla_data_dict_totalidad_de_estudiantes_por_curso, 
        (210, 140), #(210 , 80) 
        0,
        "REM-Regular", 10,
        color=(0, 0 , 0),
        align='center'
    )
    
    # OBTENGO LA TABLA DE LAS CANTIDADES DE ALUMNOS
    tabla_data_dict_totalidad_de_estudiantes_por_curso = dictList.convertir_a_lista_de_listas(escuela_data , 'tabla_data_dict_totalidad_de_estudiantes_por_curso')
    # IMPRIMO LA TABLA EN LA HOJA
    pdf_archivo_1_Primera_Hoja_Presentación_Template_Vertical.add_table_to_page_v2(        
        tabla_data_dict_totalidad_de_estudiantes_por_curso,
        160, # 185
        0,
        estilo.tableStyle_1
    )
    # agrego la frase debajo de la tabla 'Este informe se realiza el 20/05/2024 en base al …% de carga registrada en GEM.'
    # OBTENGO LA FRASE...
    porcentaje_de_carga_registrada = escuela_data['porcentaje_de_carga_registrada']    
    pdf_archivo_1_Primera_Hoja_Presentación_Template_Vertical.add_text_to_page(
        porcentaje_de_carga_registrada, 
        (210, 50), 
        0,
        "REM-Regular", 10,
        color=(0, 0 , 0),
        align='center'
    )
    

    pdfFile = PATH_FILE_TO_FINAL_PDFs_buffer +  str(escuela_id) + '_'  + str(escuela_data['datos_institucionales']['Número']) +  '_1_PRIMERA_HOJA_Fluidez_Lectora_Op_1_2025.pdf'
    pdf_archivo_1_Primera_Hoja_Presentación_Template_Vertical.save_pdf(pdfFile,)
    print('...Primera hoja guardada en : ' , pdfFile)
    
    return pdfFile # pdf_archivo_1_Primera_Hoja_Presentación_Template_Vertical

def hacer_hoja_SIN_INFORME(escuela_id , escuela_data):    
    PATH_files_ = 'src/_main_/Fluidez_Lectora_medición_1/Año_2025/mes_05_mayo/reporte_por_escuela/PDFs_templates_por_escuela/5-Quinta-Hoja-Escuela-Sin-Medición-Template-Vertica.pdf'
    pdf_archivo_ = PDF.PDFEditor(PATH_files_ , escuela_data) 

    # OBTENGO EL TÍTULO DE LA TABLA
    mensaje = escuela_data['mensaje']
    # IMPRIMO EN LA HOJA
    pdf_archivo_.add_text_to_page(
        mensaje, 
        (210, 115), 
        0,
        "REM-Regular", 10,
        color=(0, 0 , 0),
        align='center'
    )

    pdfFile = PATH_FILE_TO_FINAL_PDFs_buffer +  str(escuela_id) + '_'  + str(escuela_data['datos_institucionales']['Número']) +  '_HOJA_SIN_INFORME_Fluidez_Lectora_Op_1_2025.pdf'
    pdf_archivo_.save_pdf(pdfFile,)
    print('...Hoja Sin Informe en : ' , pdfFile)
    
    return pdfFile # pdf_archivo_

def hacer_segunda_hoja(escuela_id , escuela_data):
    # no hace nada mas que leer el archivo
    PATH_files_templates_por_escuela_2_Segunda_Hoja_Desempeños_Template_Vertical = 'src/_main_/Fluidez_Lectora_medición_1/Año_2025/mes_05_mayo/reporte_por_escuela/PDFs_templates_por_escuela/2-Segunda-Hoja-Desempeños-Template-Vertical.pdf'
    pdf_archivo_2_Segunda_Hoja_Desempeños_Template_Vertical = PDF.PDFEditor(PATH_files_templates_por_escuela_2_Segunda_Hoja_Desempeños_Template_Vertical , escuela_data)
    
    pdfFile = PATH_FILE_TO_FINAL_PDFs_buffer +  str(escuela_id) + '_'  + str(escuela_data['datos_institucionales']['Número']) +  '_2_SEGUNDA_HOJA_Fluidez_Lectora_Op_1_2025.pdf'
    pdf_archivo_2_Segunda_Hoja_Desempeños_Template_Vertical.save_pdf(pdfFile,)
    print('...Segunda hoja guardada en : ' , pdfFile)

    return pdfFile # pdf_archivo_2_Segunda_Hoja_Desempeños_Template_Vertical

def hacer_tercera_hoja(escuela_id , escuela_data):
    # DEBEMOS ITERAR SOBRE LOS CURSOS!
    lista_de_hojas = []
    for curso in escuela_data['lista_de_CURSOS_NORMALIZADOS_con_datos']:
        # acá se ponen las tablas y los gráficos por curso
        PATH_files_templates_por_escuela_3_Terccera_Hoja_Resultados_Por_Curso_Template_Vertical = 'src/_main_/Fluidez_Lectora_medición_1/Año_2025/mes_05_mayo/reporte_por_escuela/PDFs_templates_por_escuela/3-Terccera-Hoja-Resultados-Por-Curso-Template-Vertical.pdf'
        pdf_archivo_3_Terccera_Hoja_Resultados_Por_Curso_Template_Vertical = PDF.PDFEditor(PATH_files_templates_por_escuela_3_Terccera_Hoja_Resultados_Por_Curso_Template_Vertical , escuela_data)
            
        Título_1_resultado_por_grado_curso = escuela_data[curso]['Título_1_resultado_por_grado_curso']
        # IMPRIMO EN LA HOJA EL PRIMER TÍTULO
        pdf_archivo_3_Terccera_Hoja_Resultados_Por_Curso_Template_Vertical.add_text_to_page(
            Título_1_resultado_por_grado_curso, 
            (20, 260), 
            0,
            "REM-Black", 12,
            color=(60, 180 , 229),
            align='left'
        )
        
        Título_2_porcentaje_por_grado_curso = escuela_data[curso]['Título_2_porcentaje_por_grado_curso']
        # IMPRIMO EN LA HOJA EL SEGUNDO TÍTULO
        pdf_archivo_3_Terccera_Hoja_Resultados_Por_Curso_Template_Vertical.add_text_to_page(
            Título_2_porcentaje_por_grado_curso, 
            (210, 250), 
            0,
            "REM-Regular", 12,
            color=(60, 180 , 229),
            align='center'
        )
        # LEO LA TABLA DE LOS PORCENTAJES PARA PODER CALCULAR EL GRÁFICO
        porcentaje_de_estudiantes_del_curso_por_nivel_de_desempeño_según_medición = escuela_data[curso]['porcentaje_de_estudiantes_del_curso_por_nivel_de_desempeño_según_medición']        
        # LE PASO LA TABLA A LA FUNCIÓN PARA QUE LA GRAFIQUE
        # PARA QUE LA HAGA, LA FUNCIÓN DEBE CONVERTIR EL DICCIONARIO EN UN DATAFRAME
        # DEBE DEVOLVERME UN GRÁFICO PARA PODER INSERTARLO 
        # DEBO TRANSFORMAR LA TABLA EN UN DICCIONARIO        
        gráfico = barChart.Matplotlib_stacked_bar_chart(
            to_Dict.transform_to_dict(porcentaje_de_estudiantes_del_curso_por_nivel_de_desempeño_según_medición) , 
            ["#205159", "#307A8A", "#4AACAE", "#9DDEDC"] , 
            'Niveles de Desempeño',
            bar_width=0.65,
        )        
        # inserto el gráfico de comparativa
        pdf_archivo_3_Terccera_Hoja_Resultados_Por_Curso_Template_Vertical.add_matplotlib_figure_to_pdf(
            gráfico, 
            (0,135,), # 80 
            0 , 
            width_mm=105, # 120 
            height_mm=105
        ) # 120
        # IMPRIMO EN LA HOJA EL TERCER TÍTULO
        Título_3_cantidad_por_grado_curso = escuela_data[curso]['Título_3_cantidad_por_grado_curso']
        pdf_archivo_3_Terccera_Hoja_Resultados_Por_Curso_Template_Vertical.add_text_to_page(
            Título_3_cantidad_por_grado_curso, 
            (210, 120), 
            0,
            "REM-Regular", 12,
            color=(60, 180 , 229),
            align='center'
        )
        # AHORA IMPRIMO LA TABLA DE LAS CANTIDADES DE LOS ALUMNOS
        cantidad_de_estudiantes_del_curso_por_nivel_de_desempeño_según_medición = dictList.convertir_a_lista_de_listas(escuela_data[curso] , 'cantidad_de_estudiantes_del_curso_por_nivel_de_desempeño_según_medición')        
        # IMPRIMO LA TABLA EN LA HOJA
        pdf_archivo_3_Terccera_Hoja_Resultados_Por_Curso_Template_Vertical.add_table_to_page_v2(        
            cantidad_de_estudiantes_del_curso_por_nivel_de_desempeño_según_medición,
            185,
            0,
            estilo.tableStyle_5
        )

        #pdfFile = PATH_FILE_TO_FINAL_PDFs +  str(escuela_id) + '_'  + str(escuela_data['datos_institucionales']['Número']) + '_'  + curso +  '_3_TERCERA_HOJA_Fluidez_Lectora_Op_1_2025.pdf'
        #pdf_archivo_3_Terccera_Hoja_Resultados_Por_Curso_Template_Vertical.save_pdf(pdfFile,)
        lista_de_hojas.append(pdf_archivo_3_Terccera_Hoja_Resultados_Por_Curso_Template_Vertical)
        

    # Unir todos los PDFs en memoria
    pdf_final = pdf_archivo_3_Terccera_Hoja_Resultados_Por_Curso_Template_Vertical.merge_pdfs_in_memory(lista_de_hojas, additional_pdfs = None) # additional_pdfs=[pdf_extra_1, pdf_extra_2])
        
    pdfFile = PATH_FILE_TO_FINAL_PDFs_buffer +  str(escuela_id) + '_'  + str(escuela_data['datos_institucionales']['Número']) +  '_3_TERCERA_UNIDA_HOJA_Fluidez_Lectora_Op_1_2025.pdf'
    pdf_archivo_3_Terccera_Hoja_Resultados_Por_Curso_Template_Vertical.save_multiples_pdf_to_disk(pdf_final , pdfFile)
    
    return pdfFile # pdf_archivo_3_Terccera_Hoja_Resultados_Por_Curso_Template_Vertical


def hacer_listado_de_alumnos(escuela_id , escuela_data):
    listaDePDFs = []
    
    PATH_template = 'src/_main_/Fluidez_Lectora_medición_1/Año_2025/mes_05_mayo/reporte_por_escuela/PDFs_templates_por_escuela/4-Cuarta-Hoja-Listado-de-Alumnos-Template-Horizontal.pdf'
    
    print("\n📌 Listados de alumnos:")    
    listados = obtener_listados_alumnos(escuela_data)
    
    for curso, listados_curso in listados.items():
        print(f"Curso: {curso}")
        
        for tipo_listado, alumnos in listados_curso.items():
            if isinstance(alumnos, dict):  # Para los desempeños dentro de "Listado Alumnos con DESEMPEÑO"
                if not alumnos:
                    print(f"  {tipo_listado}: (Vacío)")
                    continue

                print(f"  {tipo_listado}:")                
                print('\/' * 50)
                
                for desempeno, lista in alumnos.items():
                    if not lista:
                        print(f"    {desempeno}: (Vacío)")
                        continue

                    print(f"    {desempeno}: ")
                    title_text = tipo_listado
                    subtitle_text = desempeno
                    column_widths_mm = [18, 55, 55, 20 , 20, 25, 25, 25 , 35]                
                    output_pdf_path = PATH_FILE_TO_FINAL_PDFs + f"{escuela_id}_{escuela_data['datos_institucionales']['Número']}_4_CUARTA_HOJA_{curso}_{tipo_listado}_{desempeno}_Fluidez_Lectora_Op_1_2025.pdf"

                    # ⚠️ CREAR UNA NUEVA INSTANCIA POR CADA PDF ⚠️
                    pdf_editor = PDF.PDFEditor(PATH_template, escuela_data)

                    pdf_bytes = pdf_editor.tabla_listado_grande_OK(
                        estilo.tableStyle_7,
                        title_text,
                        subtitle_text,
                        column_widths_mm,
                        dictList.convertir_a_lista_de_listas(escuela_data[curso][tipo_listado], desempeno),
                        PATH_template,
                        #output_pdf_path
                    )

                    # Verificar si el objeto devuelto es un BytesIO antes de usar seek
                    if isinstance(pdf_bytes, io.BytesIO):
                        pdf_bytes.seek(0)  # Reiniciar el puntero al inicio
                        pdf_reader = PdfReader(pdf_bytes, strict=False)
                        num_pages = len(pdf_reader.pages)
                        print(f"✅ PDF generado tiene {num_pages} páginas.")
                    else:
                        print("❌ Error: `tabla_listado_grande` no devolvió un objeto BytesIO.")                    

                    listaDePDFs.append(pdf_bytes)  # Almacenar bytes en memoria

            else:
                if not alumnos:
                    print(f"  {tipo_listado}: (Vacío)")
                    continue

                print(f"  {tipo_listado}: ")
                title_text = tipo_listado
                subtitle_text = None
                column_widths_mm = [18, 55, 55, 20 , 20, 25, 25, 25 , 35]
                output_pdf_path = PATH_FILE_TO_FINAL_PDFs + f"{escuela_id}_{escuela_data['datos_institucionales']['Número']}_4_CUARTA_HOJA_{curso}_{tipo_listado}_Fluidez_Lectora_Op_1_2025.pdf"

                # ⚠️ CREAR UNA NUEVA INSTANCIA POR CADA PDF ⚠️
                pdf_editor = PDF.PDFEditor(PATH_template, escuela_data)

                pdf_bytes = pdf_editor.tabla_listado_grande_OK(
                    estilo.tableStyle_7,
                    title_text,
                    subtitle_text,
                    column_widths_mm,
                    dictList.convertir_a_lista_de_listas(escuela_data[curso], tipo_listado),
                    PATH_template,
                    #output_pdf_path
                )

                # Verificar si el objeto devuelto es un BytesIO antes de usar seek
                if isinstance(pdf_bytes, io.BytesIO):
                    pdf_bytes.seek(0)  # Reiniciar el puntero al inicio
                    pdf_reader = PdfReader(pdf_bytes, strict=False)
                    num_pages = len(pdf_reader.pages)
                    print(f"✅ PDF generado tiene {num_pages} páginas.")
                else:
                    print("❌ Error: `tabla_listado_grande` no devolvió un objeto BytesIO.")

                listaDePDFs.append(pdf_bytes)  # Almacenar bytes en memoria
                print('\/' * 50)

    # Unir todos los PDFs en memoria
    pdf_final = PDF.PDFEditor(PATH_template, escuela_data).merge_pdfs_in_memory(listaDePDFs)

    pdfFile = PATH_FILE_TO_FINAL_PDFs_buffer + f"{escuela_id}_{escuela_data['datos_institucionales']['Número']}_4_CUARTA_HOJA_Fluidez_Lectora_Op_1_2025.pdf"
    PDF.PDFEditor(PATH_template, escuela_data).save_multiples_pdf_to_disk(pdf_final, pdfFile)

    return pdfFile # PDF.PDFEditor(PATH_template, escuela_data)

def hacer_reporte_PDF_sin_informe(json_data):
    # Desomponer el json_data en partes
    escuela_id = list(json_data.keys())[0]
    escuela_data = json_data[escuela_id]

    hacer_carátula(escuela_id, escuela_data)
    hacer_hoja_SIN_INFORME(escuela_id, escuela_data)
    
    # Obtener lista de PDFEditor desde un directorio
    print( 'Obtener lista de PDFEditor desde un directorio : ')
    lista_pdfs_en_directorio = PDF.PDFEditor.leer_pdfs_en_directorio(PATH_FILE_TO_FINAL_PDFs_buffer, escuela_data)    

    # Contar páginas de cada PDF en la lista
    print('Contar páginas de cada PDF en la lista : ')
    paginas_por_pdf = PDF.PDFEditor.contar_paginas_pdf_editors(lista_pdfs_en_directorio)
    print(paginas_por_pdf)   

    # Unir los PDFs en memoria
    pdf_unido = PDF.PDFEditor.final_union_PDFs(lista_pdfs_en_directorio)

    # Guardar el PDF final en disco
    pdfFile = PATH_FILE_TO_FINAL_PDFs + f"{escuela_id}_{escuela_data['datos_institucionales']['Número']}_Fluidez_Lectora_Op_1_2025.pdf"
    PDF.PDFEditor(PATH_files_template, escuela_data).save_multiples_pdf_to_disk(pdf_unido, pdfFile)    

    PDF.PDFEditor.eliminar_pdfs_en_directorio(PATH_FILE_TO_FINAL_PDFs_buffer)
    print('...Reporte PDF generado y guardado en : ' , pdfFile)
    print('...PDFs temporales eliminados de : ' , PATH_FILE_TO_FINAL_PDFs_buffer)
    return


# este sería el que realiza el PDF completo
def hacer_reporte_PDF(json_data):
    # Desomponer el json_data en partes
    escuela_id = list(json_data.keys())[0]
    escuela_data = json_data[escuela_id]

    A__ = hacer_carátula(escuela_id, escuela_data)
    B__ = hacer_primera_hoja(escuela_id, escuela_data)
    C__ = hacer_segunda_hoja(escuela_id, escuela_data)
    D__ = hacer_tercera_hoja(escuela_id, escuela_data)
    E__ = hacer_listado_de_alumnos(escuela_id, escuela_data)
    
    pdfFile_Final = PATH_FILE_TO_FINAL_PDFs + f"{escuela_id}_{escuela_data['datos_institucionales']['Número']}_Fluidez_Lectora_Op_1_2025.pdf"
    # armo la lista de las rutas de cada PDF, recordemos que cada función me devuelve una ruta o un path
    # en donde se encuentra cada archivo PDF
    listPDFs = [A__, B__ , C__, D__, E__,]     
    #listPDFs = [A__, B__ , C__, D__, E__, F__, G__, H__,   K__, L__, M__, N__]     
    PDF.PDFEditor.definitivo_unir_PDFs(listPDFs , pdfFile_Final )    
    PDF.PDFEditor.eliminar_pdfs_en_directorio(PATH_FILE_TO_FINAL_PDFs_buffer)
    
    

    # # Obtener lista de PDFEditor desde un directorio
    # print( 'Obtener lista de PDFEditor desde un directorio : ')
    # lista_pdfs_en_directorio = PDF.PDFEditor.leer_pdfs_en_directorio(PATH_FILE_TO_FINAL_PDFs_buffer, escuela_data)    

    # # Contar páginas de cada PDF en la lista
    # print('Contar páginas de cada PDF en la lista : ')
    # paginas_por_pdf = PDF.PDFEditor.contar_paginas_pdf_editors(lista_pdfs_en_directorio)
    # print(paginas_por_pdf)   

    # # Unir los PDFs en memoria
    # pdf_unido = PDF.PDFEditor.final_union_PDFs(lista_pdfs_en_directorio)

    # # Guardar el PDF final en disco
    # pdfFile = PATH_FILE_TO_FINAL_PDFs + f"{escuela_id}_{escuela_data['datos_institucionales']['Número']}_Fluidez_Lectora_Op_1_2025.pdf"
    # PDF.PDFEditor(PATH_files_template, escuela_data).save_multiples_pdf_to_disk(pdf_unido, pdfFile)    

    # PDF.PDFEditor.eliminar_pdfs_en_directorio(PATH_FILE_TO_FINAL_PDFs_buffer)
    # print('...Reporte PDF generado y guardado en : ' , pdfFile)
    # print('...PDFs temporales eliminados de : ' , PATH_FILE_TO_FINAL_PDFs_buffer)
    return
    


# Llamar a la función de prueba si el script se ejecuta directamente
if __name__ == '__main__':    

    # leo el archivo JSON    
    PATH_files_JSON = 'src/_main_/Fluidez_Lectora_medición_1/Año_2025/mes_05_mayo/reporte_por_escuela/reporte_por_escuela_JSON/4_1003_Fluidez_Lectora_Op_1_2025.json'
    file_JSON = lJ.leer_JSON(os.path.join(project_root, PATH_files_JSON))

    # desempaquetar el archivo JSON    
    #pJ.pretty_print_json(file_JSON)
    # Obtener el ID de la escuela (es la única clave en el JSON)
    escuela_id = list(file_JSON.keys())[0]
    escuela_data = file_JSON[escuela_id]

    Carátula_Template_Vertical = hacer_carátula(escuela_id, escuela_data)
    Primera_Hoja_Presentación_Template_Vertical = hacer_primera_hoja(escuela_id, escuela_data)
    Segunda_Hoja_Template_Vertical = hacer_segunda_hoja(escuela_id, escuela_data)
    Tercera_Hoja_Template_Vertical = hacer_tercera_hoja(escuela_id, escuela_data)
    Cuarta_Hoja_Template_Horizontal = hacer_listado_de_alumnos(escuela_id, escuela_data)    
         
    # Obtener lista de PDFEditor desde un directorio
    print( 'Obtener lista de PDFEditor desde un directorio : ')
    lista_pdfs_en_directorio = PDF.PDFEditor.leer_pdfs_en_directorio(PATH_FILE_TO_FINAL_PDFs_buffer, escuela_data)    

    # Contar páginas de cada PDF en la lista
    print('Contar páginas de cada PDF en la lista : ')
    paginas_por_pdf = PDF.PDFEditor.contar_paginas_pdf_editors(lista_pdfs_en_directorio)
    print(paginas_por_pdf)   

    # Unir los PDFs en memoria
    pdf_unido = PDF.PDFEditor.final_union_PDFs(lista_pdfs_en_directorio)

    # Guardar el PDF final en disco
    pdfFile = PATH_FILE_TO_FINAL_PDFs + f"{escuela_id}_{escuela_data['datos_institucionales']['Número']}_Fluidez_Lectora_Op_1_2025.pdf"
    PDF.PDFEditor(PATH_files_template, escuela_data).save_multiples_pdf_to_disk(pdf_unido, pdfFile)    

    resultado = PDF.PDFEditor.eliminar_pdfs_en_directorio(PATH_FILE_TO_FINAL_PDFs_buffer)   


    print('...fin')

    # print('Carátula_Template_Vertical : ' , Carátula_Template_Vertical , ' ' , type(Carátula_Template_Vertical))
    # print('Primera_Hoja_Presentación_Template_Vertical : ' , Primera_Hoja_Presentación_Template_Vertical , ' ' , type(Primera_Hoja_Presentación_Template_Vertical))
    # print('Segunda_Hoja_Template_Vertical : ' , Segunda_Hoja_Template_Vertical , ' ' , type(Segunda_Hoja_Template_Vertical))
    # print('Tercera_Hoja_Template_Vertical : ' , Tercera_Hoja_Template_Vertical , ' ' , type(Tercera_Hoja_Template_Vertical))
    # print('Cuarta_Hoja_Template_Horizontal : ' , Cuarta_Hoja_Template_Horizontal , ' ' , type(Cuarta_Hoja_Template_Horizontal))
    

    # Unir todos los PDFs en memoria    
    # PATH_files_template = 'src/_main_/Fluidez_Lectora_medición_1/2025/05_mayo/reporte_por_escuela/PDFs_templates_por_escuela/Template-Vertical.pdf'
    # print('...uniendo el PDF final de la escuela : ' , escuela_data['datos_institucionales']['Escuela'])
    # mis_pdfs_en_memoria = [Carátula_Template_Vertical, Primera_Hoja_Presentación_Template_Vertical, Segunda_Hoja_Template_Vertical, Tercera_Hoja_Template_Vertical, Cuarta_Hoja_Template_Horizontal]  # Lista de objetos PDFEditor
    # pdf_final = PDF.PDFEditor(PATH_files_template, escuela_data).merge_pdfs_in_memory(
    #     mis_pdfs_en_memoria
    # )

    # pdf_unido_memoria = PDF.PDFEditor.unir_pdfs_memoria(lista_pdfs_en_directorio)
    # # Guardar el resultado en un archivo (opcional)
    # with open("pdf_combinado_memoria.pdf", "wb") as f:
    #     f.write(pdf_unido_memoria.getbuffer())

    # Guardar el resultado en un archivo (opcional)
    # with open('src/_main_/Fluidez_Lectora_medición_1/2025/05_mayo/reporte_por_escuela/reportes_PDFs/'+str(escuela_data['Escuela_ID']) +'_' + escuela_data['datos_institucionales']['Escuela']+'_Fluidez_Lectora_Op_1_2025' +'.pdf', "wb") as f:
    #     f.write(pdf_unido.getbuffer())

    # Contar páginas directamente desde un directorio
    # print('Contar páginas directamente desde un directorio : ')
    # paginas_desde_directorio = PDF.PDFEditor.contar_paginas_pdfs_en_directorio(PATH_FILE_TO_FINAL_PDFs, escuela_data)
    # print(paginas_desde_directorio)

    #print('verificar : ')
    # Llamar a la función dentro de una instancia de PDFEditor
    # editor = PDF.PDFEditor('src/_main_/Fluidez_Lectora_medición_1/2025/05_mayo/reporte_por_escuela/PDFs_templates_por_escuela/Template-Vertical.pdf', {})  # Instancia solo para llamar la función
    # resultado = editor.verificar_pdfs_en_memoria(mis_pdfs_en_memoria)
    
    #directorio_pdfs = PATH_FILE_TO_FINAL_PDFs #"/ruta/a/tus/pdfs"

    # # verificar el tipo de los objetos en la lista
    # print('verificar el tipo de los objetos en la lista -directorios-: ')
    # for pdf in lista_pdfs_en_directorio:
    #     print(pdf ,  ' ',type(pdf))