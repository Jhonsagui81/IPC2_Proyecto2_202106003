from TDA.Nodo import *

class trabajo:
    def __init__(self):
        self.Inicio = None
        self.Final = None

    def Insertar(self, id, lista_elementos):
        NuevoNodo = NodoTrabajo(id,lista_elementos)
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
            print("se almaceno pin 1  if")
        else:
            self.Final.AsignarSiguiente(NuevoNodo)
            self.Final = NuevoNodo
            print("se almaceno pin 2  else")