from TDA.Data import *

class NodoElementos:
    def __init__(self, numero_atomico, simbolo, nombre):
        self.nuevoNodo = Elementos(numero_atomico, simbolo, nombre)
        self.Siguiente = None
    
    def AsignarSiguiente(self, Nodo):
        self.Siguiente = Nodo
    def Obtner_Atomico(self):
        return self.nuevoNodo.ObtenerAtomico()
    def ObtenerSimbolo(self):
        return self.nuevoNodo.ObtenerSimbolo()
    def ObtenerNombre(self):
        return self.nuevoNodo.ObtenerNombre()
    
class NodoMaquinas:
    def __init__(self, id, nombre, numero_pines, numero_elementos, lista_pines):
        self.Maquina = Maquina(id, nombre, numero_pines, numero_elementos, lista_pines)
        self.Siguiente = None

    def AsignarSiguiente(self, Nodo):
        self.Siguiente = Nodo

    def ObtenerId(self):
        return self.Maquina.ObtenerId()
    
    def ObtenerNombre(self):
        return self.Maquina.ObtenerNombre()
    
    def ObtenerNOPines(self):
        return self.Maquina.ObtenerNumeroPines()
    
    def ObtenerNOElementos(self):
        return self.Maquina.ObtenerNumeroElementos()
    
    def ObtenerListaPines(self):
        return self.Maquina.ObtenerListaPinas()

class NodoPinesElementos:
    def __init__(self, simbolo):
        self.PinElementos = ElementosPin(simbolo)
        self.Siguiente = None
        self.Anterior = None
    
    def AsignarSiguiente(self, Nodo):
        self.Siguiente = Nodo
        
    def ObtenerSimbolo(self):
        return self.PinElementos.ObtenerSimbolo()
    
class NodoCompuestos:
    def __init__(self, nombre, lista_compuestos):
        self.Compuesto = Compuestos(nombre, lista_compuestos)
        self.Siguiente = None
    
    def AsignarSiguiente(self, Nodo):
        self.Siguiente = Nodo

    def ObtenerNOmbre(self):
        return self.Compuesto.ObtenerNombre()
    
    def ObtenerListaElementos(self):
        return self.Compuesto.ObtenerListaElementos()
    
class NodoListaElemtCompuesto:
    def __init__(self, simbolo):
        self.ListaEleCompuesto = ElementosCompuesto(simbolo)
        self.Siguiente = None
    
    def AsignarSiguiente(self, Nodo):
        self.Siguiente = Nodo

    def ObtenerSimbolo(self):
        return self.ListaEleCompuesto.ObtenerSimbolo()

class NodoPines:
    def __init__(self, id, lista_elementos):
        self.Pin = Pin(id,lista_elementos)
        self.Siguiente = None

    def AsignarSiguiente(self, Nodo):
        self.Siguiente = Nodo

    def ObtenerId(self):
        return self.Pin.ObtenerId()
    
    def ObtenerListaElementos(self):
        return self.Pin.ObtenesListaElementos()
        