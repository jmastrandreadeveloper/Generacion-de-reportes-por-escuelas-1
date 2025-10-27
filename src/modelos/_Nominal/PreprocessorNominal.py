import pandas as pd
from src.modelos.Libs.quitar_columnas import quitar_columnas
from src.modelos.Libs.conservar_filas import conservar_filas
from src.modelos.Libs.fix_columna_edad import fix_columna_edad
from src.modelos.Libs.fix_columna_subcue import fix_columna_subcue
from src.modelos.Libs.agregar_columna_Nivel_Unificado import agregar_columna_Nivel_Unificado
from src.modelos.Libs.reordenar_columnas import reordenar_columnas
from src.modelos.Libs.obtener_datos_de_columna import obtener_datos_de_columna
from src.modelos.Libs.drop_rows import drop_rows
from src.modelos.Libs.ordenar_df_por_columna import ordenar_df_por_columna
from src.modelos.Libs.reemplazar_guión_por_cero import reemplazar_guion_por_cero
from src.modelos.__commonsLibs_.obtemer_lista_de_Escuelas.set_get_df_lista_de_Ecuela_ID import set_df_lista_de_Ecuela_ID
from src.modelos.Libs.renombrar_columnas import renombrar_columnas
from src.modelos.__commonsLibs_.obtener_lista_de_Supervisiones.set_get_df_lista_de_Supervisiones import set_df_lista_de_Supervisiones
from src.modelos.Libs.re_map_divisiones import reemplazar_valores
from src.modelos.Libs.processDivisiones import remapear_divisiones_por_escuela_curso
from src.modelos.Libs.generar_diccionario_divisiones import generar_diccionario_divisiones

import src.tools.utils as u

