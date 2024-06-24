"""relacion de herencia entre clases"""


# Relación de herencia entre clases
class Vehicle:
    """
      Clase base para vehículos, con atributos y métodos que son comunes a todo tipo de vehículos.
      La clase Vehicle proporciona una interfaz común para otros vehículos (subclases).
    """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._started = False

    def start(self):
        print("(Vehicle): Starting engine...")
        self._started = True

    def stop(self):
        print("(Vehicle): Stopping engine...")
        self._started = False


class Car(Vehicle):
    """
        Clase Car que hereda de la clase Vehicle.
        La clase Car agrega atributos y métodos específicos para carros.
    """
    def __init__(self, make, model, year, num_seats):
        super().__init__(make, model, year) # Llamada al constructor de la superclase, referencia al padre mas cercano
        self.num_seats = num_seats # Se definen los atributos especificos de la subclase

    def drive(self):
        print(f'(Car): Driving my "{self.make} - {self.model}" on the road')

    def __str__(self):
        return f'"{self.make} - {self.model}" has {self.num_seats} seats'

class Motorcycle(Vehicle):
    """
        Clase Motorcycle que hereda de la clase Vehicle.
        La clase Motorcycle agrega atributos y métodos específicos para motos.
    """
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self.num_wheels = num_wheels

    def ride(self):
        print(f'(Motor): Riding my "{self.make} - {self.model}" on the road')

    def __str__(self):
        return f'"{self.make} - {self.model}" has {self.num_wheels} wheels'



tesla = Car("Tesla", "Model S", 2022, 5)
tesla.start()
tesla.drive()
tesla.stop()
print(tesla)

harley = Motorcycle("Harley-Davidson", "Iron 883", 2021, 2)
harley.start()
harley.ride()
harley.stop()
print(harley)




print(type(tesla))
print(type(harley))

print(isinstance(tesla, Car))
print(isinstance(harley, Motorcycle))
print(isinstance(harley, Vehicle))

print(issubclass(Car, Vehicle))
print(issubclass(Motorcycle, Vehicle))

print(issubclass(Vehicle, object))
print(issubclass(Car, object))

help(object)