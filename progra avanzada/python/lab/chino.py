class Pallet:
    def __init__(self, id_pallet, peso_caja, peso_maximo=400):
        self.id_pallet = id_pallet
        self.peso_caja = peso_caja
        self.peso_maximo = peso_maximo
        self.cantidad_cajas = 0
        self.ubicacion = "00"

    def agregar_cajas(self, cantidad):
        if (self.cantidad_cajas + cantidad) * self.peso_caja > self.peso_maximo:
            print(f"No se pueden agregar {cantidad} cajas. El peso excede los {self.peso_maximo} Kg.")
        else:
            self.cantidad_cajas += cantidad
            print(f"Se han agregado {cantidad} cajas al Pallet {self.id_pallet}.")

    def retirar_cajas(self, cantidad):
        if cantidad > self.cantidad_cajas:
            print(f"No se pueden retirar {cantidad} cajas. Solo hay {self.cantidad_cajas} cajas en el Pallet {self.id_pallet}.")
        else:
            self.cantidad_cajas -= cantidad
            print(f"Se han retirado {cantidad} cajas del Pallet {self.id_pallet}.")
            if self.cantidad_cajas == 0:
                print(f"El Pallet {self.id_pallet} se ha eliminado porque no tiene cajas.")
                return True
        return False

    def mover_pallet(self, nueva_ubicacion):
        self.ubicacion = nueva_ubicacion
        print(f"El Pallet {self.id_pallet} se ha movido a la ubicación {self.ubicacion}.")

    def obtener_informacion(self):
        return {
            "ID": self.id_pallet,
            "Cantidad de cajas": self.cantidad_cajas,
            "Kilos": self.cantidad_cajas * self.peso_caja,
            "Ubicación": self.ubicacion
        }


class PalletA(Pallet):
    def __init__(self, id_pallet):
        super().__init__(id_pallet, peso_caja=5)
##<<<<<<< HEAD

##=======
##>>>>>>> 68d73688e67c6ba6676b828c29364ab14f99dbba


class PalletB(Pallet):
    def __init__(self, id_pallet):
        super().__init__(id_pallet, peso_caja=10)


class PalletC(Pallet):
    def __init__(self, id_pallet):
        super().__init__(id_pallet, peso_caja=20)


class Bodega:
    def __init__(self):
        self.pallets = []
        self.ubicaciones = {"00": []}

    def crear_pallet(self, tipo_pallet, id_pallet):
        if tipo_pallet == "A":
            nuevo_pallet = PalletA(id_pallet)
        elif tipo_pallet == "B":
            nuevo_pallet = PalletB(id_pallet)
        elif tipo_pallet == "C":
            nuevo_pallet = PalletC(id_pallet)
        else:
            print("Tipo de Pallet no válido.")
            return

        self.pallets.append(nuevo_pallet)
        self.ubicaciones["00"].append(nuevo_pallet)
        print(f"Pallet {id_pallet} de tipo {tipo_pallet} creado en la posición 00.")

    def agregar_cajas_a_pallet(self, id_pallet, cantidad):
        pallet = self.encontrar_pallet(id_pallet)
        if pallet:
            pallet.agregar_cajas(cantidad)

    def retirar_cajas_de_pallet(self, id_pallet, cantidad):
        pallet = self.encontrar_pallet(id_pallet)
        if pallet:
            if pallet.retirar_cajas(cantidad):
                self.pallets.remove(pallet)
                self.ubicaciones[pallet.ubicacion].remove(pallet)

    def mover_pallet(self, id_pallet, nueva_ubicacion):
        if nueva_ubicacion not in self.ubicaciones:
            self.ubicaciones[nueva_ubicacion] = []
        if len(self.ubicaciones[nueva_ubicacion]) > 0:
            print(f"La ubicación {nueva_ubicacion} ya está ocupada.")
        else:
            pallet = self.encontrar_pallet(id_pallet)
            if pallet:
                self.ubicaciones[pallet.ubicacion].remove(pallet)
                pallet.mover_pallet(nueva_ubicacion)
                self.ubicaciones[nueva_ubicacion].append(pallet)

    def encontrar_pallet(self, id_pallet):
        for pallet in self.pallets:
            if pallet.id_pallet == id_pallet:
                return pallet
        print(f"Pallet con ID {id_pallet} no encontrado.")
        return None

    def listar_pallets(self):
        for pallet in self.pallets:
            print(pallet.obtener_informacion())

    def obtener_informacion_pallet(self, id_pallet):
        pallet = self.encontrar_pallet(id_pallet)
        if pallet:
            print(pallet.obtener_informacion())


# Ejemplo de uso
bodega = Bodega()
bodega.crear_pallet("A", "A001")
bodega.agregar_cajas_a_pallet("A001", 50)
bodega.mover_pallet("A001", "AA")
bodega.obtener_informacion_pallet("A001")
bodega.listar_pallets()
bodega.retirar_cajas_de_pallet("A001", 50)
bodega.listar_pallets()