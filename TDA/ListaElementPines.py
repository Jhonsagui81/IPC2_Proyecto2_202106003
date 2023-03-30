from TDA.Nodo import *

class ListaElementPin:

    def __init__(self, id, MaximoElementos):
        self.Inicio = None
        self.Final = None
        self.id = id 
        self.maximo = MaximoElementos
        self.limite = 0
        self.aprobado = True
    
    def Insertar(self, simbolo):
        NuevoNodo = NodoPinesElementos(simbolo)
        if self.ExisteElemento(NuevoNodo):
            print("Este Elemento ya esta registrado en el pin ")
            self.aprobado = False
            return 
        if self.limite == self.maximo:
            print("No se puede agregar mas elementos a este pin ")
            self.aprobado = False
            return
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
            self.limite += 1
            print("agregado exitoso  if")
        else:
            self.Final.AsignarSiguiente(NuevoNodo)
            self.Final = NuevoNodo
            self.limite +=1 
            print("agregado exitoso  else")
        ##if validar si se repite elemento en el pin 
        ##validar el numero maximo de elementos 
        ##validar si existe elemento en otro pin 


    def ExisteElemento(self, NuevoNodo):
        if self.Inicio == None:
            return False
        else:
            Aux = self.Inicio
            while Aux != None:
                if NuevoNodo.ObtenerSimbolo() == Aux.ObtenerSimbolo():
                    return True
                else:
                    Aux = Aux.Siguiente
            return False
    
    def CompararListas(self, lista1):
        Auxiliar = self.Inicio
        while Auxiliar != None:
            if lista1.comparar(Auxiliar.ObtenerSimbolo()):
                return True
            else:
                Auxiliar = Auxiliar.Siguiente
        return False

    def comparar(self, sim):
        Aux = self.Inicio
        while Aux != None:
            if Aux.ObtenerSimbolo() == sim:
                return True
            else:
                Aux = Aux.Siguiente
        return False

    def Estado(self):
        self.AproMax()
        return self.aprobado
    
    def AproMax(self):
        if self.limite > self.maximo  or self.limite < self.maximo:
            self.aprobado = False

    def GraficaElementos(self):
        Aux = self.Inicio
        texto = ""
        while Aux != None:
            texto += "\t\t\t\t\t<td>"+str(Aux.ObtenerSimbolo())+"</td>\n"
            Aux = Aux.Siguiente
        return texto