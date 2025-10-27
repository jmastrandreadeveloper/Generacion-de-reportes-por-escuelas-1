import PDFEditor as PDF
import config as cf
import funcionesUtiles as fU
import os
from reportlab.lib import colors

def hacer_carátula(unaSupervisión):
    print('SUPERVISIORES..!!!')
    pdf_agosto_2024 = PDF.PDFEditor('D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas\Supervisiones Segunda Medición' + '/1-Página_Supervisión_-1-carátula.pdf' ,
                                            unaSupervisión
    )
    pdf_agosto_2024.add_text_to_page(
        'Supervisión : ' + unaSupervisión.Nombre_Supervisión, 
        (30, 80), 
        0, 
        "REM-Black", 20,
        color=(0, 15, 159),
        align='center'
    )
    # pdf_agosto_2024.add_text_to_page(
    #     unaSupervisión.Nombre_Supervisión, 
    #     (30, 70), 
    #     0,
    #     "REM-Black", 25,
    #     color=(0, 15, 159),
    #     align='left'
    # )
    pdfFile = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\PDFsSupervisiones' + '\\' + fU.sanearNombresDeArchivos(str(unaSupervisión.Nombre_Supervisión)) +  '_F. L. 2024_2'  + '_1-Carátula-1' + '.pdf'
    pdf_agosto_2024.save_pdf(pdfFile,)

    return pdfFile


def hacer_segunda_página(unaSupervisión):
    Diccionario_Informes = unaSupervisión.get_supervisión_Diccionario_Informes()
    tabla_escuelas_por_sup = Diccionario_Informes.get('FL_SUPERVISIÓN_000_unificada_cantidad_de_alumnos_por_escuela_FL_y_Nominal_lista_')
    
    #print(tabla_escuelas_por_sup)
    
    segunda_hoja = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas\Supervisiones Segunda Medición' + '/2-Página_Supervisión_-2.pdf'
    output_pdf_path = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\PDFsSupervisiones' + '\\' + fU.sanearNombresDeArchivos(str(unaSupervisión.Nombre_Supervisión)) +  '_F. L. 2024_2'  + '_2-Página-2' + '.pdf'
    pdf_supervision_mayo_2024 = PDF.PDFEditor(
        segunda_hoja ,
        unaSupervisión
    )

    # de acuerdo a la cantidad de escuelas que tiene la supervisión, se va a escalar
    # la tabla para que ocupe todo el alto del espacio entre el título
    # y el pie de página.
    cantidadDeEscuelas = len(tabla_escuelas_por_sup)  # el 2 corresponde al encabezado y al pie de la tabla
    """
        6   11
        8   11
        9   10
        10  10
        11  9
        12  9
        13  8
        14  8
        15  7
        16  7
        17  6
        18  6
        19  6
        20  6
    """    

    FONTSIZE_adjust = 0

    # Datos de la tabla
    cabecera = ['Número', 'Nombre Escuela', 'Censado/as' , 'Matrícula']

    tableStyle = [
            ('BACKGROUND', (0, 0), (-1, 0), colors.Color(49/255, 122/255, 138/255)),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),
            ('FONTNAME', (1, 1), (-1, -1), 'REM-Regular'),
            ('FONTSIZE', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 2),  # Reducido de 6 a 3
            ('TOPPADDING', (0, 0), (-1, -1), 3),    # Añadido y ajustado a 3
            ('BACKGROUND', (0, 1), (-1, -2), colors.white),
            ('BACKGROUND', (0, -1), (-1, -1), colors.Color(157/255, 222/255, 220/255)),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]

    # Añadir la tabla al PDF
    pdf_supervision_mayo_2024.add_table_to_page(        
        cabecera, 
        tabla_escuelas_por_sup, 
        23,
        0,
        tableStyle)
 

    pdf_supervision_mayo_2024.save_pdf(output_pdf_path,)
    
    return output_pdf_path

def hacer_tercera_página(unaSupervisión):
    tercera_hoja = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas\Supervisiones Segunda Medición' + '/3-Página_Supervisión_-3.pdf'
    output_pdf_path = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\PDFsSupervisiones' + '\\' + fU.sanearNombresDeArchivos(str(unaSupervisión.Nombre_Supervisión)) +  '_F. L. 2024_2'  + '_3-Página-3' + '.pdf'
    pdf_supervision_mayo_2024 = PDF.PDFEditor(
        tercera_hoja ,
        unaSupervisión
    )
    pdf_supervision_mayo_2024.save_pdf(output_pdf_path,)  
    return output_pdf_path

def hacer_cuarta_página(unaSupervisión):
    cuarta_hoja = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas\Supervisiones Segunda Medición' + '/4-Página_Supervisión_-4.pdf'
    output_pdf_path = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\PDFsSupervisiones' + '\\' + fU.sanearNombresDeArchivos(str(unaSupervisión.Nombre_Supervisión)) +  '_F. L. 2024_2'  + '_4-Página-4' + '.pdf'
    pdf_supervision_agosto_2024 = PDF.PDFEditor(
        cuarta_hoja ,
        unaSupervisión
    )
    # Cantidad de estudiantes censados por escuela según nivel de desempeño
    # Datos de la tabla
    cabecera = ['Número', 'Nombre Escuela', 'Enlace al Informe']

    # ARMO LA TABLA ...
    tabla_enlaces = []
    for unaEscuela in unaSupervisión.get_listaDeObjetosEscuelaPorSupervision():
            row = [unaEscuela.Número_escuela , unaEscuela.Nombre_Escuela , unaEscuela.get_link_a_informe()]
            tabla_enlaces.append(row)

    tableStyle = [
            ('BACKGROUND', (0, 0), (-1, 0), colors.Color(49/255, 122/255, 138/255)),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),
            ('FONTNAME', (1, 1), (-1, -1), 'REM-Regular'),
            ('FONTSIZE', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 2),  # Reducido de 6 a 3
            ('TOPPADDING', (0, 0), (-1, -1), 3),    # Añadido y ajustado a 3
            ('BACKGROUND', (0, 1), (-1, -2), colors.white),
            ('BACKGROUND', (0, -1), (-1, -1), colors.white),            
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]

    # Añadir la tabla al PDF
    pdf_supervision_agosto_2024.add_table_to_page(        
        cabecera, 
        tabla_enlaces, 
        100,
        0,
        tableStyle,
        col_widths_mm=[10, 55, 120])

    pdf_supervision_agosto_2024.save_pdf(output_pdf_path,)  
    return output_pdf_path

