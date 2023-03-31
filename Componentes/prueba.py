import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
ventana = tk.Tk()

# Establecer el título de la ventana principal
ventana.title("Ejemplo de interfaz con Tkinter")

# Crear la etiqueta del título
titulo = tk.Label(ventana, text="Opciones:", font=("Arial", 14))
titulo.grid(row=0, column=0, padx=10, pady=10, sticky="we")

# Crear el combobox
opciones = ["Opción 1", "Opción 2", "Opción 3", "Opción 4"]
combo = ttk.Combobox(ventana, values=opciones, font=("Arial", 12))
combo.grid(row=1, column=0, padx=10, pady=10, sticky="we")

# Crear los botones
boton1 = tk.Button(ventana, text="Botón 1", font=("Arial", 12))
boton1.grid(row=2, column=0, padx=10, pady=10)

boton2 = tk.Button(ventana, text="Botón 2", font=("Arial", 12))
boton2.grid(row=2, column=1, padx=10, pady=10)

boton3 = tk.Button(ventana, text="Botón 3", font=("Arial", 12))
boton3.grid(row=2, column=2, padx=10, pady=10)

# Ajustar la geometría de los botones
ventana.grid_rowconfigure(2, weight=1)
ventana.grid_columnconfigure((0,1,2), weight=1)

# Iniciar el bucle principal de la ventana
ventana.mainloop()

# combo.configure(values=("Opcion1","opcion2"))    #FUNCIONA