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
configuracion = [30, 50, 75, "diego@gmail.com", 15, 1, 5, 10, 1, 5, 10, 20, 50]
saldocoin1 = 0
saldocoin2 = 0
saldocoin3 = 0

saldobill1 = 0
saldobill2 = 0
saldobill3 = 0
saldobill4 = 0
saldobill5 = 0


# Funciones
def cerrarventana(window):
    window.destroy()
    window.update()    

def configurar():

    def guardarconfig(cantidadcarros, price, pagomin, correosuper, minutosmax, coin1, coin2, coin3, bill1, bill2, bill3, bill4, bill5):
        if cantidadcarros < 1:
            messagebox.showinfo("Error", "La cantidad de carros en el parqueo debe ser un entero mayor o igual a 1.") # Se despliega un error si no es válido
            return
        if price < 0:
            messagebox.showinfo("Error", "El precio debe ser un flotante >= 0 con máximo 2 decimales.") # Se despliega un error si no es válido
            return
        if pagomin < 0:
            messagebox.showinfo("Error", "El pago mínimo debe ser un flotante >= 0 con máximo 2 decimales.") # Se despliega un error si no es válido
            return
        if minutosmax < 0:
            messagebox.showinfo("Error", "Los minutos máximos deben ser un entero >= 0.") # Se despliega un error si no es válido
            return
        if coin1 < 0:
            messagebox.showinfo("Error", "La moneda debe ser un entero >= 0.") # Se despliega un error si no es válido
            return
        if coin2 < 0:
            messagebox.showinfo("Error", "La moneda debe ser un entero >= 0.") # Se despliega un error si no es válido
            return
        if coin3 < 0:
            messagebox.showinfo("Error", "La moneda debe ser un entero >= 0.") # Se despliega un error si no es válido
            return
        if bill1 < 0:
            messagebox.showinfo("Error", "El billete debe ser un entero >= 0.") # Se despliega un error si no es válido
            return
        if bill2 < 0:
            messagebox.showinfo("Error", "El billete debe ser un entero >= 0.") # Se despliega un error si no es válido
            return
        if bill3 < 0:
            messagebox.showinfo("Error", "El billete debe ser un entero >= 0.") # Se despliega un error si no es válido
            return
        if bill4 < 0:
            messagebox.showinfo("Error", "El billete debe ser un entero >= 0.") # Se despliega un error si no es válido
            return
        if bill5 < 0:
            messagebox.showinfo("Error", "El billete debe ser un entero >= 0.") # Se despliega un error si no es válido
            return

        if coin1 == 0:
            coin2 = 0
            coin3 = 0
        if coin2 == 0:
            coin3 = 0
        if bill1 == 0:
            bill2 = 0
            bill3 = 0
            bill4 = 0
            bill5 = 0
        if bill2 == 0:
            bill3 = 0
            bill4 = 0
            bill5 = 0
        if bill3 == 0:
            bill4 = 0
            bill5 = 0
        if bill4 == 0:
            bill5 = 0
        
        pricebill = int(price)
        pricecoin = int(price * 100 % 100)  

        if bill5 != 0:
            pricebill = pricebill % bill5

        if bill4 != 0:
            pricebill = pricebill % bill4

        if bill3 != 0:
            pricebill = pricebill % bill3

        if bill2 != 0:
            pricebill = pricebill % bill2

        if bill1 != 0:
            pricebill = pricebill % bill1

        if coin3 != 0:
            pricecoin = pricecoin % coin3

        if coin2 != 0:
            pricecoin = pricecoin % coin2

        if coin1 != 0:
            pricecoin = pricecoin % coin1

        if pricebill != 0 or pricecoin != 0:
            messagebox.showinfo("Error", "El precio mínimo no es válido >= 0.") # Se despliega un error si no es válido
            return
        global configuracion
        configuracion = configuracion + [cantidadcarros] + [price] + [pagomin] + [correosuper] + [minutosmax] + [coin1] + [coin2] + [coin3] + [bill1] + [bill2] + [bill3] + [bill4] + [bill5]
        print(configuracion)

      #  fk = open(".dat", "w")

    configurar_ventana = tk.Toplevel(ventana)
    configurar_ventana.title("Configurar")
    configurar_ventana.geometry("900x600")
    configurar_ventana.configure(bg = blanco)
    configurar_Label = tk.Label(configurar_ventana, text = "PARQUEO - CONFIGURACIÓN", font = ("Arial", 36),bg = blanco) 
    configurar_Label.grid(row = 0, column = 0)

    cantidadcar_label = tk.Label(configurar_ventana, text = "Cantidad de espacios en el parqueo (entero >= 1)", font = ("Arial", 14),bg = blanco) 
    cantidadcar_label.grid(row = 1, column = 0)
    car = tk.IntVar()
    cantidadcar = tk.Entry(configurar_ventana, textvariable = car)
    cantidadcar.grid(row = 1, column = 1)

    precio_Label = tk.Label(configurar_ventana, text = "Precio por hora (máximo dos decimales >= 0)", font = ("Arial", 14),bg = blanco) 
    precio_Label.grid(row = 2, column = 0)
    precio = tk.DoubleVar()
    precioentry = tk.Entry(configurar_ventana, textvariable = precio)
    precioentry.grid(row = 2, column = 1)


    pagomin_Label = tk.Label(configurar_ventana, text = "Pago mínimo (máximo dos decimales >= 0) ", font = ("Arial", 14),bg = blanco) 
    pagomin_Label.grid(row = 3, column = 0)
    minpay = tk.DoubleVar()
    pagominentry = tk.Entry(configurar_ventana, textvariable = minpay)
    pagominentry.grid(row = 3, column = 1)

    correosupervisor_Label = tk.Label(configurar_ventana, text = "Correo electrónico del supervisor", font = ("Arial", 14),bg = blanco) 
    correosupervisor_Label.grid(row = 4, column = 0)
    emailsuper = tk.StringVar()
    correosupervisorentry = tk.Entry(configurar_ventana, textvariable = emailsuper)
    correosupervisorentry.grid(row = 4, column = 1)

    minutosmax_Label = tk.Label(configurar_ventana, text = "Minutos máximos para salir después del pago (entero >=0)", font = ("Arial", 14),bg = blanco) 
    minutosmax_Label.grid(row = 5, column = 0)
    minmax = tk.IntVar()
    minmaxentry = tk.Entry(configurar_ventana, textvariable = minmax)
    minmaxentry.grid(row = 5, column = 1)

    tipomoneda_Label = tk.Label(configurar_ventana, text = "Tipos de moneda (máximo 3 tipos, enteros >= 0):", font = ("Arial", 14),bg = blanco) 
    tipomoneda_Label.grid(row = 6, column = 0)

    moneda1_Label = tk.Label(configurar_ventana, text = "Moneda 1, la de menor denominación (ejemplo 50)", font = ("Arial", 14),bg = blanco) 
    moneda1_Label.grid(row = 7, column = 0)
    moneda1 = tk.IntVar()
    moneda1entry = tk.Entry(configurar_ventana, textvariable = moneda1)
    moneda1entry.grid(row = 7, column = 1)

    moneda2_Label = tk.Label(configurar_ventana, text = "Moneda 2, denominación siguiente a la anterior (ejemplo 100)", font = ("Arial", 14),bg = blanco) 
    moneda2_Label.grid(row = 8, column = 0)
    moneda2 = tk.IntVar()
    moneda2entry = tk.Entry(configurar_ventana, textvariable = moneda2)
    moneda2entry.grid(row = 8, column = 1)

    moneda3_Label = tk.Label(configurar_ventana, text = "Moneda 3, denominación siguiente a la anterior (ejemplo 500)", font = ("Arial", 14),bg = blanco) 
    moneda3_Label.grid(row = 9, column = 0)
    moneda3 = tk.IntVar()
    moneda3entry = tk.Entry(configurar_ventana, textvariable = moneda3)
    moneda3entry.grid(row = 9, column = 1)

    tipobillete_Label = tk.Label(configurar_ventana, text = "Tipos de billetes (máximo 5 tipos, enteros >= 0):", font = ("Arial", 14),bg = blanco) 
    tipobillete_Label.grid(row = 10, column = 0)

    billete1_Label = tk.Label(configurar_ventana, text = "Billete 1, el de menor denominación (ejemplo 1000)", font = ("Arial", 14),bg = blanco) 
    billete1_Label.grid(row = 11, column = 0)
    billete1 = tk.IntVar()
    billete1entry = tk.Entry(configurar_ventana, textvariable = billete1)
    billete1entry.grid(row = 11, column = 1)

    billete2_Label = tk.Label(configurar_ventana, text = "Billete 2, denominación siguiente a la anterior (ejemplo 2000)", font = ("Arial", 14),bg = blanco) 
    billete2_Label.grid(row = 12, column = 0)
    billete2 = tk.IntVar()
    billete2entry = tk.Entry(configurar_ventana, textvariable = billete2)
    billete2entry.grid(row = 12, column = 1)

    billete3_Label = tk.Label(configurar_ventana, text = "Billete 3, denominación siguiente a la anterior (ejemplo 5000)", font = ("Arial", 14),bg = blanco) 
    billete3_Label.grid(row = 13, column = 0)
    billete3 = tk.IntVar()
    billete3entry = tk.Entry(configurar_ventana, textvariable = billete3)
    billete3entry.grid(row = 13, column = 1)

    billete4_Label = tk.Label(configurar_ventana, text = "Billete 4, denominación siguiente a la anterior (ejemplo 10000)", font = ("Arial", 14),bg = blanco) 
    billete4_Label.grid(row = 14, column = 0)
    billete4 = tk.IntVar()
    billete4entry = tk.Entry(configurar_ventana, textvariable = billete4)
    billete4entry.grid(row = 14, column = 1)

    billete5_Label = tk.Label(configurar_ventana, text = "Billete 5, denominación siguiente a la anterior (ejemplo 20000)", font = ("Arial", 14),bg = blanco) 
    billete5_Label.grid(row = 15, column = 0)
    billete5 = tk.IntVar()
    billete5entry = tk.Entry(configurar_ventana, textvariable = billete5)
    billete5entry.grid(row = 15, column = 1)


     
    saveconfig_button = tk.Button(configurar_ventana, text = "Guardar tiempo", command = lambda: guardarconfig(car.get(), precio.get(), \
        minpay.get(), emailsuper.get(), minmax.get(), moneda1.get(), moneda2.get(), moneda3.get(), billete1.get(), billete2.get(), \
            billete3.get(), billete4.get(), billete5.get()), bg = blanco, height = 2, width = 12)
    saveconfig_button.grid(row = 16, column = 0, padx = 4, pady = 4)    
    cancelconfig_button = tk.Button(configurar_ventana, text = "Guardar tiempo", command = lambda: cerrarventana(configurar_ventana), bg = blanco, height = 2, width = 12)
    cancelconfig_button.grid(row = 16, column = 1, padx = 4, pady = 4)   


