# esta parte del código es la que se encarga de agrupar los datos
# de diferentes formas para que luego podamos analizarlos
# desde acá se llaman a las funciones de agrupammiento
# acá se agrupa el datafrma Nominal y se le asigna un nombre

# agrupar el nominal
import pandas as pd
from src.modelos.__commonsLibs_.obtemer_datos_institucionales.group_df_datos_institucionales import group_df_datos_institucionales
from src.modelos.__commonsLibs_.obtener_lista_de_cursos_normalizados.group_df_lista_de_cursos_normalizados import group_df_lista_de_cursos_normalizados    
from src.modelos.__commonsLibs_.contar_alumnos_por_escuela_____.group_contar_alumnos_por_escuela_____ import contar_alumnos_por_escuela______group
from src.modelos.__commonsLibs_.contar_alumnos_por_escuela_y_curso_____.group_contar_alumnos_por_escuela_y_curso_____ import contar_alumnos_por_escuela_y_curso______group
from src.modelos.__commonsLibs_.contar_alumnos_por_escuela_curso_y_division_____.group_contar_alumnos_por_escuela_curso_y_division_____ import contar_alumnos_por_escuela_curso_y_division_sin_duplicados_de_alumnos_group
from src.modelos.__commonsLibs_.contar_alumnos_por_nivel_y_curso_____.group_contar_alumnos_por_nivel_y_curso_____ import contar_alumnos_por_nivel_y_curso______group
from src.modelos.__commonsLibs_.contar_alumnos_por_supervisión_y_curso_____.group_contar_alumnos_por_supervisión_y_curso_____ import contar_alumnos_por_supervisión_y_curso______group    


import src.tools.utils as u
# importamos desde herramientas de impresión
from src.tools.print_dataframe import print_dataframe as printDF   

