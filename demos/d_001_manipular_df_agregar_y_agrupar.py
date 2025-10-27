import pandas as pd

print('\n')
# Manipulación de DataFrames con pandas
print('Crear un diccionario de listas')
data = {
    'Nombre'    : ['Ana', 'Luis', 'Carlos', 'Marta'],
    'Edad'      : [28, 34, 29, 42],
    'Ciudad'    : ['Guaymallén', 'Godoy Cruz', 'San Rafael', 'San Martín']
}
# Crear un DataFrame a partir del diccionario
df = pd.DataFrame(data)
print(df,'\n')

print('Definir una función que clasifica edades')
def clasificar_edad(edad):
    if edad < 30:
        return 'Joven'
    elif edad < 40:
        return 'Adulto'
    else:
        return 'Mayor'

# Aplicar la función a la columna 'Edad'
df['Clasificación'] = df['Edad'].apply(clasificar_edad)
print(df,'\n')

# Agrupación y Agregación de Datos
# Puedes agrupar datos por una o más columnas y luego aplicar funciones de agregación como sum, mean, etc.
print('Agrupar por Ciudad y calcular la edad promedio')
grupo_ciudad = df.groupby('Ciudad')
print(grupo_ciudad['Edad'].mean(),'\n')

print('Agrupar por Clasificación y contar el número de personas en cada grupo') 
print(df.groupby('Clasificación').size(),'\n')