def cargar():
    def guardarcajero():
        pass

    global saldocoin1 # Los saldos contienen la cantidad de billetes
    global saldocoin2
    global saldocoin3

    global saldobill1
    global saldobill2
    global saldobill3
    global saldobill4
    global saldobill5
    global configuracion

    coin1 = configuracion[5]
    coin2 = configuracion[6]
    coin3 = configuracion[7]

    bill1 = configuracion[8]
    bill2 = configuracion[9]
    bill3 = configuracion[10]
    bill4 = configuracion[11]
    bill5 = configuracion[12]



    cargar_ventana = tk.Toplevel(ventana)
    cargar_ventana.title("Cargar")
    cargar_ventana.geometry("900x600")
    cargar_ventana.configure(bg = blanco)
    cargar_Label = tk.Label(cargar_ventana, text = "PARQUEO - CARGAR CAJERO", font = ("Arial", 36),bg = blanco) 
    cargar_Label.grid(row = 0, column = 0, columnspan = 6)

    denominacion_label = tk.Label(cargar_ventana, text = "DENOMINACIÓN", font = ("Arial", 14),bg = blanco) 
    denominacion_label.grid(row = 2, column = 0)

    saldoantes_label = tk.Label(cargar_ventana, text = "SALDO ANTES DE LA CARGA", font = ("Arial", 14),bg = blanco) 
    saldoantes_label.grid(row = 1, column = 1, columnspan = 2)

    cantidadantes_label = tk.Label(cargar_ventana, text = "CANTIDAD", font = ("Arial", 14),bg = blanco) 
    cantidadantes_label.grid(row = 2, column = 1)

    totalantes_label = tk.Label(cargar_ventana, text = "TOTAL", font = ("Arial", 14),bg = blanco) 
    totalantes_label.grid(row = 2, column = 2)
    
    saldocarga_label = tk.Label(cargar_ventana, text = "CARGA", font = ("Arial", 14),bg = blanco) 
    saldocarga_label.grid(row = 1, column = 3)

    cantidadcarga_label = tk.Label(cargar_ventana, text = "CANTIDAD", font = ("Arial", 14),bg = blanco) 
    cantidadcarga_label.grid(row = 2, column = 3)

    totalcarga_label = tk.Label(cargar_ventana, text = "TOTAL", font = ("Arial", 14),bg = blanco) 
    totalcarga_label.grid(row = 2, column = 4)
    
    saldototal_label = tk.Label(cargar_ventana, text = "SALDO", font = ("Arial", 14),bg = blanco) 
    saldototal_label.grid(row = 1, column = 5)

    cantidadtotal_label = tk.Label(cargar_ventana, text = "CANTIDAD", font = ("Arial", 14),bg = blanco) 
    cantidadtotal_label.grid(row = 2, column = 5)

    totaltotal_label = tk.Label(cargar_ventana, text = "TOTAL", font = ("Arial", 14),bg = blanco) 
    totaltotal_label.grid(row = 2, column = 6)

    textocoin1 = "Moneda de " + str(coin1)
    moneda1_Label = tk.Label(cargar_ventana, text = textocoin1, font = ("Arial", 14),bg = blanco) 
    moneda1_Label.grid(row = 3, column = 0)
    

    textocoin2 = "Moneda de " + str(coin2)
    moneda2_Label = tk.Label(cargar_ventana, text = textocoin2, font = ("Arial", 14),bg = blanco) 
    moneda2_Label.grid(row = 4, column = 0)

    textocoin3 = "Moneda de " + str(coin3)
    moneda3_Label = tk.Label(cargar_ventana, text = textocoin3, font = ("Arial", 14),bg = blanco) 
    moneda3_Label.grid(row = 5, column = 0)

    totalmoneda_Label = tk.Label(cargar_ventana, text = "TOTAL DE MONEDAS", font = ("Arial", 14),bg = blanco) 
    totalmoneda_Label.grid(row = 6, column = 0)

    textobill1 = "Moneda de " + str(bill1)
    billete1_Label = tk.Label(cargar_ventana, text = textobill1, font = ("Arial", 14),bg = blanco) 
    billete1_Label.grid(row = 7, column = 0)

    textobill2 = "Moneda de " + str(bill2)
    billete2_Label = tk.Label(cargar_ventana, text = textobill2, font = ("Arial", 14),bg = blanco) 
    billete2_Label.grid(row = 8, column = 0)

    textobill3 = "Moneda de " + str(bill3)
    billete3_Label = tk.Label(cargar_ventana, text = textobill3, font = ("Arial", 14),bg = blanco) 
    billete3_Label.grid(row = 9, column = 0)

    textobill4 = "Moneda de " + str(bill4)
    billete4_Label = tk.Label(cargar_ventana, text = textobill4, font = ("Arial", 14),bg = blanco) 
    billete4_Label.grid(row = 10, column = 0)
    
    textobill5 = "Moneda de " + str(bill5)
    billete5_Label = tk.Label(cargar_ventana, text = textobill5, font = ("Arial", 14),bg = blanco) 
    billete5_Label.grid(row = 11, column = 0)

    totalbillete_Label = tk.Label(cargar_ventana, text = "TOTAL DE BILLETES", font = ("Arial", 14),bg = blanco) 
    totalbillete_Label.grid(row = 12, column = 0)

    totalcajero_Label = tk.Label(cargar_ventana, text = "TOTAL DE  CAJERO", font = ("Arial", 14),bg = blanco) 
    totalcajero_Label.grid(row = 13, column = 0)

