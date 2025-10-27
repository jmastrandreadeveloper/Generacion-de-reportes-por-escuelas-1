import pandas as pd

def limpiar_df_comparado(dataframe : pd.DataFrame):
    # cambiar los tipos de datos de flotante a int
    dataframe['Cantidad_de_palabras_primer_op'] = dataframe['Cantidad_de_palabras_primer_op'].astype(int)
    dataframe['Cantidad_de_palabras_segundo_op'] = dataframe['Cantidad_de_palabras_segundo_op'].astype(int)
    dataframe['Alumno_ID'] = dataframe['Alumno_ID'].astype(int)    
    dataframe['Alumno_división'] = dataframe['Alumno_división'].astype(int)
    dataframe['DNI'] = dataframe['DNI'].astype(int)    
    dataframe['Edad_Correcta'] = dataframe['Edad_Correcta'].astype(int)    
    dataframe['Escuela_ID'] = dataframe['Escuela_ID'].astype(int)
    dataframe['Anexo'] = dataframe['Anexo'].astype(int)    
    dataframe['CUE'] = dataframe['CUE'].astype(int)
    # a las escuelas que tienen el subcue igual a un guión, hay que dejar el subcue en cero
    dataframe.loc[dataframe['subcue'] == '-', :] = 0
    dataframe['subcue'] = dataframe['subcue'].astype(int)
    dataframe['ciclo_lectivo'] = dataframe['ciclo_lectivo'].astype(int)

    # ELIMINAR TODAS LAS FILAS DE ALUMNOS QUE EN AMBOS OPERATIVOS TIENEN EN LOS DOS DESEMPEÑOS RESPECTIVAMENTE = 'Sin comparativa'
    dataframe.drop(
    dataframe[
        (dataframe['DESEMPEÑO_primer_op_'] == 'Sin comparativa') &
        (dataframe['DESEMPEÑO_segundo_op_'] == 'Sin comparativa')
    ].index, 
    inplace=True)
    # ELIMINAR LAS FILAS DONDE EL ESCULEA_ID = 0
    dataframe.drop(dataframe[(dataframe['Escuela_ID'] == 0) &(dataframe['DESEMPEÑO_segundo_op_'] == 'Sin comparativa')].index,inplace=True)
    
    return dataframe