

class Calculadora:

    def __init__( self , num1= 0 ,num2 =0):
        self.numero1 = num1
        self.numero2 = num2
        self.resultado = 0

    def sumar(self):
        self.resultado = self.numero1 +self.numero2
        return (self.resultado)

    def restar(self):
        self.resultado = self.numero1 - self.numero2
        return (self.resultado)

    def multiplicar(self):
        self.resultado = self.numero1 * self.numero2
        return (self.resultado)

    def dividir (self):

        self.resultado = self.numero1 / self.numero2
        return (self.resultado)


#en este casoe el usuario decide q numero colocar

ejemplo = Calculadora()

ejemplo.numero1 = int(input("Por favor introduzca el primer numero: "))
ejemplo.numero2 = int(input("Por favor introduzca el segundo numero: "))

print(ejemplo.multiplicar())
