#ejercicio 1 completo
"""
Filtrar una lista de numeros:
(a) Crea una lista de numeros.
(b) Define una funcion lambda que devuelve True si el numero es par.
(c) Usa la funcion filter() con la funcion lambda para obtener una lista con solo
los numeros pares
"""
#crear una lista a gusto

#definir la función lambda para verificar si un número es par
es_par = lambda x: x % 2 == 0

lista = []
ini = int(input(print("Elija num. inicial lista")))

fin = int(input(print("Elija num. final lista")))

while ini <= fin:
    lista.append(ini)
    #print(ini)
    ini = ini + 1

print("lista completa: ",lista)

# Filtrar los números pares usando la función lambda
pares = list(filter(es_par, lista))

# Imprimir la lista de números pares
print("lista num pares: ",pares)
