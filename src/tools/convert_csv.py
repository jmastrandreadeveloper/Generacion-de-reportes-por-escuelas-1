# esta utilidad sirve para convertor archivos .csv que tienen las columnas y los datos separados por comillas y los deja sin comillas
# se ejecuta desde donde está el main.py , no desde acá..moverlo para ejecutarlos desdea haí
import sys
import os
import data_loading as u 
import utils as u
from src.tools.print_dataframe import print_dataframe as printDF 

# df_nominal      = u.cargar_csv('NOMINAL_AL_30_09_2023_PARA_FL_2023_2.csv')
# df_nominal_al_21_03_2025      = u.cargar_csv('NOMINAL_AL_21_03_2025_PARA_FL_2024_1_prueba.csv')
# df_fluidez_1    = u.cargar_csv('1-fixed-1636-27-05-2024-FLUIDEZ LECTORA NOMINAL_26_27_28_29_30_31.csv')
# df_fluidez_2    = u.cargar_csv('2-fixed-1636-30-09-2024-FLUIDEZ LECTORA NOMINAL_30_31_32_33.csv')
# df_fluidez_3    = u.cargar_csv('3-06-12-2024-FLUIDEZ LECTORA NOMINAL_34_35_36_37.csv')

# df_fluidez_3_al_09_05_2025    = u.cargar_csv('3-fixed-FLUIDEZ_LECTORA_PRIMERA_MEDICIÓN_ABRIL_38_39_40_41_42_43_al_09_05_2025.csv')
# u.guardar_dataframe_a_csv(df_fluidez_3_al_09_05_2025  ,   '/data/raw/_3-fixed-FLUIDEZ_LECTORA_PRIMERA_MEDICIÓN_ABRIL_38_39_40_41_42_43_al_09_05_2025.csv')

# df_mini_nominal    = u.cargar_csv('NOMINAL_AL_09_05_2025_PARA_FL_2025_ABRIL.csv')
# u.guardar_dataframe_a_csv(df_mini_nominal  ,   '/data/raw/_NOMINAL_AL_09_05_2025_PARA_FL_2025_ABRIL.csv')


# u.guardar_dataframe_a_csv(df_nominal    ,   '/data/raw/_NOMINAL_AL_30_09_2023_PARA_FL_2023_2.csv')
# u.guardar_dataframe_a_csv(df_nominal_al_21_03_2025    ,   '/data/raw/_NOMINAL_AL_21_03_2025_PARA_FL_2024_1_prueba.csv')
# u.guardar_dataframe_a_csv(df_fluidez_1  ,   '/data/raw/_1-fixed-1636-27-05-2024-FLUIDEZ LECTORA NOMINAL_26_27_28_29_30_31.csv')
# u.guardar_dataframe_a_csv(df_fluidez_2  ,   '/data/raw/_2-fixed-1636-30-09-2024-FLUIDEZ LECTORA NOMINAL_30_31_32_33.csv')
# u.guardar_dataframe_a_csv(df_fluidez_3  ,   '/data/raw/_3-06-12-2024-FLUIDEZ LECTORA NOMINAL_34_35_36_37.csv')


# ------------------------------------------------------------------------------------
#df_nominal      = u.cargar_csv('NOMINAL_AL_13_04_2025_PARA_FL_2025_ABRIL.csv')
#df_fluidez_1    = u.cargar_csv('1-fixed-1636-27-05-2024-FLUIDEZ LECTORA NOMINAL_26_27_28_29_30_31.csv')
#df_fluidez_2    = u.cargar_csv('2-06-12-2024-FLUIDEZ LECTORA NOMINAL_34_35_36_37.csv')
#df_fluidez_3    = u.cargar_csv('3-fixed-FLUIDEZ_LECTORA_PRIMERA_MEDICIÓN_ABRIL_38_39_40_41.csv')

# u.guardar_dataframe_a_csv(df_nominal    ,   '/data/raw/_NOMINAL_AL_13_04_2025_PARA_FL_2025_ABRIL.csv')
# u.guardar_dataframe_a_csv(df_fluidez_1  ,   '/data/raw/_1-fixed-1636-27-05-2024-FLUIDEZ LECTORA NOMINAL_26_27_28_29_30_31.csv')
# u.guardar_dataframe_a_csv(df_fluidez_2  ,   '/data/raw/_2-06-12-2024-FLUIDEZ LECTORA NOMINAL_34_35_36_37.csv')
#u.guardar_dataframe_a_csv(df_fluidez_3  ,   '/data/raw/_3-fixed-FLUIDEZ_LECTORA_PRIMERA_MEDICIÓN_ABRIL_38_39_40_41.csv')

# ------------------------------------------------------------------------------------
#df_matematica_1 = u.cargar_csv('1ER AÑO - 1ERA MEDICIÓN ABRIL 2025_sábana_7.csv')
#u.guardar_dataframe_a_csv(df_matematica_1  ,   '/data/raw/_1ER AÑO - 1ERA MEDICIÓN ABRIL 2025_sábana_7.csv')


df_NOMINAL_AL_10_05_2025_PARA_MATEMATICA_2025_MAYO = u.cargar_csv('NOMINAL_AL_10_05_2025_PARA_MATEMATICA_2025_MAYO.csv')
u.guardar_dataframe_a_csv(df_NOMINAL_AL_10_05_2025_PARA_MATEMATICA_2025_MAYO  ,   '/data/raw/_NOMINAL_AL_10_05_2025_PARA_MATEMATICA_2025_MAYO.csv')

print('...fin..!')