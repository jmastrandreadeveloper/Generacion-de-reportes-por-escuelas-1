# 4 Visualización Avanzada con Seaborn
# Seaborn es una biblioteca basada en Matplotlib 
# que proporciona una interfaz de alto nivel para crear gráficos estadísticos atractivos.

# Gráfico de Dispersión
# Un gráfico de dispersión es útil para mostrar la relación entre dos variables.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print('\n')
# Crear un DataFrame de ejemplo
print('Crear un DataFrame de ejemplo')
data = {
    'Altura': [150, 160, 170, 180, 190],
    'Peso': [50, 60, 70, 80, 90]
}
df = pd.DataFrame(data)
print(df,'\n')

# Crear un gráfico de dispersión
sns.scatterplot(data=df, x='Altura', y='Peso')
plt.title('Relación entre Altura y Peso')
plt.show()