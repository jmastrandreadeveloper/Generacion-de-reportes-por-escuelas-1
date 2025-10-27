import PDFEditor as PDF
import config as cf
import funcionesUtiles as fU
import os
from reportlab.lib import colors

def hacer_carátula(unaEscuela):
    print('escuelas..!!!')
    pdf_agosto_2024 = PDF.PDFEditor('D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas\Escuelas' + '/1-Carátula-1.pdf' ,
                                            unaEscuela
    )    
    pdf_agosto_2024.add_text_to_page(
        'Escuela N° : ' + unaEscuela.Número_escuela, 
        (30, 80), 
        0, 
        "REM-Regular", 25,
        color=(0, 15, 159),
        align='left'
    )
    pdf_agosto_2024.add_text_to_page(
        unaEscuela.Nombre_Escuela[:31], 
        (30, 70), 
        0,
        "REM-Black", 25,
        color=(0, 15, 159),
        align='left'
    )
    pdfFile = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\PDFsEscuela' + '\\' + fU.sanearNombresDeArchivos(str(unaEscuela.Escuela_ID)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Número_escuela)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Nombre_Escuela)) + '_F. L. 2024_2'  + '_1-Carátula-1' + '.pdf'
    pdf_agosto_2024.save_pdf(pdfFile,)

    return pdfFile


def hacer_segunda_página(unaEscuela):
        
    Diccionario_Informes = unaEscuela.get_escuela_Diccionario_Informes()
    tabla_cantidad_de_alumnos_por_curso = Diccionario_Informes.get('Tabla Alcance de la medición en su establecimiento')
    porcentajeEstudiantesEvaluadosRespectoAlNominal = Diccionario_Informes.get('Porcentaje de carga en GEM')
    
    segunda_hoja = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas\Escuelas' + '/2-Página-2-Javi.pdf'
    output_pdf_path = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\PDFsEscuela' + '\\' + fU.sanearNombresDeArchivos(str(unaEscuela.Escuela_ID)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Número_escuela)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Nombre_Escuela)) + '_F. L. 2024_2'  + '_2-Página-2' + '.pdf'
    pdf_agosto_2024 = PDF.PDFEditor(
        segunda_hoja ,
        unaEscuela
    )

    #print(tabla_cantidad_de_alumnos_por_curso)
    cabecera = []
    cabecera = tabla_cantidad_de_alumnos_por_curso[0]
    
    datos = tabla_cantidad_de_alumnos_por_curso

    # borrar la primera fila porque es la cabecera y ya la tengo
    datos.pop(0)

    # en la tabla datos o en la tablaAuxiliar se encuentran los totales que debemos usar para sacar el pocentaje
    # Accede a la última fila
    

    # Suponiendo que ultima_fila contiene algo como ['Cantidad de estudiantes de Total', 150, 300],
    # donde 150 podría ser el número de alumnos que aprobaron y 300 el total de alumnos.

    # Extrae los valores necesarios para el cálculo
    # Accede a la última fila
    # ultima_fila = tabla_cantidad_de_alumnos_por_curso[-1]    
    # dos_ultimos_elementos = ultima_fila[-2:]    
    # censados = dos_ultimos_elementos[0]
    # matrícula = dos_ultimos_elementos[1]
    # porcentaje = (censados/matrícula) * 100

    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    #
    # BORRAR LA ULTIMA COLUMNA DE LA TABLA PARA QUE NO SE GENERE CONFUSIÓN SOBRE SEGÚN LO QUE CHARLAMOS CON JAVIER, 
    # ESA COLUMNA ES LA QUE MUESTRA EL NOMINAL O SEA ES EL NOMINAL POR CURSO PERO NO SE TOMA DEL DE FLUIDEZ, SE TOMA DEL ARCHIVO NOMINAL !!!!!!
    #
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################

    
    # quito el último elemento de la cabecera
    #cabecera = cabecera[:-1]
    # quito todos los últimos elementos de cada fila de la lista de listas de datos
    #datos = [sublista[:-1] for sublista in datos]
    
    print(cabecera)
    for row in datos: 
        print(row)

    

        
    tableStyle = [
        ('BACKGROUND', (0, 0), (-1, 0), colors.Color(49/255, 122/255, 138/255)),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),
        ('FONTNAME', (1, 1), (-1, -1), 'REM-Regular'),
        ('FONTSIZE', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),  # Reducido de 6 a 3
        ('TOPPADDING', (0, 0), (-1, -1), 6),    # Añadido y ajustado a 3
        ('BACKGROUND', (0, 1), (-1, -2), colors.white),
        ('BACKGROUND', (0, -1), (-1, -1), colors.Color(157/255, 222/255, 220/255)),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 0), (-1, 0), 6),       # Tamaño de letra más pequeño para el encabezado
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke)  # Color de texto blanco para el encabezado
    ]    

    pdf_agosto_2024.add_text_to_page(
        'Cantidad de estudiantes censado/as en su establecimiento en tercera medición 2024', 
        (210, 120), 
        0,
        "REM-Regular", 10,
        color=(0, 0 , 0),
        align='center'
    )

    pdf_agosto_2024.add_table_to_page_v2(        
        cabecera, # cabecera,    
        datos , # datos, 
        160,
        0,
        tableStyle)
    
    # agrego la frase debajo de la tabla 'Este informe se realiza el 20/05/2024 en base al …% de carga registrada en GEM.'
    pdf_agosto_2024.add_text_to_page(
        'Este informe se realizó el 09/12/2024 en base al ' + str(round(porcentajeEstudiantesEvaluadosRespectoAlNominal)) + ' % de carga registrada en GEM.', 
        (210, 48), 
        0,
        "REM-Regular", 10,
        color=(0, 0 , 0),
        align='center'
    )

    pdf_agosto_2024.save_pdf(output_pdf_path,)
    
    return output_pdf_path

