from TDA.Nodo import *

class ListaMaquinas:
    def __init__(self):
        self.Inicio = None
        self.Final = None 
        self.Limite = 0
    
    def InsertarMaquina(self, nombre, no_pines, no_elementos, lista_pines):
        if lista_pines.validacionElementes():
            NuevoNodo = NodoMaquinas(self.Limite, nombre, no_pines, no_elementos, lista_pines)
            if self.Inicio == None:
                self.Inicio = NuevoNodo
                self.Final = NuevoNodo
                self.Limite += 1
                print("Se guardo Maquina en if")
            else:
                self.Limite += 1
                self.Final.AsignarSiguiente(NuevoNodo)
                self.Final = NuevoNodo
                print("Se guardo maquina en else")
        else:
            print("maquina con problema, NO SE GUARDA")