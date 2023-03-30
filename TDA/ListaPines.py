from TDA.Nodo import *

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
                    print("HAY ELEMENTOS REPETIDOS ENTRE PINES  ")
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
        # NuevoNodo = NodoPines()
        ##if validar si se repite elemento en el pin 
        ##validar el numero maximo de elementos 
        ##validar si existe elemento en otro pin 