def hacer_segunda_página_SinPrimerOperativoyConSegundoOperativo(unaEscuela):
        
    Diccionario_Informes = unaEscuela.get_escuela_Diccionario_Informes()
    tabla_cantidad_de_alumnos_por_curso = Diccionario_Informes.get('Tabla Alcance de la medición en su establecimiento')
    porcentajeEstudiantesEvaluadosRespectoAlNominal = Diccionario_Informes.get('Porcentaje de carga en GEM')
    
    segunda_hoja = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas\Escuelas' + '/2-Página-2-Javi- 3º Medición sin primera.pdf'
    output_pdf_path = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\PDFsEscuela' + '\\' + fU.sanearNombresDeArchivos(str(unaEscuela.Escuela_ID)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Número_escuela)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Nombre_Escuela)) + '_F. L. 2024_2'  + '_2-Página-2-Javi- 2º Medición sin primera' + '.pdf'
    pdf_agosto_2024 = PDF.PDFEditor(
        segunda_hoja ,
        unaEscuela
    )

    #print(tabla_cantidad_de_alumnos_por_curso)
    cabecera = []
    cabecera = tabla_cantidad_de_alumnos_por_curso[0]
    
    datos = tabla_cantidad_de_alumnos_por_curso

    # borrar la primera fila porque es la cabecera y ya la tengo
    datos.pop(0)

    # en la tabla datos o en la tablaAuxiliar se encuentran los totales que debemos usar para sacar el pocentaje
    # Accede a la última fila
    

    # Suponiendo que ultima_fila contiene algo como ['Cantidad de estudiantes de Total', 150, 300],
    # donde 150 podría ser el número de alumnos que aprobaron y 300 el total de alumnos.

    # Extrae los valores necesarios para el cálculo
    # Accede a la última fila
    # ultima_fila = tabla_cantidad_de_alumnos_por_curso[-1]    
    # dos_ultimos_elementos = ultima_fila[-2:]    
    # censados = dos_ultimos_elementos[0]
    # matrícula = dos_ultimos_elementos[1]
    # porcentaje = (censados/matrícula) * 100

    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################
    #
    # BORRAR LA ULTIMA COLUMNA DE LA TABLA PARA QUE NO SE GENERE CONFUSIÓN SOBRE SEGÚN LO QUE CHARLAMOS CON JAVIER, 
    # ESA COLUMNA ES LA QUE MUESTRA EL NOMINAL O SEA ES EL NOMINAL POR CURSO PERO NO SE TOMA DEL DE FLUIDEZ, SE TOMA DEL ARCHIVO NOMINAL !!!!!!
    #
    ##############################################################################################################################################
    ##############################################################################################################################################
    ##############################################################################################################################################

    
    # quito el último elemento de la cabecera
    #cabecera = cabecera[:-1]
    # quito todos los últimos elementos de cada fila de la lista de listas de datos
    #datos = [sublista[:-1] for sublista in datos]
    
    print(cabecera)
    for row in datos: 
        print(row)

    

        
    tableStyle = [
        ('BACKGROUND', (0, 0), (-1, 0), colors.Color(49/255, 122/255, 138/255)),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),
        ('FONTNAME', (1, 1), (-1, -1), 'REM-Regular'),
        ('FONTSIZE', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),  # Reducido de 6 a 3
        ('TOPPADDING', (0, 0), (-1, -1), 6),    # Añadido y ajustado a 3
        ('BACKGROUND', (0, 1), (-1, -2), colors.white),
        ('BACKGROUND', (0, -1), (-1, -1), colors.Color(157/255, 222/255, 220/255)),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 0), (-1, 0), 6),       # Tamaño de letra más pequeño para el encabezado
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke)  # Color de texto blanco para el encabezado
    ]    

    pdf_agosto_2024.add_text_to_page(
        'Cantidad de estudiantes censado/as en su establecimiento en tercera medición 2024', 
        (210, 120), 
        0,
        "REM-Regular", 10,
        color=(0, 0 , 0),
        align='center'
    )

    pdf_agosto_2024.add_table_to_page_v2(        
        cabecera, # cabecera,    
        datos , # datos, 
        170,
        0,
        tableStyle)
    
    # agrego la frase debajo de la tabla 'Este informe se realiza el 20/05/2024 en base al …% de carga registrada en GEM.'
    pdf_agosto_2024.add_text_to_page(
        'Este informe se realiza el 02/12/2024 en base al ' + str(round(porcentajeEstudiantesEvaluadosRespectoAlNominal)) + ' % de carga registrada en GEM.', 
        (210, 48), 
        0,
        "REM-Regular", 10,
        color=(0, 0 , 0),
        align='center'
    )

    pdf_agosto_2024.save_pdf(output_pdf_path,)
    
    return output_pdf_path


