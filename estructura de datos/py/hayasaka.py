#!/urs/bin/python
#-*- coding: utf-8 -*-
#Nombre Autor: Ricardo Yañez, Matías Olave



import math
import re

from numpy import result_type

#funciones profe hugo
def primo(num1):
    for x in range (1,num1):
        if (num1%x==0 and x!=num1 and x!=1):
            return False
    return num1

def llena_lista_primos(nro):
    primos = []
    for i in range(2, nro):
        if primo(i):
            primos.append(i)
    return primos

def factores(numero, primos):
    divisibles=[]
    while numero > 1:
        if primo(numero):
            divisibles.append(numero)
            break
        for i in range(len(primos)):
            if numero % primos[i] == 0:
                divisibles.append(int(primos[i]))
                numero = numero // primos[i]
                break
    return divisibles

def ALista(listaSinArreglar):
    L_final=[]
    lista_Ex=[]
    L_Bases=[]
    lista=sorted(listaSinArreglar,reverse=True)
    a=lista[0]
    L_Bases.append(a)
    for i in lista:
        if i != a:
            a=i
            L_Bases.append(a)
    for i in L_Bases:
        lista_Ex.append(lista.count(i))
    cantidad=len(L_Bases)
    for i in range(cantidad):
            L_final.append(L_Bases[i])
            L_final.append(lista_Ex[i])
    return L_final


def procesar(num):#leemos el archivo con los numero y los'ordenamos'
    nume= open(num)
    numbers= []
    for linea in nume:
        linea =linea.rstrip('\n')
        #linea =linea.split(',')
        numbers.append(linea)
    nume.close()
    return numbers

def procesing(lista):

    ver=[]
    multiplicados=[]
    for ii in lista:
        los_numerosE=[]
        ii = list(re.sub(r"\s+", "", ii))

        z= 0
        x= 0
        largo =len(ii)/2

        while x<(len(ii)/2):
            numeroE =((int(ii[z]))**(int(ii[z+1])))
            x = x+1
            z = z+2
            los_numerosE.append(numeroE)
        multiplicado= math.prod(los_numerosE)
        multiplicados.append(multiplicado)

    return multiplicados

def procesing2(lista):

    resultados=[]
    z=0
    x=0
    while x<(len(lista)/2):
        resto = lista[z]%lista[z+1]
        numDividido =lista[z]/lista[z+1]
        if resto != 0:
            resultados.append("NO DIVISIBLE")
        else:
            numDividido =lista[z]/lista[z+1]
            resultados.append(numDividido)
        x= x+1
        z= z+1

    return resultados

def transformation(listadoNum):
    #print(listadoNum)
    resultados_2=[]

    for  i in listadoNum:
        if i =="NO DIVISIBLE":
            resultados_2.append("NO DIVISIBLE")

        else:
            primos = llena_lista_primos(1000)
            lista_S = factores(int(i), primos)

            listasemifinal=ALista(lista_S)
            #print(len(listasemifinal))
            contador  = 0
            for ii in listasemifinal:
                contador = contador +1
                if contador == len(listasemifinal) :
                    resultados_2.append(str(ii))
                    resultados_2.append(" ")
                    contador = 0
                else:
                    resultados_2.append(str(ii))
    return resultados_2


def salida(transformacion):
    file = open("resultado.txt", "w")

    for linea in transformacion:
        print(linea)
        if linea == "NO DIVISIBLE":
            file.write(linea+"\n")
        else:
            file.write(linea)
            file.write(" ")
            if linea == " ":
                file.write("\n")




if __name__ == '__main__':
    los_numeros =procesar('primos.txt')
    procesamiento =procesing(los_numeros)
    procesamiento2=procesing2(procesamiento)
    transformacion =transformation(procesamiento2)
    salida(transformacion)








