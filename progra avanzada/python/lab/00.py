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
    def __init__(self, id_pallet ):
        super().__init__(id_pallet, peso_caja=5)



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
            print("pallet A")
            nuevo_pallet = PalletA(id_pallet)
        elif tipo_pallet == "B":
            print("pallet B")
            nuevo_pallet = PalletB(id_pallet)
        elif tipo_pallet == "C":
            print("pallet C")
            nuevo_pallet = PalletC(id_pallet)
        else:
            print("Tipo de Pallet no válido.")
            return
        self.pallets.append(nuevo_pallet)
        self.ubicaciones["00"].append(nuevo_pallet)



bodega = Bodega()
bodega.crear_pallet("A", "A001")
bodega.crear_pallet("B", "B003")
bodega.crear_pallet("C", "C004")
bodega.crear_pallet("D", "D009")
