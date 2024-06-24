"""atributos de instancias o clases en python"""


"""Usos de __dict__ y __slots__"""
class Punto:

    def __init__(self ,x ,y):
        self.x = x
        self.y = y



punto_1 = Punto (4, 8)
punto_1.__dict__


"""ejemplo de slots"""
class Punto2:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

punto_2 = Punto2(4, 8)
punto_2.__dict__

#buscar modificar clase dinamicamente
"""_____________________________________________________________________________"""
"""Modificar valores de las instancias"""



import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, value):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError("positive number expected")
        self._radio = value

    def area(self):
        return round(math.pi * self._radio**2, 2)

circle_1 = Circulo(100)
print("Radio: ", circle_1.radio)
print("Area: ", circle_1.area())

circle_1.radio = 500
print("Radio: ", circle_1.radio)
print("Area: ", circle_1.area())