def process(dataframe: pd.DataFrame , año_mes: str = '2025_04'):
    dataFrame_name = dataframe.Name
    print(dataFrame_name)
    # dejar solamente las filas que necesitamos, estas son todas aquellas que sea CURSO_NORMALIZADO = 1°, 2°, 3°, 4°, 5°, 6°, 7°, 
    # dejar :  1°  2°  3°  4°  5°  6°  7°
    # eliminar : Múltiple Domiciliario -  Nivel I
    # dejar las columnas que hacen falta        
    dataframe_1 = conservar_filas(dataframe , 'CURSO_NORMALIZADO',['1°' , '2°' , '3°' , '4°' , '5°' , '6°' , '7°'])
    # RENOMBRAR COLUMNAS
    dataframe_1 = renombrar_columnas(dataframe_1 , {'Apellido_Alumno ' : 'Apellido' , 'Nombre_Alumno ' : 'Nombre' , 'CURSO_NORMALIZADO' : 'Curso ' ,  'Número_escuela' : 'Número' , 'Nombre_Escuela' : 'Escuela'})            
    # arreglar la columna edad para que queden todos en formato numérico
    dataframe_2 = fix_columna_edad(dataframe_1)
    # reemplazamos la columna subcue con cero
    dataframe_2 = reemplazar_guion_por_cero(dataframe_2 , 'subcue')
    # arrreglar la columna subcue para esas escuelas que no lo tienen cargado
    dataframe_2 = fix_columna_subcue(dataframe_2)    
    # agregar columna Nivel_Unificado    
    dataframe_3 = agregar_columna_Nivel_Unificado(dataframe_2)    
    
    # REMAPEAR LAS DIVISIONES   
    
    #dataframe_4 = reemplazar_valores(dataframe_3, 'División')
    # se remapea las divisiones por escuela y curso    
    dataframe_4 = remapear_divisiones_por_escuela_curso(dataframe_3, col_escuela="Escuela_ID", col_curso="Curso ", col_division="División" , col_division_id = "División_ID" )
    # y se genera un diccionario de divisiones por escuela, curso y división_id
    diccionario_divisiones = generar_diccionario_divisiones(dataframe_4 , col_escuela="Escuela_ID", col_curso="Curso ", col_division_id="División_ID", col_division="División")
    
    
    # reordenar columnas
    df_nominal_processed = reordenar_columnas(
        dataframe_4,
        ['ciclo_lectivo','Alumno_ID','Alumno_división','División_ID' ,'DNI','Apellido','Nombre','Sexo','Fecha_Nacimiento',"Edad",'Edad_Correcta','Curso ','Curso','División','Turno','Modalidad','Nivel','Nivel_Unificado','Gestión','Supervisión','Escuela_ID','CUE','subcue','Número','Anexo','Número_Anexo','Escuela','Departamento','Localidad','zona','AMBITO','Regional',
            #'Nombre_Escuela','ciclo_lectivo','Alumno_ID','Sexo','Edad','Edad_Correcta','CURSO_NORMALIZADO','Curso','División','Turno','Modalidad','Nivel','Nivel_Unificado','Gestión','Supervisión','Escuela_ID','Departamento','Localidad','zona','AMBITO','Regional'
        ]
    )
    # borramos las filas con Escuela_ID = 0
    df_nominal_processed = drop_rows(df_nominal_processed , 'Escuela_ID' ,  [0])
    # eliminar las filas donde el CURSO_NORMALIZADO tiene Grado Múltiple
    df_nominal_processed = drop_rows(df_nominal_processed , 'Curso ' ,  'Grado Múltiple')
    # ordenar el dataframe por Escuela_ID
    df_nominal_processed = ordenar_df_por_columna(df_nominal_processed , 'Escuela_ID')
    u.guardar_dataframe_a_csv(df_nominal_processed,'/data/processed/transformed/Nominal/' + año_mes + '/' + dataFrame_name + '_df_nominal_processed.csv')    
    # se implementan las funciones para el preproceso del dataframe
    # quitar columnas para deja solamente las que me inteesan
    df_nominal_datos_institucionales = quitar_columnas(df_nominal_processed , ['Alumno_división', 'DNI' , 'Apellido', 'Nombre' ,'Fecha_Nacimiento', 'ciclo_lectivo','Alumno_ID','Sexo','Edad','Edad_Correcta','Curso ','Curso','División','Turno','Modalidad' , 'División_ID'] , True)        
    #listaEscuelas_IDs = obtener_datos_de_columna(df_nominal_datos_institucionales,'Escuela_ID' , True)
    # lista de las escuelas por Escuela_ID
    _df_nominal_datos_institucionales_Escuela_ID = set_df_lista_de_Ecuela_ID(df_nominal_datos_institucionales , dataFrame_name)
    # lista de las supervisiones por Supervisión
    _df_nominal_datos_institucionales_Lista_de_Supervisiones = set_df_lista_de_Supervisiones(df_nominal_datos_institucionales , dataFrame_name)
    
    # guardar la lista de las escuelas 'listaEscuelas_IDs' para poder usarlas mas adelante
    #u.guardar_lista_simple_en_csv(listaEscuelas_IDs,'/data/processed/transformed/Nominal/lista_de_Escuela_IDs_df_nominal.csv')
    #self.group_agg = GroupAggregation(self.df_nominal_processed)
    # para que finalmente sea accedido desde otra parte, desde el reporte
    # porque de este dataframe saldrán los datos institucionales    
    u.guardar_dataframe_a_csv(df_nominal_datos_institucionales,'/data/processed/transformed/Nominal/' + año_mes + '/' + dataFrame_name + '_df_nominal_datos_institucionales.csv')
    u.guardar_dataframe_a_csv(_df_nominal_datos_institucionales_Escuela_ID,'/data/processed/transformed/Nominal/' + año_mes + '/' + dataFrame_name + '_datos_institucionales_Escuela_ID.csv')
    u.guardar_dataframe_a_csv(_df_nominal_datos_institucionales_Lista_de_Supervisiones ,'/data/processed/transformed/Nominal/' + año_mes + '/' + dataFrame_name + '_datos_institucionales_Lista_de_Supervisiones.csv')
    
    
    dict_escuela_id_curso_división_id = {}
    # Luego, asegurate de convertir la clave a string
    dict_escuela_id_curso_división_id['escuela_id_curso_división_id'] = diccionario_divisiones    
    u.save_json(dict_escuela_id_curso_división_id, '/data/processed/transformed/Nominal/2025_11/dict_escuela_id_curso_división_id.json')
    
    
    return [df_nominal_processed,
            _df_nominal_datos_institucionales_Escuela_ID, # esto se debe cambiar para dar paso a lo que trae la función get_df_lista_de_Ecuela_ID
            df_nominal_datos_institucionales,
            _df_nominal_datos_institucionales_Lista_de_Supervisiones]