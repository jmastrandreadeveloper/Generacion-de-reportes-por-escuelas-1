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
print('_'*50 + '\n' + '_'*50)

# Selección de filas
# Puedes seleccionar filas utilizando iloc para índices basados en la posición y loc para índices basados en etiquetas.
print('_'*50 + '\nSeleccionar la primera fila_______________________\n' + '_'*50)
print(df.iloc[0])
print('_'*50 + '\n' + '_'*50)