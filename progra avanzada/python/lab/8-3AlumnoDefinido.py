

class Alumno:
    #variables de la clase
    tipo = "Estudiante"

    def __init__(self, nom , ape , rut , correo):
        #variavles de instancia
        self.nombre = nom
        self.apellido = ape
        self.rut = rut
        self.email = correo

    def imprimir(self):
        #metodo imprimir
        print(self.nombre)
        print(self.apellido)
        print(self.rut)
        print(self.email)


yo = Alumno("Jorge","Martinez "," 19.877.614-1","jMartinez@alu.cum.cl")

yo.imprimir()