def hacer_quinta_página(unaSupervisión):
    Diccionario_Informes = unaSupervisión.get_supervisión_Diccionario_Informes()
    
    tabla_escuelas_por_sup = Diccionario_Informes.get('FL_SUPERVISIÓN_009_cantidad_de_estudiantes_por_desempeño')
    nombreArchivo = Diccionario_Informes.get('FL_SUPERVISIÓN_007_desempeño_crítico_por_escuela___')
    
    quinta_hoja = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas\Supervisiones Segunda Medición' + '/5-Página_Supervisión_-5-vacía.pdf'
    output_pdf_path = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\PDFsSupervisiones' + '\\' + fU.sanearNombresDeArchivos(str(unaSupervisión.Nombre_Supervisión)) +  '_F. L. 2024_2'  + '_5-Página-5' + '.pdf'
    pdf_supervision_mayo_2024 = PDF.PDFEditor(
        quinta_hoja ,
        unaSupervisión
    )

    pdf_supervision_mayo_2024.add_text_to_page(
        'RESULTADOS DE TODOS LOS CURSOS CENSADOS', 
        (210, 260), 
        0,
        "REM-Bold", 12,
        color=(157, 222 , 220),
        align='center'
    )

    pdf_supervision_mayo_2024.add_text_to_page(
        'Proporción de estudiantes por escuela según nivel de desempeño en fluidez lectora', 
        (210, 250), 
        0,
        "REM-Regular", 10,
        color=(0, 0 , 0),
        align='center'
    )

    # inserto el gráfico de ese curso...
    pdf_supervision_mayo_2024.add_image_to_page(
        nombreArchivo, 
        (0,155,), 
        0 , 
        width_mm=180, 
        height_mm=100)
    
        
    pdf_supervision_mayo_2024.add_text_to_page(
        'Cantidad de estudiantes censados por escuela según nivel de desempeño', 
        (210, 140), 
        0,
        "REM-Regular", 10,
        color=(0, 0 , 0),
        align='center'
    )    
    
    # Datos de la tabla
    cabecera = ['Número', 'Nombre Escuela', 'Crítico' , 'Básico' , 'Medio' , 'Avanzado' , 'Censados/as']

    # tableStyle = [
    #         ('BACKGROUND', (0, 0), (-1, 0), colors.Color(49/255, 122/255, 138/255)),
    #         ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    #         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    #         ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),
    #         ('FONTNAME', (1, 1), (-1, -1), 'REM-Regular'),
    #         ('FONTSIZE', (0, 0), (-1, -1), 8),
    #         ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    #         ('BACKGROUND', (0, 1), (-1, -2), colors.white),
    #         ('BACKGROUND', (0, -1), (-1, -1), colors.Color(157/255, 222/255, 220/255)),
    #         ('GRID', (0, 0), (-1, -1), 1, colors.black),
    # ]

    tableStyle = [
            ('BACKGROUND', (0, 0), (-1, 0), colors.Color(49/255, 122/255, 138/255)),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),
            ('FONTNAME', (1, 1), (-1, -1), 'REM-Regular'),
            ('FONTSIZE', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 1),  # Reducido de 6 a 3
            ('TOPPADDING', (0, 0), (-1, -1), 1),    # Añadido y ajustado a 3
            ('BACKGROUND', (0, 1), (-1, -2), colors.white), 
            ('BACKGROUND', (0, -1), (-1, -1), colors.Color(157/255, 222/255, 220/255)),           
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]

    # Añadir la tabla al PDF
    pdf_supervision_mayo_2024.add_table_to_page(        
        cabecera, 
        tabla_escuelas_por_sup, 
        23,
        0,
        tableStyle)

    pdf_supervision_mayo_2024.save_pdf(output_pdf_path,)  
    return output_pdf_path

