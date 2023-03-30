import tkinter as tk
from tkinter import filedialog as FileDialog
from xml.dom import minidom

from TDA.ListaElementos import ListaElementos
from TDA.ListaMaquinas import ListaMaquinas
from TDA.ListaElementPines import ListaElementPin
from TDA.ListaCompuestos import ListaCompuestos
from TDA.ListElementCompuesto import ListaElemtosCompuestos
from TDA.ListaPines import ListaPines

#Varibale global
ruta = ""
list_Elements = ListaElementos()

#implementaran durante ejecucion 
ventana_menu = tk.Tk()


#menu Gestion Elementos
text_area = tk.Text(ventana_menu)
label = tk.Frame(ventana_menu)
caja1 = tk.Entry(label)
caja2 = tk.Entry(label)
caja3 = tk.Entry(label)

def AbrirArchivo():
    contador_pin = 0
    global list_Elements
    global ruta

    ruta = FileDialog.askopenfilename(
        initialdir='.',
        filetypes=(
        ("Ficheros de texto", "*.xml"),
        ),
        title= "Abrir un fichero"
    )

    if ruta != "":
        doc = minidom.parse(str(ruta))
        print("\n\t-----------Leyendo el documento---------------")
        configuracion = doc.getElementsByTagName("CONFIG")
        #Congig - ETIQUETA ROOT
        for confi in configuracion:
            #Lectura - ListaElementos
            listaElemtsConfig = confi.getElementsByTagName("listaElementos")
            for ele in listaElemtsConfig:
                #Lista de elementos 
                #Lectura - elementos 
                elementConfig = ele.getElementsByTagName("elemento")
                for data in elementConfig:
                    #Lectura - datosElementos
                    no_atomico = data.getElementsByTagName("numeroAtomico")
                    simbolo = data.getElementsByTagName("simbolo")
                    nombre_elementCofig = data.getElementsByTagName("nombreElemento")
                    #obteniendo Valores
                    valor_no_atomico = int(no_atomico[0].firstChild.nodeValue)
                    valor_simbolo = str(simbolo[0].firstChild.nodeValue)
                    valor_elementoCofig = str(nombre_elementCofig[0].firstChild.nodeValue)
                    #Insertarlos en Lista - listasimple
                    list_Elements.IncertarElemento(valor_no_atomico, valor_simbolo, valor_elementoCofig)
                    


            #Lectura - ListaMaquinas 
            listaMaquinasConfig = confi.getElementsByTagName("listaMaquinas")
            for lisMaq in listaMaquinasConfig:
                #Lectura - Maquina
                list_maquina = ListaMaquinas()
                maquina = lisMaq.getElementsByTagName("Maquina")
                for maqui in maquina:
                    #Lectura - datosMaquina
                    nombre_maquina = maqui.getElementsByTagName("nombre")
                    no_pines = maqui.getElementsByTagName("numeroPines")
                    no_elemen = maqui.getElementsByTagName("numeroElementos")
                    #obteniendo valores
                    valor_nombre_maquina = str(nombre_maquina[0].firstChild.nodeValue)
                    valor_no_pines = int(no_pines[0].firstChild.nodeValue)
                    valor_no_elemen = int(no_elemen[0].firstChild.nodeValue)
                    #Insertar datos de la maquina - listaSimple
                    #Lectura de pines
                    lis_pin = maqui.getElementsByTagName("pin")
                    #Creacion Lista pin
                    lista_pin = ListaPines(valor_no_pines)
                    for pin in lis_pin:
                        contador_pin +=1
                        #Creacion Lista elementos pim 
                        lista_element_pines = ListaElementPin(contador_pin,valor_no_elemen)
                        #Lectura - elementos Pin
                        elementos_pin = pin.getElementsByTagName("elementos")
                        #Insertar info pin - listasimple  (dentro listamaquina??)
                        for dato_pin in elementos_pin:
                            simb_elemen_pin = dato_pin.getElementsByTagName("elemento")
                            #Obteniendo valores
                            for lisELe in simb_elemen_pin:
                                
                                Val_simb_eleme_pin = str(lisELe.firstChild.nodeValue)
                                lista_element_pines.Insertar(Val_simb_eleme_pin)
                                #Insertar datos elementos -listadoble  (dentro listamquina??  o dento de listapin??)
                        lista_pin.Insertar(contador_pin, lista_element_pines)
                    list_maquina.InsertarMaquina(valor_nombre_maquina,valor_no_pines, valor_no_elemen, lista_pin) ##Banderiiin

            #Lectura - ListaCompuestos
            listaCompuestos = confi.getElementsByTagName("listaCompuestos")
            for comp in listaCompuestos:
                compuesto = comp.getElementsByTagName("compuesto")
                #Creacion Lista compuestos
                lista_compuesto = ListaCompuestos()
                for compuest in compuesto:
                    #Lectura - datos compuesto 
                    nombreCompuesto = compuest.getElementsByTagName("nombre")
                    #obteniendo valores
                    valor_nombreCompuesto = str(nombreCompuesto[0].firstChild.nodeValue)
                    #Lectura de Elementos del compuesto
                    elementos_Compuesto = compuest.getElementsByTagName("elementos")
                    #Creacion lista elementos Compuesto
                    list_elemt_compuesto = ListaElemtosCompuestos()
                    for ele_comp in elementos_Compuesto:
                        #lectura - elemento 
                        elemen_compues = ele_comp.getElementsByTagName("elemento")
                        for ele_com in elemen_compues:
                        #Obtener valores
                            valor_elemen_compues = str(ele_com.firstChild.nodeValue)
                            #Insertar elemento - listasimple
                            list_elemt_compuesto.Insertar(valor_elemen_compues, list_Elements)
                    #Insertar dato Compuesto - listasimple  (nombre, listasimple)
                    lista_compuesto.Insertar(valor_nombreCompuesto, list_elemt_compuesto)

