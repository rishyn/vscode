#ejercicio 2 completo
"""
Calcular el cuadrado de cada elemento en una lista:
(a) Crea una lista de numeros.
(b) Define una funcion lambda que devuelve el cuadrado del numero.
(c) Usa la funcion map() con la funcion lambda para obtener una lista con los
cuadrados de cada elemento.
"""
#crear una lista a gusto

#definir la función lambda para verificar si un número es par
cuadrado = lambda x: x**2 

lista = []
ini = int(input(print("Elija num. inicial lista")))

fin = int(input(print("Elija num. final lista")))

while ini <= fin:
    lista.append(ini)
    #print(ini)
    ini = ini + 1

print("lista completa: ",lista)

# Aplicar la función lambda a cada elemento de la lista
cuadrados = list(map(cuadrado, lista))

print("lista de cuadrados",cuadrados)