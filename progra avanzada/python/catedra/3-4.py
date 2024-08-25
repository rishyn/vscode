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


class Nave:
    """Clase que define el comportamiento de una nave."""
    def __init__(self, cant_tripulantes, tipo_equipo: TipoEquipo):
        self._cant_tripulantes = cant_tripulantes
        self._tipo_equipo = tipo_equipo # Tipo de equipo de la nave (Marciano o Terricola), se usa Enum por simplicidad
        self._destruida = False
        self._tripulacion = self._inicializa_tripulacion()

    @property
    def tipo_equipo(self):
        """Devuelve el tipo de equipo de la nave."""
        return self._tipo_equipo

    @property
    def esta_destruida(self):
        """Devuelve si la nave está destruida."""
        return self._destruida

    @property
    def tripulantes_vivos(self):
        """Devuelve la cantidad de tripulantes vivos que quedan."""
        t_vivos = 0
        for t in self._tripulacion:
            if t.esta_vivo:
                t_vivos += 1

        return t_vivos

    def _inicializa_tripulacion(self):
        """
            Inicializa la tripulación de la nave en función del tipo de equipo y la cantidad de tripulantes.

            Returns:
                Lista de tripulantes.
        """
        if self._tipo_equipo == TipoEquipo.Marciano:
            return [Marciano(random.randint(7,10)) for _ in range(self._cant_tripulantes)]  # Para una ejecucion mas realista los marcianos se crean con una resistencia variada
        else:
            return [Terricola(random.randint(3,5)) for _ in range(self._cant_tripulantes)]  # Para una ejecucion mas realista los terricolas se crean con una salud variada

    def recibir_disparo(self, disparo: int): # De esta clase solo se debía definir este método
        """
            Recibe un disparo, notifica a todos sus tripulantes y actualiza el estado de la nave.

            Args:
                disparo: Número del disparo recibido.
        """
        flag_vivo = False
        for t in self._tripulacion:
            if t.esta_vivo:
                t.recibir_disparo(disparo)

            if t.esta_vivo:
                flag_vivo = True

        if not flag_vivo:
            print(f"Nave del equipo {self._tipo_equipo.value} destruida")
            self._destruida = True
        else:
            print(f"Quedan {self.tripulantes_vivos} en la nave")

    def disparar(self):
        """Realiza un disparo generando un aleatorio entre 0 y 9."""
        return random.randint(0,9)