def hacer_resultados_por_curso_página(unaSupervisión):
    Diccionario_Informes = unaSupervisión.get_supervisión_Diccionario_Informes()
    diccionarioPorCursoGraficos = Diccionario_Informes.get('FL_SUPERVISIÓN_006_desempeño_crítico_por_escuela_curso')
    diccionarioPorCursoTablas = Diccionario_Informes.get('FL_SUPERVISIÓN_008_cantidad_de_estudiantes_por_desempeño_y_curso')

    nivel_grados = {
        'Primario': ['2°', '3°', '4°', '5°', '6°', '7°'],
        'Secundario Orientado': ['1°', '2°', '3°', '4°', '5°'],
        'Secundario Técnico': ['1°', '2°', '3°', '4°', '5°', '6°']
    }

    nivel_etiqueta = {
        'Primario': 'GRADO',
        'Secundario Orientado': 'AÑO',
        'Secundario Técnico': 'AÑO'
    }

    nivel_tipo = {
        'Primario': 'PRIMARIA',
        'Secundario Orientado': 'SECUNDARIA',
        'Secundario Técnico': 'SECUNDARIA'
    }

    lista_de_output_pdf_path = []

    nivel_original = unaSupervisión.NivelOriginal
    if nivel_original in nivel_grados:
        for grado in nivel_grados[nivel_original]:
            output_pdf_path = hoja_6(
                unaSupervisión,
                diccionarioPorCursoGraficos.get(f'{grado}_gráfico'),
                diccionarioPorCursoTablas.get(f'{grado}_lista_desempeño'),
                grado,
                nivel_etiqueta[nivel_original],
                nivel_tipo[nivel_original]                
            )
            lista_de_output_pdf_path.append(output_pdf_path)

    return lista_de_output_pdf_path


def hoja_6(unaSupervisión, gráfico , lista_desempeño , grado , nivel_etiqueta , nivel_tipo):
    sexta_hoja =  'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas\Supervisiones Segunda Medición' + '/5-Página_Supervisión_-5-vacía.pdf'
    output_pdf_path = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\PDFsSupervisiones' + '\\' + fU.sanearNombresDeArchivos(str(unaSupervisión.Nombre_Supervisión)) +  '_F. L. 2024_2'  + ' ' + grado + ' ' + '_6-Página-6' + '.pdf'
    pdf_supervision_mayo_2024 = PDF.PDFEditor(
        sexta_hoja ,
        unaSupervisión
    )

    pdf_supervision_mayo_2024.add_text_to_page(
        'RESULTADOS DE ' + grado + ' ' + nivel_etiqueta +  ' DE ' + nivel_tipo , 
        (210, 260), 
        0,
        "REM-Bold", 12,
        color=(157, 222 , 220),
        align='center'
    )

    pdf_supervision_mayo_2024.add_text_to_page(
        'Proporción de estudiantes por escuela según nivel de desempeño en fluidez lectora', 
        (210, 250), 
        0,
        "REM-Regular", 10,
        color=(0, 0 , 0),
        align='center'
    )

    # inserto el gráfico de ese curso...
    pdf_supervision_mayo_2024.add_image_to_page(
        gráfico, 
        (0,155,), 
        0 , 
        width_mm=180, 
        height_mm=100)
    
    pdf_supervision_mayo_2024.add_text_to_page(
        'Cantidad de estudiantes censados por escuela según nivel de desempeño', 
        (210, 140), 
        0,
        "REM-Regular", 10,
        color=(0, 0 , 0),
        align='center'
    )    
    
    # Datos de la tabla
    cabecera = ['Número', 'Nombre Escuela', 'Crítico' , 'Básico' , 'Medio' , 'Avanzado' , 'Censados/as']

    tableStyle = [
            ('BACKGROUND', (0, 0), (-1, 0), colors.Color(49/255, 122/255, 138/255)),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),
            ('FONTNAME', (1, 1), (-1, -1), 'REM-Regular'),
            ('FONTSIZE', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 1),  # Reducido de 6 a 3
            ('TOPPADDING', (0, 0), (-1, -1), 1),    # Añadido y ajustado a 3
            ('BACKGROUND', (0, 1), (-1, -2), colors.white),
            ('BACKGROUND', (0, -1), (-1, -1), colors.Color(157/255, 222/255, 220/255)),            
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]

    # Añadir la tabla al PDF
    pdf_supervision_mayo_2024.add_table_to_page(        
        cabecera, 
        lista_desempeño, 
        23,
        0,
        tableStyle)


    pdf_supervision_mayo_2024.save_pdf(output_pdf_path,)  
    return output_pdf_path

def hacer_séptima_página(unaSupervisión):    

    unaSupervisionConFluidezLectora = unaSupervisión
    Diccionario_Informes = unaSupervisión.get_supervisión_Diccionario_Informes()
    
    # obtengo el listado de escuelas de la supervisión
    listaDeObjetosEscuelas_Supervision = []
    listaDeObjetosEscuelas_Supervision = unaSupervisionConFluidezLectora.get_listaDeObjetosEscuelaPorSupervision()

    lista = []

    for unaEscuela in listaDeObjetosEscuelas_Supervision:
        listadoDeAlumnosCríticos = unaEscuela.get_escuela_Diccionario_Informes().get('tabla_CRITICOS_POR_ESCUELA')
        listado_de_casos_raros = unaEscuela.get_escuela_Diccionario_Informes().get('raras')
        # imprimo la hojas de los alumnos críticos siempre y cuando la lista no esté vacía
        if listadoDeAlumnosCríticos is not None :
            print('alumnos críticos...!!!')
            for alumno in listadoDeAlumnosCríticos:
                print(alumno)
            nombrePDF_críticos = hoja_8(unaSupervisión,unaEscuela,'LISTADO DE ESTUDIANTES EN NIVEL DE DESEMPEÑO CRÍTICO POR ESCUELA Y CURSO' , listadoDeAlumnosCríticos)
            lista.append(nombrePDF_críticos)
        # ahora imprimo los alumnos con casos raros siempre y cuando la lista no esté vacía        
        if listado_de_casos_raros is not None :
            print('alumnos raros...!!!')
            for alumno in listado_de_casos_raros:
                print(alumno)
            nombrePDF_inconsistentes = hoja_8(unaSupervisión,unaEscuela,'LISTADO DE ESTUDIANTES A OBSERVAR POR MEDICIÓN INCONSISTENTE' , listado_de_casos_raros)
            lista.append(nombrePDF_inconsistentes)    
    
    return lista # ya devuelve la lista

