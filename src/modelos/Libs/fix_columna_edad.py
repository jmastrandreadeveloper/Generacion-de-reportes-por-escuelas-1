import pandas as pd
import numpy as np
from src.modelos.Libs.reordenar_columnas import reordenar_columnas

def fix_columna_edad(dataframe : pd.DataFrame):
    print('...arreglando datos de la columna edad...')
    def create_age_reference() -> dict:
        """
        Crear un diccionario de referencia de edades.
        """
        age_reference = {
            ('Primario', '1°'): 6,
            ('Primario', '2°'): 7,
            ('Primario', '3°'): 8,
            ('Primario', '4°'): 9,
            ('Primario', '5°'): 10,
            ('Primario', '6°'): 11,
            ('Primario', '7°'): 12,

            ('Secundario Orientado', '1°'): 13,
            ('Secundario Orientado', '2°'): 14,
            ('Secundario Orientado', '3°'): 15,
            ('Secundario Orientado', '4°'): 16,
            ('Secundario Orientado', '5°'): 17,
            ('Secundario Orientado', '6°'): 18,

            ('Secundario Técnico', '1°'): 13,
            ('Secundario Técnico', '2°'): 14,
            ('Secundario Técnico', '3°'): 15,
            ('Secundario Técnico', '4°'): 16,
            ('Secundario Técnico', '5°'): 17,
            ('Secundario Técnico', '6°'): 18,
        }
        return age_reference

    
    def correct_invalid_ages(dataframe , age_reference: dict) :
        """
        Corrige las edades inválidas utilizando la referencia de edades.
        """
        # Definir la función para obtener la edad correcta
        def get_correct_age(row, distancia):
            key = (row['Nivel'], row['Curso'])
            
            if key in age_reference:
                reference_age = age_reference[key]
                try:
                    current_age = int(row['Edad'])
                    if abs(current_age - reference_age) > distancia:
                        return reference_age
                    else:
                        return current_age
                except ValueError:
                    # Si la edad no es un número válido, devolver la edad de referencia
                    return reference_age
            else:
                try:
                    return int(row['Edad'])
                except ValueError:
                    # Si la edad no es un número válido y no se encuentra la clave en el diccionario,
                    # se devuelve np.nan (o puedes devolver otro valor si lo prefieres)
                    return np.nan

        

        # esto significa que la diferencia entre la edad leída del df
        # y la que se toma como referencia no debe ser mayor a 2
        # sive para cuando tenemos un valor demasiado grande o muy chico
        # en alguno de esos casos debo poder resolverlo buscando su edad referencia
        distancia_entre_edades = 2

        # Corregir edades inválidas
        # if invalid_ages_mask.any():
        #     dataframe.loc[invalid_ages_mask, 'Edad'] = dataframe[invalid_ages_mask].apply(get_correct_age, axis=1, distancia=distancia_entre_edades)
        
        # Rastrear edades fuera del límite permitido y corregirlas
        # for (curso, nivel), edad in age_reference.items():
        #     mask = (dataframe['CURSO_NORMALIZADO'] == curso) & (dataframe['Nivel'] == nivel)
        #     dataframe.loc[mask & (dataframe['Edad'] > edad), 'Edad'] = edad
        dataframe['Edad_Correcta'] = dataframe.apply(get_correct_age, axis=1, distancia=distancia_entre_edades)
        # reordenar las columnas
        # reordenar columnas
        dataframe = reordenar_columnas(
            dataframe,
            [
                'ciclo_lectivo','Alumno_ID','Sexo','Edad','Edad_Correcta','Curso ','Curso','División','Turno','Modalidad','Nivel','Gestión','Supervisión','Escuela_ID','Departamento','Localidad','zona','AMBITO','Regional',]
        )
        return dataframe

    def validate_data(dataframe):
        # Create age reference based on the dataframe
        age_reference = create_age_reference()
        # Correct invalid ages
        dataframe = correct_invalid_ages(dataframe , age_reference)
        return dataframe
    
    validate_data(dataframe)
    return dataframe