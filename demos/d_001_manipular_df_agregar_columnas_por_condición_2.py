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
# Aplicar funciones
# Puedes aplicar funciones a las columnas o filas de un DataFrame utilizando apply.
# Definir una función que clasifica edades
def clasificar_edad(edad):
    if edad < 30:
        return 'Joven'
    elif edad < 40:
        return 'Adulto'
    else:
        return 'Mayor'

# Aplicar la función a la columna 'Edad'
df['Clasificación'] = df['Edad'].apply(clasificar_edad)
print(df,'\n')