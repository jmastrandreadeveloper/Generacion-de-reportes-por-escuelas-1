import pandas as pd

# Manipulación de DataFrames con pandas
# Introducción
# En este tutorial, aprenderás cómo manipular y transformar los datos dentro de un DataFrame utilizando pandas. 
# Cubriremos operaciones comunes como seleccionar, filtrar, agregar, y transformar datos.
print('_'*50 + '\nCrear un diccionario de listas____________________\n' + '_'*50)
data = {
    'Nombre'    : ['Ana', 'Luis', 'Carlos', 'Marta'],
    'Edad'      : [28, 34, 29, 42],
    'Ciudad'    : ['Guaymallén', 'Godoy Cruz', 'San Rafael', 'San Martín']
}
# Crear un DataFrame a partir del diccionario
df = pd.DataFrame(data)
print(df)
print('_'*50 + '\n' + '_'*50)

# Selección de columnas
# Puedes seleccionar una o más columnas de un DataFrame utilizando el nombre de la columna o una lista de nombres de columnas.
print('_'*50 + '\nSeleccionar una columna___________________________\n' + '_'*50)
print(df['Nombre'])
print('_'*50 + '\n' + '_'*50)