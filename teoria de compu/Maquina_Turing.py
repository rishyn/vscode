'''
NOMBRE_ESTUDIANTE: RICARDO ANTONIO YAÑEZ VEGA
NOMBRE_PROFESOR: Verónica Leddermann G.
FECHA: 2025-12-09
NOMBRE_RAMO: Teoría de la Computación INF-323
Evaluacion final ,creacion de una Maquina de Turing
'''

class MaquinaTuring:
    """
    Representa la definicion de la Maquina de Turing.
    """
    def __init__(self, n, m, alfabeto, transiciones):
        self.n = n 
        self.m = m 
        self.alfabeto = alfabeto
        self.blanco = alfabeto[0] # Símbolo blanco, que es el primero
        self.delta = {} 
        
        # Carga las transiciones: (q, lee) -> (escribe, mov, sig)
        for q, lee, escribe, mov, sig in transiciones:
            self.delta[(q, lee)] = (escribe, mov, sig)

    def mostrar(self):
        """
        Imprime la definicion formal de la MT.
        """
        print(f"Estados = {self.n}")
        print(f"Simbolos ({self.m}): {' '.join(self.alfabeto)}")
        print("Funcion de transicion:")
        
        header = "    "
        for s in self.alfabeto:
            header += f"{s:>8}"
        print(header)
        print("    " + "-" * (8 * self.m))

        for q in range(self.n):
            print(f"{q:>2} |", end="")
            for s in self.alfabeto:
                if (q, s) in self.delta:
                    e, m, sig = self.delta[(q, s)]
                    print(f" {e} {m} {sig:>2} |", end="")
                else:
                    print("  - -  - |", end="")
            print()
        print()


class Cinta:
    """
    Simula la cinta y el proceso de ejecucion de la MT.
    """
    def __init__(self, mt, entrada):
        self.mt = mt
        self.celda = [self.mt.blanco] + list(entrada) + [self.mt.blanco]
        self.cabezal = 1 
        self.estado = 0   
        self.max_pasos = 10000 

    def mostrar_cinta(self, mensaje):
        """
        Imprime el contenido de la cinta y la posicion del cabezal.
        """
        print(mensaje)
        print("|" + "|".join(self.celda) + "|")
        posicion_flecha = self.cabezal * 2 + 1 
        print(" " * posicion_flecha + "^")
        print()
        
    def _esta_cinta_limpia(self):
        """
        Verifica si la cinta solo contiene el simbolo blanco ('-').
        """
        return all(simbolo == self.mt.blanco for simbolo in self.celda)

    def ejecutar(self):
        """
        Bucle principal de la simulacion de la Maquina de Turing.
        """
        self.mostrar_cinta("Cinta de entrada para el caso:")

        pasos = 0
        while self.estado != -1 and pasos < self.max_pasos:
            pasos += 1

            # 1. Expandir cinta si el cabezal se sale
            if self.cabezal < 0:
                self.celda.insert(0, self.mt.blanco)
                self.cabezal = 0
            elif self.cabezal >= len(self.celda):
                self.celda.append(self.mt.blanco)

            # 2. Leer el simbolo
            simbolo = self.celda[self.cabezal]

            # 3. Obtener la transicion
            if (self.estado, simbolo) not in self.mt.delta:
                # Si no hay transicion, forzamos la parada
                self.estado = -1
                break

            escribe, mov, nuevo_estado = self.mt.delta[(self.estado, simbolo)]

            # 4. Ejecutar la accion
            self.celda[self.cabezal] = escribe

            # 5. Mover cabezal
            if mov == 'd':
                self.cabezal += 1
            elif mov == 'i':
                self.cabezal -= 1

            # 6. Cambiar estado
            self.estado = nuevo_estado

        # Mostrar resultado final
        self.mostrar_cinta("La cinta queda:")

        # Condicion de aceptacion: Parada (-1) Y Cinta Limpia.

        es_aceptada = False
        
        if self.estado == -1:
            if self._esta_cinta_limpia():
                es_aceptada = True

        if es_aceptada:
            print("La cadena es aceptada.")
        else:
            print("La cadena no es aceptada.")
        print()


# ======================= PROGRAMA PRINCIPAL =======================
if __name__ == "__main__":
    
    print(">>> Maquina de Turing <<<")
    
    
    # 1. n m
    n, m = map(int, input("Ingrese num de estados (n) y num de símbolos (m) (separados por espacio): ").split())

    # 2. alfabeto
    alfabeto = input(f"Ingrese los {m} simbolos del alfabeto (separados por espacio): ").split()
    if len(alfabeto) != m:
        print("Error: El numero de símbolos del alfabeto no coincide con 'm'.")

    # 3. transiciones (exactamente n*m líneas)
    print(f"\nIngresa las {n*m} transiciones: ")
    transiciones_raw = []
    for _ in range(n * m):
        linea = input().split()
        if len(linea) != 5:
            print("Error de formato: Cada transición debe tener 5 elementos (s, x, y, m, t).")
        
        q = int(linea[0])
        lee = linea[1]
        escribe = linea[2]
        mov = linea[3]
        sig = int(linea[4])
        transiciones_raw.append((q, lee, escribe, mov, sig))


    transiciones_corregidas = []
    simbolo_blanco = alfabeto[0]
        
    for q, lee, escribe, mov, sig in transiciones_raw:
        if lee == simbolo_blanco and escribe != simbolo_blanco and sig == -1:
    
            print(f"[INFO] Corrigiendo transición: {q} {lee} {escribe} {mov} {sig} -> {q} {lee} {simbolo_blanco} {mov} {sig}")
            escribe = simbolo_blanco 
                
        transiciones_corregidas.append((q, lee, escribe, mov, sig))


    # Crear y mostrar la máquina
    print("\n" + "="*40)
    mt = MaquinaTuring(n, m, alfabeto, transiciones_corregidas)
    mt.mostrar()
    print("="*40)

    # 4. número de casos
    k = int(input("\n¿Cuántas cadenas quieres probar? "))

    # 5. procesar cada caso
    for i in range(k):
        cadena = input(f"\nCadena {i+1}: ").strip()
        print(f"\n--- CASO DE PRUEBA {i+1}: '{cadena}' ---")
        simulador = Cinta(mt, cadena)
        simulador.ejecutar()

