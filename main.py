import matplotlib.pyplot as plt
import pandas as pd

# Cargar los datos desde el archivo CSV
data = pd.read_csv('tu_archivo.csv')

# Crear un gráfico, por ejemplo, un gráfico de barras
plt.bar(data['Columna_X'], data['Columna_Y'])
plt.xlabel('Etiqueta del eje X')
plt.ylabel('Etiqueta del eje Y')
plt.title('Título del gráfico')

# Guardar el gráfico en un archivo .jpg
plt.savefig('mi_grafico.jpg')

# Mostrar el gráfico (opcional)
plt.show()