def ListElementos():
    #para limpiar Pantalla
    label.grid_forget()

    #Funcionalidad 
    text_area.delete(1.0, tk.END)
    list_Elements.OrdenarElementos()
    texto = list_Elements.Impimir()
    text_area.insert(1.0, texto)
    text_area.pack()

def AgregarElemento():
    atomi=caja1.get()
    simb=caja2.get()
    name=caja3.get()
    list_Elements.IncertarElemento(atomi,simb, name)
    list_Elements.OrdenarElementos()
    

def VentanaAgregarElemento():
    text_area.pack_forget()
    
    # Crear etiquetas
    etiqueta1 = tk.Label(label, text="Numero Atomico:")
    etiqueta1.grid(row=0, column=0)

    etiqueta2 = tk.Label(label, text="Simbolo Elemento:")
    etiqueta2.grid(row=1, column=0)

    etiqueta3 = tk.Label(label, text="Nombre Elemento:")
    etiqueta3.grid(row=2, column=0)
    
    # Crear cajas de texto
    caja1.grid(row=0, column=1)
    caja2.grid(row=1, column=1)
    caja3.grid(row=2, column=1)

    #Crear boton
    add_button = tk.Button(label, text="Agregar Elemento",bg="Green" ,command=AgregarElemento)
    add_button.grid(row=1, column=2)

    #Incorporar Frame en ventana
    label.grid()

def Compuesto():
    text_area.pack_forget()
    label.grid_forget()

# # Crear una ventana
# ventana_principal = tk.Tk()

# # Establecer el tamaño de la ventana principal
# ventana_principal.geometry("800x600")
# ventana_principal.title("Bienvenido")

# # Crear un canvas y mostrar una imagen en él

# imagen = tk.PhotoImage(file="./imagen/Sin.png")  #REcomendable 
# ancho = imagen.width()
# alto = imagen.height()

# canvas = tk.Canvas(ventana_principal, width=ancho, height=alto)
# canvas.create_image(0, 0, anchor=tk.NW, image=imagen)
# canvas.pack(fill=tk.BOTH, expand=True)

# # Crear un botón para iniciar el programa
# def iniciar_programa():
#     ventana_principal.destroy()
#     mostrar_menu()

# boton_iniciar = tk.Button(ventana_principal, text="Iniciar Programa",bg="Green", bd=5, command=iniciar_programa)
# boton_iniciar.pack(side=tk.BOTTOM, fill=tk.X)

# Función para mostrar la ventana del menú

# Crear una nueva ventana


#Establecer el tamano de la ventana secundaria 
ventana_menu.geometry("800x600")
ventana_menu.title("Menu Principal")

# Crear una barra de menú
barra_menu = tk.Menu(ventana_menu)
    
    
# Crear las opciones del menú
opcion1 = tk.Menu(barra_menu, tearoff=0)
opcion1.add_command(label="Abrir", command=AbrirArchivo)

opcion2 = tk.Menu(barra_menu, tearoff=0)
opcion2.add_command(label="Generar xml")

opcion3 = tk.Menu(barra_menu, tearoff=0)
opcion3.add_command(label="Lista de Elementos", command=ListElementos)
opcion3.add_command(label="Agregar Nuevo Elemento", command=VentanaAgregarElemento)

opcion4 = tk.Menu(barra_menu, tearoff=0)
opcionInterna = tk.Menu(opcion4, tearoff=0) #Para almacenar sub dentro de sub
opcion4.add_command(label="Lista Compuestos", command=Compuesto) #opcion 
opcion4.add_cascade(label="Analizar Compuesto", menu=opcionInterna) #opcion con subopciones
opcionInterna.add_command(label="Seleccionar Compuesto")
opcionInterna.add_command(label="Lista de Maquinas y Tiempos")
opcionInterna.add_command(label="Grafica de Instrucciones")

opcion5 = tk.Menu(barra_menu, tearoff=0)
opcion5.add_command(label="Grafica de Maquinas")

opcion6 = tk.Menu(barra_menu, tearoff=0)
opcion6.add_cascade(label="Acerca de...")

    
    # opcionInterna.add_command(label="OpcionInterna")
    # Agregar las opciones al menú.
barra_menu.add_cascade(label="Cargar XML", menu=opcion1)
barra_menu.add_cascade(label="Generar XML", menu=opcion2)
barra_menu.add_cascade(label="Gestionar Elementos", menu=opcion3)
barra_menu.add_cascade(label="Gestionar Compuestos", menu=opcion4)
barra_menu.add_cascade(label="Gestionar Maquinas", menu=opcion5)
barra_menu.add_cascade(label="Ayuda", menu=opcion6)

    #Para opciones Internas
    # opcion6.add_cascade(label="Ayuda", menu = opcionInterna)
    
    # Mostrar la barra de menú en la ventana
ventana_menu.config(menu=barra_menu)

    # Mostrar la ventana
ventana_menu.mainloop()
    
# Ejecutar la ventana principal
# ventana_principal.mainloop()
