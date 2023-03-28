import tkinter as tk
from tkinter import filedialog as FileDialog

#Varibale global
ruta = ""

def AbrirArchivo():
    global ruta

    ruta = FileDialog.askopenfilename(
        initialdir='.',
        filetypes=(
        ("Ficheros de texto", "*.xml"),
        ),
        title= "Abrir un fichero"
    )
    ##PENDIENTE ESTA ACCION 
    # if ruta != "":
    #     fichero = open(ruta, 'r')
    #     contenido = fichero.read()
    #     caja_texto.delete(1.0, 'end')
    #     caja_texto.insert('insert', contenido)
    #     fichero.close()
    #     ventana.title(ruta + " - Mi editor")


# Crear una ventana
ventana_principal = tk.Tk()

# Establecer el tamaño de la ventana principal
ventana_principal.geometry("800x600")
ventana_principal.title("Bienvenido")

# Crear un canvas y mostrar una imagen en él

imagen = tk.PhotoImage(file="./imagen/Sin.png")  #REcomendable 
ancho = imagen.width()
alto = imagen.height()

canvas = tk.Canvas(ventana_principal, width=ancho, height=alto)
canvas.create_image(0, 0, anchor=tk.NW, image=imagen)
canvas.pack(fill=tk.BOTH, expand=True)

# Crear un botón para iniciar el programa
def iniciar_programa():
    ventana_principal.destroy()
    mostrar_menu()

boton_iniciar = tk.Button(ventana_principal, text="Iniciar Programa",bg="Green", bd=5, command=iniciar_programa)
boton_iniciar.pack(side=tk.BOTTOM, fill=tk.X)

# Función para mostrar la ventana del menú
def mostrar_menu():
    # Crear una nueva ventana
    ventana_menu = tk.Tk()

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
    opcion3.add_command(label="Lista de Elementos")
    opcion3.add_command(label="Agregar Nuevo Elemento")

    opcion4 = tk.Menu(barra_menu, tearoff=0)
    opcionInterna = tk.Menu(opcion4, tearoff=0) #Para almacenar sub dentro de sub
    opcion4.add_command(label="Lista Compuestos") #opcion 
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
ventana_principal.mainloop()
