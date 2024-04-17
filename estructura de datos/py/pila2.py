
class pila:
    def __init__(self):
        #crear una pila
        self.items=[]

    def apilar(self,x):
        #agregar el elemento a la pila
        self.items.append(x)

    def desapilar(self):
        if (self.items == []):
            return print ("la lista esta vacia, no se puede desapilar")

        else:
            return self.items.pop()

    def verlista(self):
        return print(self.items)

    def es_vacia(self):
        #True si la lista esta vacia ,false si esta con contenido
        return print(self.items == [])

    def largo(self):
        return len(self.items)


    def suma(self):
        return sum(self.items)

    def media(self):
        media = sum(self.items)/len(self.items)

        return media

    def sumaAlCuadrado(self):
        suma_al_cuadrado = 0
        for item in self.items:
            suma_al_cuadrado += (item - (sum(self.items)/len(self.items)))**2
        return suma_al_cuadrado

    def varianza(self):
        if(len(self.items)< 2):
            return print ("No se puede sacar varianza ,agregar mas numeros!")
        else:
            suma_al_cuadrado = 0
            for item in self.items:
                suma_al_cuadrado += (item - (sum(self.items)/len(self.items)))**2
            varianza = suma_al_cuadrado/len(self.items)
            return varianza