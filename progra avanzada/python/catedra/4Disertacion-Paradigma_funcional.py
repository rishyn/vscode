# -*- coding: utf-8 -*-
# 4Disertacion-Paradigma_funcional.py

# __description__ = "Mediante el usuario ingrese una lista de largo n con numero
# perteneciente a los naturales el codigo tiene el proposito de ordenarlos"
# __author__ = "Ricardo Yañez Vega , Angel Lara "



def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    medio = len(arr) // 2
    izquierda = arr[:medio]
    derecha = arr[medio:]

    return merge(merge_sort(izquierda), merge_sort(derecha))

def merge(izquierda, derecha):
    if not izquierda:
        return derecha
    if not derecha:
        return izquierda

    if izquierda[0] < derecha[0]:
        return [izquierda[0]] + merge(izquierda[1:], derecha)
    else:
        return [derecha[0]] + merge(izquierda, derecha[1:])



if __name__ == "__main__" :

    #Lista
    arr = []

    i = 1

    #Ingresar el largo de la lista a gusto del cliente
    largo = int(input("Ingrese el largo de la lista "))

    #Ingresa los numero hata el maximo del largo
    while i < largo+1:
        print("Ingrese el numero N°",i)
        numero = int(input())

        arr.append(numero)

        i += 1

    #Imprimir la lista orginal
    print("La lista ingresada es ", arr)

    #Pasarle la lista a la funcion para q la ordene
    arr_ordenado = merge_sort(arr)

    #Imprimir la lista ordenada
    print("Lista ordenada ", arr_ordenado )