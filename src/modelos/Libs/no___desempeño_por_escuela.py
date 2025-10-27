from src.modelos.Libs.porcentajes_desempeño import porcentajes_desempeño
from src.modelos.Libs.clean_dataframe import clean_dataframe

def desempeño_por_escuela(_df_Escuela_ID_Alumno_ID_count , _df_Escuela_ID_DESEMPEÑO_Alumno_ID_count ):
    # porcentaje de desempeño por escuela
    _df_Desempeño_por_Escuela = porcentajes_desempeño(
        ['Escuela_ID'],
        _df_Escuela_ID_Alumno_ID_count,
        _df_Escuela_ID_DESEMPEÑO_Alumno_ID_count,
        'Total_Alumnos_por_Tipo_de_Desempeño',
        'Total_Alumnos_por_Escuela_ID',
        'Desempeño_por_Escuela'
    )
    # fix las columnas para que queden con valores enteros y los float con dos valores después del punto
    _df_Desempeño_por_Escuela = clean_dataframe(
        _df_Desempeño_por_Escuela,
        ['Total_Alumnos_por_Tipo_de_Desempeño','Total_Alumnos_por_Escuela_ID'],
        ['Desempeño_por_Escuela']
    )