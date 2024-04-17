# -*- coding: utf-8 -*-
# Ejercicio_3-Paradigma_Estructurado.py

# __description__ = "Un juego de sudoku"
# __author__ = "Ricardo Yañez Vega"


"""
Un juego de Sudoku se considera correcto si cumple las siguientes condiciones:
Cada fila y columna contiene los números del 1 al 9 sin repetirse.
Cada subcuadrícula de 3x3 contiene los números del 1 al 9 sin repetirse.

Desarrolle un programa utilizando el paradigma estructurado que dada una matriz de 9x9,
determine si el Sudoku es correcto o no.
Desarrolle un programa utilizando el paradigma funcional que dada una matriz de 9x9,
determine si el Sudoku es correcto o no.

"""

correcto = True

#definir matriz
sudoku = [  [6 , 3 , 7 , 1 , 5 , 9 , 2 , 4 , 8],
            [2 , 8 , 1 , 3 , 4 , 7 , 9 , 5 , 6],
            [5 , 9 , 4 , 2 , 6 , 8 , 1 , 7 , 3],
            [8 , 1 , 6 , 5 , 9 , 2 , 7 , 3 , 4],
            [4 , 2 , 9 , 7 , 8 , 3 , 6 , 1 , 5],
            [3 , 7 , 5 , 6 , 1 , 4 , 8 , 2 , 9],
            [7 , 4 , 2 , 9 , 3 , 6 , 5 , 8 , 1],
            [9 , 5 , 3 , 8 , 2 , 1 , 4 , 6 , 7],
            [1 , 6 , 8 , 4 , 7 , 5 , 3 , 9 , 2] ]

larg = len(sudoku)



for i in sudoku:
    if sum(i) != 45:
        correcto = False


for j in range(larg):
    suma_columna = 0
    for k in range(larg):
        suma_columna += sudoku[j][k]
    if suma_columna != 45:
        correcto =False

if correcto:
    print("Sudoku es correcto.")
else:
    print("sudoku es incorrecto.")