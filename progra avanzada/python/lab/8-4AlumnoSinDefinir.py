class Alumno:
    #variables de la clase

    tipo = "Estudiante"

    def __init__(self ,  nom = " ", ape = " ", rut = " ", correo = " "):

        #varibles de instancias
        self.nombre= nom
        self.apellido = ape
        self.rut = rut
        self.email = correo


    def imprimir(self):
        #metodo imprimir
        print(self.nombre)
        print(self.apellido)
        print(self.rut)
        print(self.email)


#aqui declaramos a justo del cliente los nombres de la varibles

yo = Alumno()
yo.nombre = input("Introduzca el nombre del alumno: ")
yo.apellido = input("Introduzca el apellido del alumno: ")
yo.rut = input("Introduzca el rut del alumno: ")
yo.email = input("Introduzca el email del alumno: ")
yo.imprimir()
