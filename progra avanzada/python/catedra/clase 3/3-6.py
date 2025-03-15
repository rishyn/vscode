
"""Realcion de compocicion entre calses"""

# Relacion de composición entre clases
class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

    def __del__(self):
        print("Motor eliminado")

class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor("V8") # Se crea la instancia del objeto parte dentro del objeto compuesto

    def __del__(self):
        del self.motor # Elimina la instancia del objeto parte dentro del objeto compuesto
        print("Auto eliminado")


auto_1 = Auto("Toyota", "Corolla") # Se crea instancia de objeto compuesto
print(auto_1.motor.tipo)

del auto_1 # Elimina la instancia de Auto