def hoja_8(unaSupervisión,unaEscuela,títuloDeLaTabla , listaDeAlumnos):
    cabecera = ['DNI', 'Apellido', 'Nombre', 'Número', 'Nombre Esc.', 'Curso', 'División', 'Cantidad de palabras']
    column_widths_mm = [15 , 40 , 40 , 35 , 70 , 17 , 25 , 25 ]  # anchos en milímetros
    
    tableStyle = [
        ('BACKGROUND', (0, 0), (-1, 0), colors.Color(157/255, 222/255, 220/255)),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Centrado vertical del título de las columnas de la tabla
        ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('FONTNAME', (0, 1), (-1, -1), 'REM-Regular'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]

    octava_hoja =  'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas\Supervisiones Segunda Medición' + '/5-Página-5-vacía-landscape.pdf'
    output_pdf_path = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\PDFsSupervisiones' + '\\' + fU.sanearNombresDeArchivos(str(unaSupervisión.Nombre_Supervisión)) +  '_F. L. 2024_2'  + '_8-Página-8_' + str(unaEscuela.Escuela_ID) + '.pdf'
    pdf_supervision_mayo_2024 = PDF.PDFEditor(
        octava_hoja ,
        unaSupervisión
    )

    # me tiene que devolver una lista de paths...para después poder buscarlos y unirlos..!
    listaDePaths = []    
    title_text = f"<b>"+títuloDeLaTabla+"</b>"

    pdf = pdf_supervision_mayo_2024.tabla_listado_grande(
        tableStyle,
        title_text,
        column_widths_mm,
        listaDeAlumnos,
        cabecera,
        octava_hoja,
        output_pdf_path
    )

    #

    return output_pdf_path #listaDePaths

def hacer_hoja_FL_SUPERVISIÓN_007_desempeño_general_de_toda_la_SUPERVISÓN(unaSupervisión):
    """
    diccionario_Diccionario_Informes['FL_SUPERVISIÓN_007_desempeño_general_de_toda_la_SUPERVISÓN_imágen'] = pathImagen
    diccionario_Diccionario_Informes['FL_SUPERVISIÓN_007_desempeño_general_de_toda_la_SUPERVISÓN_tabla_cantidad_de_alumnos_Supervisión'] = tabla_cantidad_de_alumnos_Supervisión
    """
    Diccionario_Informes = unaSupervisión.get_supervisión_Diccionario_Informes()
    gráfico = Diccionario_Informes.get('FL_SUPERVISIÓN_007_desempeño_general_de_toda_la_SUPERVISÓN_imágen')
    print('....gráfico... : ', gráfico)
    tabla_cantidad_de_alumnos_Supervisión = Diccionario_Informes.get('FL_SUPERVISIÓN_007_desempeño_general_de_toda_la_SUPERVISÓN_tabla_cantidad_de_alumnos_Supervisión')
    print(tabla_cantidad_de_alumnos_Supervisión)
    
    hoja_FL_SUPERVISIÓN_007_desempeño_general_de_toda_la_SUPERVISÓN =  'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas\Supervisiones Segunda Medición' + '/5-Página_Supervisión_-5-vacía.pdf'
    output_pdf_path = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\PDFsSupervisiones' + '\\' + fU.sanearNombresDeArchivos(str(unaSupervisión.Nombre_Supervisión)) +  '_F. L. 2024_2'  + ' '  + '_FL_SUPERVISIÓN_007_' + '.pdf'
    pdf_supervision_mayo_2024 = PDF.PDFEditor(
        hoja_FL_SUPERVISIÓN_007_desempeño_general_de_toda_la_SUPERVISÓN ,
        unaSupervisión
    )

    pdf_supervision_mayo_2024.add_text_to_page(
        'Comparativa de Desempeño entre la primera y tercera medición', 
        (210, 250), 
        0,
        "REM-Regular", 10,
        color=(0, 0 , 0),
        align='center'
    )

    # inserto el gráfico de ese curso...
    pdf_supervision_mayo_2024.add_image_to_page(
        gráfico, 
        (0,155,), 
        0 , 
        width_mm=180, 
        height_mm=100)
    
    pdf_supervision_mayo_2024.add_text_to_page(
        'Cantidad de estudiantes censados en la primera medición y la tercera del 2024', 
        (210, 140), 
        0,
        "REM-Regular", 10,
        color=(0, 0 , 0),
        align='center'
    )    
    

    # Tabla
    # ['DESEMPEÑO', '1er Medición Mayo 2024', '3er Medición Noviembre 2024']
    # [['Crítico', 774, 757], ['Básico', 1010, 996], ['Medio', 841, 707], ['Avanzado', 163, 162], ['Total', 2788, 2622]]

    # Datos de la tabla
    cabecera = ['DESEMPEÑO', '1er Medición Mayo 2024', '3er Medición Noviembre 2024' ]
    datos = tabla_cantidad_de_alumnos_Supervisión

    tableStyle = [
            ('BACKGROUND', (0, 0), (-1, 0), colors.Color(49/255, 122/255, 138/255)),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),
            ('FONTNAME', (1, 1), (-1, -1), 'REM-Regular'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),  # esto ajusta el espacio del texto dentro de la celda
            ('TOPPADDING', (0, 0), (-1, -1), 6),    # Añadido y ajustado a 3
            ('BACKGROUND', (0, 1), (-1, -2), colors.white),
            ('BACKGROUND', (0, -1), (-1, -1), colors.Color(157/255, 222/255, 220/255)),            
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]

    # Añadir la tabla al PDF
    pdf_supervision_mayo_2024.add_table_to_page(        
        cabecera, 
        datos, 
        100,
        0,
        tableStyle)


    pdf_supervision_mayo_2024.save_pdf(output_pdf_path,)  
    return output_pdf_path



