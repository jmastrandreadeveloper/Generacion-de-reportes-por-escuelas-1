from src.modelos.Libs.determinar_desempeño_por_fila import determinar_desempeño_por_fila

def calcular_DESEMPEÑO_por_Alumno_ID(dataframe):
    dataframe['DESEMPEÑO'] =   dataframe.apply(lambda row: determinar_desempeño_por_fila( row ), axis=1)
    # reordenar columnas..
    dataframe = dataframe.reindex(columns=[        
        'DESEMPEÑO',
        'Alumno_ID',
        'Operativo',
        'CURSO_NORMALIZADO',
        'Curso',
        'División',
        'Ausente',
        'Cantidad_de_palabras',
        'Prosodia',
        'Incluido',
        'Turno',
        'Modalidad',
        'Nivel',
        'Nivel_Unificado',
        'Gestión',
        'Supervisión',
        'Escuela_ID',
        'Departamento',
        'Localidad',
        'zona',
        'Regional',
        'ciclo_lectivo',
        'separador'])
    return dataframe