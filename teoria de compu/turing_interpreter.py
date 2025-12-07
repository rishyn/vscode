# Archivo: turing_interpreter.py

# =================================================================
# INTERPRETE DE UNA MÁQUINA DE TURING (MT)
# Teoría de la Computación - Evaluación Final
# =================================================================

class TuringMachine:
    """
    Representa la definición estática de una Máquina de Turing:
    (S, Sigma, Gamma, delta, s0, SF).
    """
    def __init__(self, n_estados, n_simbolos, alfabeto, transiciones):
        # n: número de estados (sin incluir el estado de parada -1) [cite: 8]
        self.n_estados = n_estados
        # m: número de símbolos del alfabeto [cite: 8]
        self.n_simbolos = n_simbolos
        # Gamma: Alfabeto de la máquina. El primero es el símbolo blanco. [cite: 8]
        self.alfabeto = alfabeto 
        
        # Diccionario para almacenar la función de transición delta
        # Clave: (estado_actual, símbolo_leído)
        # Valor: (símbolo_a_escribir, movimiento, nuevo_estado) [cite: 8]
        self.delta = {}
        self._cargar_transiciones(transiciones)
        
    def _cargar_transiciones(self, transiciones):
        """
        Carga la función de transición a partir de una lista de tuplas 
        (s, x, y, m, t) [cite: 8].
        """
        # La tupla es (estado_actual, símbolo_leído, símbolo_a_escribir, movimiento, nuevo_estado)
        for s, x, y, m, t in transiciones:
            # Asegura que para cada estado s y cada símbolo x habrá una tupla. [cite: 8]
            self.delta[(s, x)] = (y, m, t)

    def obtener_transicion(self, estado, simbolo):
        """
        Busca y retorna la tupla de acción (y, m, t) para un par (estado, símbolo).
        """
        return self.delta.get((estado, simbolo), None)

    def __str__(self):
        """
        Genera una representación formateada de la MT.
        """
        output = f"Estados: {self.n_estados}\n"
        output += f"Símbolos ({self.n_simbolos}): {' '.join(self.alfabeto)}\n"
        output += "Función de transición:\n"
        
        # Generar el encabezado de la tabla
        header = f"{' ':<5}|"
        for sim in self.alfabeto:
            header += f"{sim:^15}|"
        output += "-" * (len(header) + 1) + "\n"
        output += header + "\n"
        output += "-" * (len(header) + 1) + "\n"
        
        # Generar las filas de la tabla (solo estados de 0 a n-1)
        for s in range(self.n_estados):
            row = f"{s:<5}|"
            for x in self.alfabeto:
                try:
                    y, m, t = self.delta[(s, x)]
                    transition_str = f"{y} {m} {t}"
                except KeyError:
                    transition_str = "---" 
                row += f"{transition_str:^15}|"
            output += row + "\n"
        
        return output

class TapeSimulator:
    """
    Simula la ejecución de una Máquina de Turing sobre una cinta.
    """
    def __init__(self, mt, cadena_inicial):
        self.mt = mt
        self.simbolo_blanco = mt.alfabeto[0] # El primer símbolo es el blanco [cite: 8]
        self.cinta = list(cadena_inicial)
        self.estado_actual = 0  # El estado inicial es 0 [cite: 8]
        self.posicion_cabezal = 0 # Inicialmente en el primer símbolo de la cadena
        self.pasos = 0
        self.aceptada = False
        
        # Pre-expandir la cinta para simular infinitud y manejar los movimientos iniciales
        self._expandir_cinta_inicial()

    def _expandir_cinta_inicial(self):
        """
        Agrega un símbolo blanco al inicio y al final de la cadena de entrada.
        Esto es una convención para el manejo de la cinta.
        """
        self.cinta.insert(0, self.simbolo_blanco)
        self.cinta.append(self.simbolo_blanco)
        self.posicion_cabezal += 1 # El cabezal se ajusta a la nueva posición 1

    def _expandir_cinta(self):
        """
        Expande la cinta si el cabezal se mueve fuera de los límites actuales.
        """
        if self.posicion_cabezal < 0:
            # Si se mueve a la izquierda del inicio, agrega un blanco
            self.cinta.insert(0, self.simbolo_blanco)
            self.posicion_cabezal = 0 # El cabezal está en la nueva posición 0
        elif self.posicion_cabezal >= len(self.cinta):
            # Si se mueve a la derecha del final, agrega un blanco
            self.cinta.append(self.simbolo_blanco)
        
    def _mover_cabezal(self, movimiento):
        """
        Ajusta la posición del cabezal según el movimiento ('i', 'd', 'q'). [cite: 8]
        """
        if movimiento == 'i':  # Mover a la izquierda
            self.posicion_cabezal -= 1
        elif movimiento == 'd':  # Mover a la derecha
            self.posicion_cabezal += 1
        # 'q' no mueve el cabezal

    def imprimir_cinta(self, encabezado):
        """
        Imprime el contenido de la cinta y la posición del cabezal.
        """
        print(encabezado) # Imprimir el encabezado (e.g., "Cinta antes..." o "La cinta queda:") 
        
        # Imprimir la cinta con formato |símbolo|símbolo|...
        cinta_str = "|".join(self.cinta)
        print(f"|{cinta_str}|")
        
        # Calcular la posición del marcador ^
        # Posición de ^ = (índice del cabezal * 2) + 1 (por el '|' inicial)
        pos_cabezal_display = (self.posicion_cabezal * 2) + 1 
        
        # Imprimir el marcador del cabezal
        cabezal_line = " " * pos_cabezal_display + "^"
        print(cabezal_line)
        
    def simular(self):
        """
        Ejecuta la MT paso a paso hasta alcanzar el estado de parada (-1).
        """
        MAX_PASOS = 10000 # Límite para evitar bucles infinitos no deseados

        # Imprimir cinta antes de la ejecución 
        self.imprimir_cinta("Cinta de entrada para el caso:") 

        while self.estado_actual != -1 and self.pasos < MAX_PASOS: 
            self.pasos += 1
            
            # 1. Asegurar la expansión de la cinta
            self._expandir_cinta() 
            
            # 2. Leer el símbolo
            simbolo_leido = self.cinta[self.posicion_cabezal]

            # 3. Obtener la transición delta(s, x) = (y, m, t)
            transicion = self.mt.obtener_transicion(self.estado_actual, simbolo_leido)

            if transicion is None:
                # Caso de terminación implícita por MT mal definida (no debe pasar según las reglas [cite: 8])
                print(f"La simulación se detiene: Transición no definida para el estado {self.estado_actual} y el símbolo '{simbolo_leido}'.")
                break 

            simbolo_a_escribir, movimiento, nuevo_estado = transicion
            
            # 4. Escribir el nuevo símbolo [cite: 8]
            self.cinta[self.posicion_cabezal] = simbolo_a_escribir
            
            # 5. Mover el cabezal [cite: 8]
            self._mover_cabezal(movimiento)
            
            # 6. Cambiar de estado [cite: 8]
            self.estado_actual = nuevo_estado
            
        # Imprimir cinta luego de la ejecución 
        self.imprimir_cinta("\nLa cinta queda:")

        # Imprimir mensaje de aceptación 
        if self.estado_actual == -1:
            self.aceptada = True 
            print("La cadena es aceptada.") 
        else:
            self.aceptada = False
            print("La cadena no es aceptada (Posiblemente superó el límite de pasos).")
            
        return self.aceptada