# def hacer_hoja_sin_medición_mayo(unaEscuela):
#     hoja_sin_medición = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas' + '/2-Página-2 - SIN MEDICIÓN REGISTRADA en mayo.pdf'
#     output_pdf_path = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\PDFsEscuela' + '\\' + fU.sanearNombresDeArchivos(str(unaEscuela.Escuela_ID)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Número_escuela)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Nombre_Escuela)) + '_F. L. 2024_2'  + '_2-Página-2' + '.pdf'
#     pdf_agosto_2024 = PDF.PDFEditor(
#         hoja_sin_medición ,
#         unaEscuela
#     )
#     pdf_agosto_2024.save_pdf(output_pdf_path,)
#     return output_pdf_path


# def hacer_hoja_sin_medición_agosto(unaEscuela):
#     hoja_sin_medición = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas' + '/2-Página-2 - SIN MEDICIÓN REGISTRADA en agosto.pdf'
#     output_pdf_path = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\PDFsEscuela' + '\\' + fU.sanearNombresDeArchivos(str(unaEscuela.Escuela_ID)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Número_escuela)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Nombre_Escuela)) + '_F. L. 2024_2'  + '_2-Página-2' + '.pdf'
#     pdf_agosto_2024 = PDF.PDFEditor(
#         hoja_sin_medición ,
#         unaEscuela
#     )
#     pdf_agosto_2024.save_pdf(output_pdf_path,)
#     return output_pdf_path


# def hacer_tercera_página(unaEscuela):
#     # esta hoja se tiene que crear en caso de que la segunda se haya creado...
#     # si no tiene comparativa porque no tiene cargado para ningún curso, no debería
#     # crear esta página..!!
#     # SI PARA TODOS LOS CURSOS DE LA ESCUELA NO HAY COMPARATIVA, ENTONCES NO CREAR ESTA HOJA Y DEVOLVER None

#     diccionario_Informes = unaEscuela.get_escuela_Diccionario_Informes()
#     gráficos = diccionario_Informes.get('FL_ESCUELA_010_comparativa_según_progreso')
#     # obtengo la cantidad de claves para ese diccionario de gráficos 
#     # si para todas las claves el resultado es 'sin comparativa'
#     # entonces es que esa escuela no tuvo medición para poder comparar 
#     valores = list(gráficos.values())

#     # Verificar si todos los valores son iguales
#     if len(valores) < 2:
#         return True  # Si hay 0 o 1 valores, todos son iguales por defecto
    
#     primer_valor = valores[0]
    
#     for valor in valores[1:]:
    
#         if valor != primer_valor:
    
#             tercera_hoja = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas' + '/3-Página-3.pdf'
#             output_pdf_path = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\PDFsEscuela' + '\\' + fU.sanearNombresDeArchivos(str(unaEscuela.Escuela_ID)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Número_escuela)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Nombre_Escuela)) + '_F. L. 2024_2'  + '_3-Página-3.pdf' + '.pdf'
#             pdf_agosto_2024 = PDF.PDFEditor(
#                 tercera_hoja ,
#                 unaEscuela
#             )
#             pdf_agosto_2024.save_pdf(output_pdf_path,)
#         else:
#             output_pdf_path = None

#     return output_pdf_path

# def hacer_hoja_por_curso(unaEscuela):
#     # usamos las claves del diccionario tablas
#     # pero lo vamos a meter en un try..
#     try:
    
#         tableStyle = [
#                 ('BACKGROUND', (0, 0), (-1, 0), colors.Color(49/255, 122/255, 138/255)),
#                 ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#                 ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#                 ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),
#                 ('FONTNAME', (1, 1), (-1, -1), 'REM-Regular'),
#                 ('FONTSIZE', (0, 0), (-1, -1), 12),
#                 ('BOTTOMPADDING', (0, 0), (-1, -1), 6),  # Reducido de 6 a 3
#                 ('TOPPADDING', (0, 0), (-1, -1), 6),    # Añadido y ajustado a 3
#                 ('BACKGROUND', (0, 1), (-1, -2), colors.white),
#                 ('BACKGROUND', (0, -1), (-1, -1), colors.Color(157/255, 222/255, 220/255)),
#                 ('GRID', (0, 0), (-1, -1), 1, colors.black),
#         ]        

#         # Definir los colores deseados
#         color_columna_1 = colors.Color(32/255, 81/255, 89/255)  # "#205159"
#         color_columna_2 = colors.Color(48/255, 122/255, 138/255)  # "#307A8A"
#         color_columna_3 = colors.Color(74/255, 172/255, 174/255)  # "#4AACAE"
        
#         # Estilo de la tabla
#         tableStyle_datos_comparativa = [
#             ('BACKGROUND', (0, 0), (0, -1), color_columna_1),  # Color columna 1, incluyendo encabezado
#             ('BACKGROUND', (1, 0), (1, -1), color_columna_2),  # Color columna 2, incluyendo encabezado
#             ('BACKGROUND', (2, 0), (2, -1), color_columna_3),  # Color columna 3, incluyendo encabezado
#             ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),  # Color del texto blanco en todas las celdas
#             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#             ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),
#             ('FONTNAME', (1, 1), (-1, -1), 'REM-Regular'),
#             ('FONTSIZE', (0, 0), (-1, -1), 12),
#             ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
#             ('TOPPADDING', (0, 0), (-1, -1), 6),
#             ('GRID', (0, 0), (-1, -1), 1, colors.black),
#         ]
        
