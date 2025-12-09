# turing_simple.py
# Un intérprete básico de Máquina de Turing para la evaluación final
# (mucho más corto y legible que el original)

class MaquinaTuring:
    def __init__(self, estados, simbolos, alfabeto, transiciones):
        self.estados = estados
        self.alfabeto = alfabeto                # el primero es el blanco
        self.blanco = alfabeto[0]
        self.delta = {}                          # (estado, simbolo) -> (escribir, mover, nuevo_estado)

        for s, lee, escribe, mueve, nuevo in transiciones:
            self.delta[(s, lee)] = (escribe, mueve, nuevo)

    def __str__(self):
        print(f"Estados: 0..{self.estados-1}")
        print(f"Alfabeto: {' '.join(self.alfabeto)}")
        print("\nTransiciones:")
        print("estado |", "  ".join(f"{s:>3}" for s in self.alfabeto))
        print("-" * 40)
        for q in range(self.estados):
            fila = f"{q:>6} |"
            for s in self.alfabeto:
                if (q, s) in self.delta:
                    e, m, sig = self.delta[(q, s)]
                    fila += f" {e} {m} {sig} "
                else:
                    fila += "  ---  "
                fila += "|"
            print(fila)
        return ""

class Cinta:
    def __init__(self, mt, entrada):
        self.mt = mt
        self.cinta = ['_', entrada, '_']        # _ es el blanco
        self.cinta = [c for c in ''.join(self.cinta)]  # aplana la lista
        self.cabezal = 1                        # empieza sobre el primer símbolo real
        self.estado = 0

    def mostrar(self, titulo=""):
        if titulo:
            print(titulo)
        print("|" + "|".join(self.cinta) + "|")
        print(" " * (self.cabezal * 2 + 1) + "^")
        print()

    def paso(self):
        if self.estado == -1:
            return False

        simbolo = self.cinta[self.cabezal]
        if (self.estado, simbolo) not in self.mt.delta:
            print("No hay transición definida → se detiene")
            self.estado = -1
            return False

        escribe, mueve, siguiente = self.mt.delta[(self.estado, simbolo)]

        # ejecutar la transición
        self.cinta[self.cabezal] = escribe

        if mueve == 'd':
            self.cabezal += 1
        elif mueve == 'i':
            self.cabezal -= 1
        # 'q' = quieto, no hace nada

        # expandir cinta si hace falta
        if self.cabezal < 0:
            self.cinta.insert(0, self.mt.blanco)
            self.cabezal = 0
        elif self.cabezal >= len(self.cinta):
            self.cinta.append(self.mt.blanco)

        self.estado = siguiente
        return True

    def ejecutar(self):
        self.mostrar("Cinta inicial:")
        pasos = 0
        while self.paso() and pasos < 10000:
            pasos += 1

        self.mostrar("Cinta final:")
        if self.estado == -1:
            print("→ Cadena ACEPTADA")
        else:
            print("→ Cadena RECHAZADA (o bucle)")

# ==================== PROGRAMA PRINCIPAL ====================

print("=== Intérprete simple de Máquina de Turing ===\n")

# 1. n y m
n, m = map(int, input("n (estados) y m (símbolos): ").split())

# 2. alfabeto
alfabeto = input(f"{m} símbolos del alfabeto (separados por espacio): ").split()

# 3. transiciones
print(f"\nIngresa las {n*m} transiciones (s lee escribe mueve nuevo):")
trans = []
for _ in range(n * m):
    linea = input().split()
    s = int(linea[0])
    lee, escribe, mueve, nuevo = linea[1], linea[2], linea[3], int(linea[4])
    trans.append((s, lee, escribe, mueve, nuevo))

# crear máquina
mt = MaquinaTuring(n, m, alfabeto, trans)
print(mt)

# casos de prueba
casos = int(input("\n¿Cuántas cadenas quieres probar? "))
for i in range(casos):
    cadena = input(f"\nCadena {i+1}: ")
    print(f"\n--- Caso {i+1} ---")
    cinta = Cinta(mt, cadena)
    cinta.ejecutar()
    print("-" * 50)