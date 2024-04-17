# -*- coding: utf-8 -*-
# 4Disertacion-Paradigma_estructurado.py

# __description__ = "Mediante el usuario ingrese una lista de largo n con numero
# perteneciente a los naturales el codigo tiene el proposito de ordenarlos"
# __author__ = "Ricardo Yañez Vega , "



def merge_sort(arr):
    if len(arr) <= 1:
        return arr


    # Dividir el arreglo en mitades
    medio = len(arr) // 2
    izquierda = arr[:medio]
    derecha = arr[medio:]

    # Llamar recursivamente a merge_sort para ordenar cada mitad
    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)

    # Combinar las mitades ordenadas
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0

    # Combinar las dos mitades en orden
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Agregar elementos restantes de izquierda, si los hay
    while i < len(izquierda):
        resultado.append(izquierda[i])
        i += 1

    # Agregar elementos restantes de derecha, si los hay
    while j < len(derecha):
        resultado.append(derecha[j])
        j += 1

    return resultado

if __name__ == "__main__" :

    #Lista vacia
    arr = []

    i = 1

    #Ingresar el largo de la lista a gusto del cliente
    largo = int(input("Ingrese el largo de la lista "))

    #Ingresar los numero hasta el maximo del largo
    while i < largo+1:
        print("Ingrese el numero N°",i)
        numero = int(input())

        arr.append(numero)

        i += 1

    #Imprimir la lista orginal
    print("La lista ingresada es ", arr)

    #Pasarle la lista para q la ordene
    arr_ordenado = merge_sort(arr)

    #Imprimir la lista ordenada
    print("Lista ordenada ", arr_ordenado )