# Empiezan los labels con los números.

    cantidadcoin1antes_Label = tk.Label(cargar_ventana, text = str(saldocoin1), font = ("Arial", 14),bg = blanco) 
    cantidadcoin1antes_Label.grid(row = 3, column = 1)

    cantidadcoin2antes_Label = tk.Label(cargar_ventana, text = str(saldocoin2), font = ("Arial", 14),bg = blanco) 
    cantidadcoin2antes_Label.grid(row = 4, column = 1)

    cantidadcoin3antes_Label = tk.Label(cargar_ventana, text = str(saldocoin3), font = ("Arial", 14),bg = blanco) 
    cantidadcoin3antes_Label.grid(row = 5, column = 1)

    cantidadbill1antes_Label = tk.Label(cargar_ventana, text = str(saldobill1), font = ("Arial", 14),bg = blanco) 
    cantidadbill1antes_Label.grid(row = 7, column = 1)

    cantidadbill2antes_Label = tk.Label(cargar_ventana, text = str(saldobill2), font = ("Arial", 14),bg = blanco) 
    cantidadbill2antes_Label.grid(row = 8, column = 1)

    cantidadbill3antes_Label = tk.Label(cargar_ventana, text = str(saldobill3), font = ("Arial", 14),bg = blanco) 
    cantidadbill3antes_Label.grid(row = 9, column = 1)

    cantidadbill4antes_Label = tk.Label(cargar_ventana, text = str(saldobill4), font = ("Arial", 14),bg = blanco) 
    cantidadbill4antes_Label.grid(row = 10, column = 1)

    cantidadbill5antes_Label = tk.Label(cargar_ventana, text = str(saldobill5), font = ("Arial", 14),bg = blanco) 
    cantidadbill5antes_Label.grid(row = 11, column = 1)

    totalcoin1antes_Label = tk.Label(cargar_ventana, text = str(saldocoin1), font = ("Arial", 14),bg = blanco) 
    totalcoin1antes_Label.grid(row = 3, column = 1)

    totalcoin2antes_Label = tk.Label(cargar_ventana, text = str(saldocoin2), font = ("Arial", 14),bg = blanco) 
    totalcoin2antes_Label.grid(row = 4, column = 1)

    totalcoin3antes_Label = tk.Label(cargar_ventana, text = str(saldocoin3), font = ("Arial", 14),bg = blanco) 
    totalcoin3antes_Label.grid(row = 5, column = 1)

    totalmonedaantes_Label = tk.Label(cargar_ventana, text = str(saldocoin1 + saldocoin2 + saldocoin3), font = ("Arial", 14),bg = blanco) 
    totalmonedaantes_Label.grid(row = 6, column = 1)

    totalbill1antes_Label = tk.Label(cargar_ventana, text = str(saldobill1), font = ("Arial", 14),bg = blanco) 
    totalbill1antes_Label.grid(row = 7, column = 1)

    totalbill2antes_Label = tk.Label(cargar_ventana, text = str(saldobill2), font = ("Arial", 14),bg = blanco) 
    totalbill2antes_Label.grid(row = 8, column = 1)

    totalbill3antes_Label = tk.Label(cargar_ventana, text = str(saldobill3), font = ("Arial", 14),bg = blanco) 
    totalbill3antes_Label.grid(row = 9, column = 1)

    totalbill4antes_Label = tk.Label(cargar_ventana, text = str(saldobill4), font = ("Arial", 14),bg = blanco) 
    totalbill4antes_Label.grid(row = 10, column = 1)

    totalbill5antes_Label = tk.Label(cargar_ventana, text = str(saldobill5), font = ("Arial", 14),bg = blanco) 
    totalbill5antes_Label.grid(row = 11, column = 1)
   
    totalbilleteantes_Label = tk.Label(cargar_ventana, text = str(saldobill1 + saldobill2 + saldobill3 + saldobill4 + saldobill5), font = ("Arial", 14),bg = blanco) 
    totalbilleteantes_Label.grid(row = 12, column = 1)

