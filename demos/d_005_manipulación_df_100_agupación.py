# 7 exploraremos técnicas avanzadas de manipulación de datos utilizando pandas. 
# Esto incluye operaciones complejas de agrupación, pivotaje, y manejo de datos de series temporales.

# 1. Agrupación Avanzada
# Agrupación con múltiples funciones de agregación
# Puedes aplicar múltiples funciones de agregación a la vez utilizando agg.

import pandas as pd

print('\n')
# Crear un DataFrame de ejemplo
print('Crear un DataFrame de ejemplo')
data = {
    'Categoría': ['A', 'A', 'A', 'B', 'B', 'B'],
    'Valor': [10, 15, 14, 20, 22, 21]
}
df = pd.DataFrame(data)
print(df,'\n')

# Agrupar por 'Categoría' y aplicar múltiples funciones de agregación
print('Agrupar por Categoría y aplicar múltiples funciones de agregación')
result = df.groupby('Categoría').agg({
    'Valor': ['mean', 'sum', 'min', 'max']
})
print(result,'\n')