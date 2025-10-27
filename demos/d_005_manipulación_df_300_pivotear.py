# 7 exploraremos técnicas avanzadas de manipulación de datos utilizando pandas. 
# Esto incluye operaciones complejas de agrupación, pivotaje, y manejo de datos de series temporales.

# 2. Pivotaje y Despivotaje
# Crear tablas pivote
# Las tablas pivote son útiles para reorganizar y resumir datos.

import pandas as pd

print('\n')
# Crear un DataFrame de ejemplo
print('Crear un DataFrame de ejemplo')
data = {
    'Fecha': ['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-02'],
    'Ciudad': ['Madrid', 'Madrid', 'Barcelona', 'Barcelona'],
    'Ventas': [100, 150, 200, 250]
}
df = pd.DataFrame(data)
print(df,'\n')

# Crear una tabla pivote
print('Crear una tabla pivote')
pivot = df.pivot_table(index='Fecha', columns='Ciudad', values='Ventas', aggfunc='sum')
print(pivot,'\n')