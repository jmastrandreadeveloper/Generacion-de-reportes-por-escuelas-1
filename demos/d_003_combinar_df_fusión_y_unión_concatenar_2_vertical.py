# Fusión y Unión de DataFrames con pandas
# En este tutorial, aprenderás cómo combinar DataFrames 
# utilizando las funciones merge, concat y join de pandas. 
# Estas operaciones te permiten fusionar datos de diferentes 
# fuentes en un solo DataFrame para un análisis más completo.

# 2. Concatenación de DataFrames con concat
# La función concat te permite concatenar DataFrames a lo largo de un eje (filas o columnas).
# Concatenación vertical (añadir filas)

import pandas as pd

print('\n')
print('Crear el primer DataFrame de ejemplo')
data1 = {
    'Nombre': ['Ana', 'Luis'],
    'Edad': [28, 34]
}
df1 = pd.DataFrame(data1)
print(df1,'\n')

print('Crear el segundo DataFrame de ejemplo')
data2 = {
    'Nombre': ['Carlos', 'Marta'],
    'Edad': [29, 42]
}
df2 = pd.DataFrame(data2)
print(df2,'\n')

# Concatenar los DataFrames verticalmente
print('Concatenar los DataFrames verticalmente')
df_concat = pd.concat([df1, df2], axis=0)
print(df_concat,'\n')