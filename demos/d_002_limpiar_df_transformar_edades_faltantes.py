# demo para limpiar edades faltantes
# la idea de la demo es la de poder cambiar los valores de las edades
# basandonos en el nivel y el curso y teniendo como referencia
# un diccionario que nos permita tomarlo y compararlo
# además habrán casos que hay edades que están fuera de rango y que
# se tendran que acomodar a las edades permitidas
import pandas as pd
import numpy as np

print('\n')
print('Crear un DataFrame de ejemplo')
data = {
    'Nivel': ['Primario', 'Secundario Orientado', 'Secundario Técnico' , 'Primario'],
    'Curso': ['1°', '2°', '3°' , '2°'],
    'Edad': ['5', '31', '-' , '1']
}
df = pd.DataFrame(data)
print(df,'\n')

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

        ('Secundario Técnico', '1°'): 13,
        ('Secundario Técnico', '2°'): 14,
        ('Secundario Técnico', '3°'): 15,
        ('Secundario Técnico', '4°'): 16,
        ('Secundario Técnico', '5°'): 17,
        ('Secundario Técnico', '6°'): 18,
    }

# esto significa que la diferencia entre la edad leída del df
# y la que se toma como referencia no debe ser mayor a 2
# sive para cuando tenemos un valor demasiado grande o muy chico
# en alguno de esos casos debo poder resolverlo buscando su edad referencia
distancia_entre_edades = 2

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
            # esto es para el caso que sea por ejemplo un signo -
            return reference_age
    return np.nan

df['Edad_Correcta'] = df.apply(get_correct_age, axis=1, distancia=distancia_entre_edades)

print(df,'\n')