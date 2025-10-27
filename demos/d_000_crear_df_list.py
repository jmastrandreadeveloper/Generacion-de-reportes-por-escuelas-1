import pandas as pd

print('\n')
# Creación de un DataFrame desde una lista de diccionarios
# Otra forma de crear un DataFrame es a partir de una lista de diccionarios.
print('Crear una lista de diccionarios')
data = [
    {'Nombre': 'Ana', 'Edad': 28, 'Ciudad': 'Guaymallén'},
    {'Nombre': 'Luis', 'Edad': 34, 'Ciudad': 'Godoy Cruz'},
    {'Nombre': 'Carlos', 'Edad': 29, 'Ciudad': 'San Rafael'},
    {'Nombre': 'Marta', 'Edad': 42, 'Ciudad': 'San Martín'}
]
index = ['A','B','C','D',]
# Crear un DataFrame a partir de la lista de diccionarios
df = pd.DataFrame(data, index=index)
# Mostrar el DataFrame
print(df,'\n')