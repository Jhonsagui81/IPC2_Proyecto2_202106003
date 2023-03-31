from TDA.Nodo import *
import os

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
    
    def Impimir(self):
        Retorno = "La lista tiene: ["
        if self.Inicio == None:
            return "La lista está vacía."
        Auxiliar = self.Inicio
        while Auxiliar != None:
            Retorno += str(Auxiliar.ObtenerNombre())
            if Auxiliar.Siguiente != None:
                Retorno += ", "
            Auxiliar = Auxiliar.Siguiente
        Retorno += "]"
        return Retorno

    def GenerarDibujo(self):
        estilo = '''bgcolor="#c04343"'''
        texto = "digraph {\n"
        texto += "\ttb1 [\n"
        texto += "\t\tshape=plaintext\n"
        texto += "\t\tlabel=<\n"
        texto += "\t\t\t<table border='0' cellborder='1' color='blue' cellspacing='0'>\n"
        Auxiliar = self.Inicio
        while Auxiliar != None:
            texto += "\t\t\t\t<tr>\n"
            texto += "\t\t\t\t\t<td "+estilo+" colspan="'"'+str(Auxiliar.ObtenerNOElementos()+1)+'"'">"+str(Auxiliar.ObtenerNombre())+"</td>\n"
            texto += "\t\t\t\t</tr>\n"
            
            text = Auxiliar.ObtenerListaPines().DibujoPines()
            texto += text

            texto += "\t\t\t\t<tr>\n"
            texto += "\t\t\t\t\t<td colspan="'"'+str("")+str(Auxiliar.ObtenerNOElementos()+1)+'"'"> </td>\n"
            texto += "\t\t\t\t</tr>\n"
            Auxiliar = Auxiliar.Siguiente
        texto += "\t\t\t</table>\n"
        texto += "\t>];\n"
        texto += "}\n"
        file = open("/home/jhonatan/Descargas/grafica_maquinas.dot", "w")
        file.write(texto)
        file.close()
        os.system("dot -Tpdf /home/jhonatan/Descargas/grafica_maquinas.dot -o  /home/jhonatan/Descargas/grafica_maquinas.pdf")
        