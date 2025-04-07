import pandas as pd
from collections import defaultdict

def abrepelis():
    file = pd.read_csv("movies.csv", sep=",")
    dic = file.set_index("movieId")["title"].to_dict()
    return file, dic

def abreratings(threshold=4.0):
    file = pd.read_csv("ratings.csv", sep=",")
    dicc = defaultdict(list)
    Gt = set()
    U = set()
    M = set()
    for index, row in file.iterrows():
        user_id = int(row["userId"])
        movie_id = int(row["movieId"])
        rating = row["rating"]
        if rating >= threshold:
            dicc[user_id].append((movie_id, rating))
            Gt.add((user_id, movie_id))
            U.add(user_id)
            M.add(movie_id)
    return file, dicc, Gt, U, M

def construir_diccionarios(Gt):
    Ut = defaultdict(set)
    Mt = defaultdict(set)
    for u, m in Gt:
        Ut[u].add(m)
        Mt[m].add(u)
    return Ut, Mt

def calcular_jaccard(set1, set2):
    if not set1 and not set2:
        return 0.0
    return len(set1 & set2) / len(set1 | set2)

def SIMu(u1, u2, Ut):
    return calcular_jaccard(Ut[u1], Ut[u2])

def SIMm(m1, m2, Mt):
    return calcular_jaccard(Mt[m1], Mt[m2])

def recomendar_por_usuarios(target_user, Ut, U, k=5):
    similares = sorted(U - {target_user}, key=lambda u: SIMu(target_user, u, Ut), reverse=True)[:k]
    recomendaciones = set()
    for vecino in similares:
        recomendaciones |= Ut[vecino]
    return recomendaciones - Ut[target_user]

def recomendar_por_items(target_user, Ut, Mt, M, k=5):
    peliculas_vistas = Ut[target_user]
    recomendaciones = set()
    for m in peliculas_vistas:
        similares = sorted(M - {m}, key=lambda x: SIMm(m, x, Mt), reverse=True)[:k]
        recomendaciones |= set(similares)
    return recomendaciones - peliculas_vistas

def recomendar_por_popularidad(filtrados, Ut, target_user, top_n=10):
    populares = filtrados.groupby('movieId').size().sort_values(ascending=False).index.tolist()
    ya_vistas = Ut[target_user]
    recomendaciones = [m for m in populares if m not in ya_vistas]
    return recomendaciones[:top_n]

def mostrar_recomendaciones(user_id, recomendaciones, dic_peliculas, titulo):
    print(f"\n📌 {titulo} para el usuario {user_id}:")
    for i, movie_id in enumerate(list(recomendaciones)[:5]):
        print(f"{i+1}. {dic_peliculas.get(movie_id, 'Título no encontrado')}")

def main():
    peliculas_df, dic_peliculas = abrepelis()
    ratings_df, dicc, Gt, U, M = abreratings()
    Ut, Mt = construir_diccionarios(Gt)

    user_id = 2
    print(f"\nCardinalidades:\n|U| = {len(U)}, |M| = {len(M)}, |Gt| = {len(Gt)}")

    rec_usuarios = recomendar_por_usuarios(user_id, Ut, U)
    mostrar_recomendaciones(user_id, rec_usuarios, dic_peliculas, "Recomendación basada en Usuarios")

    rec_items = recomendar_por_items(user_id, Ut, Mt, M)
    mostrar_recomendaciones(user_id, rec_items, dic_peliculas, "Recomendación basada en Ítems")

    rec_popularidad = recomendar_por_popularidad(ratings_df, Ut, user_id)
    mostrar_recomendaciones(user_id, rec_popularidad, dic_peliculas, "Recomendación por Popularidad")

if __name__ == "__main__":
    main()
