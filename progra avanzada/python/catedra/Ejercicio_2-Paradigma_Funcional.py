# -*- coding: utf-8 -*-
# Ejercicio_2-Paradigma_funcional.py

# __description__ = "Comprueba si una matriz dada es un cuadrado mágico"
# __author__ = "Ricardo Yañez Vega"


"""
Clase 2. Ejercicio 2: Cuadrado Mágico

Se considera un cuadrado mágico aquel en el cual las filas, columnas, y las diagonales principal y secundaria suman lo mismo.
Por ejemplo:
  8, 1, 6
  3, 5, 7
  4, 9, 2

a) Desarrolle un programa utilizando el paradigma estructurado que dada una matriz determine si es un cuadrado mágico.
b) Desarrolle un programa utilizando el paradigma funcional que dada una matriz determine si es un cuadrado mágico.

"""




def calculo_sum_d(largo):
    #calcular la suma de los elementros , diagonal principal y segundaria

    suma_diagonal_principal = 0
    suma_diagonal_secundaria = 0
    for i in range(n):
        suma_diagonal_principal += matriz[i][i]
        suma_diagonal_secundaria += matriz[i][largo - i - 1]

    if suma_diagonal_principal != suma_diagonal_secundaria:

        return suma_diagonal_principal , 0

    return suma_diagonal_principal


def suma_fila(matriz):


    suma_filas = [ ]
    for fila in matriz:
        suma_filas.append(sum(fila))

    return suma_filas


def comprobante (las_sumas):


    if not all (suma == las_sumas[0] for suma in las_sumas):
        magic = False
        return magic


def suma_columna(largo , matriz):


    suma_columnas = []
    for j in range (largo):
        s_columna = 0
        for i in range(largo):
            s_columna += matriz[i][j]
        suma_columnas.append(s_columna)

    return suma_columnas



if __name__ == "__main__":
    #cranearselas con el input para una matriz perosnalizada


    magic = 1

    #definir la matriz
    matriz = [  [2, 7, 6],
                [9, 5, 1],
                [4, 3, 8] ]

    #tamaño de la matriz
    n = len(matriz)

    sum_total_d = 0

    calculo_sum_diag = calculo_sum_d(n)

    sumas_f = suma_fila(matriz)

    magic = comprobante (sumas_f)

    sumas_c = suma_columna (n,matriz)

    magic = comprobante(sumas_c)




    if (magic == 1):
        print("La matriz ES un cuadrado mágico.")
    else:
        print("La matriz NO es un cuadrado mágico.")
