"""Comportamiento de clases en python mediante metodos"""

"""implementacion de metodos en python"""

"""
metodos de instancia q se usan  SELF
metodos de clase q se usa CLS como primer argunmento
metodos estaticos q no toman ni la clase ni la instancia
"""

"""Metodos de instancia especiales
llamados DUNDER o Metodos Magicos    q son __str__  ___repr___"""


class Auto:
    ruedas = 4

    def __init__(self, marca, modelo, año, color, aceleracion=10):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.aceleracion = aceleracion
        self.encendido = False
        self.velocidad = 0
        self.max_velocidad = 200

    def acelerar(self):
        if not self.encendido:
            print("Auto apagado!")
            return
        if self.velocidad + self.aceleracion <= self.max_velocidad:
            self.velocidad += self.aceleracion
        else:
            self.velocidad = self.max_velocidad
        print(f"Acelerando a {self.velocidad} km/h...")

    def frenar(self):
        if self.velocidad - self.aceleracion >= 0:
            self.velocidad -= self.aceleracion
        else:
            self.velocidad = 0
        print(f"Frenando a {self.velocidad} km/h...")

    def encender(self):
        self.encendido = True
        print("Auto encendido...")

    def apagar(self):
        self.velocidad = 0
        self.encendido = False
        print("Auto apagado...")

    def __str__(self):
        """
          Proporciona una representación informal en cadena de la clase.
          Puede acceder a la representación informal de cadena de un objeto utilizando str() o print().

          Returns:
            Devuelve una cadena que representa el objeto de forma amigable.
        """
        return f"{self.marca}, {self.modelo}, {self.color}: ({self.año})"

    def __repr__(self):
        """
          Proporciona una representación de cadena dirigida principalmente a los programadores de Python,
          devuelve una cadena que permite volver a crear el objeto si es posible.
          Puede acceder a la representación formal de cadena de un objeto utilizando la función incorporada repr().

        Returns:
          Devuelve lo que se conoce como la representación formal en cadena de un objeto.
        """
        return (
            f"{type(self).__name__}"
            f'(make="{self.marca}", '
            f'model="{self.modelo}", '
            f"year={self.año}, "
            f'color="{self.color}")'
        )

    def __iter__(self):
        yield from (self.marca, self.modelo, self.año, self.color)


"""lo q imprime

ford_mustang = Auto("Ford", "Mustang", 2022, "Negro")

print(ford_mustang)
str(ford_mustang)

Ford, Mustang, Negro: (2022)
'Ford, Mustang, Negro: (2022)'  str rapidamente permite copiar el contenido..

"""

"""
repr(ford_mustang)

'Auto(make="Ford", model="Mustang", year=2022, color="Negro")' sirve como lista , no puede servir mm...

"""


"""________________________________________________________________________________________________"""

"""metodos de clases"""

class Auto:
    ruedas = 4

    def __init__(self, marca, modelo, año, color, aceleracion=10):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.aceleracion = aceleracion
        self.encendido = False
        self.velocidad = 0
        self.max_velocidad = 200

    @classmethod
    def from_sequence(cls, sequence):
        return cls(*sequence)

    @staticmethod
    def mostrar_mensaje(usuario):
        print(f"Hola {usuario}! Este es tu auto")

ford_mustang = Auto.from_sequence(("Ford", "Mustang", 2022, "Negro"))

print(ford_mustang.__dict__)

Auto.mostrar_mensaje("Pepe")
ford_mustang.mostrar_mensaje("Pepe")


"""
Los métodos estáticos no toman la instancia o la clase como argumento.
Por lo tanto, son funciones regulares definidas dentro de una clase. También se podrían definir fuera de la clase como una función independiente.
Para definir un método estático en una clase se usa el decorador @staticmethod.
Los métodos estáticos no operan sobre la instancia o la clase. Funcionan como funciones independientes encerradas en una clase.
Se definirá un método estático en lugar de una función normal fuera de la clase cuando esa función esté estrechamente relacionada con la clase y se desee agrupar por comodidad o por coherencia con la API de tu código, pero no afecten necesariamente a la clase o a sus instancias.

"""