def hacer_hoja_sin_medición_mayo(unaEscuela):
    hoja_sin_medición = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas\Escuelas' + '/2-Página-2 - SIN MEDICIÓN REGISTRADA en mayo.pdf'
    output_pdf_path = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\PDFsEscuela' + '\\' + fU.sanearNombresDeArchivos(str(unaEscuela.Escuela_ID)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Número_escuela)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Nombre_Escuela)) + '_F. L. 2024_2'  + '_2-Página-2' + '.pdf'
    pdf_agosto_2024 = PDF.PDFEditor(
        hoja_sin_medición ,
        unaEscuela
    )
    pdf_agosto_2024.save_pdf(output_pdf_path,)
    return output_pdf_path


def hacer_hoja_sin_medición_agosto(unaEscuela):
    hoja_sin_medición = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas\Escuelas' + '/2-Página-2 - SIN MEDICIÓN REGISTRADA en Noviembre.pdf'
    output_pdf_path = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\PDFsEscuela' + '\\' + fU.sanearNombresDeArchivos(str(unaEscuela.Escuela_ID)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Número_escuela)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Nombre_Escuela)) + '_F. L. 2024_2'  + '_2-Página-2' + '.pdf'
    pdf_agosto_2024 = PDF.PDFEditor(
        hoja_sin_medición ,
        unaEscuela
    )
    pdf_agosto_2024.save_pdf(output_pdf_path,)
    return output_pdf_path


# def hacer_tercera_página(unaEscuela):
#     # esta hoja se tiene que crear en caso de que la tercera se haya creado...
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
    
#             tercera_hoja = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas\Escuelas' + '/3-Página-3.pdf'
#             output_pdf_path = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\PDFsEscuela' + '\\' + fU.sanearNombresDeArchivos(str(unaEscuela.Escuela_ID)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Número_escuela)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Nombre_Escuela)) + '_F. L. 2024_2'  + '_3-Página-3' + '.pdf'
#             pdf_agosto_2024 = PDF.PDFEditor(
#                 tercera_hoja ,
#                 unaEscuela
#             )
#             pdf_agosto_2024.save_pdf(output_pdf_path,)
#         else:
#             output_pdf_path = None

