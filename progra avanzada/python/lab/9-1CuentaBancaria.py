

listaBanco = []


class CuentaBancaria:


    def __init__(self, _numero = " ", _titular = " ", _saldo = 0):
        #variables de instancia
        self.numero = _numero
        self.titular = _titular
        self.saldo = _saldo

    def depositar(self, _cantidad):
        #metodo para depositar dinero en la cuenta
        self.saldo = self.saldo + _cantidad
        print("Se a depositado la cantidad de:", _cantidad , "y el nuevo saldo de la cuenta es:", self.saldo)

    def retirar(self , _cantiad):
        #metodo para retirar dienro de la cuenta
        if _cantiad > self.saldo:
            print("Saldo insuficiente para el retiro")
        else:
            self.saldo = self.saldo - _cantiad
            print("Se ha retirado al cantidad de:", _cantiad ,"y el nuevo saldo de la cuenta es:", self.saldo)

    def mostrar_datos(self):
        #metodo para mostrar los datos de la cuenta
        print("Numero de cuenta:",self.numero)
        print("Titular:", self.titular)
        print("Saldo disponible:",self.saldo)

    def imprimir_datos(self):
        # metodo para imprimir linealmente los datos de la cuenta
        print("Numero de la cuenta:", self.numero, "Titular:", self.titular, "Saldo disponible:",self.saldo)


def crear_cuenta():
    numero_cuenta = input("Ingrese le numero de la cuenta: ")
    titular_cuenta= input("Ingrese el nombre del titular de la nueva cuenta: ")
    saldo_inicial = int(input("Ingrese el saldo inicial de la nueva cuenta:"))
    objeto_cuenta = CuentaBancaria(numero_cuenta, titular_cuenta, saldo_inicial)
    listaBanco.append (objeto_cuenta)
    print("Cuenta creada satisfactoriamente")