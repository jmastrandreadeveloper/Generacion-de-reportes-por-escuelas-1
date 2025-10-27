# 5 Gráfico de Caja (Boxplot)
# Un gráfico de caja es útil para mostrar 
# la distribución de una variable y detectar valores atípicos.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print('\n')
# Crear un DataFrame de ejemplo
print('Crear un DataFrame de ejemplo')
data = {
    'Categoría': ['A', 'A', 'A', 'B', 'B', 'B'],
    'Valor': [10, 15, 14, 20, 22, 21]
}
df = pd.DataFrame(data)
print(df,'\n')

# Crear un gráfico de caja
sns.boxplot(data=df, x='Categoría', y='Valor')
plt.title('Distribución de Valores por Categoría')
plt.show()