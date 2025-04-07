import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar estilo visual
sns.set(style="whitegrid")

# Cargar los datos
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

# Gráfico 1: Distribución de Calificaciones
plt.figure(figsize=(8, 5))
sns.histplot(ratings['rating'], bins=10, color='cornflowerblue')
plt.title("Distribución de Calificaciones", fontsize=14)
plt.xlabel("Rating", fontsize=12)
plt.ylabel("Frecuencia", fontsize=12)
plt.tight_layout()
plt.savefig("grafico_distribucion_ratings.png")  # Guarda como imagen
plt.show()

# Gráfico 2: Top 10 Películas con Más Calificaciones
top10 = ratings['movieId'].value_counts().head(10).rename_axis('movieId').reset_index(name='num_ratings')
top10 = top10.merge(movies[['movieId', 'title']], on='movieId')

plt.figure(figsize=(10, 6))
sns.barplot(data=top10, y='title', x='num_ratings', palette="viridis")
plt.title("Top 10 Películas Más Calificadas", fontsize=14)
plt.xlabel("Número de Calificaciones", fontsize=12)
plt.ylabel("Película", fontsize=12)
plt.tight_layout()
plt.savefig("grafico_top10_peliculas.png")  # Guarda como imagen
plt.show()

# Gráfico 3: Calificaciones por Usuario
user_activity = ratings['userId'].value_counts()

plt.figure(figsize=(8, 5))
sns.histplot(user_activity, bins=30, color='salmon')
plt.title("Distribución de Calificaciones por Usuario", fontsize=14)
plt.xlabel("Número de Calificaciones", fontsize=12)
plt.ylabel("Cantidad de Usuarios", fontsize=12)
plt.tight_layout()
plt.savefig("grafico_actividad_usuarios.png")  # Guarda como imagen
plt.show()
