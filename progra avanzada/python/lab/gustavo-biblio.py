from os import system
libreria = {}

def incluir():
    print()
    nombre = input("Ingrese el nombre del Libro: ")
    isbn = int(input("Ingrese el ISBN del libro: "))
    autor = (input(f"Autor del libro \"{nombre}\": "))
    incluir = {isbn : [nombre,autor]}
    libreria.update(incluir)
    return 


def buscar():
    buscar = int(input('Ingrese el ISBN a buscar: '))
    try:
        print(f"Nombre: {list(libreria[buscar])[0]}\nEdad: {list(libreria[buscar])[1]}")
    except KeyError:
        print("No existe ese ISBN en la base de datos.")
    return


def mostrar():
    print(libreria)
    return


def limpiar_consola():
    input("Presione Enter para continuar...")
    system('cls')
    return

def menu():
    print("\nMenu Principal")
    print("------------------------------------------")
    print("1. Ingresar Datos")
    print("2. Buscar por ISBN..")
    print("3. Imprimir Toda la base de datos.")
    print("4. Eliminar elemento de base de datos.")
    print("5. Salir")
    print("------------------------------------------")



if __name__ == "__main__":
    while True:
        menu()
        opcion = input(">>")
        if opcion == '1':
            print("Cuantos Libros desea ingresar? ")
            n = int(input())
            for i in range(n):
                incluir()
            limpiar_consola()
        elif opcion =='2' and len(libreria)>0:
            buscar()
            limpiar_consola()
        elif opcion =='3':
            mostrar()
            limpiar_consola()
        elif opcion == '4' and  len(libreria) > 0:
            buscar = int(input('Ingrese el ISBN a buscar: '))
            try:
                print(f"El libro es...\nNombre: {list(libreria[buscar])[0]}\nEdad:{list(libreria[buscar])[1]}")
                confirmar = str(input("¿Desea eliminarlo? Y/N ")).lower()
                if confirmar=='y':
                    libreria.pop(buscar)
                else:
                    continue
            except KeyError:
                print("No existe ese ISBN en la base de datos.")
            limpiar_consola()
        elif opcion == "5":
            limpiar_consola()
            break