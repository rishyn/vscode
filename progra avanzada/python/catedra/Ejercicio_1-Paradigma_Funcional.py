# -*- coding: utf-8 -*-
# Ejercicio_1-Paradigma_Funcional.py

# __description__ = "Comprueba si dos números enteros son números amigos"
# __author__ = "Ricardo Yañez Vega"


"""
Clase 2. Ejercicio 1: Números Amigos

Dos números son amigos, si cada uno de ellos es igual a la suma de los divisores del otro. Por ejemplo, 220 y 284 son amigos, ya que:
  Suma de divisores de 284 : 1 + 2 + 4 + 71 + 142 = 220
  Suma de divisores de 220: 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284

a) Desarrolle un programa utilizando el paradigma estructurado que dado dos números compruebe si son amigos.
b) Desarrolle un programa utilizando el paradigma funcional que dado dos números compruebe si son amigos.
c) BONUS: Dado un número m, muestre todas las parejas de números amigos menores o iguales que m.

"""

def div (num):

    suma = 0
    divisores = []
    for i in range(1 , num//2 +1):
        if num % i ==0:
            suma += i
            divisores.append(i)

    return suma , divisores


def impri_lista(num,lista,suma):
    
    print(f"Suma de los divisores de {num}: ",end="")
    for d in lista[0:-1]:
        print(d , end="+")
    print(f"{lista[-1]}={suma}")


if __name__ == "__main__":
    #un impuct si uno quiere entradas personalizadas

    # definir los numeros
    n = 220
    m = 284

    divi_n = div(n)
    divi_m = div(m)

    lista_n = divi_n[1]
    lista_m = divi_m[1]

    if (divi_n[0] == m) and (divi_m[0] == n):
        print("Los números SON AMIGOS porque: ")
    else:
        print("Los números NO SON AMIGOS porque: ")

    impri_lista(n,lista_n,divi_n[0])
    impri_lista(m,lista_m,divi_m[0])
