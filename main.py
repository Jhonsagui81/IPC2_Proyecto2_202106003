import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as FileDialog
from xml.dom import minidom
from tkPDFViewer import tkPDFViewer as pdf
from tkinter import Toplevel
import re

from TDA.ListaElementos import ListaElementos
from TDA.ListaMaquinas import ListaMaquinas
from TDA.ListaElementPines import ListaElementPin
from TDA.ListaCompuestos import ListaCompuestos
from TDA.ListElementCompuesto import ListaElemtosCompuestos
from TDA.ListaPines import ListaPines

#Varibale global
ruta = ""
list_Elements = ListaElementos()
list_maquina = ListaMaquinas()
lista_compuesto = ListaCompuestos()

#implementaran durante ejecucion 
ventana_menu = tk.Tk()
text_area = tk.Text(ventana_menu)


#MENU GESTION ELEMENTOS
label = tk.Frame(ventana_menu)
caja1 = tk.Entry(label)
caja2 = tk.Entry(label)
caja3 = tk.Entry(label)

#MENU GESTION COMPUESTOS
analizar = tk.Frame(ventana_menu)
titulo = tk.Label(analizar, text="Compuestos Disponibles:", font=("Arial", 14))
combo = ttk.Combobox(analizar, font=("Arial", 12))

AnalizaMaquina = tk.Frame(ventana_menu)
tituloMaq = tk.Label(AnalizaMaquina, text="Maquinas y Tiempos", font=("Arial", 14))
comboMaquina = ttk.Combobox(AnalizaMaquina, font=("Arial", 12))

# boton2 = tk.Button(analizar, text="Botón 2", font=("Arial", 12))
# boton3 = tk.Button(analizar, text="Botón 3", font=("Arial", 12))

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
                
                maquina = lisMaq.getElementsByTagName("Maquina")
                for maqui in maquina:
                    contador_pin = 0
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

#MENU GESTION ELEMENTOS
def ListElementos():
    #para limpiar Pantalla
    label.grid_forget()
    analizar.grid_forget()
    AnalizaMaquina.grid_forget()

    #Funcionalidad 
    text_area.delete(1.0, tk.END)
    list_Elements.OrdenarElementos()
    texto = list_Elements.Impimir()
    text_area.insert(1.0, texto)
    text_area.pack(expand=True, fill="both")
    text_area.pack_propagate(False)
    # text_area.place(relx=0.5, rely=0.5, anchor="center")

def AgregarElemento():
    atomi=caja1.get()
    simb=caja2.get()
    name=caja3.get()
    list_Elements.IncertarElemento(atomi,simb, name)
    list_Elements.OrdenarElementos()
    
def VentanaAgregarElemento():
    text_area.pack_forget()
    analizar.grid_forget()
    AnalizaMaquina.grid_forget()


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
    label.grid(row=2, column=2,)

#MENU GESTION COMPUESTOS 
def ListaCompuestosVentana():
    text_area.pack_forget()
    analizar.grid_forget()
    AnalizaMaquina.grid_forget()

    #Funcionalidad 
    text_area.delete(1.0, tk.END)
    info = lista_compuesto.CompuestooLista()

    text_area.insert(1.0, info)
    text_area.pack(expand=True, fill="both")
    text_area.pack_propagate(False)
    # text_area.place(relx=0.5, rely=0.5, anchor="center")

def VentanaAnalizarCompuesto():
    #LIMPIAR cualquier cosa
    text_area.pack_forget()
    label.grid_forget()
    AnalizaMaquina.grid_forget()
    
    #incorporar la etiqueta del título
    titulo.grid(row=0, column=0, padx=10, pady=10, sticky="we")

    # Incorporar el combobox
    combo.grid(row=1, column=0, padx=10, pady=10, sticky="we")
    


    text=lista_compuesto.Compuestos()
    texto = text.split(",")

    combo.configure(values=(texto))    #FUNCIONA

    # combo.bind("<<ComboboxSelected>>", lambda _ : print(f"Mes pre-seleccionado '{combo.get()}'"))


    #incorporar los botones
    boton1 = tk.Button(analizar, text="Analizar Compuesto",background="green", font=("Arial", 12), command=VentanaMaquina)
    boton1.grid(row=1, column=2, padx=10, pady=10)

    # Ajustar    la geometría de los botones
    analizar.grid_rowconfigure(2, weight=1)
    analizar.grid_columnconfigure((0,1,2), weight=1)
    analizar.grid()

