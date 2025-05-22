#Librerias:
import pandas as pd
import matplotlib.pyplot as plt 
#Para visualizacion de datos
import os
#Para importar clases especificas de la libreria
from tkinter import messagebox, simpledialog
#Math y Random
import random as rd
import csv
# Archivo de almacenamiento
archivo_csv = 'registros.csv'

class Procesos():
    #Mostrar recetas al iniciar y actualizar
    def cargar_registros(self):
        if os.path.isfile(archivo_csv):
            df = pd.read_csv(archivo_csv)
            return df
        
    # Función para registrar una nueva receta
    def registrar_entrada(self):
        nombre_receta = simpledialog.askstring("Nombre","Ingrese el nombre de la receta")
        tiempo_coccion = int(rd.uniform(15,90))
        celsius = simpledialog.askfloat("Temperatura","Ingrese la temperatura de cocción en °C")
        farenh = (celsius * 1.8) + 32

        fila = {
        'Nombre_receta': nombre_receta,
        'Tiempo_coccion': f"{tiempo_coccion}min",
        'Temperatura_C': celsius,
        'Temperatura_F': farenh
        }
    
        # Verificar si ya existe el archivo
        archivo_existe = os.path.isfile(archivo_csv)

        with open(archivo_csv, 'a', newline='') as f:
            escritor = csv.DictWriter(f, fieldnames=fila.keys())
            if not archivo_existe:
                escritor.writeheader()
            escritor.writerow(fila)

    def buscar(self):
        archivo_existe = os.path.isfile('registros.csv')
        if not archivo_existe:
            messagebox.showwarning("Error", "No existen datos")
        else:
            i = simpledialog.askinteger("Nombre","Ingrese el numero de receta a buscar")
            return i
    
    def eliminar(self):
        archivo_existe = os.path.isfile('registros.csv')
        if not archivo_existe:
            messagebox.showwarning("Error", "No existen datos")
        else:
            data = pd.read_csv('registros.csv')
            receta_eliminada = simpledialog.askinteger("Nombre","Ingrese el numero de receta a eliminar")
            data.drop([receta_eliminada, receta_eliminada], axis = 0,inplace=True) 
            data.to_csv("registros.csv", index = False)

