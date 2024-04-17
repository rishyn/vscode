#!/urs/bin/python
#-*- coding: utf-8 -*-
#Nombre Autor: Ricardo Yañez, Matías Olave



import math
import re








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
        #ver.append(ii)

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
    resultados_2=[]

    x=0
    z=0
    while x<len(listadoNum) :
        if listadoNum[z] =="NO DIVISIBLE":
            resultados_2.append("NO DIVISIBLE")

        else:
            num_descom =descomponer_factores(listadoNum[z])
            resultados_2.append(num_descom)

            z=z+1
        x = x+1

    #resultados_2=resultados_2[0]
    return num_descom

def descomponer_factores(numero):
    #print(end='')
    Factor_Pri =2
    Primer_Factor= True
    cantidad_factores=0
    while numero> 1:
        if numero% Factor_Pri ==0:
            cantidad_factores = cantidad_factores+1
            numero//= Factor_Pri
        else:
            Primer_Factor,cantidad_factores = escribe_factor(Primer_Factor,Factor_Pri, cantidad_factores)
            Factor_Pri = siguiente_primo(Factor_Pri)
    Primer_Factor, cantidad_factores = escribe_factor(Primer_Factor,Factor_Pri,cantidad_factores)


def escribe_factor(Primer_Factor,Factor_Pri,cantidad_factores):


    if cantidad_factores> 0:
        if Primer_Factor:
            Primer_Factor =False
        else:
            print(' ',end='')


        print('{:d} {:d}'.format(Factor_Pri,cantidad_factores),end='')
        
        cantidad_factores =0
    return Primer_Factor, cantidad_factores







def siguiente_primo(num):
    while True:
        num =num +1
        if es_primo(num):
            return num



def es_primo(num):
    if num <= 1:
        return False
    encontrar_divi = False
    i = 2
    while i <= math.sqrt(num) and not encontrar_divi:
        if num % i == 0:
            encontrar_divi = True
        i= i+1
    return not encontrar_divi

















if __name__ == '__main__':
    los_numeros =procesar('primos.txt')
    procesamiento =procesing(los_numeros)
    procesamiento2=procesing2(procesamiento)
    transformacion =transformation(procesamiento2)
    print(transformacion)