#     print('hacer_tercera_página ' , output_pdf_path)
#     return output_pdf_path

def hacer_tercera_página(unaEscuela):   
    
    tercera_hoja = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas\Escuelas' + '/3-Página-3.pdf'
    output_pdf_path = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\PDFsEscuela' + '\\' + fU.sanearNombresDeArchivos(str(unaEscuela.Escuela_ID)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Número_escuela)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Nombre_Escuela)) + '_F. L. 2024_2'  + '_3-Página-3' + '.pdf'
    pdf_agosto_2024 = PDF.PDFEditor(
        tercera_hoja ,
        unaEscuela
    )
    pdf_agosto_2024.save_pdf(output_pdf_path,)

    return output_pdf_path

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
#         hoja_vacía = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas\Escuelas' + '/4-Página-4-vacía.pdf'
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

#             print('--------- hacer_hoja_por_curso ' , cursos , ' ' , gráfico)
            
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
#             # # inserto la leyenda debajo de la tabla
#             # # SE QUITA A PEDIDO DE JAVIER
#             # pdf_agosto_2024.add_text_to_page(
#             #     'De la matrícula actual de ' + cursos + gradoAño + ' ' + str(matriculasNominalPorCurso.get(cursos)) + ' estudiantes, en la tercera medición se cuenta con registro de ' + str(matriculasNominalFluidezLectoraPorCurso.get(cursos)) + ' estudiantes.', 
#             #     (0, 185), 
#             #     0,
#             #     "REM-Bold", 8,
#             #     color=(0, 0 , 0),
#             #     align='center'
#             # )
#             # inserto la leyenda arriba del gráfico
#             pdf_agosto_2024.add_text_to_page(
#                 'Comparación entre primera y tercera medición del censo de Fluidez Lectora 2024. Cantidad de estudiantes por curso según progreso entre niveles de desempeño.', 
#                 (0, 180), # 163 
#                 0,
#                 "REM-Regular", 12,
#                 color=(60, 180 , 229),
#                 align='center-multiline'
#             )
#             # inserto el gráfico de comparativa
#             pdf_agosto_2024.add_image_to_page(
#                 gráfico, 
#                 (0,90,), # 80 
#                 0 , 
#                 width_mm=85, # 120 
#                 height_mm=85) # 120
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

#     print('hacer_hoja_por_curso ' , listaDePáginas)

#     return listaDePáginas

def hacer_tercera_página_SinPrimerOperativoyConSegundoOperativo(unaEscuela):   
    
    tercera_hoja = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas\Escuelas' + '/3-Página-3 - 2º Medición sin primera.pdf'
    output_pdf_path = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\PDFsEscuela' + '\\' + fU.sanearNombresDeArchivos(str(unaEscuela.Escuela_ID)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Número_escuela)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Nombre_Escuela)) + '_F. L. 2024_2'  + '_3-Página-3 - 2º Medición sin primera' + '.pdf'
    pdf_agosto_2024 = PDF.PDFEditor(
        tercera_hoja ,
        unaEscuela
    )
    pdf_agosto_2024.save_pdf(output_pdf_path,)

    return output_pdf_path

