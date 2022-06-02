import tkinter as tk
from tkinter import messagebox
from tkinter import *
import time
from datetime import date
import random
import os

# Colores

blanco = "#ffffff"
negro = "#000000"
opcionColor = ("#03fca5")
select_color = "#77ff77"
wait_color = "#ff0000"

# Variables importantes

parqueo = {}
detalle_de_uso = []


# Funciones

def configurar():
    pass

def cargar():
    pass

def saldo():
    pass

def cajero():
    pass

def ingreso():
    pass

def entrada():
    pass

def cajero():
    pass

def salida():
    pass

def ayuda():
    pass

ventana = tk.Tk()

ventana.geometry("1000x1000")
ventana.title("Parqueo")
ventana.configure(bg = blanco)

titulo = tk.Label(ventana, text = "Parqueo", font = ("Comic Sans", 30), bg = blanco)
titulo.grid(row = 0, column = 2)

configuracion_button = tk.Button(ventana, text = "Configuración", command = lambda: configurar(), bg = select_color, height = 2, width = 10)
configuracion_button.grid(row = 1, column = 0, padx = 4, pady = 4)
cargar_button = tk.Button(ventana, text = "Cargar \n Cajero", command = lambda: cargar(), bg = select_color, height = 2, width = 10)
cargar_button.grid(row = 1, column = 1, padx = 4, pady = 4)
saldo_button = tk.Button(ventana, text = "Saldo del \n cajero", command = lambda: saldo(), bg = select_color, height = 2, width = 10)
saldo_button.grid(row = 1, column = 2, padx = 4, pady = 4)
ingreso_button = tk.Button(ventana, text = "Ingresos de \n dinero", command = lambda: ingreso(), bg = select_color, height = 2, width = 10)
ingreso_button.grid(row = 1, column = 3, padx = 4, pady = 4)
entrada_button = tk.Button(ventana, text = "Entrada del \n vehículo", command = lambda: entrada(), bg = select_color, height = 2, width = 10)
entrada_button.grid(row = 1, column = 4, padx = 4, pady = 4)
cajero_button = tk.Button(ventana, text = "Cajero del \n parqueo", command = lambda: cajero(), bg = select_color, height = 2, width = 10)
cargar_button.grid(row = 1, column = 5, padx = 4, pady = 4)
salida_button = tk.Button(ventana, text = "Salida del \n vehículo", command = lambda: salida(), bg = select_color, height = 2, width = 10)
salida_button.grid(row = 1, column = 6, padx = 4, pady = 4)
ayuda_button = tk.Button(ventana, text = "Ayuda", command = lambda: ayuda(), bg = select_color, height = 2, width = 10)
ayuda_button.grid(row = 1, column = 7, padx = 4, pady = 4)


ventana.mainloop()


