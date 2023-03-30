import tkinter as tk

# Crear ventana
ventana = tk.Tk()
ventana.title("Ejemplo de ventana con cajas de texto y etiquetas a un lado")

# Crear etiquetas
etiqueta1 = tk.Label(ventana, text="Parámetro 1:")
etiqueta1.grid(row=0, column=0)

etiqueta2 = tk.Label(ventana, text="Parámetro 2:")
etiqueta2.grid(row=1, column=0)

etiqueta3 = tk.Label(ventana, text="Parámetro 3:")
etiqueta3.grid(row=2, column=0)

# Crear cajas de texto
caja1 = tk.Entry(ventana)
caja1.grid(row=0, column=1)

caja2 = tk.Entry(ventana)
caja2.grid(row=1, column=1)

caja3 = tk.Entry(ventana)
caja3.grid(row=2, column=1)

# Mostrar ventana
ventana.mainloop()

