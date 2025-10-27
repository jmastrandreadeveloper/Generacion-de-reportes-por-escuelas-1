import pandas as pd

print('\n')
# Creación de un DataFrame desde un diccionario
# Una de las formas más comunes de crear un DataFrame es a partir de un diccionario de listas.
print('Crear un diccionario de listas')
data = {
    'Nombre'    : ['Ana', 'Luis', 'Carlos', 'Marta'],
    'Edad'      : [28, 34, 29, 42],
    'Ciudad'    : ['Guaymallén', 'Godoy Cruz', 'San Rafael', 'San Martín']
}
index = ['Indice 1','Indice 2','Indice 3','Indice 4',]
print(data,'\n')
# Crear un DataFrame a partir del diccionario
df = pd.DataFrame(data, index=index)
# Mostrar el DataFrame
print(df,'\n')