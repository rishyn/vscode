import random

class MascotaVirtual:
    def __init__(self, nombre):
        self.nombre = nombre
        self.salud = 100
        self.felicidad = 100
        self.hambre = 0
        self.sueno = 0
    
    def alimentar(self):
        self.hambre -= 10
        self.felicidad += 5
    
    def jugar(self):
        self.felicidad += 10
        self.hambre += 5
    
    def dormir(self):
        self.sueno -= 10
        self.salud += 10
    
    def estado(self):
        print("Nombre:", self.nombre)
        print("Salud:", self.salud)
        print("Felicidad:", self.felicidad)
        print("Hambre:", self.hambre)
        print("Sueño:", self.sueno)
    
    def ciclo_de_vida(self):
        self.salud -= random.randint(0, 5)
        self.felicidad -= random.randint(0, 5)
        self.hambre += random.randint(0, 5)
        self.sueno += random.randint(0, 5)

# Ejemplo de uso
mascota = MascotaVirtual("Fluffy")

while True:
    comando = input("¿Qué deseas hacer? (alimentar/jugar/dormir/estado/salir) ")
    
    if comando == "alimentar":
        mascota.alimentar()
    elif comando == "jugar":
        mascota.jugar()
    elif comando == "dormir":
        mascota.dormir()
    elif comando == "estado":
        mascota.estado()
    elif comando == "salir":
        break
    
    mascota.ciclo_de_vida()
    
    if mascota.salud <= 0 or mascota.felicidad <= 0 or mascota.hambre >= 100 or mascota.sueno >= 100:
        print("Lo siento, tu mascota ha fallecido.")
        break