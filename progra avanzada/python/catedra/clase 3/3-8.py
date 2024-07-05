# Herencia múltiple
class Persona:
  def __init__(self, nombre, apellido, edad, sexo):
    print("Inicializando Persona")
    self.nombre = nombre
    self.apellido = apellido
    self.sexo = sexo
    self.edad = edad

class Empleado(Persona):
  def __init__(self, nombre, apellido, edad, sexo, salario):
    print("Inicializando Empleado")
    super().__init__(nombre, apellido, edad, sexo)
    self.salario = salario

class InteligenciaArtificial(Persona):
  def __init__(self, nombre, apellido, edad, sexo):
    print("Inicializando IA")
    super().__init__(nombre, apellido, edad=None, sexo=None)
    self.is_a_bot = True

class EmpleadoAI(Empleado, InteligenciaArtificial):
  def __init__(self, nombre, apellido, edad, sexo, salario, nombre_inteligencia_artificial):
    super().__init__(nombre, apellido, edad, sexo, salario)
    #InteligenciaArtificial.__init__(self, nombre_inteligencia_artificial, apellido, edad, sexo)


e = EmpleadoAI("Siri", "Microsoft", edad=100, sexo="Femenino", salario=2000, nombre_inteligencia_artificial="Cortana")
print(vars(e))
print(EmpleadoAI.__mro__)



"""______________________________________________________________________________________________________"""

class Figura:
  def __init__(self, color):
    self.color = color

  def area(self):
    raise NotImplementedError

class Circulo(Figura):
  def __init__(self, color, radio):
    Figura.__init__(self, color)
    self.radio = radio

  def area(self):
    return 3.1415 * self.radio ** 2

class Rectangulo(Figura):
  def __init__(self, color, base, altura):
    super().__init__(color)
    self.base = base
    self.altura = altura

  def area(self):
    return self.base * self.altura

class CirculoRectangulo(Circulo, Rectangulo):
  def __init__(self, color, radio, base, altura):
    Circulo.__init__(self, color, radio)  # Inicializar directamente Círculo
    Rectangulo.__init__(self, color, base, altura)  # Inicializar directamente Rectángulo

  #def area(self):
  #  return Circulo.area(self) + Rectangulo.area(self)

# Crear una instancia de CirculoRectangulo
figura = CirculoRectangulo("rojo", 3, 5, 7)

# Calcular y mostrar el área
# El método área es ambiguo ya que está definido en ambas clases padre.
# Tenemos que especificar qué método de área queremos utilizar
print(f"El área del circulo es: {figura.area()}") # Esto utilizará Circulo.area() por defecto debido al MRO
print(f"El área del rectángulo es: {Rectangulo.area(figura)}") # Necesitamos llamar explícitamente a Rectangulo.area()

