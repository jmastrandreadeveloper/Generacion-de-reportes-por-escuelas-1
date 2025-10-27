import pandas as pd

# Manipulación de DataFrames con pandas
print('_'*50 + '\nCrear un diccionario de listas____________________\n' + '_'*50)
data = {
    'Nombre'    : ['Ana', 'Luis', 'Carlos', 'Marta'],
    'Edad'      : [28, 34, 29, 42],
    'Ciudad'    : ['Guaymallén', 'Godoy Cruz', 'San Rafael', 'San Martín']
}
# Crear un DataFrame a partir del diccionario
df = pd.DataFrame(data)
print(df)

# Selección de un subconjunto de datos
# Puedes seleccionar un subconjunto de datos especificando tanto filas como columnas. 
print('_'*50 + '\nSeleccionar filas y columnas específicas por etiquetas_________\n' + '_'*50)
print(df.loc[0:2, ['Nombre', 'Ciudad']])
print('_'*50 + '\n' + '_'*50)