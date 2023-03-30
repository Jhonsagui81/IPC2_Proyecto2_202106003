from TDA.Nodo import NodoElementos

class ListaElementos:
    def __init__(self):
        self.Inicio = None
        self.Final = None 
        self.Limite = 0
    
    def IncertarElemento(self, numero_atomico, simbolo, nombre):
        NuevoNodo = NodoElementos(numero_atomico,simbolo,nombre,)
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
            print("Elemento asignador exitoso ")
            self.Limite += 1
        else:
            Actual = self.Inicio
            bandera = False
            while Actual != None:
                if NuevoNodo.ObtenerNombre().lower() == Actual.ObtenerNombre().lower() or NuevoNodo.Obtner_Atomico() == Actual.Obtner_Atomico() or NuevoNodo.ObtenerSimbolo()  == Actual.ObtenerSimbolo():
                    print("EL elemento esta repetido")
                    bandera = True
                    Actual = Actual.Siguiente
                else:
                    Actual = Actual.Siguiente
            if bandera == False:
                self.Limite += 1
                self.Final.AsignarSiguiente(NuevoNodo)
                self.Final = NuevoNodo
                print("Elemento aisgnado exitodo else")

    def Existe(self, elemento):
        Aux = self.Inicio
        while Aux != None:
            if Aux.ObtenerSimbolo() == elemento:
                return True
            else:
                Aux = Aux.Siguiente
        return False