def group(
    df_nominal : pd.DataFrame,
    df_nominal_processed : pd.DataFrame,
    _df_nominal_datos_institucionales_Escuela_ID : pd.DataFrame,
    df_nominal_datos_institucionales : pd.DataFrame,
    _df_nominal_datos_institucionales_Lista_de_Supervisiones : pd.DataFrame,
    año_mes: str = '2025_04'  # año_mes es el nombre de la carpeta donde se guardarán los archivos procesados, por ejemplo: '2025_04' para abril de 2025
    ):
    
    _df_datos_institucionales = group_df_datos_institucionales(df_nominal_datos_institucionales , as_json=False)
    u.guardar_dataframe_a_csv(_df_datos_institucionales,'/data/processed/transformed/Nominal/' + año_mes + '/' + df_nominal.Name + '_df_datos_institucionales.csv')
    printDF('Datos institucionales',_df_datos_institucionales)
    # hago los agrupamientos desde acá sin utilizar un archivo intermedio
    ############################################################################################
    # Alumno_división;DNI;Apellido_Alumno ;Nombre_Alumno ;Fecha_Nacimiento;Nivel;Nivel_Unificado;Gestión;Supervisión;Escuela_ID;CUE;subcue;Número_escuela;Anexo;Número_Anexo;Nombre_Escuela;Departamento;Localidad;zona;AMBITO;Regional
    # 5997184;55923102;STAGNOLI;Fabrizio Leonel;2016-12-01;Primario;Primario;Privada;01 - Primario Privada;2565;5001274;00;P001;0;P001-0;DON BOSCO;CAPITAL;3º SECCION - PARQUE O'HIGGINS;10%;Urbano;NO CORRESPONDE
    # 5997171;55922862;MANCHINI SANCHEZ;Amadeo Gabriel;2016-11-24;Primario;Primario;Privada;01 - Primario Privada;2565;5001274;00;P001;0;P001-0;DON BOSCO;CAPITAL;3º SECCION - PARQUE O'HIGGINS;10%;Urbano;NO CORRESPONDE    
    
    _df_Escuela_ID_CURSO_NORMALIZADO_list = group_df_lista_de_cursos_normalizados(df_nominal_processed)
    u.guardar_dataframe_a_csv(_df_Escuela_ID_CURSO_NORMALIZADO_list,'/data/processed/transformed/Nominal/' + año_mes + '/' + df_nominal.Name + '_df_Escuela_ID_CURSO_NORMALIZADO_list.csv')
    printDF('Lista de cursos normalizados por escuela',_df_Escuela_ID_CURSO_NORMALIZADO_list)
    """
    # ╒════╤══════════════╤══════════════════════════════════════╕
    # │    │  Escuela_ID  │                    CURSO_NORMALIZADO │
    # ╞════╪══════════════╪══════════════════════════════════════╡
    # │ 0  │      0       │                                  [0] │
    # ├────┼──────────────┼──────────────────────────────────────┤
    # │ 1  │      4       │ ['2°', '3°', '4°', '5°', '6°', '7°'] │
    # ├────┼──────────────┼──────────────────────────────────────┤
    # │ 2  │      5       │ ['2°', '3°', '4°', '5°', '6°', '7°'] │
    # ├────┼──────────────┼──────────────────────────────────────┤
    # │ 3  │      6       │ ['2°', '3°', '4°', '5°', '6°', '7°'] │
    # ├────┼──────────────┼──────────────────────────────────────┤
    # │ 4  │      7       │ ['2°', '3°', '4°', '5°', '6°', '7°'] │
    # ├────┼──────────────┼──────────────────────────────────────┤
    # │ 5  │      8       │ ['2°', '3°', '4°', '5°', '6°', '7°'] │
    # ├────┼──────────────┼──────────────────────────────────────┤
    # │ 6  │      9       │ ['2°', '3°', '4°', '5°', '6°', '7°'] │
    # ├────┼──────────────┼──────────────────────────────────────┤
    # │ 7  │      10      │ ['2°', '3°', '4°', '5°', '6°', '7°'] │
    # ├────┼──────────────┼──────────────────────────────────────┤
    # │ 8  │      11      │ ['2°', '3°', '4°', '5°', '6°', '7°'] │
    # ├────┼──────────────┼──────────────────────────────────────┤
    # │ 9  │      12      │ ['2°', '3°', '4°', '5°', '6°', '7°'] │
    # ╘════╧══════════════╧══════════════════════════════════════╛
    """
    
    _cantidad_de_alumnos_por_escuela = contar_alumnos_por_escuela______group(df_nominal_processed)
    u.guardar_dataframe_a_csv(_cantidad_de_alumnos_por_escuela,'/data/processed/transformed/Nominal/' + año_mes + '/' + df_nominal.Name + '_cantidad_de_alumnos_por_escuela.csv')
    printDF('Cantidad de alumnos por escuela',_cantidad_de_alumnos_por_escuela)
    """
    # ╒════╤══════════════╤═════════════════════════╕
    # │    │  Escuela_ID  │   matricula_por_escuela │
    # ╞════╪══════════════╪═════════════════════════╡
    # │ 0  │      0       │                     852 │
    # ├────┼──────────────┼─────────────────────────┤
    # │ 1  │      4       │                     728 │
    # ├────┼──────────────┼─────────────────────────┤
    # │ 2  │      5       │                     300 │
    # ├────┼──────────────┼─────────────────────────┤
    # │ 3  │      6       │                     266 │
    # ├────┼──────────────┼─────────────────────────┤
    # │ 4  │      7       │                     534 │
    # ├────┼──────────────┼─────────────────────────┤
    # │ 5  │      8       │                     247 │
    # ├────┼──────────────┼─────────────────────────┤
    # │ 6  │      9       │                     687 │
    # ├────┼──────────────┼─────────────────────────┤
    # │ 7  │      10      │                     671 │
    # ├────┼──────────────┼─────────────────────────┤
    # │ 8  │      11      │                     365 │
    # ├────┼──────────────┼─────────────────────────┤
    # │ 9  │      12      │                     436 │
    # ╘════╧══════════════╧═════════════════════════╛
    """

    _cantidad_de_alumnos_por_escuela_y_curso = contar_alumnos_por_escuela_y_curso______group(df_nominal_processed)
    u.guardar_dataframe_a_csv(_cantidad_de_alumnos_por_escuela_y_curso,'/data/processed/transformed/Nominal/' + año_mes + '/' + df_nominal.Name + '_cantidad_de_alumnos_por_escuela_y_curso.csv')
    printDF('Cantidad de alumnos por escuela y curso' , _cantidad_de_alumnos_por_escuela_y_curso)
    """
    # ╒════╤══════════════╤═════════════════════╤═════════════════════════════════╕
    # │    │  Escuela_ID  │   CURSO_NORMALIZADO │   matricula_por_escuela_y_curso │
    # ╞════╪══════════════╪═════════════════════╪═════════════════════════════════╡
    # │ 0  │      0       │                   0 │                             852 │
    # ├────┼──────────────┼─────────────────────┼─────────────────────────────────┤
    # │ 1  │      4       │                  2° │                             128 │
    # ├────┼──────────────┼─────────────────────┼─────────────────────────────────┤
    # │ 2  │      4       │                  3° │                             119 │
    # ├────┼──────────────┼─────────────────────┼─────────────────────────────────┤
    # │ 3  │      4       │                  4° │                             120 │
    # ├────┼──────────────┼─────────────────────┼─────────────────────────────────┤
    # │ 4  │      4       │                  5° │                             117 │
    # ├────┼──────────────┼─────────────────────┼─────────────────────────────────┤
    # │ 5  │      4       │                  6° │                             123 │
    # ├────┼──────────────┼─────────────────────┼─────────────────────────────────┤
    # │ 6  │      4       │                  7° │                             121 │
    # ├────┼──────────────┼─────────────────────┼─────────────────────────────────┤
    # │ 7  │      5       │                  2° │                              47 │
    # ├────┼──────────────┼─────────────────────┼─────────────────────────────────┤
    # │ 8  │      5       │                  3° │                              50 │
    # ├────┼──────────────┼─────────────────────┼─────────────────────────────────┤
    # │ 9  │      5       │                  4° │                              52 │    
    # ╘════╧══════════════╧═════════════════════╧═════════════════════════════════╛
    """
    
    _cantidad_de_alumnos_por_escuela_curso_y_división = contar_alumnos_por_escuela_curso_y_division_sin_duplicados_de_alumnos_group(df_nominal_processed)
    u.guardar_dataframe_a_csv(_cantidad_de_alumnos_por_escuela_curso_y_división,'/data/processed/transformed/Nominal/' + año_mes + '/' + df_nominal.Name + '_cantidad_de_alumnos_por_escuela_curso_y_división.csv')
    printDF('Cantidad de alumnos por escuela , curso y división', _cantidad_de_alumnos_por_escuela_curso_y_división)
    """
    # ╒════╤══════════════╤═════════════════════╤════════════╤══════════════════════════════════════════╕
    # │    │  Escuela_ID  │   CURSO_NORMALIZADO │  División  │   matricula_por_escuela_curso_y_division │
    # ╞════╪══════════════╪═════════════════════╪════════════╪══════════════════════════════════════════╡
    # │ 0  │      0       │                   0 │     0      │                                      852 │
    # ├────┼──────────────┼─────────────────────┼────────────┼──────────────────────────────────────────┤
    # │ 1  │      4       │                  2° │     A      │                                       25 │
    # ├────┼──────────────┼─────────────────────┼────────────┼──────────────────────────────────────────┤
    # │ 2  │      4       │                  2° │     B      │                                       21 │
    # ├────┼──────────────┼─────────────────────┼────────────┼──────────────────────────────────────────┤
    # │ 3  │      4       │                  2° │     C      │                                       20 │
    # ├────┼──────────────┼─────────────────────┼────────────┼──────────────────────────────────────────┤
    # │ 4  │      4       │                  2° │     D      │                                       23 │
    # ├────┼──────────────┼─────────────────────┼────────────┼──────────────────────────────────────────┤
    # │ 5  │      4       │                  2° │     E      │                                       19 │
    # ├────┼──────────────┼─────────────────────┼────────────┼──────────────────────────────────────────┤
    # │ 6  │      4       │                  2° │     F      │                                       20 │
    # ├────┼──────────────┼─────────────────────┼────────────┼──────────────────────────────────────────┤
    # │ 7  │      4       │                  3° │     A      │                                       31 │
    # ├────┼──────────────┼─────────────────────┼────────────┼──────────────────────────────────────────┤
    # │ 8  │      4       │                  3° │     B      │                                       31 │
    # ├────┼──────────────┼─────────────────────┼────────────┼──────────────────────────────────────────┤
    # │ 9  │      4       │                  3° │     C      │                                       28 │
    # ╘════╧══════════════╧═════════════════════╧════════════╧══════════════════════════════════════════╛
    """
    
    _cantidad_de_alumnos_por_nivel_y_curso = contar_alumnos_por_nivel_y_curso______group(df_nominal_processed)
    u.guardar_dataframe_a_csv(_cantidad_de_alumnos_por_nivel_y_curso,'/data/processed/transformed/Nominal/' + año_mes + '/' + df_nominal.Name + '_cantidad_de_alumnos_por_nivel_y_curso.csv')
    printDF('Cantidad de alumnos por nivel y curso',_cantidad_de_alumnos_por_nivel_y_curso)    
    """
    # ╒════╤═══════════════════╤═════════════════════╤═══════════════════════════════╕
    # │    │  Nivel_Unificado  │   CURSO_NORMALIZADO │   matricula_por_nivel_y_curso │
    # ╞════╪═══════════════════╪═════════════════════╪═══════════════════════════════╡
    # │ 0  │         0         │                   0 │                           852 │
    # ├────┼───────────────────┼─────────────────────┼───────────────────────────────┤
    # │ 1  │     Primario      │                  1° │                           594 │
    # ├────┼───────────────────┼─────────────────────┼───────────────────────────────┤
    # │ 2  │     Primario      │                  2° │                         32309 │
    # ├────┼───────────────────┼─────────────────────┼───────────────────────────────┤
    # │ 3  │     Primario      │                  3° │                         33304 │
    # ├────┼───────────────────┼─────────────────────┼───────────────────────────────┤
    # │ 4  │     Primario      │                  4° │                         34971 │
    # ├────┼───────────────────┼─────────────────────┼───────────────────────────────┤
    # │ 5  │     Primario      │                  5° │                         32891 │
    # ├────┼───────────────────┼─────────────────────┼───────────────────────────────┤
    # │ 6  │     Primario      │                  6° │                         32006 │
    # ├────┼───────────────────┼─────────────────────┼───────────────────────────────┤
    # │ 7  │     Primario      │                  7° │                         32056 │
    # ├────┼───────────────────┼─────────────────────┼───────────────────────────────┤
    # │ 8  │    Secundario     │                  1° │                         34026 │
    # ├────┼───────────────────┼─────────────────────┼───────────────────────────────┤
    # │ 9  │    Secundario     │                  2° │                         30847 │
    # ╘════╧═══════════════════╧═════════════════════╧═══════════════════════════════╛
    """

    _cantidad_de_alumnos_por_supervisión_y_curso = contar_alumnos_por_supervisión_y_curso______group(df_nominal_processed)
    u.guardar_dataframe_a_csv(_cantidad_de_alumnos_por_supervisión_y_curso,'/data/processed/transformed/Nominal/' + año_mes + '/' + df_nominal.Name + '_cantidad_de_alumnos_por_supervisión_y_curso.csv')
    printDF('Cantidad de alumnos por Supervisión y curso',_cantidad_de_alumnos_por_supervisión_y_curso)
    """
    # ╒════╤═══════════════╤═════════════════════╤═════════════════════════════════════╕
    # │    │  Supervisión  │   CURSO_NORMALIZADO │   matricula_por_supervisión_y_curso │
    # ╞════╪═══════════════╪═════════════════════╪═════════════════════════════════════╡
    # │ 0  │       0       │                   0 │                                 852 │
    # ├────┼───────────────┼─────────────────────┼─────────────────────────────────────┤
    # │ 1  │       -       │                  1° │                                   1 │
    # ├────┼───────────────┼─────────────────────┼─────────────────────────────────────┤
    # │ 2  │       -       │                  3° │                                   1 │
    # ├────┼───────────────┼─────────────────────┼─────────────────────────────────────┤
    # │ 3  │       -       │                  4° │                                   2 │
    # ├────┼───────────────┼─────────────────────┼─────────────────────────────────────┤
    # │ 4  │ 01 - Primario │                  2° │                                 641 │
    # ├────┼───────────────┼─────────────────────┼─────────────────────────────────────┤
    # │ 5  │ 01 - Primario │                  3° │                                 700 │
    # ├────┼───────────────┼─────────────────────┼─────────────────────────────────────┤
    # │ 6  │ 01 - Primario │                  4° │                                 720 │
    # ├────┼───────────────┼─────────────────────┼─────────────────────────────────────┤
    # │ 7  │ 01 - Primario │                  5° │                                 738 │
    # ├────┼───────────────┼─────────────────────┼─────────────────────────────────────┤
    # │ 8  │ 01 - Primario │                  6° │                                 697 │
    # ├────┼───────────────┼─────────────────────┼─────────────────────────────────────┤
    # │ 9  │ 01 - Primario │                  7° │                                 681 │
    # ╘════╧═══════════════╧═════════════════════╧═════════════════════════════════════╛
    """

    # creaar un listado de escuelas por supervisión
    # usando el df nominal para tener todas las escuelas de las supervisiones
    #_listado_de_escuelas_por_supervisión 
        

    return 
    # [
    #     _df_Escuela_ID_CURSO_NORMALIZADO_list,
    #     _cantidad_de_alumnos_por_escuela,
    #     _cantidad_de_alumnos_por_escuela_y_curso,
    #     _cantidad_de_alumnos_por_escuela_curso_y_división,
    #     _cantidad_de_alumnos_por_nivel_y_curso,
    #     _cantidad_de_alumnos_por_supervisión_y_curso
    # ]