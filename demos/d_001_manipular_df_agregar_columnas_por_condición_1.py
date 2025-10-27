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

# Agregar columnas
# Puedes agregar nuevas columnas a un DataFrame basado en cálculos u otros datos.
print('Agregar una columna que indica si la persona es mayor de 30 años')
df['Mayor_de_30'] = df['Edad'] > 30
print(df,'\n')