#####

    cantidadcoin1carga_Label = tk.Label(cargar_ventana, text = str(saldocoin1), font = ("Arial", 14),bg = blanco) 
    cantidadcoin1carga_Label.grid(row = 3, column = 2)

    cantidadcoin2carga_Label = tk.Label(cargar_ventana, text = str(saldocoin2), font = ("Arial", 14),bg = blanco) 
    cantidadcoin2carga_Label.grid(row = 4, column = 2)

    cantidadcoin3carga_Label = tk.Label(cargar_ventana, text = str(saldocoin3), font = ("Arial", 14),bg = blanco) 
    cantidadcoin3carga_Label.grid(row = 5, column = 2)

    cantidadbill1carga_Label = tk.Label(cargar_ventana, text = str(saldobill1), font = ("Arial", 14),bg = blanco) 
    cantidadbill1carga_Label.grid(row = 7, column = 2)

    cantidadbill2carga_Label = tk.Label(cargar_ventana, text = str(saldobill2), font = ("Arial", 14),bg = blanco) 
    cantidadbill2carga_Label.grid(row = 8, column = 2)

    cantidadbill3carga_Label = tk.Label(cargar_ventana, text = str(saldobill3), font = ("Arial", 14),bg = blanco) 
    cantidadbill3carga_Label.grid(row = 9, column = 2)

    cantidadbill4carga_Label = tk.Label(cargar_ventana, text = str(saldobill4), font = ("Arial", 14),bg = blanco) 
    cantidadbill4carga_Label.grid(row = 10, column = 2)

    cantidadbill5carga_Label = tk.Label(cargar_ventana, text = str(saldobill5), font = ("Arial", 14),bg = blanco) 
    cantidadbill5carga_Label.grid(row = 11, column = 2)

    totalcoin1carga_Label = tk.Label(cargar_ventana, text = str(saldocoin1 * coin1), font = ("Arial", 14),bg = blanco) 
    totalcoin1carga_Label.grid(row = 3, column = 2)

    totalcoin2carga_Label = tk.Label(cargar_ventana, text = str(saldocoin2 * coin2), font = ("Arial", 14),bg = blanco) 
    totalcoin2carga_Label.grid(row = 4, column = 2)

    totalcoin3carga_Label = tk.Label(cargar_ventana, text = str(saldocoin3 * coin3), font = ("Arial", 14),bg = blanco) 
    totalcoin3carga_Label.grid(row = 5, column = 2)

    totalmonedacarga_Label = tk.Label(cargar_ventana, text = str(saldocoin1 * coin1 + saldocoin2 * coin2+ saldocoin3 * coin3), font = ("Arial", 14),bg = blanco) 
    totalmonedacarga_Label.grid(row = 6, column = 2)

    totalbill1carga_Label = tk.Label(cargar_ventana, text = str(saldobill1 * bill1), font = ("Arial", 14),bg = blanco) 
    totalbill1carga_Label.grid(row = 7, column = 2)

    totalbill2carga_Label = tk.Label(cargar_ventana, text = str(saldobill2 * bill2), font = ("Arial", 14),bg = blanco) 
    totalbill2carga_Label.grid(row = 8, column = 2)

    totalbill3carga_Label = tk.Label(cargar_ventana, text = str(saldobill3 *  bill3), font = ("Arial", 14),bg = blanco) 
    totalbill3carga_Label.grid(row = 9, column = 2)

    totalbill4carga_Label = tk.Label(cargar_ventana, text = str(saldobill4 * bill4 ), font = ("Arial", 14),bg = blanco) 
    totalbill4carga_Label.grid(row = 10, column = 2)

    totalbill5carga_Label = tk.Label(cargar_ventana, text = str(saldobill5 * bill5), font = ("Arial", 14),bg = blanco) 
    totalbill5carga_Label.grid(row = 11, column = 2)

    totalbilletecarga_Label = tk.Label(cargar_ventana, text = str(saldobill1 * bill1 + saldobill2 * bill2 + saldobill3 *  bill3+ saldobill4 * bill4 + saldobill5 * bill5), font = ("Arial", 14),bg = blanco) 
    totalbilletecarga_Label.grid(row = 12, column = 2)