def leer_entrada_y_simular():
    """
    Función principal que lee la especificación de la MT, el número de casos 
    y ejecuta el simulador para cada cadena.
    """
    print("\n>>> Intérprete de Máquina de Turing <<<")
    try:
        # --- LECTURA DE LA ESPECIFICACIÓN DE LA MT ---
        
        # 1. n (estados) y m (símbolos)
        # Ejemplo: 4 3 
        linea_nm = input("Ingrese n (estados sin parada) y m (símbolos): ").split()
        if not linea_nm:
             return
        n, m = map(int, linea_nm)
        
        # 2. Alfabeto Gamma
        # Ejemplo: - a b 
        alfabeto = input(f"Ingrese los {m} símbolos del alfabeto (separados por espacio): ").split()
        if len(alfabeto) != m:
            print(f"Error: Se esperaban {m} símbolos pero se leyeron {len(alfabeto)}. Terminando.")
            return

        # 3. n*m tuplas de transición
        transiciones = []
        n_transiciones_esperadas = n * m
        print(f"Ingrese las {n_transiciones_esperadas} tuplas de transición (s, x, y, m, t) [Enter después de cada tupla]:")
        
        for _ in range(n_transiciones_esperadas):
            linea = input().split()
            if len(linea) != 5:
                print(f"Advertencia: Tupla incorrecta. Se esperaban 5 elementos, se encontraron {len(linea)}. Terminando.")
                return
            
            s = int(linea[0])
            x = linea[1] 
            y = linea[2] 
            m_mov = linea[3] 
            t = int(linea[4]) 
            transiciones.append((s, x, y, m_mov, t))
            
        # --- CREACIÓN E IMPRESIÓN DE LA MT ---
        mt = TuringMachine(n, m, alfabeto, transiciones)
        
        print("\n" + "="*40)
        print("INFORMACIÓN DE LA MÁQUINA DE TURING")
        print("="*40)
        print(mt) 
        print("="*40 + "\n")

        # --- LECTURA DE CASOS Y SIMULACIÓN ---
        
        # 4. Número de casos de prueba
        # Ejemplo: 2 
        n_casos_str = input("Ingrese el número de cadenas de prueba: ")
        n_casos = int(n_casos_str)
        print(f"Iniciando simulación para {n_casos} casos de prueba...")

        # 5. Simulación para cada cadena de prueba
        for i in range(n_casos):
            cadena = input(f"Ingrese la cadena {i+1} de prueba: ")
            print(f"\n=========================================")
            print(f"CASO DE ENTRADA {i+1}: {cadena}")
            print(f"=========================================")
            
            # Inicializar y simular
            simulador = TapeSimulator(mt, cadena)
            simulador.simular()

    except EOFError:
        print("\nFin de la entrada de datos (EOF).")
    except ValueError as e:
        print(f"\nError de formato de entrada (asegúrese de usar enteros y símbolos correctos): {e}")
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")

# --- Ejecución del programa ---
if __name__ == "__main__":
    leer_entrada_y_simular()