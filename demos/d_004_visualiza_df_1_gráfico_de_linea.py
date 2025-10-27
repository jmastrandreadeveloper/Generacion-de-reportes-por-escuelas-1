# 1. Creación de Gráficos Básicos con pandas
# Gráfico de Línea
# Un gráfico de línea es útil para mostrar datos a lo largo del tiempo.

import pandas as pd
import matplotlib.pyplot as plt

print('\n')
# Crear un DataFrame de ejemplo
print('Crear un DataFrame de ejemplo')
data = {
    'Fecha': pd.date_range(start='2023-01-01', periods=6, freq='M'),
    'Ventas': [200, 150, 400, 300, 200, 700]
}
df = pd.DataFrame(data)
print(df,'\n')

# Establecer la columna 'Fecha' como índice
df.set_index('Fecha', inplace=True)

# Crear un gráfico de línea
df.plot(kind='line', y='Ventas', title='Ventas Mensuales')
plt.ylabel('Ventas')
plt.show()
