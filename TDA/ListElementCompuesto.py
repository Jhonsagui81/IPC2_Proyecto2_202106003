from TDA.Nodo import NodoListaElemtCompuesto

class ListaElemtosCompuestos:
    def __init__(self):
        self.Inicio = None
        self.Final = None 
        self.Limite = 0
    
    def Insertar(self, simbolo, lista_elementos_base):
        if lista_elementos_base.Existe(simbolo):
            NuevoNodo = NodoListaElemtCompuesto(simbolo)
            if self.Inicio == None:
                self.Inicio = NuevoNodo
                self.Final = NuevoNodo
                self.Limite += 1
                print("se asigno elemento. if")
            else:
                self.Final.AsignarSiguiente(NuevoNodo)
                self.FInal = NuevoNodo
                self.Limite += 1
                print("se asigno elemento. else")
        else:
            print("Elemento no existe en lista original")
        # NuevoNodo = NodoListaElemtCompuesto(simbolo)