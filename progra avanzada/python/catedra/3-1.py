"""definicion de clases y creacion de objetos en python"""

class ClassName:
    #class body
    pass

class Coche:
    """esta clase define el estado y comportamiento de un coche"""
    ruedas = 4

    def __init__(self , color , aceleracion):

        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    def acelera(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frena(self):
        v = self.velocidad - self.aceleracion
        if v < 0 :
            self.velocidad = v

