

#bucle WHILE

# definir la lista

edades = [10 , 12 , 9 , 11 , 10]

#calculamos el largo de la lista

n = len(edades)

i = 0
total = 0

while i < n:
    total = total + edades[i]

    i += 1

print("La suma de las edades de la lista es",total)



#bucle FOR

#definir la lista
alumnos = ["Ana" , "Juan" , "Carlos" , "Marta"]

for nombre in alumnos:
    print("En esta clase estudia " + nombre)