def VentanaMaquina():
    
    #LIMPIAR cualquier cosa
    text_area.pack_forget()
    label.grid_forget()
    analizar.grid_forget()
    
    #obtener lista de elementos del compuesto seleccionado 
    res = combo.get()
    print("se selecciona:" +res)
    #lista de elementos de compuesto 
    listacompuet = lista_compuesto.BuscarCompuesto(res)
    


    # Crear la etiqueta del título
    tituloMaq.grid(row=0, column=0, padx=10, pady=10, sticky="we")
    # Crear el combobox
    comboMaquina.grid(row=1, column=0, padx=10, pady=10, sticky="we")

    #Pasar lista de elemetntos a la maquina
    estado = list_maquina.AsignarCompuestoOperar(listacompuet)
    estados = estado.split(",")

    # combo.configure(values=(texto))    #FUNCIONA
    comboMaquina.configure(values=(estados))

    # Crear los botones
    boton1 = tk.Button(AnalizaMaquina, text="Ver Instrucciones",background="green", font=("Arial", 12), command=VentanaMaquina)
    boton1.grid(row=1, column=2, padx=10, pady=10)



    # Ajustar la geometría de los botones
    AnalizaMaquina.grid_rowconfigure(2, weight=1)
    AnalizaMaquina.grid_columnconfigure((0,1,2), weight=1)
    AnalizaMaquina.grid()


#MENU GESTION DE MAQUINAS
v1 = pdf.ShowPdf()
v2 = pdf.ShowPdf()

def graficaMaquinas():
    #genera Dibujo
    list_maquina.GenerarDibujo(list_Elements)
    
    #mostrar Dibujo Ventana
    ventana_maquina = Toplevel(ventana_menu)
    ventana_maquina.title("Maquinas Disponibles")
    ventana_maquina.geometry("800x600+400+100")
    ventana_maquina.configure(bg="White")
    
    v1.img_object_li.clear()
    
    v2 = v1.pdf_view(ventana_maquina, pdf_location=open("/home/jhonatan/Descargas/grafica_maquinas.pdf","r"), width=77, height=100)
    v2.pack()
    
#TEMAS DE AYUDA
def ayuda():
    label.grid_forget()
    text_area.pack_forget()
    analizar.grid_forget()
    AnalizaMaquina.grid_forget()
    
    text_area.delete(1.0, tk.END)
    Retorno = "NOMBRE"+"\t\t\t"+"APELLIDO"+"\t\t\t"+"CARNET"+"\n\n"
    Retorno += "Jhonatan Alexander"+"\t\t\t"+"Aguilar Reyes"+"\t\t\t"+"202106003"+"\n"
    Retorno += "Link de la documentacion: ...pendiendte"
    
    text_area.insert(1.0, Retorno)
    text_area.pack()

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
ventana_menu.geometry("800x200")
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
# opcionInterna = tk.Menu(opcion4, tearoff=0) #Para almacenar sub dentro de sub
opcion4.add_command(label="Lista Compuestos", command=ListaCompuestosVentana) #opcion 
opcion4.add_command(label="Analizar Compuesto", command=VentanaAnalizarCompuesto) #opcion con subopciones
# opcionInterna.add_command(label="Seleccionar Compuesto")
# opcionInterna.add_command(label="Lista de Maquinas y Tiempos")
# opcionInterna.add_command(label="Grafica de Instrucciones")

opcion5 = tk.Menu(barra_menu, tearoff=0)
opcion5.add_command(label="Grafica de Maquinas", command=graficaMaquinas)

opcion6 = tk.Menu(barra_menu, tearoff=0)
opcion6.add_command(label="Acerca de...", command=ayuda)

    
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
