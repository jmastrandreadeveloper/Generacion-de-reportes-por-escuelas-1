# Fusión y Unión de DataFrames con pandas
# En este tutorial, aprenderás cómo combinar DataFrames 
# utilizando las funciones merge, concat y join de pandas. 
# Estas operaciones te permiten fusionar datos de diferentes 
# fuentes en un solo DataFrame para un análisis más completo.

# 4. Combinar datos con diferentes índices
# Puedes manejar diferentes índices en las combinaciones utilizando merge con los parámetros left_index y right_index.

import pandas as pd

print('\n')
print('Crear el primer DataFrame de ejemplo')
data1 = {
    'Nombre': ['Ana', 'Luis'],
    'Edad': [28, 34]
}
df1 = pd.DataFrame(data1, index=['A', 'B'])
print(df1,'\n')

print('Crear el segundo DataFrame de ejemplo')
data2 = {
    'Ciudad': ['Malargüe', 'San Carlos'],
    'Salario': [50000, 60000]
}
df2 = pd.DataFrame(data2, index=['A', 'C'])
print(df2,'\n')

# Unir los DataFrames usando el índice
print('Unir los DataFrames usando el índice')
df_joined = df1.join(df2)
print(df_joined,'\n')