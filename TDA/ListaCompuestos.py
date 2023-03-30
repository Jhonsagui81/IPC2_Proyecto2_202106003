from TDA.Nodo import NodoCompuestos

class ListaCompuestos:
    def __init__(self):
        self.Inicio = None
        self.Final = None 
        self.Limite = 0
    
    def Insertar(self, nombre, lista_elementos):
        NuevoNodo = NodoCompuestos(nombre, lista_elementos)
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
            self.Limite +=1
            print("ASIGNO COMPUESTO if")
        else:
            self.Final.AsignarSiguiente(NuevoNodo)
            self.Final = NuevoNodo
            self.Limite += 1
            print("ASIGNO COMPUESTO else")