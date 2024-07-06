from abc import ABC, abstractmethod
import random
from enum import Enum

class TipoEquipo(Enum):
    Marciano = "Marciano"
    Terricola = "Terricola"

class Guerrero(ABC):
    """Clase abstracta que define el comportamiento de un guerrero."""
    def __init__(self):
        self._target = random.randint(0,9) # Inicializa un guerrero con un numero aleatorio entre 0 y 9
        self._vivo = True # cuando se crea el gerrero esta vivo

    @abstractmethod
    def recibir_disparo(self, disparo : int):
        """metodo abstracto q define el comportamiento recibir_disparo para cualquier guerrero"""
        pass

    def _comprobar_muerte(self):
        """comprueba si el guerrero a muerto"""
        if not self._vivo:
            print(f"Guerrero muerto")

    @property
    def esta_vivo(self):
        """devuelve si el guerrero esta vivo"""
        return self._vivo


class Marciano(Guerrero): # Hereda de la clase Guerrero
    """Clase que define el comportamiento de un guerrero marciano."""
    def __init__(self, disparos_morir=10):
        super().__init__() # Se debe llamar al constructor de la clase padre
        self._disparos_morir = disparos_morir # Número de disparos que debe recibir el marciano para morir. Por defecto es 10 en el argumento

    def recibir_disparo(self, disparo: int):
        """
            Recibe un disparo y actualiza el estado del marciano.

            Args:
                disparo: Número del disparo recibido.
        """
        if disparo == self._target:
            self._disparos_morir -= 1

        if self._disparos_morir <= 0:
            self._vivo = False

        self._comprobar_muerte()

    def __str__(self):
        return f"Marciano {self._vivo} con {self._disparos_morir} disparos para morir"


class Terricola(Guerrero): # Hereda de la clase Guerrero
    """Clase que define el comportamiento de un guerrero terrícola."""
    def __init__(self, salud=5):
        super().__init__() # Se debe llamar al constructor de la clase padre
        self._salud = salud # Salud del terrícola. Por defecto es 5 en el argumento

    def recibir_disparo(self, disparo: int):
        """
            Recibe un disparo y actualiza el estado del terrícola.

            Args:
                disparo: Número del disparo recibido.
        """
        if disparo == self._target+1 or disparo == self._target-1: # Condicion (+-)1 para disminuir salud. Equivalente: disparo+1 == self._target or disparo-1 == self._target:
            self._salud -= 1

        if self._salud <= 0:
            self._vivo = False

        self._comprobar_muerte()

    def __str__(self):
        return f"Terricola {self._vivo} con {self._salud} de salud"