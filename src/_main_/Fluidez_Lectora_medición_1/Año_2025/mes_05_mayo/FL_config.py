# este archivo configura el preprocesador de la medición de fluidez lectora
# y lo prepara para el análisis
# de la medición de fluidez lectora
# del mes de mayo del año 2025
# se declaran acá los archivos a usar

import pandas as pd

# si verbose = True, se muestran los mensajes de los procesos
verbose = True

FL_mes_05_mayo_2025 = {
    # 'dataframe_Nominal': {
    #     'archivo': '/_NOMINAL_AL_13_04_2025_PARA_FL_2025_ABRIL.csv',
    #     'nombre': 'df_nominal'
    # },
    'dataframe_Nominal': {
        'archivo': '/_NOMINAL_AL_09_05_2025_PARA_FL_2025_ABRIL.csv',
        'nombre': 'df_nominal'
    },
    'FL_dicts_2024_2025': {
        'mayo_2024': {
            'archivo': '/_1-fixed-1636-27-05-2024-FLUIDEZ LECTORA NOMINAL_26_27_28_29_30_31.csv',
            'nombre': 'df_Fluidez_1'
        },
        'diciembre_2024': {
            'archivo': '/_2-06-12-2024-FLUIDEZ LECTORA NOMINAL_34_35_36_37.csv',
            'nombre': 'df_Fluidez_2'
        },
        # 'abril_2025': {
        #     'archivo': '/_3-fixed-FLUIDEZ_LECTORA_PRIMERA_MEDICIÓN_ABRIL_38_39_40_41.csv',
        #     'nombre': 'df_Fluidez_3'
        # }
        # se hace esto porque vamos a sacar nuevamente los informes para algnas escuelas
        'abril_2025': {
            'archivo': '/_3-fixed-FLUIDEZ_LECTORA_PRIMERA_MEDICIÓN_ABRIL_38_39_40_41_42_43_al_09_05_2025.csv',
            'nombre': 'df_Fluidez_3'
        }
    }
}

data_dict_ALUMNOS_CON_DESEMPEÑO = {
    'Primera_Medición_Año_Anterior':[
        '/df_Fluidez_1_alumnos_con_MÁXIMA_cant_palabras.csv',                
        {'Cant. palabras' :  'Cant. palabras 1° med. 2024' , 'DESEMPEÑO' : 'Desemp. 1° med. 2024' , } ,
    ]
    ,
    'ültima_Medición_Año_Anterior':[
        '/df_Fluidez_2_alumnos_con_MÁXIMA_cant_palabras.csv',
        {'Cant. palabras' :  'Cant. palabras 3° med. 2024' , 'DESEMPEÑO' : 'Desemp. 3° med. 2024' , } ,
    ]
    ,
    'Primera_Medición_Año_Actual':[
       '/df_Fluidez_3_alumnos_con_MÁXIMA_cant_palabras.csv',
        {'Cant. palabras' :  'Cant. palabras 1° med. 2025'   , 'DESEMPEÑO' : 'Desemp. prim. med. 2025' ,  } ,
    ]
}