def hacer_hoja_por_curso(unaEscuela):
    # usamos las claves del diccionario tablas
    
    
    tableStyle = [
            ('BACKGROUND', (0, 0), (-1, 0), colors.Color(49/255, 122/255, 138/255)),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),
            ('FONTNAME', (1, 1), (-1, -1), 'REM-Regular'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),  # Reducido de 6 a 3
            ('TOPPADDING', (0, 0), (-1, -1), 6),    # Añadido y ajustado a 3
            ('BACKGROUND', (0, 1), (-1, -2), colors.white),
            ('BACKGROUND', (0, -1), (-1, -1), colors.Color(157/255, 222/255, 220/255)),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]        

    # Definir los colores deseados
    color_columna_1 = colors.Color(32/255, 81/255, 89/255)  # "#205159"
    color_columna_2 = colors.Color(48/255, 122/255, 138/255)  # "#307A8A"
    color_columna_3 = colors.Color(74/255, 172/255, 174/255)  # "#4AACAE"
    
    # Estilo de la tabla
    tableStyle_datos_comparativa = [
        ('BACKGROUND', (0, 0), (0, -1), color_columna_1),  # Color columna 1, incluyendo encabezado
        ('BACKGROUND', (1, 0), (1, -1), color_columna_2),  # Color columna 2, incluyendo encabezado
        ('BACKGROUND', (2, 0), (2, -1), color_columna_3),  # Color columna 3, incluyendo encabezado
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),  # Color del texto blanco en todas las celdas
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),
        ('FONTNAME', (1, 1), (-1, -1), 'REM-Regular'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]
    
    if unaEscuela.Nivel == 'Primario' :
        gradoAño = 'grado'
    else:
        gradoAño = 'año'
    hoja_vacía = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas\Escuelas' + '/4-Página-4-vacía.pdf'
    diccionario = unaEscuela.get_escuela_Diccionario_Informes()

    # tanto gráficos como tabla son diccionarios los dos..!
    gráficos = diccionario.get('FL_ESCUELA_010_comparativa_según_progreso')
    tablas = diccionario.get('FL_ESCUELA_009_tabla_cantidad_estudiantes_curso_y_desempeño_por_medicion_v2')    
    matriculasNominalPorCurso = diccionario.get('FL_ESCUELA_000_cantidad_de_alumnos_por_curso_nominal_diccionario')
    matriculasNominalFluidezLectoraPorCurso = diccionario.get('FL_ESCUELA_000_Cantidad de alumnos con DESEMPEÑO por curso fluidez_diccionario')
    tabla_comparativa = diccionario.get('FL_ESCUELA_010_comparativa_según_progreso_tabla')
    # for cla in list(diccionario.keys()):
    #     print('claves :' , cla )
    # print('matrículasPorCurso : ' , matriculasPorCurso)

    # armo una lista donde voy a colocar las hojas de para cada uno de los informes
    # la idea es que pueda devolver la lista para que se sepa donde está cada archivo
    listaDePáginas = []

    for cursos , gráfico in gráficos.items():

        print('--------- hacer_hoja_por_curso ' , cursos , ' ' , gráfico)
        
        cabecera = []
        # obtengo la cabecera
        cabecera = tablas.get(cursos)[0]

        # obtengo toda la tabla
        datos = tablas.get(cursos)
        # borrar la primera fila porque es la cabecera y ya la tengo
        datos.pop(0)

        # hago lo mismo con la tabla de las comparativas es para la tablita que sale debajo del gráfico para que se vean bien los números
        cabecera_comparativa = []
        # obtengo la cabecera
        print('cursos : ----> : ', cursos)
        if gráfico != 'sin comparativa':
            cabecera_comparativa = tabla_comparativa.get(cursos)[0]

            # obtengo toda la tabla
            datos_comparativa = tabla_comparativa.get(cursos)
            # borrar la primera fila porque es la cabecera y ya la tengo
            datos_comparativa.pop(0)
            
            # defino el path, cambia el curso
            output_pdf_path = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\PDFsEscuela' + '\\' + fU.sanearNombresDeArchivos(str(unaEscuela.Escuela_ID)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Número_escuela)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Nombre_Escuela)) + '_F. L. 2024_2'  + '_4-Página-4-_' + cursos + '_.pdf'
            # agrego la página
            listaDePáginas.append(output_pdf_path)
            # creo el pdf vacío
            pdf_agosto_2024 = PDF.PDFEditor(
                hoja_vacía ,
                unaEscuela
            )
            # agrego la frase 'Resultados de xº grado de nnnn'
            pdf_agosto_2024.add_text_to_page(
                'Resultados de ' + cursos + ' ' + gradoAño +' de ' + unaEscuela.Nivel, 
                (20, 260), 
                0,
                "REM-Black", 12,
                color=(60, 180 , 229),
                align='left'
            )
            # agrego la frase 'Cantidad de estudiantes por medición'
            pdf_agosto_2024.add_text_to_page(
                'Cantidad de estudiantes por medición', 
                (210, 250), 
                0,
                "REM-Regular", 12,
                color=(60, 180 , 229),
                align='center'
            )
            # Añadir la tabla al PDF
            pdf_agosto_2024.add_table_to_page(        
                cabecera, 
                datos, 
                193,
                0,
                tableStyle)        
            # # inserto la leyenda debajo de la tabla
            # # SE QUITA A PEDIDO DE JAVIER
            # pdf_agosto_2024.add_text_to_page(
            #     'De la matrícula actual de ' + cursos + gradoAño + ' ' + str(matriculasNominalPorCurso.get(cursos)) + ' estudiantes, en la tercera medición se cuenta con registro de ' + str(matriculasNominalFluidezLectoraPorCurso.get(cursos)) + ' estudiantes.', 
            #     (0, 185), 
            #     0,
            #     "REM-Bold", 8,
            #     color=(0, 0 , 0),
            #     align='center'
            # )
            # inserto la leyenda arriba del gráfico
            pdf_agosto_2024.add_text_to_page(
                'Comparación entre primera y tercera medición del censo de Fluidez Lectora 2024. Cantidad de estudiantes por curso según progreso entre niveles de desempeño.', 
                (0, 180), # 163 
                0,
                "REM-Regular", 12,
                color=(60, 180 , 229),
                align='center-multiline'
            )
            # inserto el gráfico de comparativa
            pdf_agosto_2024.add_image_to_page(
                gráfico, 
                (0,90,), # 80 
                0 , 
                width_mm=85, # 120 
                height_mm=85) # 120
            # tabla comparativa
            pdf_agosto_2024.add_table_to_page(        
                cabecera_comparativa, 
                datos_comparativa, 
                55,
                0,
                tableStyle_datos_comparativa)
            # inserto la leyenda abajo de la tablita
            pdf_agosto_2024.add_text_to_page(
                'El presente análisis se realiza sobre el total de los estudiantes que cuentan con registros en las mediciones de Mayo y de Noviembre.', 
                (0, 40), 
                0,
                "REM-Regular", 12,
                color=(0, 0 , 0),
                align='center-multiline'
            )

            # grabo a esa página
            pdf_agosto_2024.save_pdf(output_pdf_path,)
    

    print('hacer_hoja_por_curso ' , listaDePáginas)

    return listaDePáginas

