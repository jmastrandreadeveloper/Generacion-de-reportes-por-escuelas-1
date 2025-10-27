import pandas as pd

# Manipulación de DataFrames con pandas
print('_'*70 + '\nCrear un diccionario de listas________________________________________\n' + '_'*70)
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
print('_'*70 + '\nSeleccionar las dos primeras filas y las dos primeras columnas________\n' + '_'*70)
print(df.iloc[:2, :2])
print('_'*70 + '\n' + '_'*70)