#         if unaEscuela.Nivel == 'Primario' :
#             gradoAño = 'grado'
#         else:
#             gradoAño = 'año'
#         hoja_vacía = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas' + '/4-Página-4-vacía.pdf'
#         diccionario = unaEscuela.get_escuela_Diccionario_Informes()

#         # tanto gráficos como tabla son diccionarios los dos..!
#         gráficos = diccionario.get('FL_ESCUELA_010_comparativa_según_progreso')
#         tablas = diccionario.get('FL_ESCUELA_009_tabla_cantidad_estudiantes_curso_y_desempeño_por_medicion_v2')    
#         matriculasNominalPorCurso = diccionario.get('FL_ESCUELA_000_cantidad_de_alumnos_por_curso_nominal_diccionario')
#         matriculasNominalFluidezLectoraPorCurso = diccionario.get('FL_ESCUELA_000_Cantidad de alumnos con DESEMPEÑO por curso fluidez_diccionario')
#         tabla_comparativa = diccionario.get('FL_ESCUELA_010_comparativa_según_progreso_tabla')
#         # for cla in list(diccionario.keys()):
#         #     print('claves :' , cla )
#         # print('matrículasPorCurso : ' , matriculasPorCurso)

#         # armo una lista donde voy a colocar las hojas de para cada uno de los informes
#         # la idea es que pueda devolver la lista para que se sepa donde está cada archivo
#         listaDePáginas = []
    
#         for cursos , gráfico in gráficos.items():
            
#             cabecera = []
#             # obtengo la cabecera
#             cabecera = tablas.get(cursos)[0]

#             # obtengo toda la tabla
#             datos = tablas.get(cursos)
#             # borrar la primera fila porque es la cabecera y ya la tengo
#             datos.pop(0)

#             # hago lo mismo con la tabla de las comparativas es para la tablita que sale debajo del gráfico para que se vean bien los números
#             cabecera_comparativa = []
#             # obtengo la cabecera
#             print('cursos : ----> : ', cursos)
#             cabecera_comparativa = tabla_comparativa.get(cursos)[0]

#             # obtengo toda la tabla
#             datos_comparativa = tabla_comparativa.get(cursos)
#             # borrar la primera fila porque es la cabecera y ya la tengo
#             datos_comparativa.pop(0)
            
#             # defino el path, cambia el curso
#             output_pdf_path = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\PDFsEscuela' + '\\' + fU.sanearNombresDeArchivos(str(unaEscuela.Escuela_ID)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Número_escuela)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Nombre_Escuela)) + '_F. L. 2024_2'  + '_4-Página-4-_' + cursos + '_.pdf'
#             # agrego la página
#             listaDePáginas.append(output_pdf_path)
#             # creo el pdf vacío
#             pdf_agosto_2024 = PDF.PDFEditor(
#                 hoja_vacía ,
#                 unaEscuela
#             )
#             # agrego la frase 'Resultados de xº grado de nnnn'
#             pdf_agosto_2024.add_text_to_page(
#                 'Resultados de ' + cursos + gradoAño +' de ' + unaEscuela.Nivel, 
#                 (20, 260), 
#                 0,
#                 "REM-Black", 12,
#                 color=(60, 180 , 229),
#                 align='left'
#             )
#             # agrego la frase 'Cantidad de estudiantes por medición'
#             pdf_agosto_2024.add_text_to_page(
#                 'Cantidad de estudiantes por medición', 
#                 (210, 250), 
#                 0,
#                 "REM-Regular", 12,
#                 color=(60, 180 , 229),
#                 align='center'
#             )
#             # Añadir la tabla al PDF
#             pdf_agosto_2024.add_table_to_page(        
#                 cabecera, 
#                 datos, 
#                 193,
#                 0,
#                 tableStyle)        
#             # inserto la leyenda debajo de la tabla
#             pdf_agosto_2024.add_text_to_page(
#                 'De la matrícula actual de ' + cursos + gradoAño + ' ' + str(matriculasNominalPorCurso.get(cursos)) + ' estudiantes, en la segunda medición se cuenta con registro de ' + str(matriculasNominalFluidezLectoraPorCurso.get(cursos)) + ' estudiantes.', 
#                 (0, 185), 
#                 0,
#                 "REM-Bold", 8,
#                 color=(0, 0 , 0),
#                 align='center'
#             )
#             # inserto la leyenda arriba del gráfico
#             pdf_agosto_2024.add_text_to_page(
#                 'Comparación entre primera y segunda medición del censo de Fluidez Lectora 2024. Cantidad de estudiantes por curso según progreso entre niveles de desempeño.', 
#                 (0, 163), 
#                 0,
#                 "REM-Regular", 12,
#                 color=(60, 180 , 229),
#                 align='center-multiline'
#             )
#             # inserto el gráfico de comparativa
#             pdf_agosto_2024.add_image_to_page(
#                 gráfico, 
#                 (0,80,), 
#                 0 , 
#                 width_mm=120, 
#                 height_mm=120)
#             # tabla comparativa
#             pdf_agosto_2024.add_table_to_page(        
#                 cabecera_comparativa, 
#                 datos_comparativa, 
#                 55,
#                 0,
#                 tableStyle_datos_comparativa)
#             # inserto la leyenda abajo de la tablita
#             pdf_agosto_2024.add_text_to_page(
#                 'El presente análisis se realiza sobre el total de los estudiantes que cuentan con registros en las mediciones de mayo y de agosto.', 
#                 (0, 40), 
#                 0,
#                 "REM-Regular", 12,
#                 color=(0, 0 , 0),
#                 align='center-multiline'
#             )

