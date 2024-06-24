

"""relacion entre clases y objetos """

"""
asociacion (conexion entre clases)
dependencia (realcion de uso)
generalizacion/ especializacion( herencia)

"""

# Relacion de asociación entre clases mediante clase asociativa
class Cliente:
  def __init__(self, nombreCompleto, rut, direccion, clienteVIP):
    self.nombreCompleto = nombreCompleto
    self.rut = rut
    self.direccion = direccion
    self.clienteVIP = clienteVIP

class Libro:
  def __init__(self, idLibro, titulo, autor, precioBase, cantidadStock, numeroPaginas, bestSeller):
    self.idLibro = idLibro
    self.titulo = titulo
    self.autor = autor
    self.precioBase = precioBase
    self.cantidadStock = cantidadStock
    self.numeroPaginas = numeroPaginas
    self.bestSeller = bestSeller

class OrdenVenta:
  def __init__(self, rutCliente, idLibro, cantidad):
    self.rutCliente = rutCliente # referencia a instancia de Cliente mediante rutCliente
    self.idLibros = [idLibro] # referencia a instancia de Libro mediante idLibro
    self.cantidadLibros = [cantidad]

  def __str__(self):
    return f"Cliente: {self.rutCliente}, Libro: {self.idLibros}, Cantidad: {self.cantidadLibros}"

  def __del__(self):
    print("Orden de venta eliminada")

  def adicionarLibro(self, idLibro, cantidad):
    self.idLibros.append(idLibro)
    self.cantidadLibros.append(cantidad)



cliente_1 = Cliente("Pedro Perez", "12345678-9", "Calle 123", True)
cliente_2 = Cliente("Maria Rodriguez", "98765432-1", "Avenida 456", False)

libro_1 = Libro(1, "Libro 1", "Autor 1", 10.0, 10, 300, False)
libro_2 = Libro(2, "Libro 2", "Autor 2", 15.0, 5, 400, True)

orden_venta_1 = OrdenVenta("12345678-9", 1, 2)
orden_venta_1.adicionarLibro(2, 3)

orden_venta_2 = OrdenVenta("98765432-1", 2, 1)

print(orden_venta_1)
print(orden_venta_2)

del orden_venta_1 # Elimina la instancia de OrdenVenta
print(cliente_1) # No se eliminan las instancias referenciadas en orden_venta_1