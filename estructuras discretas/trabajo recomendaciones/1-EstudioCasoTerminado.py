import pandas as pd

# Función para cargar las películas
def abrepelis():
    file = pd.read_csv("movies.csv", sep = ",")
    dic = file.set_index("movieId")["title"].to_dict()
    # Diccionario que contiene las ids de las peliculas y los titulos de las peliculas
    return file, dic

# Función para cargar las calificaciones de las películas
def abreratings():
    file = pd.read_csv("ratings.csv", sep = ",")
    dicc = {}
    for index, row in file.iterrows():
        user_id = int(row["userId"])
        movie_id = int(row["movieId"])
        rating = row["rating"]

        # Guardamos las tuplas (movie_id, rating) para cada user_id
        if user_id not in dicc:
            dicc[user_id] = []
        dicc[user_id].append((movie_id, rating))  # Añadimos la tupla (movie_id, rating)
    
    return file, dicc

# Función para recomendar películas
def recomendar_peliculas(user_id, dicc, dic, rating_minimo=4.0):
    # Obtener las películas que el usuario ha visto (en base a dicc)
    peliculas_vistas = {movie_id for movie_id, rating in dicc.get(user_id, [])}
    
    # Lista de películas recomendadas
    peliculas_recomendadas = []
    
    # Recorrer todas las películas en el diccionario dic (todas las películas)
    for movie_id, title in dic.items():
        # Comprobar que la película no haya sido vista por el usuario
        if movie_id not in peliculas_vistas:
            # Filtrar solo las películas con rating >= rating_minimo
            for _, rating in dicc.get(user_id, []):
                if rating >= rating_minimo and movie_id not in peliculas_vistas:
                    peliculas_recomendadas.append(title)
                    break
    
    return peliculas_recomendadas

def calcular_jaccard(set1, set2):
    if not set1 and not set2:
        return 0.0
    return len(set1 & set2) / len(set1 | set2)

if __name__ == "__main__":
    # Cargar los datos
    _, dic_peliculas = abrepelis()
    _, dic_calificaciones = abreratings()

    # Recomendar películas al usuario con id x
    user_id = 2
    recomendaciones = recomendar_peliculas(user_id, dic_calificaciones, dic_peliculas, rating_minimo=4.0)
    print("Películas recomendadas para el usuario", user_id, ":")
    n = 0
    # Delimitar la cantidad de peliculas recomendadas para no mostrarlas todas
    while n < 5:
        print(recomendaciones[n])
        n+=1
    print(f"El resultado de la métrica de Jaccard es: {calcular_jaccard(set(dic_calificaciones),set(dic_peliculas))}")