#             # grabo a esa página
#             pdf_agosto_2024.save_pdf(output_pdf_path,)
#     except:
#         pass

#     return listaDePáginas


def listado_alumnos_Con_DESEMPEÑO(unaEscuela):

    tableStyle = [
        ('BACKGROUND', (0, 0), (-1, 0), colors.Color(157/255, 222/255, 220/255)),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Centrado vertical del título de las columnas de la tabla
        ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('FONTNAME', (0, 1), (-1, -1), 'REM-Regular'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]
    
    if unaEscuela.Nivel == 'Primario' :
        gradoAño = 'grado'
    else:
        gradoAño = 'año'
    hoja_vacía = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas' + '/5-Página-5-vacía-landscape.pdf'    
    tipos_desempeño = ['Crítico','Básico','Medio','Avanzado']
    cabecera = [
        'DNI', 
        'Apellido', 
        'Nombre', 
        'Curso', 
        'Div.', 
        'Cant. palabras 1° medición', 
        'Cant. palabras 2° medición', 
        'Desempeño 2° medición',
        'Comparativa' 
    ]
    column_widths_mm = [18, 55, 55, 20 , 20, 25, 25, 25 , 35 ]  # anchos en milímetros

    diccionario = unaEscuela.get_escuela_Diccionario_Informes()
    diciconario_por_curso_alumnos = diccionario.get('FL_ESCUELA_011_listado_de_alumnos_por_curso_desempeño_y_comparativa')

    pdf_agosto_2024 = PDF.PDFEditor(    
        hoja_vacía ,
        unaEscuela
    )    

    # me tiene que devolver una lista de paths...para después poder buscarlos y unirlos..!
    listaDePaths = []
    alumnosPorDesempeño = {}
    for curso, diccionarioPorDesempeño in diciconario_por_curso_alumnos.items():        
        for desempeño in tipos_desempeño:
            alumnosPorDesempeño = diccionarioPorDesempeño.get(desempeño , {}) # por si no viene nada            
            #print(alumnosPorDesempeño)
            # solo hacemos el listado en caso de que haya desempeño            
            if len(alumnosPorDesempeño) > 0 :
                # print(curso)
                # print(desempeño)
                # print(alumnosPorDesempeño)
                title_text = f"<b>Listado de estudiantes de {curso} {gradoAño} con desempeño {desempeño}</b>"
                
                output_pdf_path = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\PDFsEscuela' + '\\' + fU.sanearNombresDeArchivos(str(unaEscuela.Escuela_ID)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Número_escuela)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Nombre_Escuela)) + '_F. L. 2024_1'  + '_5-Página-5_' + curso + '_' + desempeño +'_.pdf'
                pdfPorCurso = pdf_agosto_2024.tabla_listado_grande(
                    tableStyle,
                    title_text,
                    column_widths_mm,
                    alumnosPorDesempeño,
                    cabecera,
                    hoja_vacía,
                    output_pdf_path
                )
                listaDePaths.append(pdfPorCurso)

    return listaDePaths


def listado_alumnos_Incluidos_SI(unaEscuela):
    
    tableStyle = [
        ('BACKGROUND', (0, 0), (-1, 0), colors.Color(157/255, 222/255, 220/255)),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Centrado vertical del título de las columnas de la tabla
        ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('FONTNAME', (0, 1), (-1, -1), 'REM-Regular'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]
    cabecera = [
        'DNI' , 
        'Apellido' , 
        'Nombre' , 
        'Curso' , 
        'Div.' 
    ]
    column_widths_mm = [18, 55, 55, 20 , 20 ]  # anchos en milímetros
    
    
    if unaEscuela.Nivel == 'Primario' :
        gradoAño = 'grado'
    else:
        gradoAño = 'año'
    hoja_vacía = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas' + '/5-Página-5-vacía-landscape.pdf'    
    
   

    diccionario = unaEscuela.get_escuela_Diccionario_Informes()
    diciconario_por_curso_alumnos = diccionario.get('FL_ESCUELA_011_listado_de_alumnos_por_curso_Incluidos_SI')

    pdf_agosto_2024 = PDF.PDFEditor(    
        hoja_vacía ,
        unaEscuela
    )

    # me tiene que devolver una lista de paths...para después poder buscarlos y unirlos..!
    listaDePaths = []
    for curso, listadoSiIncluidos in diciconario_por_curso_alumnos.items():        
        #print(curso)
        #print(listadoSiIncluidos)
        title_text = f"<b>Listado de estudiantes de {curso} {gradoAño} incluidos Si</b>"
        output_pdf_path = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\PDFsEscuela' + '\\' + fU.sanearNombresDeArchivos(str(unaEscuela.Escuela_ID)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Número_escuela)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Nombre_Escuela)) + '_F. L. 2024_1'  + '_5-Página-5_' + curso + '_' + '_incluidos_Si' +'_.pdf'
        pdfPorCurso = pdf_agosto_2024.tabla_listado_grande(
            tableStyle,
            title_text,
            column_widths_mm,
            listadoSiIncluidos,
            cabecera,
            hoja_vacía,
            output_pdf_path
        )

        listaDePaths.append(pdfPorCurso)

    return listaDePaths

def listado_alumnos_cant_palabras_mayor_300(unaEscuela):
    tableStyle = [
        ('BACKGROUND', (0, 0), (-1, 0), colors.Color(157/255, 222/255, 220/255)),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Centrado vertical del título de las columnas de la tabla
        ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('FONTNAME', (0, 1), (-1, -1), 'REM-Regular'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]
    cabecera = [
        'DNI' , 
        'Apellido' , 
        'Nombre' , 
        'Curso' , 
        'Div.' ,
        'Cant. de palabras leídas' 
    ]
    column_widths_mm = [18, 55, 55, 20 , 30 , 20 , ]  # anchos en milímetros
    
    
    if unaEscuela.Nivel == 'Primario' :
        gradoAño = 'grado'
    else:
        gradoAño = 'año'
    hoja_vacía = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas' + '/5-Página-5-vacía-landscape.pdf'    

    diccionario = unaEscuela.get_escuela_Diccionario_Informes()
    diciconario_por_curso_alumnos = diccionario.get('FL_ESCUELA_011_listado_de_alumnos_por_curso_mayores_a_299')

    pdf_agosto_2024 = PDF.PDFEditor(    
        hoja_vacía ,
        unaEscuela
    )

    # me tiene que devolver una lista de paths...para después poder buscarlos y unirlos..!
    listaDePaths = []
    for curso, listadoSiIncluidos in diciconario_por_curso_alumnos.items():        
        #print(curso)
        #print(listadoSiIncluidos)
        title_text = f"<b>Listado de estudiantes de {curso} {gradoAño} con más de 300 palabras leídas</b>"
        output_pdf_path = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\PDFsEscuela' + '\\' + fU.sanearNombresDeArchivos(str(unaEscuela.Escuela_ID)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Número_escuela)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Nombre_Escuela)) + '_F. L. 2024_1'  + '_5-Página-5_' + curso + '_' + '_mayores_a_300_' +'_.pdf'
        pdfPorCurso = pdf_agosto_2024.tabla_listado_grande(
            tableStyle,
            title_text,
            column_widths_mm,
            listadoSiIncluidos,
            cabecera,
            hoja_vacía,
            output_pdf_path
        )

        listaDePaths.append(pdfPorCurso)

    return listaDePaths

def lista_de_archivo_listado_alumnos_sin_DESEMPEÑO(unaEscuela):
    tableStyle = [
        ('BACKGROUND', (0, 0), (-1, 0), colors.Color(157/255, 222/255, 220/255)),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Centrado vertical del título de las columnas de la tabla
        ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('FONTNAME', (0, 1), (-1, -1), 'REM-Regular'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]
    cabecera = [
        'DNI' , 
        'Apellido' , 
        'Nombre' , 
        'Curso' , 
        'Div.',
        'Desempeño' 
    ]
    column_widths_mm = [18, 55, 55, 20 , 30 , 35 ]  # anchos en milímetros
    
    
    if unaEscuela.Nivel == 'Primario' :
        gradoAño = 'grado'
    else:
        gradoAño = 'año'
    hoja_vacía = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas' + '/5-Página-5-vacía-landscape.pdf'    
       

    diccionario = unaEscuela.get_escuela_Diccionario_Informes()
    diciconario_por_curso_alumnos = diccionario.get('FL_ESCUELA_011_listado_de_alumnos_por_curso_sin_DESEMPEÑO')

    pdf_agosto_2024 = PDF.PDFEditor(    
        hoja_vacía ,
        unaEscuela
    )

    # me tiene que devolver una lista de paths...para después poder buscarlos y unirlos..!
    listaDePaths = []
    for curso, listadoSiIncluidos in diciconario_por_curso_alumnos.items():        
        #print(curso)
        #print(listadoSiIncluidos)
        title_text = f"<b>Listado de estudiantes de {curso} {gradoAño} sin desempeño</b>"
        output_pdf_path = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\PDFsEscuela' + '\\' + fU.sanearNombresDeArchivos(str(unaEscuela.Escuela_ID)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Número_escuela)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Nombre_Escuela)) + '_F. L. 2024_1'  + '_5-Página-5_' + curso + '_' + '_sin_DESEMPEÑO_' +'_.pdf'
        pdfPorCurso = pdf_agosto_2024.tabla_listado_grande(
            tableStyle,
            title_text,
            column_widths_mm,
            listadoSiIncluidos,
            cabecera,
            hoja_vacía,
            output_pdf_path
        )

        listaDePaths.append(pdfPorCurso)

    return listaDePaths


def unirPDFs(unaEscuela,pdf_paths, output_pdf_path):
    hoja_vacía = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas\Supervisiones Segunda Medición' + '/4-Página-4-vacía.pdf'
    pdf_agosto_2024 = PDF.PDFEditor(
        hoja_vacía ,
        unaEscuela
    ) 
    
    pdf_agosto_2024.fusionar_pdfs(
        output_pdf_path,
        pdf_paths,        
    )
    return

def borrar_archivos(lista_de_rutas):
    """
    Elimina los archivos especificados en la lista de rutas.

    Args:
        lista_de_rutas (list): Lista de rutas de archivos a eliminar.
    """
    for ruta in lista_de_rutas:
        try:
            os.remove(ruta)
            print(f"Archivo eliminado: {ruta}")
        except FileNotFoundError:
            print(f"Error: El archivo no encontrado {ruta}")
        except PermissionError:
            print(f"Error: Permiso denegado para eliminar {ruta}")
        except Exception as e:
            print(f"Error al eliminar {ruta}: {e}")
