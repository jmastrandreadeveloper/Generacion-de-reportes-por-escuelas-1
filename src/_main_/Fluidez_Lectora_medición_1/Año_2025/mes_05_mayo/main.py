# la nueva manera de escribir el código será utilizando menos archivos intermedios 
# como por ejemplo los GroupAggregation, estos se harán directamente 
# llamando funciones desde el main
import os
import sys


# el project_root tiene una profundidad de carpetas medidas por los '..', eso es lo que dice la linea de abajo
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..' , '..' )) # E:\GitHub\python_data_analysis_v3\src
sys.path.append(project_root)
# obligatorio para poder acceder a todas las funcionalidades de las librerias para el proyecto y todo lo demas
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))
# en esta parte le digo que los datos van a estar dentro de dos subcarpetas acá mismo
raw_data = os.path.join(os.path.dirname(__file__),'data','raw')

import src.tools.utils as u
# importamos desde herramientas de impresión
from src.tools.print_dataframe import print_dataframe as printDF

import src._main_.Fluidez_Lectora_medición_1.Año_2025.mes_05_mayo.FL_config as configFL

from src.modelos._Nominal.PreprocessorNominal import process as processNominal
from src.modelos._Nominal.GroupNominal import group as groupNominal
from src.modelos._Análisis_Fluidez_Lectora.PreprocessorFluidezLectora import process as processFluidezLectora
from src.modelos._Análisis_Fluidez_Lectora.PreprocessorFluidezLectora import unir_dataframes_alumnos_Incluidos_SI_distintos_operativos
from src.modelos._Análisis_Fluidez_Lectora.PreprocessorFluidezLectora import unir_dataframes_alumnos_con_desempeño_MAX_PALABRAS_distintos_operativos

from src.modelos._Análisis_Fluidez_Lectora.GroupFluidezLectora import group as groupFluidezLectora

def procesar_nominal(data_dict):
    info = data_dict['dataframe_Nominal']
    df_nominal = u.cargar_csv_2(raw_data + info['archivo'])
    df_nominal.Name = info['nombre']

    df_nominal_processed, _df_escuela_id, df_datos_institucionales, _df_supervisiones = processNominal(df_nominal)

    groupNominal(
        df_nominal,
        df_nominal_processed,
        _df_escuela_id,
        df_datos_institucionales,
        _df_supervisiones
    )
    return

def procesar_fluidez(dict_fluidez):
    for key, info in dict_fluidez.items():
        df = u.cargar_csv_2(raw_data + '/' + info['archivo'].lstrip('/'))
        df.Name = info['nombre']

        (dataframe_,
        _df_alumnos_incluidos_SI,
        _df_alumnos_incluidos_NO,
        _df_alumnos_con_DESEMPEÑO,
        _df_alumnos_sin_DESEMPEÑO,
        _df_alumnos_menor_a_300_palabras,
        _df_alumnos_mayor_a_300_palabras,
        _df_alumnos_con_MÁXIMA_cant_palabras,
        _df_Escuela_ID) = processFluidezLectora(df)

        dataframe_.Name = info['nombre']

        groupFluidezLectora(
            dataframe_,
            _df_alumnos_incluidos_SI,
            _df_alumnos_incluidos_NO,
            _df_alumnos_con_DESEMPEÑO,
            _df_alumnos_sin_DESEMPEÑO,
            _df_alumnos_menor_a_300_palabras,
            _df_alumnos_mayor_a_300_palabras,
            _df_alumnos_con_MÁXIMA_cant_palabras,
            _df_Escuela_ID
        )
    return
    
if __name__ == "__main__":
    procesar_nominal(configFL.FL_mes_05_mayo_2025)
    procesar_fluidez(configFL.FL_mes_05_mayo_2025['FL_dicts_2024_2025'])
       
    
    unir_dataframes_alumnos_con_desempeño_MAX_PALABRAS_distintos_operativos()
    unir_dataframes_alumnos_Incluidos_SI_distintos_operativos()

    # acá se podría llamar a una función para que haga una compararación entre dos operativos para poder
    # determinar el progreso de los alumnos