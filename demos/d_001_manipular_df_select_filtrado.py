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

# Puedes filtrar datos en un DataFrame utilizando condiciones lógicas.
print('_'*50 + '\nFiltrar filas donde la edad es mayor de 30_________\n' + '_'*50)
print(df[df['Edad'] > 30])
print('_'*70 + '\n' + '_'*70)


print('_'*50 + '\nFiltrar filas donde la ciudad es Guaymallén o San Martín_________\n' + '_'*50)
print(df[df['Ciudad'].isin(['Guaymallén', 'San Martín'])])
print('_'*70 + '\n' + '_'*70)