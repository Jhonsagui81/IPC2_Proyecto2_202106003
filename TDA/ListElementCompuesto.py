from TDA.Nodo import NodoListaElemtCompuesto
from tkinter import messagebox as MessageBox



class ListaElemtosCompuestos:
    def __init__(self):
        self.Inicio = None
        self.Final = None 
        self.Limite = 0
        self.Aprobacion = True

    def Estado(self):
        return self.Aprobacion

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
                self.Final = NuevoNodo
                self.Limite += 1
                print("se asigno elemento. else")
        else:
            self.Aprobacion = False
            MessageBox.showinfo("ERROR","Elemento del compuesto no existe en lista original")

    def ElementosCompuesto(self):
        Retorno = ""
        if self.Inicio == None:
            return "La lista está vacía."
        Auxiliar = self.Inicio
        while Auxiliar != None:
            Retorno += str(Auxiliar.ObtenerSimbolo()+",")
            Auxiliar = Auxiliar.Siguiente
        
        return Retorno

    def buscarELemeto1(self, simbolo):
        texto = ""
        contador = 0
        Auxiliar = self.Inicio
        while Auxiliar != None:
            if Auxiliar.ObtenerSimbolo() == simbolo:
                return True
            Auxiliar = Auxiliar.Siguiente

    def buscarELemeto(self, simbolo):
        contador = 0
        Auxiliar = self.Inicio
        while Auxiliar != None:
            if Auxiliar.ObtenerSimbolo() == simbolo:
                contador += 1
                texto = str(simbolo)
            Auxiliar = Auxiliar.Siguiente
        texto += " se repite "+str(contador)+" Veces +"
        return contador

    def maximoELementosCOmpuesto(self):
        return self.Limite