def hacer_hoja_por_curso_SinPrimerOperativoyConSegundoOperativo(unaEscuela):

    # usamos las claves del diccionario tablas
    
    
    tableStyle = [
            ('BACKGROUND', (0, 0), (-1, 0), colors.Color(49/255, 122/255, 138/255)),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),
            ('FONTNAME', (1, 1), (-1, -1), 'REM-Regular'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),  # Reducido de 6 a 3
            ('TOPPADDING', (0, 0), (-1, -1), 6),    # Añadido y ajustado a 3
            ('BACKGROUND', (0, 1), (-1, -2), colors.white),
            ('BACKGROUND', (0, -1), (-1, -1), colors.Color(157/255, 222/255, 220/255)),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]        

    # Definir los colores deseados
    #color_columna_1 = colors.Color(32/255, 81/255, 89/255)  # "#205159"
    #color_columna_2 = colors.Color(48/255, 122/255, 138/255)  # "#307A8A"
    #color_columna_3 = colors.Color(74/255, 172/255, 174/255)  # "#4AACAE"
    
    # Estilo de la tabla
    # tableStyle_datos_comparativa = [
    #     ('BACKGROUND', (0, 0), (0, -1), color_columna_1),  # Color columna 1, incluyendo encabezado
    #     ('BACKGROUND', (1, 0), (1, -1), color_columna_2),  # Color columna 2, incluyendo encabezado
    #     ('BACKGROUND', (2, 0), (2, -1), color_columna_3),  # Color columna 3, incluyendo encabezado
    #     ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),  # Color del texto blanco en todas las celdas
    #     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    #     ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),
    #     ('FONTNAME', (1, 1), (-1, -1), 'REM-Regular'),
    #     ('FONTSIZE', (0, 0), (-1, -1), 12),
    #     ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    #     ('TOPPADDING', (0, 0), (-1, -1), 6),
    #     ('GRID', (0, 0), (-1, -1), 1, colors.black),
    # ]
    
    if unaEscuela.Nivel == 'Primario' :
        gradoAño = 'grado'
    else:
        gradoAño = 'año'
    hoja_vacía = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas\Escuelas' + '/4-Página-4-vacía.pdf'
    diccionario = unaEscuela.get_escuela_Diccionario_Informes()

    # tanto gráficos como tabla son diccionarios los dos..!
    gráficos = diccionario.get('FL_ESCUELA_002_desempeño_por_curso_segundo_op_gráfico')
    print(gráficos)    
    tablas = diccionario.get('FL_ESCUELA_002_desempeño_por_curso_segundo_op_tabla')    
    print(tablas)
    
   

    # armo una lista donde voy a colocar las hojas de para cada uno de los informes
    # la idea es que pueda devolver la lista para que se sepa donde está cada archivo
    listaDePáginas = []

    for cursos , gráfico in gráficos.items():

        print('--------- hacer_hoja_por_curso ' , cursos , ' ' , gráfico)
        
        cabecera = []
        # obtengo la cabecera
        cabecera = tablas.get(cursos)[0]

        # obtengo toda la tabla
        datos = tablas.get(cursos)
        # borrar la primera fila porque es la cabecera y ya la tengo
        #datos.pop(0)

        # hago lo mismo con la tabla de las comparativas es para la tablita que sale debajo del gráfico para que se vean bien los números
        cabecera = []
        # obtengo la cabecera
        print('cursos : ----> : ', cursos)
        
        cabecera = tablas.get(cursos)[0]

        # obtengo toda la tabla
        datos = tablas.get(cursos)
        # borrar la primera fila porque es la cabecera y ya la tengo
        datos.pop(0)
        
        # defino el path, cambia el curso
        output_pdf_path = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\PDFsEscuela' + '\\' + fU.sanearNombresDeArchivos(str(unaEscuela.Escuela_ID)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Número_escuela)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Nombre_Escuela)) + '_F. L. 2024_2'  + '_4-Página-4-_' + cursos + '_.pdf'
        # agrego la página
        listaDePáginas.append(output_pdf_path)
        # creo el pdf vacío
        pdf_agosto_2024 = PDF.PDFEditor(
            hoja_vacía ,
            unaEscuela
        )
        # agrego la frase 'Resultados de xº grado de nnnn'
        pdf_agosto_2024.add_text_to_page(
            'Resultados de ' + cursos + ' ' + gradoAño +' de ' + unaEscuela.Nivel, 
            (20, 260), 
            0,
            "REM-Black", 12,
            color=(60, 180 , 229),
            align='left'
        )
        # agrego la frase 'Cantidad de estudiantes por medición'
        pdf_agosto_2024.add_text_to_page(
            'Cantidad de estudiantes por desempeño', 
            (210, 250), 
            0,
            "REM-Regular", 12,
            color=(60, 180 , 229),
            align='center'
        )
        # Añadir la tabla al PDF
        pdf_agosto_2024.add_table_to_page(        
            cabecera, 
            datos, 
            193,
            0,
            tableStyle)        
        
        # inserto la leyenda arriba del gráfico
        pdf_agosto_2024.add_text_to_page(
            'Porcentajes de desempeño.', 
            (0, 180), # 163 
            0,
            "REM-Regular", 12,
            color=(60, 180 , 229),
            align='center-multiline'
        )
        # inserto el gráfico de comparativa
        pdf_agosto_2024.add_image_to_page(
            gráfico, 
            (0,90,), # 80 
            0 , 
            width_mm=85, # 120 
            height_mm=85) # 120
        
        # inserto la leyenda abajo de la tablita
        pdf_agosto_2024.add_text_to_page(
            'El presente análisis se realiza sobre el total de los estudiantes que cuentan con registros en la medición de Noviembre.', 
            (0, 40), 
            0,
            "REM-Regular", 12,
            color=(0, 0 , 0),
            align='center-multiline'
        )

        # grabo a esa página
        pdf_agosto_2024.save_pdf(output_pdf_path,)
    

    print('hacer_hoja_por_curso ' , listaDePáginas)
    
    return listaDePáginas


