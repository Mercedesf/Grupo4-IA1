import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 1. Definir los puntos (pares de números del 0 al 5)
puntos_totales = np.array([
    [5, 4], [4, 3], [2, 1], [3, 1], [0, 0], 
    [5, 3], [5, 2], [3, 0], [1, 1], [4, 5], 
    [4, 0], [1, 4], [0, 5], [5, 1], [5, 5], 
    [3, 4], [2, 0], [0, 3], [3, 5], [4, 2], 
    [2, 2], [3, 3], [4, 4]
])

# 2. Tomar solo 20 puntos como pide el inciso 3.1
# (Si necesitas usar los 23, simplemente cambia a: puntos = puntos_totales)
puntos = puntos_totales[:20]

# 3. Implementar el algoritmo K-means para 2 grupos
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
kmeans.fit(puntos)

# 4. Obtener las clasificaciones (etiquetas) y los centroides
etiquetas = kmeans.labels_
centroides = kmeans.cluster_centers_

# 5. Graficar los resultados
plt.figure(figsize=(8, 6))

# Asignar colores según el grupo (0 o 1)
colores = ['#1f77b4' if etiqueta == 0 else '#ff7f0e' for etiqueta in etiquetas]

# Graficar los puntos
plt.scatter(puntos[:, 0], puntos[:, 1], c=colores, s=100, edgecolors='black', zorder=2, label='Puntos clasificados')

# Graficar los centroides
plt.scatter(centroides[:, 0], centroides[:, 1], c='red', s=200, marker='X', zorder=3, label='Centroides')

# Configurar el gráfico para que coincida con el rango [0, 5]
plt.xlim(-0.5, 6)
plt.ylim(-0.5, 6)
plt.xticks(np.arange(0, 7, 1))
plt.yticks(np.arange(0, 7, 1))

plt.title('Clasificación K-means (k=2)')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.grid(True, linestyle='--', alpha=0.7, zorder=1)
plt.legend()
plt.show()