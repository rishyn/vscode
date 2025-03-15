"""relacion de agregacion entre clases"""


# Relacion de agregación entre clases
class Estudiante:
    def __init__(self, nombre, rut, carrera):
        self.nombre = nombre
        self.rut = rut
        self.carrera = carrera
        self.cursos = [] # lista para almacenar referencias a instancias de Curso
        self.notas = []

    def inscribir_curso(self, curso):
        """
          Inscribe el curso en el estudiante

          Args:
            curso: instancia de Curso
        """
        self.cursos.append(curso)
        self.notas.append(1)

    def agregar_nota(self, idx, nota):
        if idx < len(self.cursos):
            self.notas[idx] = nota

    def obtener_nota(self, idx):
        if idx < len(self.cursos):
            return self.notas[idx]
        else:
            return None

    def promedio(self):
        return sum(self.notas) / len(self.notas)

    def __del__(self):
        print("Estudiante eliminado")

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre





curso_1 = Curso("Python programming")
curso_2 = Curso("Data Science")

estudiante_1 = Estudiante("Juan", "12345678-9", "Informatica")
estudiante_2 = Estudiante("Maria", "98765432-1", "Industrial")

estudiante_1.inscribir_curso(curso_1)
estudiante_1.inscribir_curso(curso_2)

estudiante_1.agregar_nota(0, 90)
estudiante_1.agregar_nota(1, 85)

for curso in estudiante_1.cursos:
    print(f"Curso: {curso.nombre}, Nota: {estudiante_1.obtener_nota(estudiante_1.cursos.index(curso))}")

print(f"Promedio: {estudiante_1.promedio()}")

del estudiante_1 # Elimina la instancia de Estudiante
print(curso_1) # No se eliminan las instancias referenciadas en estudiante_1