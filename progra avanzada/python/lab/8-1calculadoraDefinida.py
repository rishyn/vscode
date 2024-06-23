class Calculadora:

    def __init__(self , num1 , num2 ):
        #variables de instancia
        self.numero_1 = num1
        self.numero_2 = num2
        self.resultado = 0

    def suma (self):
        #metodo suma
        self.resultado = self.numero_1 + self.numero_2
        return self.resultado

    def resta(self):
        #metodo resta
        self.resultado = self.numero_1 - self.numero_2
        return self.resultado

    def multiplicador (self):
        #metodo multiplicador
        self.resultado = self.numero_1 * self.numero_2
        return self.resultado

    def dividir(self):
        #metodo dividir
        self.resultado = self.numero_1 / self.numero_2
        return self.resultado


#definida por q se le entregan las variables en el mismo codigo
mi_calculo = Calculadora(20 , 10)
print (mi_calculo.dividir())