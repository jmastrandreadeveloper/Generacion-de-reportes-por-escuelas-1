import pandas as pd
from src.modelos.Libs.tipoDesempeño import tipoDesempeño
from src.modelos.Libs.comparar import comparar

def determinar_y_comparar_desempeños(dataframe: pd.DataFrame):
    # hacemos la determinación y la comparativa
    dataframe.loc[dataframe['DESEMPEÑO_primer_op']  == 0 , 'DESEMPEÑO_primer_op']  = 'Sin determinar'
    dataframe.loc[dataframe['DESEMPEÑO_segundo_op'] == 0 , 'DESEMPEÑO_segundo_op'] = 'Sin determinar'
    # # reemplazar Desempeño Por Codigo _ PARA_DOS_OPERATIVOS2:
    dataframe['DESEMPEÑO_primer_op_'] = dataframe['DESEMPEÑO_primer_op'].apply(tipoDesempeño)
    dataframe['DESEMPEÑO_segundo_op_'] = dataframe['DESEMPEÑO_segundo_op'].apply(tipoDesempeño)
    # MÉTODO 1 DE COMARACIÓN
    dataframe['compara'] = dataframe.apply(
        lambda row: comparar(row['DESEMPEÑO_primer_op_'], row['DESEMPEÑO_segundo_op_']), axis=1
    )
    return dataframe