def listado_alumnos_Con_DESEMPEÑO(unaEscuela):

    tableStyle = [
        ('BACKGROUND', (0, 0), (-1, 0), colors.Color(157/255, 222/255, 220/255)),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Centrado vertical del título de las columnas de la tabla
        ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('FONTNAME', (0, 1), (-1, -1), 'REM-Regular'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]
    
    if unaEscuela.Nivel == 'Primario' :
        gradoAño = 'grado'
    else:
        gradoAño = 'año'
    hoja_vacía = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas\Escuelas' + '/5-Página-5-vacía-landscape.pdf'    
    tipos_desempeño = ['Crítico','Básico','Medio','Avanzado']
    cabecera = [
        'DNI', 
        'Apellido', 
        'Nombre', 
        'Curso', 
        'Div.', 
        'Cant. palabras 1° medición', 
        'Cant. palabras 3° medición', 
        'Desempeño 3° medición',
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
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
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
        'Cantidad de palabras 1er Op.',        
        'Cantidad de palabras 3er Op.' 
    ]
    column_widths_mm = [18, 55, 55, 20 , 20 , 20 , 20 , ]  # anchos en milímetros
    
    
    if unaEscuela.Nivel == 'Primario' :
        gradoAño = 'grado'
    else:
        gradoAño = 'año'
    hoja_vacía = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas\Escuelas' + '/5-Página-5-vacía-landscape.pdf'    
    
   

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
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
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
    hoja_vacía = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas\Escuelas' + '/5-Página-5-vacía-landscape.pdf'    

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
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
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
    hoja_vacía = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas\Escuelas' + '/5-Página-5-vacía-landscape.pdf'    
       

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
        title_text = f"<b>Listado de estudiantes de {curso} {gradoAño} que no fueron evaluados</b>"
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

def hacer_el_listado_de_los_alumnos_de_primer_grado(unaEscuela):
    
    tableStyle = [
        ('BACKGROUND', (0, 0), (-1, 0), colors.Color(157/255, 222/255, 220/255)),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Centrado vertical del título de las columnas de la tabla
        ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('FONTNAME', (0, 1), (-1, -1), 'REM-Regular'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]
    """
    'DNI' , 
    'Apellido_Alumno' , 
    'Nombre_Alumno' , 
    'CURSO_NORMALIZADO' , 
    'División' ,
    'Cantidad_de_palabras',
    'Prosodia',
    'Incluido
    """
    cabecera = [
        'DNI' , 
        'Apellido' , 
        'Nombre' , 
        'Curso' , 
        'Div.',        
        'Cant. de palabras leídas',
        'Prosodia',
        'Incluido' 
    ]
    column_widths_mm = [18, 55, 55, 20 , 20, 25, 25, 25 , 35 ]  # anchos en milímetros
    
    
    # esto se ejecuta solamente para las escuelas primarias porque es el puto listado de los de primer grado que tanto rompe las bolas el Javi!!!
    listaDePaths = []
    if unaEscuela.Nivel == 'Primario' :
        gradoAño = 'grado'
    
        hoja_vacía = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas\Escuelas' + '/5-Página-5-vacía-landscape.pdf'       

        diccionario = unaEscuela.get_escuela_Diccionario_Informes()
        diciconario_por_curso_alumnos = diccionario.get('FL_ESCUELA_011_listado_de_alumnos_de_PRIMARIA_PRIMER_GRADO_sin_DESEMPEÑO')

        
        print(diciconario_por_curso_alumnos)

        pdf_agosto_2024 = PDF.PDFEditor(    
            hoja_vacía ,
            unaEscuela
        )
        
        
        for curso, listadoSiIncluidos in diciconario_por_curso_alumnos.items():
            #print(curso)
            #print(listadoSiIncluidos)
            title_text = f"<b>Listado de estudiantes de {curso} {gradoAño} </b>"
            output_pdf_path = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\PDFsEscuela' + '\\' + fU.sanearNombresDeArchivos(str(unaEscuela.Escuela_ID)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Número_escuela)) + '_' + fU.sanearNombresDeArchivos(str(unaEscuela.Nombre_Escuela)) + '_F. L. 2024_1'  + '_5-Página-5_' + curso + '_' + '_LISTADO_DE_PRIMER_GRADO_' +'_.pdf'
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
    hoja_vacía = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas\Escuelas' + '/4-Página-4-vacía.pdf'
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