# Se piden los datos a cargar:

    moneda1 = tk.StringVar()
    moneda2 = tk.StringVar()
    moneda3 = tk.StringVar()
    moneda1.set("0")
    moneda2.set("0")
    moneda3.set("0")
    billete1 = tk.IntVar()
    billete2 = tk.IntVar()
    billete3 = tk.IntVar()
    billete4 = tk.IntVar()
    billete5 = tk.IntVar()

    moneda1entry = tk.Entry(cargar_ventana, textvariable = moneda1)
    moneda1entry.grid(row = 3, column = 3)
    moneda2entry = tk.Entry(cargar_ventana, textvariable = moneda2)
    moneda2entry.grid(row = 4, column = 3)
    moneda3entry = tk.Entry(cargar_ventana, textvariable = moneda3)
    moneda3entry.grid(row = 5, column = 3)

    totalmonedacarga1_Label = tk.Label(cargar_ventana, text = "0", font = ("Arial", 14),bg = blanco) 
    totalmonedacarga1_Label.grid(row = 6, column = 3)

    def update():
        if  moneda1.get() == "":
            moneda1.set("0")
        if  moneda2.get() == "":
            moneda2.set("0")
        if  moneda3.get() == "":
            moneda3.set("0")
        totalmonedacarga1_Label['text'] = str(int(moneda1.get()) + int(moneda2.get()) + int(moneda3.get()))
        cargar_ventana.after(1,update)

    update()

    billete1entry = tk.Entry(cargar_ventana, textvariable = billete1)
    billete1entry.grid(row = 7, column = 3)
    billete2entry = tk.Entry(cargar_ventana, textvariable = billete2)
    billete2entry.grid(row = 8, column = 3)
    billete3entry = tk.Entry(cargar_ventana, textvariable = billete3)
    billete3entry.grid(row = 9, column = 3)
    billete4entry = tk.Entry(cargar_ventana, textvariable = billete4)
    billete4entry.grid(row = 10, column = 3)
    billete5entry = tk.Entry(cargar_ventana, textvariable = billete5)
    billete5entry.grid(row = 11, column = 3)
    
    cantidadcoin1carga2_Label = tk.Label(cargar_ventana, text = str(saldocoin1), font = ("Arial", 14),bg = blanco) 
    cantidadcoin1carga2_Label.grid(row = 3, column = 4)

    cantidadcoin2carga2_Label = tk.Label(cargar_ventana, text = str(saldocoin2), font = ("Arial", 14),bg = blanco) 
    cantidadcoin2carga2_Label.grid(row = 4, column = 4)

    cantidadcoin3carga2_Label = tk.Label(cargar_ventana, text = str(saldocoin3), font = ("Arial", 14),bg = blanco) 
    cantidadcoin3carga2_Label.grid(row = 5, column = 4)

    cantidadbill1carga2_Label = tk.Label(cargar_ventana, text = str(saldobill1), font = ("Arial", 14),bg = blanco) 
    cantidadbill1carga2_Label.grid(row = 7, column = 4)

    cantidadbill2carga2_Label = tk.Label(cargar_ventana, text = str(saldobill2), font = ("Arial", 14),bg = blanco) 
    cantidadbill2carga2_Label.grid(row = 8, column = 4)

    cantidadbill3carga2_Label = tk.Label(cargar_ventana, text = str(saldobill3), font = ("Arial", 14),bg = blanco) 
    cantidadbill3carga2_Label.grid(row = 9, column = 4)

    cantidadbill4carga2_Label = tk.Label(cargar_ventana, text = str(saldobill4), font = ("Arial", 14),bg = blanco) 
    cantidadbill4carga2_Label.grid(row = 10, column = 4)

    cantidadbill5carga2_Label = tk.Label(cargar_ventana, text = str(saldobill5), font = ("Arial", 14),bg = blanco) 
    cantidadbill5carga2_Label.grid(row = 11, column = 4)

    totalcoin1carga2_Label = tk.Label(cargar_ventana, text = str(saldocoin1 * coin1), font = ("Arial", 14),bg = blanco) 
    totalcoin1carga2_Label.grid(row = 3, column = 4)

    totalcoin2carga2_Label = tk.Label(cargar_ventana, text = str(saldocoin2 * coin2), font = ("Arial", 14),bg = blanco) 
    totalcoin2carga2_Label.grid(row = 4, column = 4)

    totalcoin3carga2_Label = tk.Label(cargar_ventana, text = str(saldocoin3 * coin3), font = ("Arial", 14),bg = blanco) 
    totalcoin3carga2_Label.grid(row = 5, column = 4)

    totalmonedacarga2_Label = tk.Label(cargar_ventana, text = str(saldocoin1 * coin1 + saldocoin2 * coin2+ saldocoin3 * coin3), font = ("Arial", 14),bg = blanco) 
    totalmonedacarga2_Label.grid(row = 6, column = 4)

    totalbill1carga2_Label = tk.Label(cargar_ventana, text = str(saldobill1 * bill1), font = ("Arial", 14),bg = blanco) 
    totalbill1carga2_Label.grid(row = 7, column = 4)

    totalbill2carga2_Label = tk.Label(cargar_ventana, text = str(saldobill2 * bill2), font = ("Arial", 14),bg = blanco) 
    totalbill2carga2_Label.grid(row = 8, column = 4)

    totalbill3carga2_Label = tk.Label(cargar_ventana, text = str(saldobill3 *  bill3), font = ("Arial", 14),bg = blanco) 
    totalbill3carga2_Label.grid(row = 9, column = 4)

    totalbill4carga2_Label = tk.Label(cargar_ventana, text = str(saldobill4 * bill4 ), font = ("Arial", 14),bg = blanco) 
    totalbill4carga2_Label.grid(row = 10, column = 4)

    totalbill5carga2_Label = tk.Label(cargar_ventana, text = str(saldobill5 * bill5), font = ("Arial", 14),bg = blanco) 
    totalbill5carga2_Label.grid(row = 11, column = 4)

    totalbilletecarga2_Label = tk.Label(cargar_ventana, text = str(saldobill1 * bill1 + saldobill2 * bill2 + saldobill3 *  bill3+ saldobill4 * bill4 + saldobill5 * bill5), font = ("Arial", 14),bg = blanco) 
    totalbilletecarga2_Label.grid(row = 12, column = 4)
     
    savecajero_button = tk.Button(cargar_ventana, text = "Ok", command = lambda: guardarcajero(), bg = blanco, height = 2, width = 12)
    savecajero_button.grid(row = 16, column = 0, padx = 4, pady = 4)    
    cancelcajero_button = tk.Button(cargar_ventana, text = "Cancelar", command = lambda: cerrarventana(cargar_ventana), bg = blanco, height = 2, width = 12)
    cancelcajero_button.grid(row = 16, column = 1, padx = 4, pady = 4)   
    vaciarcajero_button = tk.Button(cargar_ventana, text = "Vaciar cajero", command = lambda: cerrarventana(cargar_ventana), bg = blanco, height = 2, width = 12)
    vaciarcajero_button.grid(row = 16, column = 2, padx = 4, pady = 4)   


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


