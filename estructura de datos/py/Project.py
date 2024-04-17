#!/urs/bin/python
#-*- coding: utf-8 -*-
#integrantes: Bernardo Fuentes Galdames, Daniel Yañez Morales



import math
from os import startfile
import re


def n_primo(primer_numero):
    for c in range (1, primer_numero):
        if (primer_numero%c == 0 and c != primer_numero and c != 1):
            return False
    return primer_numero

def lis_completa(numero):
    n_primos = []
    for i in range(2, numero):
        if n_primo(i):
            n_primos.append(i)
    return n_primos

def variables(num, n_primos):
    division = []
    while num > 1:
        if n_primo(num):
            division.append(num)
            break
        for i in range(len(n_primos)):
            if num % n_primos[i] == 0:
                division.append(int(n_primos[i]))
                num = num // n_primos[i]
                break
    return division

def lis_a(no_terminada):
 #   print(no_terminada)
    bas_lis = []
    ej_lis = []
    ult_lis = []
    lis = sorted(no_terminada, reverse = True)
    a = lis[0]
    bas_lis.append(a)
    for i in lis:
        if i != a:
            a = i
            bas_lis.append(a)
    for i in bas_lis:
        ej_lis.append(lis.count(i))
    proporcion=len(bas_lis)
    for i in range(proporcion):
            ult_lis.append(bas_lis[i])
            ult_lis.append(ej_lis[i])
    return ult_lis


def ordenar(numer):
    n= open(numer)
    cantidad = []
    for lin in n:
        lin = lin.rstrip('\n')
        cantidad.append(lin)
    n.close()
    return cantidad

def ordenando(lis):

    observacion = []
    result_multi = []
    for ii in lis:
        la_cant_num = []
        ii = list(re.sub(r"\s+", "", ii))

        b = 0
        c = 0
        cant_largura =len(ii)/2

        while c<(len(ii)/2):
            cant_num = ((int(ii[b]))**(int(ii[b+1])))
            c = c+1
            b = b+2
            la_cant_num.append(cant_num)
        multi = math.prod(la_cant_num)
        result_multi.append(multi)

    return result_multi

def ordenado(lis):


    result = []
    b = 0
    c = 0
    while c<(len(lis)/2):
        resto = lis[b]%lis[b+1]
        cant_divi = lis[b]/lis[b+1]
        if resto != 0:
            result.append("NO DIVISIBLE")
        else:
            cant_divi = lis[b]/lis[b+1]
            result.append(cant_divi)
        c = c+1
        b = b+1
    print(result)
    return result

def formacion(alistacion):
   # print(alistacion)
    segundo_resultado = []

    for  i in alistacion:
        if i == "NO DIVISIBLE":
            segundo_resultado.append("NO DIVISIBLE")

        else:
            n_primos = lis_completa(1000)
            lis_x = variables(int(i), n_primos)
            casi_terminada = lis_a(lis_x)
            segundo_resultado.append(casi_terminada)
    return segundo_resultado

def salida(forma):

    print(forma)
    file = open("resultado.txt", "w")
    for linea in forma:
        if linea == "NO DIVISIBLE":
            file.write(linea+"\n")
        else:
            listToStr = ' '.join([str(elem) for elem in linea])
            file.write(listToStr+"\n")
    file.close()

if __name__ == '__main__':
    numeros_finales = ordenar('primos.txt')
    primer_ordenamiento = ordenando(numeros_finales)
    segundo_ordenamiento = ordenado(primer_ordenamiento)
    forma = formacion(segundo_ordenamiento)
    salida(forma)



