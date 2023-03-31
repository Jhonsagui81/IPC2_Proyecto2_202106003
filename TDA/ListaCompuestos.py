from TDA.Nodo import NodoCompuestos

class ListaCompuestos:
    def __init__(self):
        self.Inicio = None
        self.Final = None 
        self.Limite = 0
    
    def Insertar(self, nombre, lista_elementos):
        if lista_elementos.Estado():
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
        else:
            print("Compuesto CON problema NOSE GUARDA")

    def CompuestooLista(self):
        Retorno = "COMPUESTO"+"\t\t\t\t\t"+"FORMULA"+"\n\n"
        if self.Inicio == None:
            return "La lista está vacía."
        Auxiliar = self.Inicio
        while Auxiliar != None:
            texto = Auxiliar.ObtenerListaElementos().ElementosCompuesto()
            Retorno += str(Auxiliar.ObtenerNOmbre())+"\t\t\t\t\t"+str(texto)
            if Auxiliar.Siguiente != None:
                Retorno += "\n"
            Auxiliar = Auxiliar.Siguiente
        
        return Retorno

    def Compuestos(self):
        Texto = ""
        Auxiliar = self.Inicio
        while Auxiliar != None:
            Texto += '"'+str(Auxiliar.ObtenerNOmbre())+'"'+","
            Auxiliar = Auxiliar.Siguiente
        
        return Texto[0:-1]