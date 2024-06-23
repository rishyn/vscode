alumnos = {}



Calumnos = int(input("Cuantos alumnos desea ingresar: "))
i=1





while i < Calumnos+1 :

    Datos  = []

    print("Ingrese el rut del alumno N°",i,": ")
    rut = input()

    print("Ingrese el nombre del alumno N°",i,": ")
    nombre = input()

    print("Ingrese el apellido del alumno N°",i,":")
    apellido = input()

    print("Ingrese la fecha de nacimiento del alumno N°",i,":")
    Fnacimiento =input()

    Datos.append(nombre)
    Datos.append(apellido)
    Datos.append(Fnacimiento)

    alumnos [rut] = Datos


    i += 1


print(alumnos)














