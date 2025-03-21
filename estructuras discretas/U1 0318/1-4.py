#ejercicio 3 completo
"""
Calcular el promedio de una lista de numeros:
(a) Crea una lista de numeros.
(b) Define una funcion lambda que devuelve la suma de dos numeros.
(c) Usa la funcion reduce() con la funcion lambda para calcular la suma de todos
los numeros en la lista.
(d) Divide la suma por la longitud de la lista para obtener el promedio.
"""
#crear una lista a gusto

#definir la función lambda para verificar si un número es par
sumar = lambda a, b: a + b

lista = []

ini = int(input(print("Elija num. inicial lista")))

fin = int(input(print("Elija num. final lista")))

while ini <= fin:
    lista.append(ini)
    #print(ini)
    ini = ini + 1

suma_total = sum(lista)

promedio = (suma_total/len(lista))

print("lista completa: ", lista)
print("suma total: ", suma_total)
print("promedio: ", promedio)