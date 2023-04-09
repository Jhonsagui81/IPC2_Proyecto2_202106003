from TDA.Nodo import *
from tkinter import messagebox as MessageBox
from TDA.trabajo import trabajo

class ListaPines:

    def __init__(self, pines):
        self.Inicio = None
        self.Final = None
        self.aprobacion = True
        self.limite = 0
        self.Pines = pines
    
    def Insertar(self, id, lista_elementos):
        NuevoNodo = NodoPines(id,lista_elementos)
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
            self.limite +=1
            print("se almaceno pin 1  if")
        else:
            Aux = self.Inicio
            banderin = False
            while Aux != None:
                if Aux.ObtenerListaElementos().CompararListas(NuevoNodo.ObtenerListaElementos()):
                    self.aprobacion = False
                    MessageBox.showinfo("Error!","HAY ELEMENTOS REPETIDOS ENTRE PINES  ")
                    banderin = True
                    return
                else: 
                    Aux = Aux.Siguiente
            if banderin == False:
                self.limite +=1
                self.Final.AsignarSiguiente(NuevoNodo)
                self.Final = NuevoNodo
                print("se almaceno pin 2  else")

    def validacionElementes(self):
        self.AproMax()
        Aux = self.Inicio
        while Aux != None:
            if Aux.ObtenerListaElementos().Estado():
                if self.aprobacion:
                    return True
                else:
                    return False
            else:
                return False
            
    def AproMax(self):
        if self.limite > self.Pines  or self.limite < self.Pines:
            self.aprobacion = False

    def DibujoPines(self):
        texto = ""
        estilo = '''bgcolor="#3498db"'''
        estilo2 = '''bgcolor="green"'''
        Auxiliar = self.Inicio
        while Auxiliar != None:
            texto += "\t\t\t\t<tr "+estilo2+">\n"
            texto += "\t\t\t\t\t<td "+estilo+">"+"Pin "+str(Auxiliar.ObtenerId())+"</td>\n"
            text = Auxiliar.ObtenerListaElementos().GraficaElementos()
            texto += text
            texto += "\t\t\t\t</tr>\n"
            Auxiliar = Auxiliar.Siguiente
        return texto

    def AnalizarCOmpues(self, lista_compuesto):
        Auxiliar = self.Inicio
        estado = True
        contadorCoincidencia = 0
        coincidencia = lista_compuesto.maximoELementosCOmpuesto()
        print("Total compuesto: "+str(coincidencia))
        while Auxiliar != None:
            contadorCoincidencia += Auxiliar.ObtenerListaElementos().AnalizarCompuesto(lista_compuesto)
            Auxiliar = Auxiliar.Siguiente
        print("El total de coincidencia logradas: "+str(contadorCoincidencia))
        if contadorCoincidencia == coincidencia:
            estado = True

        else:
            estado = False
        return estado

