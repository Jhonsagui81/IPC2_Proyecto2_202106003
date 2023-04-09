class trabajo:
    def Insertar(self, id, lista_elementos):
        NuevoNodo = NodoPines(id,lista_elementos)
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
            self.limite +=1
            print("se almaceno pin 1  if")
        else:
            if banderin == False:
                self.limite +=1
                self.Final.AsignarSiguiente(NuevoNodo)
                self.Final = NuevoNodo
                print("se almaceno pin 2  else")