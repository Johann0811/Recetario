#Para interfaz
import tkinter as tk
import pandas as pd
from tkinter.scrolledtext import ScrolledText
import os 
#Importo la clase y el archivo_csv
from funciones import archivo_csv
from funciones import Procesos

procesos = Procesos()

def actualizar():
    DataFrame = procesos.cargar_registros()
    archivo_existe = os.path.isfile(archivo_csv)
    if not archivo_existe:
        mensaje = "No hay registros disponibles"
        text_area.delete("1.0",tk.END)
        text_area.insert(tk.END, mensaje)
    else:
        text_area.delete("1.0",tk.END)
        text_area.insert(tk.END, DataFrame.to_string(index=True))

def nueva_receta():
    procesos.registrar_entrada()

def buscar_receta():
    i = procesos.buscar()
    data = pd.read_csv(archivo_csv)

    text_area.delete("1.0",tk.END)
    mensaje = pd.DataFrame([data.loc[i].to_dict()])
    text_area.insert(tk.END, mensaje)

def eliminar_receta():
    procesos.eliminar()

ventana = tk.Tk()
ventana.title("Visualización de los datos")
ventana.geometry()

boton_añadir = tk.Button(ventana, text="Nueva receta", command=nueva_receta)
boton_añadir.grid(row=0, column=0)

boton_registros = tk.Button(ventana, text="Actualizar", command=actualizar)
boton_registros.grid(row=0, column=1)

boton_eliminar = tk.Button(ventana, text="Eliminar receta", command=eliminar_receta)
boton_eliminar.grid(row=0, column=2)

boton_buscar = tk.Button(ventana, text="Buscar receta", command=buscar_receta)
boton_buscar.grid(row=1, column=0)

text_area = ScrolledText(ventana, width= 70, height= 30)
text_area.grid(row=1, column=1)


content_frame = tk.Frame(ventana)
content_frame.grid(row=1, column=2)

actualizar() 

ventana.mainloop()


        