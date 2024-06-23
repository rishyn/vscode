
#definir el diccionario
libro = {}

#declarar las variables
fin = False

#iniciar el bucle while

while not fin :
    respuesta = input("Para añadir 'A', para Eliminar 'E' y para Salir 'S': ")
    if respuesta == 'A':
        codigo = input("Introduzca el codigo del libro: ")
        nombre = input("Introduzca el nombre del libro: ")
        libro[codigo] = nombre
        print("Libro añadido exitosamente al diccionario")

    elif respuesta == 'E':
        codigo = input("Introduzca el codigo del libro q desea eliminar: ")
        if codigo in libro.keys():
            del( libro[codigo])
            print("El codigo del libro con el codigo " + codigo + "a sido eliminado")
        else:
            print("El libro no c encuentra en el diccionario ")

    else:
        fin = True

print("El listado del libro final es" , libro)
