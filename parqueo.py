from distutils.command.config import config
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from datetime import datetime
from datetime import date
from datetime import timedelta
import os
import smtplib
from fpdf import FPDF


EMAIL_ADDRESS = os.environ.get('DB_USER')
EMAIL_PASSWORD = os.environ.get('DB_PASSWORD')

def enviar_correo(subject, body):
    global configuracion
    global  EMAIL_ADDRESS
    global EMAIL_PASSWORD

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(EMAIL_ADDRESS, 'supervisor.parqueo.dgr@gmail.com', msg)

def imprimir_recibo(montoapagar, horaentrada, horasalida, tiempocobrado, placa):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size = 20)

    pdf.cell(200,10, txt = "Factura Cajero", ln = 1, align = "C")

    pdf.set_font("Arial", size = 16)

    placatext =  "Placa del vehículo: " + str(placa)
    horaentradatxt = "Fecha de entrada: " + str(horaentrada)
    horasalidatxt = "Fecha de salida: " + str(horasalida)
    tiempocobradotxt = "Tiempo cobrado: " + str(tiempocobrado)
    montocobradotxt = "Monto cobrado: " + str(montoapagar)

    pdf.cell(200,10, txt = placatext, ln = 3, align = "L")
    pdf.cell(200,10, txt = horaentradatxt, ln = 4, align = "L")
    pdf.cell(200,10, txt = horasalidatxt, ln = 5, align = "L")
    pdf.cell(200,10, txt = tiempocobradotxt, ln = 6, align = "L")
    pdf.cell(200,10, txt = montocobradotxt, ln = 7, align = "L")

    nombrepdf = "Factura_" + str(placa) + ".pdf"

    pdf.output(nombrepdf)




# Colores

blanco = "#ffffff"
negro = "#000000"
opcionColor = ("#03fca5")
select_color = "#77ff77"
wait_color = "#ff0000"

# Variables importantes

parqueo = {1:[606393, "19/06/2022 10:57:30", "", 0], 2:[54321, "17/06/2022 8:57:30", "19/06/2022 12:00:30", 30]}
detalle_de_uso = [[12345, "16/06/2022 3:23:15", "16/06/2022 3:39:31", 25.00, 2],[24132, "20/06/2022 3:23:15", "20/06/2022 3:39:31", 35.00, 2]]
ingresotarjeta = [[35.00, 24132]]

configuracion = [30, 5, 3, 'supervisor.parqueo.dgr@gmail.com', 15, 1, 5, 10, 1, 5, 10, 20, 50]
saldocoin1 = 100
saldocoin2 = 100
saldocoin3 = 100

saldobill1 = 100
saldobill2 = 100
saldobill3 = 100
saldobill4 = 100
saldobill5 = 100

entradacoin1 = saldocoin1
entradacoin2 = saldocoin2
entradacoin3 = saldocoin3

entradabill1 = saldobill1
entradabill2 = saldobill2
entradabill3 = saldobill3
entradabill4 = saldobill4
entradabill5 = saldobill5

salidacoin1 = 0
salidacoin2 = 0
salidacoin3 = 0

salidabill1 = 0
salidabill2 = 0
salidabill3 = 0
salidabill4 = 0
salidabill5 = 0



# Funciones
def cerrarventana(window):
    window.destroy()
    window.update()    





def configurar():
    if len(parqueo) > 0:
        return

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
    configurar_Label = tk.Label(configurar_ventana, text = "PARQUEO - CONFIGURACIÓN", font = ("Microsoft YaHei", 36),bg = blanco) 
    configurar_Label.grid(row = 0, column = 0)

    cantidadcar_label = tk.Label(configurar_ventana, text = "Cantidad de espacios en el parqueo (entero >= 1)", font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadcar_label.grid(row = 1, column = 0)
    car = tk.IntVar()
    cantidadcar = tk.Entry(configurar_ventana, textvariable = car)
    cantidadcar.grid(row = 1, column = 1)

    precio_Label = tk.Label(configurar_ventana, text = "Precio por hora (máximo dos decimales >= 0)", font = ("Microsoft YaHei", 14),bg = blanco) 
    precio_Label.grid(row = 2, column = 0)
    precio = tk.DoubleVar()
    precioentry = tk.Entry(configurar_ventana, textvariable = precio)
    precioentry.grid(row = 2, column = 1)


    pagomin_Label = tk.Label(configurar_ventana, text = "Pago mínimo (máximo dos decimales >= 0) ", font = ("Microsoft YaHei", 14),bg = blanco) 
    pagomin_Label.grid(row = 3, column = 0)
    minpay = tk.DoubleVar()
    pagominentry = tk.Entry(configurar_ventana, textvariable = minpay)
    pagominentry.grid(row = 3, column = 1)

    correosupervisor_Label = tk.Label(configurar_ventana, text = "Correo electrónico del supervisor", font = ("Microsoft YaHei", 14),bg = blanco) 
    correosupervisor_Label.grid(row = 4, column = 0)
    emailsuper = tk.StringVar()
    correosupervisorentry = tk.Entry(configurar_ventana, textvariable = emailsuper)
    correosupervisorentry.grid(row = 4, column = 1)

    minutosmax_Label = tk.Label(configurar_ventana, text = "Minutos máximos para salir después del pago (entero >=0)", font = ("Microsoft YaHei", 14),bg = blanco) 
    minutosmax_Label.grid(row = 5, column = 0)
    minmax = tk.IntVar()
    minmaxentry = tk.Entry(configurar_ventana, textvariable = minmax)
    minmaxentry.grid(row = 5, column = 1)

    tipomoneda_Label = tk.Label(configurar_ventana, text = "Tipos de moneda (máximo 3 tipos, enteros >= 0):", font = ("Microsoft YaHei", 14),bg = blanco) 
    tipomoneda_Label.grid(row = 6, column = 0)

    moneda1_Label = tk.Label(configurar_ventana, text = "Moneda 1, la de menor denominación (ejemplo 50)", font = ("Microsoft YaHei", 14),bg = blanco) 
    moneda1_Label.grid(row = 7, column = 0)
    moneda1 = tk.IntVar()
    moneda1entry = tk.Entry(configurar_ventana, textvariable = moneda1)
    moneda1entry.grid(row = 7, column = 1)

    moneda2_Label = tk.Label(configurar_ventana, text = "Moneda 2, denominación siguiente a la anterior (ejemplo 100)", font = ("Microsoft YaHei", 14),bg = blanco) 
    moneda2_Label.grid(row = 8, column = 0)
    moneda2 = tk.IntVar()
    moneda2entry = tk.Entry(configurar_ventana, textvariable = moneda2)
    moneda2entry.grid(row = 8, column = 1)

    moneda3_Label = tk.Label(configurar_ventana, text = "Moneda 3, denominación siguiente a la anterior (ejemplo 500)", font = ("Microsoft YaHei", 14),bg = blanco) 
    moneda3_Label.grid(row = 9, column = 0)
    moneda3 = tk.IntVar()
    moneda3entry = tk.Entry(configurar_ventana, textvariable = moneda3)
    moneda3entry.grid(row = 9, column = 1)

    tipobillete_Label = tk.Label(configurar_ventana, text = "Tipos de billetes (máximo 5 tipos, enteros >= 0):", font = ("Microsoft YaHei", 14),bg = blanco) 
    tipobillete_Label.grid(row = 10, column = 0)

    billete1_Label = tk.Label(configurar_ventana, text = "Billete 1, el de menor denominación (ejemplo 1000)", font = ("Microsoft YaHei", 14),bg = blanco) 
    billete1_Label.grid(row = 11, column = 0)
    billete1 = tk.IntVar()
    billete1entry = tk.Entry(configurar_ventana, textvariable = billete1)
    billete1entry.grid(row = 11, column = 1)

    billete2_Label = tk.Label(configurar_ventana, text = "Billete 2, denominación siguiente a la anterior (ejemplo 2000)", font = ("Microsoft YaHei", 14),bg = blanco) 
    billete2_Label.grid(row = 12, column = 0)
    billete2 = tk.IntVar()
    billete2entry = tk.Entry(configurar_ventana, textvariable = billete2)
    billete2entry.grid(row = 12, column = 1)

    billete3_Label = tk.Label(configurar_ventana, text = "Billete 3, denominación siguiente a la anterior (ejemplo 5000)", font = ("Microsoft YaHei", 14),bg = blanco) 
    billete3_Label.grid(row = 13, column = 0)
    billete3 = tk.IntVar()
    billete3entry = tk.Entry(configurar_ventana, textvariable = billete3)
    billete3entry.grid(row = 13, column = 1)

    billete4_Label = tk.Label(configurar_ventana, text = "Billete 4, denominación siguiente a la anterior (ejemplo 10000)", font = ("Microsoft YaHei", 14),bg = blanco) 
    billete4_Label.grid(row = 14, column = 0)
    billete4 = tk.IntVar()
    billete4entry = tk.Entry(configurar_ventana, textvariable = billete4)
    billete4entry.grid(row = 14, column = 1)

    billete5_Label = tk.Label(configurar_ventana, text = "Billete 5, denominación siguiente a la anterior (ejemplo 20000)", font = ("Microsoft YaHei", 14),bg = blanco) 
    billete5_Label.grid(row = 15, column = 0)
    billete5 = tk.IntVar()
    billete5entry = tk.Entry(configurar_ventana, textvariable = billete5)
    billete5entry.grid(row = 15, column = 1)


     
    saveconfig_button = tk.Button(configurar_ventana, text = "Guardar configuración", command = lambda: guardarconfig(car.get(), precio.get(), \
        minpay.get(), emailsuper.get(), minmax.get(), moneda1.get(), moneda2.get(), moneda3.get(), billete1.get(), billete2.get(), \
            billete3.get(), billete4.get(), billete5.get()), bg = blanco, height = 2, width = 20)
    saveconfig_button.grid(row = 16, column = 0, padx = 4, pady = 4)    
    cancelconfig_button = tk.Button(configurar_ventana, text = "Cancelar", command = lambda: cerrarventana(configurar_ventana), bg = blanco, height = 2, width = 12)
    cancelconfig_button.grid(row = 16, column = 1, padx = 4, pady = 4)   


def cargar():
    def guardarcajero(window):
        global saldocoin1 # Los saldos contienen la cantidad de billetes
        global saldocoin2
        global saldocoin3

        global saldobill1
        global saldobill2
        global saldobill3
        global saldobill4
        global saldobill5

        global entradacoin1
        global entradacoin2
        global entradacoin3

        global entradabill1
        global entradabill2
        global entradabill3
        global entradabill4
        global entradabill5

        saldocoin1 = int(cantidadcoin1saldo_Label['text'])
        saldocoin2 = int(cantidadcoin2saldo_Label['text']) 
        saldocoin3 = int(cantidadcoin3saldo_Label['text'])

        saldobill1 = int(cantidadbill1saldo_Label['text'] )
        saldobill2 = int(cantidadbill2saldo_Label['text'] )
        saldobill3 = int(cantidadbill3saldo_Label['text'])
        saldobill4 = int(cantidadbill4saldo_Label['text'] )
        saldobill5 = int(cantidadbill5saldo_Label['text'] )

        entradacoin1 = int(cantidadcoin1saldo_Label['text'])
        entradacoin2 = int(cantidadcoin2saldo_Label['text']) 
        entradacoin3 = int(cantidadcoin3saldo_Label['text'])

        entradabill1 = int(cantidadbill1saldo_Label['text'] )
        entradabill2 = int(cantidadbill2saldo_Label['text'] )
        entradabill3 = int(cantidadbill3saldo_Label['text'])
        entradabill4 = int(cantidadbill4saldo_Label['text'] )
        entradabill5 = int(cantidadbill5saldo_Label['text'] )

        cerrarventana(window)

    def vaciarcajero(window):
        global saldocoin1 # Los saldos contienen la cantidad de billetes
        global saldocoin2
        global saldocoin3

        global saldobill1
        global saldobill2
        global saldobill3
        global saldobill4
        global saldobill5

        saldocoin1 = 0
        saldocoin2 = 0
        saldocoin3 = 0

        saldobill1 = 0
        saldobill2 = 0
        saldobill3 = 0
        saldobill4 = 0
        saldobill5 = 0
        cerrarventana(window)

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
    cargar_Label = tk.Label(cargar_ventana, text = "PARQUEO - CARGAR CAJERO", font = ("Microsoft YaHei", 36),bg = blanco) 
    cargar_Label.grid(row = 0, column = 0, columnspan = 6)

    denominacion_label = tk.Label(cargar_ventana, text = "DENOMINACIÓN", font = ("Microsoft YaHei", 14),bg = blanco) 
    denominacion_label.grid(row = 2, column = 0)

    saldoantes_label = tk.Label(cargar_ventana, text = "SALDO ANTES DE LA CARGA", font = ("Microsoft YaHei", 14),bg = blanco) 
    saldoantes_label.grid(row = 1, column = 1, columnspan = 2)

    cantidadantes_label = tk.Label(cargar_ventana, text = "CANTIDAD", font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadantes_label.grid(row = 2, column = 1)

    totalantes_label = tk.Label(cargar_ventana, text = "TOTAL", font = ("Microsoft YaHei", 14),bg = blanco) 
    totalantes_label.grid(row = 2, column = 2)
    
    saldocarga_label = tk.Label(cargar_ventana, text = "CARGA", font = ("Microsoft YaHei", 14),bg = blanco) 
    saldocarga_label.grid(row = 1, column = 3, columnspan = 2)

    cantidadcarga_label = tk.Label(cargar_ventana, text = "CANTIDAD", font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadcarga_label.grid(row = 2, column = 3)

    totalcarga_label = tk.Label(cargar_ventana, text = "TOTAL", font = ("Microsoft YaHei", 14),bg = blanco) 
    totalcarga_label.grid(row = 2, column = 4)
    
    saldototal_label = tk.Label(cargar_ventana, text = "SALDO", font = ("Microsoft YaHei", 14),bg = blanco) 
    saldototal_label.grid(row = 1, column = 5, columnspan = 2)

    cantidadtotal_label = tk.Label(cargar_ventana, text = "CANTIDAD", font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadtotal_label.grid(row = 2, column = 5)

    totaltotal_label = tk.Label(cargar_ventana, text = "TOTAL", font = ("Microsoft YaHei", 14),bg = blanco) 
    totaltotal_label.grid(row = 2, column = 6)

    textocoin1 = "Moneda de " + str(coin1)
    moneda1_Label = tk.Label(cargar_ventana, text = textocoin1, font = ("Microsoft YaHei", 14),bg = blanco) 
    moneda1_Label.grid(row = 3, column = 0)
    

    textocoin2 = "Moneda de " + str(coin2)
    moneda2_Label = tk.Label(cargar_ventana, text = textocoin2, font = ("Microsoft YaHei", 14),bg = blanco) 
    moneda2_Label.grid(row = 4, column = 0)

    textocoin3 = "Moneda de " + str(coin3)
    moneda3_Label = tk.Label(cargar_ventana, text = textocoin3, font = ("Microsoft YaHei", 14),bg = blanco) 
    moneda3_Label.grid(row = 5, column = 0)

    totalmoneda_Label = tk.Label(cargar_ventana, text = "TOTAL DE MONEDAS", font = ("Microsoft YaHei", 14),bg = blanco) 
    totalmoneda_Label.grid(row = 6, column = 0)

    textobill1 = "Billete de " + str(bill1)
    billete1_Label = tk.Label(cargar_ventana, text = textobill1, font = ("Microsoft YaHei", 14),bg = blanco) 
    billete1_Label.grid(row = 7, column = 0)

    textobill2 = "Billete de " + str(bill2)
    billete2_Label = tk.Label(cargar_ventana, text = textobill2, font = ("Microsoft YaHei", 14),bg = blanco) 
    billete2_Label.grid(row = 8, column = 0)

    textobill3 = "Billete de " + str(bill3)
    billete3_Label = tk.Label(cargar_ventana, text = textobill3, font = ("Microsoft YaHei", 14),bg = blanco) 
    billete3_Label.grid(row = 9, column = 0)

    textobill4 = "Billete de " + str(bill4)
    billete4_Label = tk.Label(cargar_ventana, text = textobill4, font = ("Microsoft YaHei", 14),bg = blanco) 
    billete4_Label.grid(row = 10, column = 0)
    
    textobill5 = "Billete de " + str(bill5)
    billete5_Label = tk.Label(cargar_ventana, text = textobill5, font = ("Microsoft YaHei", 14),bg = blanco) 
    billete5_Label.grid(row = 11, column = 0)

    totalbillete_Label = tk.Label(cargar_ventana, text = "TOTAL DE BILLETES", font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbillete_Label.grid(row = 12, column = 0)

    totalcajero_Label = tk.Label(cargar_ventana, text = "TOTAL DE  CAJERO", font = ("Microsoft YaHei", 14),bg = blanco) 
    totalcajero_Label.grid(row = 13, column = 0)

# Empiezan los labels con los números.

    cantidadcoin1antes_Label = tk.Label(cargar_ventana, text = str(saldocoin1), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadcoin1antes_Label.grid(row = 3, column = 1)

    cantidadcoin2antes_Label = tk.Label(cargar_ventana, text = str(saldocoin2), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadcoin2antes_Label.grid(row = 4, column = 1)

    cantidadcoin3antes_Label = tk.Label(cargar_ventana, text = str(saldocoin3), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadcoin3antes_Label.grid(row = 5, column = 1)

    cantidadmonedaantes_Label = tk.Label(cargar_ventana, text = str(saldocoin1 + saldocoin2 + saldocoin3), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadmonedaantes_Label.grid(row = 6, column = 1)

    cantidadbill1antes_Label = tk.Label(cargar_ventana, text = str(saldobill1), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadbill1antes_Label.grid(row = 7, column = 1)

    cantidadbill2antes_Label = tk.Label(cargar_ventana, text = str(saldobill2), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadbill2antes_Label.grid(row = 8, column = 1)

    cantidadbill3antes_Label = tk.Label(cargar_ventana, text = str(saldobill3), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadbill3antes_Label.grid(row = 9, column = 1)

    cantidadbill4antes_Label = tk.Label(cargar_ventana, text = str(saldobill4), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadbill4antes_Label.grid(row = 10, column = 1)

    cantidadbill5antes_Label = tk.Label(cargar_ventana, text = str(saldobill5), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadbill5antes_Label.grid(row = 11, column = 1)

    cantidadbilletesantes_Label = tk.Label(cargar_ventana, text = str(saldobill1 + saldobill2 + saldobill3 + saldobill4 + saldobill5), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadbilletesantes_Label.grid(row = 12, column = 1)

    totalcoin1carga_Label = tk.Label(cargar_ventana, text = str((saldocoin1 * coin1) / 100), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalcoin1carga_Label.grid(row = 3, column = 2)

    totalcoin2carga_Label = tk.Label(cargar_ventana, text = str((saldocoin2 * coin2)/100), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalcoin2carga_Label.grid(row = 4, column = 2)

    totalcoin3carga_Label = tk.Label(cargar_ventana, text = str((saldocoin3 * coin3)/ 100), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalcoin3carga_Label.grid(row = 5, column = 2)

    totalmonedacarga_Label = tk.Label(cargar_ventana, text = str((saldocoin1 * coin1 + saldocoin2 * coin2+ saldocoin3 * coin3)/100), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalmonedacarga_Label.grid(row = 6, column = 2)

    totalbill1carga_Label = tk.Label(cargar_ventana, text = str(saldobill1 * bill1), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbill1carga_Label.grid(row = 7, column = 2)

    totalbill2carga_Label = tk.Label(cargar_ventana, text = str(saldobill2 * bill2), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbill2carga_Label.grid(row = 8, column = 2)

    totalbill3carga_Label = tk.Label(cargar_ventana, text = str(saldobill3 *  bill3), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbill3carga_Label.grid(row = 9, column = 2)

    totalbill4carga_Label = tk.Label(cargar_ventana, text = str(saldobill4 * bill4 ), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbill4carga_Label.grid(row = 10, column = 2)

    totalbill5carga_Label = tk.Label(cargar_ventana, text = str(saldobill5 * bill5), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbill5carga_Label.grid(row = 11, column = 2)

    totalbilletecarga_Label = tk.Label(cargar_ventana, text = str(saldobill1 * bill1 + saldobill2 * bill2 + saldobill3 *  bill3+ saldobill4 * bill4 + saldobill5 * bill5), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbilletecarga_Label.grid(row = 12, column = 2)

# Se piden los datos a cargar:

    moneda1 = tk.StringVar()
    moneda2 = tk.StringVar()
    moneda3 = tk.StringVar()
    moneda1.set("0")
    moneda2.set("0")
    moneda3.set("0")
    billete1 = tk.StringVar()
    billete2 = tk.StringVar()
    billete3 = tk.StringVar()
    billete4 = tk.StringVar()
    billete5 = tk.StringVar()
    billete1.set("0")
    billete2.set("0")
    billete3.set("0")
    billete4.set("0")
    billete5.set("0")

    moneda1entry = tk.Entry(cargar_ventana, textvariable = moneda1)
    moneda1entry.grid(row = 3, column = 3)
    moneda2entry = tk.Entry(cargar_ventana, textvariable = moneda2)
    moneda2entry.grid(row = 4, column = 3)
    moneda3entry = tk.Entry(cargar_ventana, textvariable = moneda3)
    moneda3entry.grid(row = 5, column = 3)

    totalmonedacarga1_Label = tk.Label(cargar_ventana, text = "0", font = ("Microsoft YaHei", 14),bg = blanco) 
    totalmonedacarga1_Label.grid(row = 6, column = 3)
    totalbilletecarga1_Label = tk.Label(cargar_ventana, text = "0", font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbilletecarga1_Label.grid(row = 12, column = 3)

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

    totalcoin1carga2_Label = tk.Label(cargar_ventana, text = "0", font = ("Microsoft YaHei", 14),bg = blanco) 
    totalcoin1carga2_Label.grid(row = 3, column = 4)

    totalcoin2carga2_Label = tk.Label(cargar_ventana, text = "0", font = ("Microsoft YaHei", 14),bg = blanco) 
    totalcoin2carga2_Label.grid(row = 4, column = 4)

    totalcoin3carga2_Label = tk.Label(cargar_ventana, text = "0", font = ("Microsoft YaHei", 14),bg = blanco) 
    totalcoin3carga2_Label.grid(row = 5, column = 4)

    totalmonedacarga2_Label = tk.Label(cargar_ventana, text ="0", font = ("Microsoft YaHei", 14),bg = blanco) 
    totalmonedacarga2_Label.grid(row = 6, column = 4)

    totalbill1carga2_Label = tk.Label(cargar_ventana, text = "0", font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbill1carga2_Label.grid(row = 7, column = 4)

    totalbill2carga2_Label = tk.Label(cargar_ventana, text = "0", font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbill2carga2_Label.grid(row = 8, column = 4)

    totalbill3carga2_Label = tk.Label(cargar_ventana, text = "0", font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbill3carga2_Label.grid(row = 9, column = 4)

    totalbill4carga2_Label = tk.Label(cargar_ventana, text = "0", font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbill4carga2_Label.grid(row = 10, column = 4)

    totalbill5carga2_Label = tk.Label(cargar_ventana, text = "0", font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbill5carga2_Label.grid(row = 11, column = 4)

    totalbilletecarga2_Label = tk.Label(cargar_ventana, text = "0", font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbilletecarga2_Label.grid(row = 12, column = 4)

######
    cantidadcoin1saldo_Label = tk.Label(cargar_ventana, text = str(saldocoin1), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadcoin1saldo_Label.grid(row = 3, column = 5)

    cantidadcoin2saldo_Label = tk.Label(cargar_ventana, text = str(saldocoin2), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadcoin2saldo_Label.grid(row = 4, column = 5)

    cantidadcoin3saldo_Label = tk.Label(cargar_ventana, text = str(saldocoin3), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadcoin3saldo_Label.grid(row = 5, column = 5)

    cantidadmonedasaldo_Label = tk.Label(cargar_ventana, text = str(saldocoin1 + saldocoin2 + saldocoin3), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadmonedasaldo_Label.grid(row = 6, column = 5)

    cantidadbill1saldo_Label = tk.Label(cargar_ventana, text = str(saldobill1), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadbill1saldo_Label.grid(row = 7, column = 5)

    cantidadbill2saldo_Label = tk.Label(cargar_ventana, text = str(saldobill2), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadbill2saldo_Label.grid(row = 8, column = 5)

    cantidadbill3saldo_Label = tk.Label(cargar_ventana, text = str(saldobill3), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadbill3saldo_Label.grid(row = 9, column = 5)

    cantidadbill4saldo_Label = tk.Label(cargar_ventana, text = str(saldobill4), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadbill4saldo_Label.grid(row = 10, column = 5)

    cantidadbill5saldo_Label = tk.Label(cargar_ventana, text = str(saldobill5), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadbill5saldo_Label.grid(row = 11, column = 5)

    cantidadbilletesaldo_Label = tk.Label(cargar_ventana, text = str(saldobill1 + saldobill2 + saldobill3 + saldobill4 + saldobill5), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadbilletesaldo_Label.grid(row = 12, column = 5)

    totalcoin1saldo_Label = tk.Label(cargar_ventana, text = str((saldocoin1 * coin1)/ 100), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalcoin1saldo_Label.grid(row = 3, column = 6)

    totalcoin2saldo_Label = tk.Label(cargar_ventana, text = str((saldocoin2 * coin2)/100), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalcoin2saldo_Label.grid(row = 4, column = 6)

    totalcoin3saldo_Label = tk.Label(cargar_ventana, text = str((saldocoin3 * coin3)/100), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalcoin3saldo_Label.grid(row = 5, column = 6)

    totalmonedasaldo_Label = tk.Label(cargar_ventana, text = str((saldocoin1 * coin1 + saldocoin2 * coin2+ saldocoin3 * coin3)/100), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalmonedasaldo_Label.grid(row = 6, column = 6)

    totalbill1saldo_Label = tk.Label(cargar_ventana, text = str(saldobill1 * bill1), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbill1saldo_Label.grid(row = 7, column = 6)

    totalbill2saldo_Label = tk.Label(cargar_ventana, text = str(saldobill2 * bill2), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbill2saldo_Label.grid(row = 8, column = 6)

    totalbill3saldo_Label = tk.Label(cargar_ventana, text = str(saldobill3 * bill3), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbill3saldo_Label.grid(row = 9, column = 6)

    totalbill4saldo_Label = tk.Label(cargar_ventana, text = str(saldobill4 * bill4), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbill4saldo_Label.grid(row = 10, column = 6)

    totalbill5saldo_Label = tk.Label(cargar_ventana, text = str(saldobill5 * bill5), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbill5saldo_Label.grid(row = 11, column = 6)

    totalbilletesaldo_Label = tk.Label(cargar_ventana, text = str(saldobill1*bill1 + saldobill2*bill2 + saldobill3*bill3 + saldobill4*bill4 + saldobill5*bill5), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbilletesaldo_Label.grid(row = 12, column = 6)

    totalcajerosaldo_Label = tk.Label(cargar_ventana, text = str((saldocoin1 * coin1 + saldocoin2 * coin2+ saldocoin3 * coin3) / 100 + saldobill1*bill1 + saldobill2*bill2 + saldobill3*bill3 + saldobill4*bill4 + saldobill5*bill5), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalcajerosaldo_Label.grid(row = 13, column = 6)


    def update():
        if  moneda1.get() == "" or  int(moneda1.get()) < 0:
            moneda1.set("0")
        if  moneda2.get() == "" or  int(moneda2.get()) < 0:
            moneda2.set("0")
        if  moneda3.get() == "" or  int(moneda3.get()) < 0:
            moneda3.set("0")
        if  billete1.get() == "" or  int(billete1.get()) < 0:
            billete1.set("0")
        if  billete2.get() == "" or  int(billete2.get()) < 0:
            billete2.set("0")
        if  billete3.get() == "" or  int(billete3.get()) < 0:
            billete3.set("0")
        if  billete4.get() == "" or  int(billete4.get()) < 0:
            billete4.set("0")
        if  billete5.get() == "" or  int(billete5.get()) < 0:
            billete5.set("0")
        totalmonedacarga1_Label['text'] = str((int(moneda1.get()) + int(moneda2.get()) + int(moneda3.get())))
        totalbilletecarga1_Label['text'] = str(int(billete1.get()) + int(billete2.get()) + int(billete3.get()) + int(billete4.get()) + int(billete5.get()))
        totalcoin1carga2_Label['text'] = str((int(moneda1.get()) *  coin1)/100)
        totalcoin2carga2_Label['text'] = str((int(moneda2.get()) *  coin2)/100)
        totalcoin3carga2_Label['text'] = str((int(moneda3.get()) *  coin3)/100)
        totalmonedacarga2_Label['text'] = str((int(moneda1.get()) *  coin1 + int(moneda2.get()) *  coin2 + int(moneda3.get()) *  coin3)/100)
        totalbill1carga2_Label['text'] = str(int(billete1.get()) *  bill1)
        totalbill2carga2_Label['text'] = str(int(billete2.get()) *  bill2)
        totalbill3carga2_Label['text'] = str(int(billete3.get()) *  bill3)
        totalbill4carga2_Label['text'] = str(int(billete4.get()) *  bill4)    
        totalbill5carga2_Label['text'] = str(int(billete5.get()) *  bill5)
        totalbilletecarga2_Label['text'] = str(int(billete1.get()) *  bill1 + int(billete2.get()) *  bill2 + int(billete3.get()) *  bill3 + int(billete4.get()) *  bill4 + int(billete5.get()) *  bill5)
        cantidadcoin1saldo_Label['text'] = str(saldocoin1 + int(moneda1.get()))
        cantidadcoin2saldo_Label['text'] = str(saldocoin2 + int(moneda2.get()))
        cantidadcoin3saldo_Label['text'] = str(saldocoin3 +  int(moneda3.get()))
        cantidadmonedasaldo_Label['text'] = str(saldocoin1 +  int(moneda1.get())+ saldocoin2 + int(moneda2.get()) + saldocoin3 +  int(moneda3.get())) 
        cantidadbill1saldo_Label['text'] = str(saldobill1 + int(billete1.get()))
        cantidadbill2saldo_Label['text'] = str(saldobill2+ int(billete2.get()))
        cantidadbill3saldo_Label['text'] = str(saldobill3 + int(billete3.get()))
        cantidadbill4saldo_Label['text'] = str(saldobill4 + int(billete4.get()))
        cantidadbill5saldo_Label['text'] = str(saldobill5 + int(billete5.get()))
        cantidadbilletesaldo_Label['text'] = str(saldobill1 + int(billete1.get()) + saldobill2+ int(billete2.get()) + saldobill3 + int(billete3.get()) + saldobill4 + int(billete4.get()) + saldobill5 + int(billete5.get()))
        totalcoin1saldo_Label['text'] = str(((saldocoin1 +  int(moneda1.get())) *coin1)/100)
        totalcoin2saldo_Label['text'] = str(((saldocoin2 +  int(moneda2.get())) *coin2)/100)
        totalcoin3saldo_Label['text'] = str(((saldocoin3 +  int(moneda3.get())) *coin3)/100)
        totalmonedasaldo_Label['text'] = str(((saldocoin1 +  int(moneda1.get())) *coin1 + (saldocoin2 +  int(moneda2.get())) *coin2 + (saldocoin3 +  int(moneda3.get())) *coin3)/100)
        totalbill1saldo_Label['text'] = str((saldobill1 + int(billete1.get())) * bill1)
        totalbill2saldo_Label['text'] = str((saldobill2 + int(billete2.get())) * bill2)
        totalbill3saldo_Label['text'] = str((saldobill3 + int(billete3.get())) * bill3)
        totalbill4saldo_Label['text'] = str((saldobill4 + int(billete4.get())) * bill4)
        totalbill5saldo_Label['text'] = str((saldobill5 + int(billete5.get())) * bill5)
        totalbilletesaldo_Label['text'] = str((saldobill1 + int(billete1.get())) * bill1 + (saldobill2+ int(billete2.get())) * bill2 + (saldobill3 + int(billete3.get())) * bill3+ (saldobill4 + int(billete4.get())) * bill4 + (saldobill5 + int(billete5.get())) * bill5)
        totalcajerosaldo_Label['text'] = str(((saldocoin1 +  int(moneda1.get())) *coin1 + (saldocoin2 +  int(moneda2.get())) *coin2 + (saldocoin3 +  int(moneda3.get())) *coin3) / 100 + \
             (saldobill1 + int(billete1.get())) * bill1 + (saldobill2 + int(billete2.get())) * \
                bill2 +  (saldobill3 + int(billete3.get())) * bill3 + (saldobill4 + int(billete4.get())) * bill4 + (saldobill5 + int(billete5.get())) * bill5)

        cargar_ventana.after(1,update)
    update()
     
    savecajero_button = tk.Button(cargar_ventana, text = "Ok", command = lambda: guardarcajero(cargar_ventana), bg = blanco, height = 2, width = 12)
    savecajero_button.grid(row = 16, column = 0, padx = 4, pady = 4)    
    cancelcajero_button = tk.Button(cargar_ventana, text = "Cancelar", command = lambda: cerrarventana(cargar_ventana), bg = blanco, height = 2, width = 12)
    cancelcajero_button.grid(row = 16, column = 1, padx = 4, pady = 4)   
    vaciarcajero_button = tk.Button(cargar_ventana, text = "Vaciar cajero", command = lambda: vaciarcajero(cargar_ventana), bg = blanco, height = 2, width = 12)
    vaciarcajero_button.grid(row = 16, column = 2, padx = 4, pady = 4)   


def saldo():
    global saldocoin1 # Los saldos contienen la cantidad de billetes
    global saldocoin2
    global saldocoin3

    global saldobill1
    global saldobill2
    global saldobill3
    global saldobill4
    global saldobill5

    global entradacoin1
    global entradacoin2
    global entradacoin3

    global entradabill1
    global entradabill2
    global entradabill3
    global entradabill4
    global entradabill5

    global salidacoin1
    global salidacoin2
    global salidacoin3

    global salidabill1
    global salidabill2
    global salidabill3
    global salidabill4
    global salidabill5

    global configuracion

    coin1 = configuracion[5]
    coin2 = configuracion[6]
    coin3 = configuracion[7]

    bill1 = configuracion[8]
    bill2 = configuracion[9]
    bill3 = configuracion[10]
    bill4 = configuracion[11]
    bill5 = configuracion[12]



    saldo_ventana = tk.Toplevel(ventana)
    saldo_ventana.title("Saldo")
    saldo_ventana.geometry("900x600")
    saldo_ventana.configure(bg = blanco)
    saldo_Label = tk.Label(saldo_ventana, text = "PARQUEO - SALDO DEL CAJERO", font = ("Microsoft YaHei", 36),bg = blanco) 
    saldo_Label.grid(row = 0, column = 0, columnspan = 6)

    denominacion_label = tk.Label(saldo_ventana, text = "DENOMINACIÓN", font = ("Microsoft YaHei", 14),bg = blanco) 
    denominacion_label.grid(row = 2, column = 0)

    saldoentrada_label = tk.Label(saldo_ventana, text = "ENTRADAS", font = ("Microsoft YaHei", 14),bg = blanco) 
    saldoentrada_label.grid(row = 1, column = 1, columnspan = 2)

    cantidadentrada_label = tk.Label(saldo_ventana, text = "CANTIDAD", font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadentrada_label.grid(row = 2, column = 1)

    totalentrada_label = tk.Label(saldo_ventana, text = "TOTAL", font = ("Microsoft YaHei", 14),bg = blanco) 
    totalentrada_label.grid(row = 2, column = 2)
    
    saldosalidas_label = tk.Label(saldo_ventana, text = "SALIDAS", font = ("Microsoft YaHei", 14),bg = blanco) 
    saldosalidas_label.grid(row = 1, column = 3, columnspan = 2)

    cantidadsalidas_label = tk.Label(saldo_ventana, text = "CANTIDAD", font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadsalidas_label.grid(row = 2, column = 3)

    totalsalidas_label = tk.Label(saldo_ventana, text = "TOTAL", font = ("Microsoft YaHei", 14),bg = blanco) 
    totalsalidas_label.grid(row = 2, column = 4)
    
    saldosaldo_label = tk.Label(saldo_ventana, text = "SALDO", font = ("Microsoft YaHei", 14),bg = blanco) 
    saldosaldo_label.grid(row = 1, column = 5, columnspan = 2)

    cantidadsaldo_label = tk.Label(saldo_ventana, text = "CANTIDAD", font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadsaldo_label.grid(row = 2, column = 5)

    totalsaldo_label = tk.Label(saldo_ventana, text = "TOTAL", font = ("Microsoft YaHei", 14),bg = blanco) 
    totalsaldo_label.grid(row = 2, column = 6)

    textocoin1 = "Moneda de " + str(coin1)
    moneda1_Label = tk.Label(saldo_ventana, text = textocoin1, font = ("Microsoft YaHei", 14),bg = blanco) 
    moneda1_Label.grid(row = 3, column = 0)
    

    textocoin2 = "Moneda de " + str(coin2)
    moneda2_Label = tk.Label(saldo_ventana, text = textocoin2, font = ("Microsoft YaHei", 14),bg = blanco) 
    moneda2_Label.grid(row = 4, column = 0)

    textocoin3 = "Moneda de " + str(coin3)
    moneda3_Label = tk.Label(saldo_ventana, text = textocoin3, font = ("Microsoft YaHei", 14),bg = blanco) 
    moneda3_Label.grid(row = 5, column = 0)

    totalmoneda_Label = tk.Label(saldo_ventana, text = "TOTAL DE MONEDAS", font = ("Microsoft YaHei", 14),bg = blanco) 
    totalmoneda_Label.grid(row = 6, column = 0)

    textobill1 = "Billete de " + str(bill1)
    billete1_Label = tk.Label(saldo_ventana, text = textobill1, font = ("Microsoft YaHei", 14),bg = blanco) 
    billete1_Label.grid(row = 7, column = 0)

    textobill2 = "Billete de " + str(bill2)
    billete2_Label = tk.Label(saldo_ventana, text = textobill2, font = ("Microsoft YaHei", 14),bg = blanco) 
    billete2_Label.grid(row = 8, column = 0)

    textobill3 = "Billete de " + str(bill3)
    billete3_Label = tk.Label(saldo_ventana, text = textobill3, font = ("Microsoft YaHei", 14),bg = blanco) 
    billete3_Label.grid(row = 9, column = 0)

    textobill4 = "Billete de " + str(bill4)
    billete4_Label = tk.Label(saldo_ventana, text = textobill4, font = ("Microsoft YaHei", 14),bg = blanco) 
    billete4_Label.grid(row = 10, column = 0)
    
    textobill5 = "Billete de " + str(bill5)
    billete5_Label = tk.Label(saldo_ventana, text = textobill5, font = ("Microsoft YaHei", 14),bg = blanco) 
    billete5_Label.grid(row = 11, column = 0)

    totalbillete_Label = tk.Label(saldo_ventana, text = "TOTAL DE BILLETES", font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbillete_Label.grid(row = 12, column = 0)

# Empiezan los labels con los números.

    cantidadcoin1entrada_Label = tk.Label(saldo_ventana, text = str(entradacoin1), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadcoin1entrada_Label.grid(row = 3, column = 1)

    cantidadcoin2entrada_Label = tk.Label(saldo_ventana, text = str(entradacoin2), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadcoin2entrada_Label.grid(row = 4, column = 1)

    cantidadcoin3entrada_Label = tk.Label(saldo_ventana, text = str(entradacoin3), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadcoin3entrada_Label.grid(row = 5, column = 1)

    cantidadmonedaentrada_Label = tk.Label(saldo_ventana, text = str(entradacoin1 + entradacoin2 + entradacoin3), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadmonedaentrada_Label.grid(row = 6, column = 1)

    cantidadbill1entrada_Label = tk.Label(saldo_ventana, text = str(entradabill1), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadbill1entrada_Label.grid(row = 7, column = 1)

    cantidadbill2entrada_Label = tk.Label(saldo_ventana, text = str(entradabill2), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadbill2entrada_Label.grid(row = 8, column = 1)

    cantidadbill3entrada_Label = tk.Label(saldo_ventana, text = str(entradabill3), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadbill3entrada_Label.grid(row = 9, column = 1)

    cantidadbill4entrada_Label = tk.Label(saldo_ventana, text = str(entradabill4), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadbill4entrada_Label.grid(row = 10, column = 1)

    cantidadbill5entrada_Label = tk.Label(saldo_ventana, text = str(entradabill5), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadbill5entrada_Label.grid(row = 11, column = 1)

    cantidadbilletesentrada_Label = tk.Label(saldo_ventana, text = str(entradabill1 + entradabill2 +entradabill3 +entradabill4 +entradabill5), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadbilletesentrada_Label.grid(row = 12, column = 1)

    totalcoin1entrada_Label = tk.Label(saldo_ventana, text = str((entradacoin1 * coin1)/100), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalcoin1entrada_Label.grid(row = 3, column = 2)

    totalcoin2entrada_Label = tk.Label(saldo_ventana, text = str((entradacoin2 * coin2)/100), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalcoin2entrada_Label.grid(row = 4, column = 2)

    totalcoin3entrada_Label = tk.Label(saldo_ventana, text = str((entradacoin3 * coin3)/100), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalcoin3entrada_Label.grid(row = 5, column = 2)

    totalmonedaentrada_Label = tk.Label(saldo_ventana, text = str((entradacoin1 * coin1 + saldocoin2 * coin2+ saldocoin3 * coin3)/100), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalmonedaentrada_Label.grid(row = 6, column = 2)

    totalbill1entrada_Label = tk.Label(saldo_ventana, text = str(entradabill1 * bill1), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbill1entrada_Label.grid(row = 7, column = 2)

    totalbill2entrada_Label = tk.Label(saldo_ventana, text = str(entradabill2 * bill2), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbill2entrada_Label.grid(row = 8, column = 2)

    totalbill3entrada_Label = tk.Label(saldo_ventana, text = str(entradabill3 *  bill3), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbill3entrada_Label.grid(row = 9, column = 2)

    totalbill4entrada_Label = tk.Label(saldo_ventana, text = str(entradabill4 * bill4 ), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbill4entrada_Label.grid(row = 10, column = 2)

    totalbill5entrada_Label = tk.Label(saldo_ventana, text = str(entradabill5 * bill5), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbill5entrada_Label.grid(row = 11, column = 2)

    totalbilleteentrada_Label = tk.Label(saldo_ventana, text = str(entradabill1 * bill1 +entradabill2 * bill2 + entradabill3 *  bill3+ entradabill4 * bill4 + entradabill5 * bill5), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbilleteentrada_Label.grid(row = 12, column = 2)

# Se dan los datos de las salidas:

    cantidadcoin1salida_Label = tk.Label(saldo_ventana, text = str(salidacoin1), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadcoin1salida_Label.grid(row = 3, column = 3)

    cantidadcoin2salida_Label = tk.Label(saldo_ventana, text = str(salidacoin2), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadcoin2salida_Label.grid(row = 4, column = 3)

    cantidadcoin3salida_Label = tk.Label(saldo_ventana, text = str(salidacoin3), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadcoin3salida_Label.grid(row = 5, column = 3)

    cantidadmonedasalida_Label = tk.Label(saldo_ventana, text = str(salidacoin1 + salidacoin2 + salidacoin3), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadmonedasalida_Label.grid(row = 6, column = 3)

    cantidadbill1salida_Label = tk.Label(saldo_ventana, text = str(salidabill1), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadbill1salida_Label.grid(row = 7, column = 3)

    cantidadbill2salida_Label = tk.Label(saldo_ventana, text = str(salidabill2), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadbill2salida_Label.grid(row = 8, column = 3)

    cantidadbill3salida_Label = tk.Label(saldo_ventana, text = str(salidabill3), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadbill3salida_Label.grid(row = 9, column = 3)

    cantidadbill4salida_Label = tk.Label(saldo_ventana, text = str(salidabill4), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadbill4salida_Label.grid(row = 10, column = 3)

    cantidadbill5salida_Label = tk.Label(saldo_ventana, text = str(salidabill5), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadbill5salida_Label.grid(row = 11, column = 3)

    cantidadbilletessalida_Label = tk.Label(saldo_ventana, text = str(salidabill1 + salidabill2 +salidabill3 +salidabill4 +salidabill5), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadbilletessalida_Label.grid(row = 12, column = 3)

    totalcoin1salida_Label = tk.Label(saldo_ventana, text = str((salidacoin1 * coin1)/100), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalcoin1salida_Label.grid(row = 3, column = 4)

    totalcoin2salida_Label = tk.Label(saldo_ventana, text = str((salidacoin2 * coin2)/100), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalcoin2salida_Label.grid(row = 4, column = 4)

    totalcoin3salida_Label = tk.Label(saldo_ventana, text = str((salidacoin3 * coin3)/100), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalcoin3salida_Label.grid(row = 5, column = 4)

    totalmonedasalida_Label = tk.Label(saldo_ventana, text = str((salidacoin1 * coin1 + salidacoin2 * coin2+ salidacoin3 * coin3)/100), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalmonedasalida_Label.grid(row = 6, column = 4)

    totalbill1salida_Label = tk.Label(saldo_ventana, text = str(salidabill1 * bill1), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbill1salida_Label.grid(row = 7, column = 4)

    totalbill2salida_Label = tk.Label(saldo_ventana, text = str(salidabill2 * bill2), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbill2salida_Label.grid(row = 8, column = 4)

    totalbill3salida_Label = tk.Label(saldo_ventana, text = str(salidabill3 *  bill3), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbill3salida_Label.grid(row = 9, column = 4)

    totalbill4salida_Label = tk.Label(saldo_ventana, text = str(salidabill4 * bill4 ), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbill4salida_Label.grid(row = 10, column = 4)

    totalbill5salida_Label = tk.Label(saldo_ventana, text = str(salidabill5 * bill5), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbill5salida_Label.grid(row = 11, column = 4)

    totalbilletesalida_Label = tk.Label(saldo_ventana, text = str(salidabill1 * bill1 +salidabill2 * bill2 + salidabill3 *  bill3+ salidabill4 * bill4 + salidabill5 * bill5), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbilletesalida_Label.grid(row = 12, column = 4)

######
    cantidadcoin1saldo_Label = tk.Label(saldo_ventana, text = str(saldocoin1), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadcoin1saldo_Label.grid(row = 3, column = 5)

    cantidadcoin2saldo_Label = tk.Label(saldo_ventana, text = str(saldocoin2), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadcoin2saldo_Label.grid(row = 4, column = 5)

    cantidadcoin3saldo_Label = tk.Label(saldo_ventana, text = str(saldocoin3), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadcoin3saldo_Label.grid(row = 5, column = 5)

    cantidadmonedasaldo_Label = tk.Label(saldo_ventana, text = str(saldocoin1 + saldocoin2 + saldocoin3), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadmonedasaldo_Label.grid(row = 6, column = 5)

    cantidadbill1saldo_Label = tk.Label(saldo_ventana, text = str(saldobill1), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadbill1saldo_Label.grid(row = 7, column = 5)

    cantidadbill2saldo_Label = tk.Label(saldo_ventana, text = str(saldobill2), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadbill2saldo_Label.grid(row = 8, column = 5)

    cantidadbill3saldo_Label = tk.Label(saldo_ventana, text = str(saldobill3), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadbill3saldo_Label.grid(row = 9, column = 5)

    cantidadbill4saldo_Label = tk.Label(saldo_ventana, text = str(saldobill4), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadbill4saldo_Label.grid(row = 10, column = 5)

    cantidadbill5saldo_Label = tk.Label(saldo_ventana, text = str(saldobill5), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadbill5saldo_Label.grid(row = 11, column = 5)

    cantidadbilletesaldo_Label = tk.Label(saldo_ventana, text = str(saldobill1 + saldobill2 + saldobill3 + saldobill4 + saldobill5), font = ("Microsoft YaHei", 14),bg = blanco) 
    cantidadbilletesaldo_Label.grid(row = 12, column = 5)

    totalcoin1saldo_Label = tk.Label(saldo_ventana, text = str((saldocoin1 * coin1)/100), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalcoin1saldo_Label.grid(row = 3, column = 6)

    totalcoin2saldo_Label = tk.Label(saldo_ventana, text = str((saldocoin2 * coin2)/100), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalcoin2saldo_Label.grid(row = 4, column = 6)

    totalcoin3saldo_Label = tk.Label(saldo_ventana, text = str((saldocoin3 * coin3)/100), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalcoin3saldo_Label.grid(row = 5, column = 6)

    totalmonedasaldo_Label = tk.Label(saldo_ventana, text = str((saldocoin1 * coin1 + saldocoin2 * coin2+ saldocoin3 * coin3)/100), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalmonedasaldo_Label.grid(row = 6, column = 6)

    totalbill1saldo_Label = tk.Label(saldo_ventana, text = str(saldobill1 * bill1), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbill1saldo_Label.grid(row = 7, column = 6)

    totalbill2saldo_Label = tk.Label(saldo_ventana, text = str(saldobill2 * bill2), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbill2saldo_Label.grid(row = 8, column = 6)

    totalbill3saldo_Label = tk.Label(saldo_ventana, text = str(saldobill3 * bill3), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbill3saldo_Label.grid(row = 9, column = 6)

    totalbill4saldo_Label = tk.Label(saldo_ventana, text = str(saldobill4 * bill4), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbill4saldo_Label.grid(row = 10, column = 6)

    totalbill5saldo_Label = tk.Label(saldo_ventana, text = str(saldobill5 * bill5), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbill5saldo_Label.grid(row = 11, column = 6)

    totalbilletesaldo_Label = tk.Label(saldo_ventana, text = str(saldobill1*bill1 + saldobill2*bill2 + saldobill3*bill3 + saldobill4*bill4 + saldobill5*bill5), font = ("Microsoft YaHei", 14),bg = blanco) 
    totalbilletesaldo_Label.grid(row = 12, column = 6)

    oksaldo_button = tk.Button(saldo_ventana, text = "OK", command = lambda: cerrarventana(saldo_ventana), bg = blanco, height = 2, width = 12)
    oksaldo_button.grid(row = 16, column = 0, padx = 4, pady = 4)  

def ingreso():

    def calcularingreso(fechainicio,fechafin):
        global parqueo
        global ingresotarjeta
        global detalle_de_uso
        print("fechafin", fechafin)
        ingresosefectivo = 0
        ingresostarjeta = 0
        ingresosestimados = 0
        fechainicio = fechainicio.split("/")
        dia1 = fechainicio[0]
        mes1 = fechainicio[1]
        year1 = fechainicio[2]
        fechainicio = str(dia1) +"/" + str(mes1) + "/"+ str(year1)
        while fechainicio != fechafin:
            print("fecha inicio", fechainicio)
            for elem in parqueo:
                print("parqueo elem",parqueo[elem])
                print(parqueo[elem][2])
                if parqueo[elem][2]!= "":
                    fecha = parqueo[elem][1].split()
                    fecha = fecha[0]
                    if fecha == fechainicio:
                        if parqueo[elem][3] != 0:
                            j = 0
                            while j < len(ingresotarjeta):
                                if parqueo[elem][0] == ingresotarjeta[j][1]:
                                    ingresostarjeta += parqueo[elem][3]
                                    break
                                j += 1
                            if j == len(ingresotarjeta):
                                ingresosefectivo += parqueo[elem][3]
            for carro in detalle_de_uso:
                print(carro)
                if carro[2] != "":
                    fecha = carro[2].split()
                    fecha = fecha[0]
                    if fecha == fechainicio:
                        if carro[3] != 0:
                            j = 0
                            while j < len(ingresotarjeta):
                                if carro[0] == ingresotarjeta[j][1]:
                                    ingresostarjeta += carro[3]
                                    break
                                j += 1
                            if j == len(ingresotarjeta):
                                ingresosefectivo += carro[3]
            nuevafecha = date(int(year1), int(mes1), int(dia1))
            nuevafecha += timedelta(days = 1)
            fechainicio = nuevafecha.strftime("%d/%m/%Y")
            fechainicio = fechainicio.split("/")
            dia1 = fechainicio[0]
            mes1 = fechainicio[1]
            year1 = fechainicio[2]
            fechainicio = str(dia1) +"/" + str(mes1) + "/"+ str(year1)

        totalefectivonum_Label['text'] = ingresosefectivo
        totaltarjetanum_Label['text'] = ingresostarjeta
        totalingresosnum_Label['text'] = (ingresostarjeta + ingresosefectivo)


        for elem in parqueo:
            montoestimado = 0
            print("parqueo elem estimado",parqueo[elem])
            print(parqueo[elem][2])
            if parqueo[elem][2] == "":
                fecha = parqueo[elem][1]
                fechalista = fecha.split()
                fecha = fechalista[0].split("/")
                tiempo=fechalista[1].split(":")
                date1 = datetime(int(fecha[2]), int(fecha[1]), int(fecha[0]), int(tiempo[0]), int(tiempo[1]), int(tiempo[2]))
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                fechalista = dt_string.split()
                fecha2 = fechalista[0].split("/")
                tiempo2=fechalista[1].split(":")
                date2 = datetime(int(fecha2[2]), int(fecha2[1]), int(fecha2[0]), int(tiempo2[0]), int(tiempo2[1]), int(tiempo2[2]))
                print(date1)
                print(date2)
                difference = date2 - date1
                print(difference)
                difference = difference.total_seconds() / 60
                if difference < 60:
                    montoestimado = configuracion[2]
                else:
                    montoestimado = configuracion[1] / 60 * difference
                    montoestimado = "{:.2f}".format(montoestimado)
                    montoestimado= float(montoestimado)
            ingresosestimados += montoestimado
        estimadosingresosnum_Label['text'] = ingresosestimados
                



    ingreso_ventana = tk.Toplevel(ventana)
    ingreso_ventana.title("Ingreso")
    ingreso_ventana.geometry("900x600")
    ingreso_ventana.configure(bg = blanco)
    ingreso_Label = tk.Label(ingreso_ventana, text = "PARQUEO - INGRESOS DE DINERO", font = ("Microsoft YaHei", 20),bg = blanco) 
    ingreso_Label.grid(row = 0, column = 0,columnspan = 2)

    deldia_Label = tk.Label(ingreso_ventana, text = "Del día", font = ("Microsoft YaHei", 14),bg = blanco) 
    deldia_Label.grid(row = 1, column = 0)
    aldia_Label = tk.Label(ingreso_ventana, text = "Al día", font = ("Microsoft YaHei", 14),bg = blanco) 
    aldia_Label.grid(row = 2, column = 0)

    fechainicio = tk.StringVar()
    fechainicio.set("dd/mm/aaaa")
    fechafin = tk.StringVar()
    fechafin.set("dd/mm/aaaa")

    fechainentry = tk.Entry(ingreso_ventana, textvariable = fechainicio)
    fechainentry.grid(row = 1, column = 1)
    fechafinentry = tk.Entry(ingreso_ventana, textvariable = fechafin)
    fechafinentry.grid(row = 2, column = 1)
    totalefectivo_Label = tk.Label(ingreso_ventana, text = "TOTAL DE INGRESOS EN EFECTIVO", font = ("Microsoft YaHei", 14),bg = blanco) 
    totalefectivo_Label.grid(row = 3, column = 0)
    totaltarjeta_Label = tk.Label(ingreso_ventana, text = "TOTAL DE INGRESOS EN TARJETA", font = ("Microsoft YaHei", 14),bg = blanco) 
    totaltarjeta_Label.grid(row = 4, column = 0)
    totalingresos_Label = tk.Label(ingreso_ventana, text = "TOTAL DE INGRESOS POR RECIBIR", font = ("Microsoft YaHei", 14),bg = blanco) 
    totalingresos_Label.grid(row = 5, column = 0)
    estimadosingresos_Label = tk.Label(ingreso_ventana, text = "ESTIMADO DE INGRESOS POR RECIBIR", font = ("Microsoft YaHei", 14),bg = blanco) 
    estimadosingresos_Label.grid(row = 6, column = 0)

    totalefectivonum_Label = tk.Label(ingreso_ventana, text = "X", font = ("Microsoft YaHei", 14),bg = blanco) 
    totalefectivonum_Label.grid(row = 3, column = 1)
    totaltarjetanum_Label = tk.Label(ingreso_ventana, text = "X", font = ("Microsoft YaHei", 14),bg = blanco) 
    totaltarjetanum_Label.grid(row = 4, column = 1)
    totalingresosnum_Label = tk.Label(ingreso_ventana, text = "X", font = ("Microsoft YaHei", 14),bg = blanco) 
    totalingresosnum_Label.grid(row = 5, column = 1)
    estimadosingresosnum_Label = tk.Label(ingreso_ventana, text = "X", font = ("Microsoft YaHei", 14),bg = blanco) 
    estimadosingresosnum_Label.grid(row = 6, column = 1)

    okingreso_button = tk.Button(ingreso_ventana, text = "Cancelar", command = lambda: cerrarventana(ingreso_ventana), bg = blanco, height = 2, width = 12)
    okingreso_button.grid(row = 16, column = 1, padx = 4, pady = 4)  
    calcularingreso_button = tk.Button(ingreso_ventana, text = "Calcular", command = lambda: calcularingreso(fechainicio.get(),fechafin.get()), bg = blanco, height = 2, width = 12)
    calcularingreso_button.grid(row = 16, column = 0, padx = 4, pady = 4)  

def entrada():
    global configuracion
    global parqueo
    def guardarvehiculo(window, placa, hora, campo, espacios):
        global parqueo
        if espacios == False:
            messagebox.showinfo("Error", "NO HAY ESPACIO") # Se despliega un error si no es válido
            cerrarventana(window)
            return
        else:
            vehiculo = [placa, hora, "", ""]
            parqueo[campo] = vehiculo
            cerrarventana(window)
    entrada_ventana = tk.Toplevel(ventana)
    entrada_ventana.title("Entrada")
    entrada_ventana.geometry("900x600")
    entrada_ventana.configure(bg = blanco)
    entrada_Label = tk.Label(entrada_ventana, text = "PARQUEO - ENTRADA DE VEHÍCULO", font = ("Microsoft YaHei", 20),bg = blanco) 
    entrada_Label.grid(row = 0, column = 0,columnspan = 2)
    campoasignado = -1
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    espacios = False
    
    espacios_Label = tk.Label(entrada_ventana, text = "", font = ("Microsoft YaHei", 14),bg = blanco) 
    espacios_Label.grid(row = 1, column = 0)

    if (configuracion[0] - len(parqueo)) > 0:
        i = 1
        while i <= configuracion[0]:
            if i in parqueo:
                i += 1
            else:
                campoasignado = i
                espacios_Label.config(text = "Espacios disponibles: " + str(configuracion[0] - len(parqueo)))
                espacios = True
                break
    else:
        espacios_Label.config(text = "NO HAY ESPACIO", fg = "#bf0f02")


    
    placa_Label = tk.Label(entrada_ventana, text = "SU PLACA", font = ("Microsoft YaHei", 14),bg = blanco) 
    placa_Label.grid(row = 2, column = 0)

    placa = tk.IntVar()


    placaentry = tk.Entry(entrada_ventana, textvariable = placa)
    placaentry.grid(row = 2, column = 1)

    
    campo_Label = tk.Label(entrada_ventana, text = "Campo asignado", font = ("Microsoft YaHei", 14),bg = blanco) 
    campo_Label.grid(row = 3, column = 0)
    campoasignado_Label = tk.Label(entrada_ventana, text = campoasignado, font = ("Microsoft YaHei", 14),bg = blanco) 
    campoasignado_Label.grid(row = 3, column = 1)
    horaentrada_Label = tk.Label(entrada_ventana, text = "Hora de entrada", font = ("Microsoft YaHei", 14),bg = blanco) 
    horaentrada_Label.grid(row = 4, column = 0)
    hora_Label = tk.Label(entrada_ventana, text = dt_string, font = ("Microsoft YaHei", 14),bg = blanco) 
    hora_Label.grid(row = 4, column = 1)
    preciohora_Label = tk.Label(entrada_ventana, text = "Precio por hora", font = ("Microsoft YaHei", 14),bg = blanco) 
    preciohora_Label.grid(row = 5, column = 0)
    preciohour_Label = tk.Label(entrada_ventana, text = configuracion[1], font = ("Microsoft YaHei", 14),bg = blanco) 
    preciohour_Label.grid(row = 5, column = 1)

    okentrada_button = tk.Button(entrada_ventana, text = "OK", command = lambda: guardarvehiculo(entrada_ventana, placa, dt_string, campoasignado, espacios), bg = blanco, height = 2, width = 12)
    okentrada_button.grid(row = 6, column = 0, padx = 4, pady = 4)  
    cancelarentrada_button = tk.Button(entrada_ventana, text = "Cancelar", command = lambda: cerrarventana(entrada_ventana), bg = blanco, height = 2, width = 12)
    cancelarentrada_button.grid(row = 6, column = 1, padx = 4, pady = 4)

def cajero():
    def selectplate(placa):
        global parqueo
        global configuracion
        global montoapagar
        global tiempocobrado
        i = 0
        while i <= len(parqueo) and montoapagar == -1:
            if i in parqueo:
                if parqueo[i][0] == placa:
                    
                    fecha = parqueo[i][1]
                    fechalista = fecha.split()
                    fecha = fechalista[0].split("/")
                    tiempo=fechalista[1].split(":")
                    date1 = datetime(int(fecha[2]), int(fecha[1]), int(fecha[0]), int(tiempo[0]), int(tiempo[1]), int(tiempo[2]))
                    now = datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    fechalista = dt_string.split()
                    fecha2 = fechalista[0].split("/")
                    tiempo2=fechalista[1].split(":")
                    date2 = datetime(int(fecha2[2]), int(fecha2[1]), int(fecha2[0]), int(tiempo2[0]), int(tiempo2[1]), int(tiempo2[2]))
                    print(date1)
                    print(date2)
                    tiempocobrado = date2 - date1
                    print(tiempocobrado)
                    tiempo1_label['text'] = parqueo[i][1]
                    tiempo2_label['text'] = dt_string
                    tiempousado_label['text'] = str(tiempocobrado)
                    difference = tiempocobrado.total_seconds() / 60
                    if difference < 60:
                        montoapagar = configuracion[2]
                    else:
                        montoapagar = configuracion[1] / 60 * difference
                        montoapagar = "{:.2f}".format(montoapagar)
                        montoapagar= float(montoapagar)
                    apagarmonto_label['text'] = montoapagar
                     
                    break
            i += 1        
        if i > len(parqueo):
            print(parqueo)
            print(detalle_de_uso)
            messagebox.showinfo("Error", "ESA PLACA NO ESTÁ EN EL PARQUEO") # Se despliega un error si no es válido   

    def vuelto():
        global pagado
        global configuracion
        global montoporpagar
        global saldocoin1 # Los saldos contienen la cantidad de billetes
        global saldocoin2
        global saldocoin3

        global saldobill1
        global saldobill2
        global saldobill3
        global saldobill4
        global saldobill5   

        global salidacoin1
        global salidacoin2
        global salidacoin3

        global salidabill1
        global salidabill2
        global salidabill3
        global salidabill4
        global salidabill5

        coin1 = configuracion[5]
        coin2 = configuracion[6]
        coin3 = configuracion[7]

        bill1 = configuracion[8]
        bill2 = configuracion[9]
        bill3 = configuracion[10]
        bill4 = configuracion[11]
        bill5 = configuracion[12]

        print(pagado)
        print(montoapagar)
        vuelto = pagado - montoapagar
        print(vuelto)
        vuelto = "{:.2f}".format(vuelto)
        vuelto = vuelto.split(".")
        entero = int(vuelto[0])
        decimal = int(vuelto[1])
        print(entero, decimal)
        if saldobill5 > 0:
            vueltobill5 = entero  //  bill5
            if vueltobill5 >= saldobill5:
                vueltobill5 = saldobill5
            entero -= (vueltobill5 * bill5)
            saldobill5 -= vueltobill5
            salidabill5 += vueltobill5
        else:
            vueltobill5 = 0

        if saldobill4 > 0:
            vueltobill4 = entero  //  bill4
            if vueltobill4 >= saldobill4:
                vueltobill4 = saldobill4
            entero -= (vueltobill4 * bill4)
            saldobill4 -= vueltobill4
            salidabill4+= vueltobill4
        else:
            vueltobill4 = 0

        if saldobill3 > 0:
            vueltobill3 = entero  //  bill3
            if vueltobill3 >= saldobill3:
                vueltobill3 = saldobill3
            entero -= (vueltobill3 * bill3)
            saldobill3 -= vueltobill3
            salidabill3 += vueltobill3
        else:
            vueltobill3 = 0

        if saldobill2 > 0:
            vueltobill2 = entero  //  bill2
            if vueltobill2 >= saldobill2:
                vueltobill2 = saldobill2
            entero -= (vueltobill2 * bill2)
            saldobill2 -= vueltobill2
            salidabill2 += vueltobill2
        else:
            vueltobill2 = 0

        if saldobill1 > 0:
            vueltobill1 = entero  //  bill1
            if vueltobill1 >= saldobill1:
                vueltobill1 = saldobill1
            entero -= (vueltobill1 * bill1)
            saldobill1 -= vueltobill1
            salidabill1 += vueltobill1
        else:
            vueltobill1 = 0
        print(entero)
        if saldocoin3 > 0:
            vueltocoin3 = decimal  //  (coin3)
            if vueltocoin3 >= saldocoin3:
                vueltocoin3 = saldocoin3
            decimal -= (vueltocoin3 * (coin3))
            saldocoin3 -= vueltocoin3
            salidacoin3 += vueltocoin3
        else:
            vueltocoin3 = 0

        if saldocoin2 > 0:
            vueltocoin2 = decimal  //  (coin2)
            if vueltocoin2 >= saldocoin2:
                vueltocoin2 = saldocoin2
            decimal -= (vueltocoin2 * (coin2))
            saldocoin2 -= vueltocoin2
            salidacoin2 += vueltocoin2
        else:
            vueltocoin2 = 0

        if saldocoin1> 0:
            vueltocoin1 = decimal  //  (coin1)
            if vueltocoin1 >= saldocoin1:
                vueltocoin1 = saldocoin1
            decimal -= (vueltocoin1 *  (coin1))
            saldocoin1 -= vueltocoin1
            salidacoin1 += vueltocoin1
        else:
            vueltocoin1 = 0

        print(decimal)
        print(vueltobill5)
        print(vueltobill4)
        print(vueltobill3)
        print(vueltobill2)
        print(vueltobill1)
        print(vueltocoin3)
        print(vueltocoin2)
        print(vueltocoin1)
        vuelto = entero + decimal / 100
        print(vuelto)
        if vuelto > 0:
            messagebox.showinfo("Error", "NO SE PUEDE DAR EL CAMBIO. SE ENVIÓ UN MENSAJE AL SUPERVISOR.") # Se despliega un error si no es válido   
            enviar_correo('Insuficientes fondos en el cajero', 'No hay suficientes fondos en el cajero para devolver un cambio. Favor ir a cargar el cajero')
            anular_pago(cajero_ventana)
            return False

        if  saldocoin1 < 5:
            correotexto = 'Hay poca cantidad de monedas de ' + str(coin1)
            enviar_correo(correotexto, correotexto)
        if  saldocoin2 < 5:
            correotexto = 'Hay poca cantidad de monedas de ' + str(coin2)
            enviar_correo(correotexto, correotexto)
        if  saldocoin3 < 5:
            correotexto = 'Hay poca cantidad de monedas de ' + str(coin3)
            enviar_correo(correotexto, correotexto)
        if  saldobill1 < 5:
            correotexto = 'Hay poca cantidad de billetes de ' + str(bill1)
            enviar_correo(correotexto, correotexto)
        if  saldobill2 < 5:
            correotexto = 'Hay poca cantidad de billetes de ' + str(bill2)
            enviar_correo(correotexto, correotexto)
        if  saldobill3 < 5:
            correotexto = 'Hay poca cantidad de billetes de ' + str(bill3)
            enviar_correo(correotexto, correotexto)
        if  saldobill4 < 5:
            correotexto = 'Hay poca cantidad de billetes de ' + str(bill4)
            enviar_correo(correotexto, correotexto)
        if  saldobill5 < 5:
            correotexto = 'Hay poca cantidad de billetes de ' + str(bill5)
            enviar_correo(correotexto, correotexto)
    
    
        coin1cambio_label['text'] = str(vueltocoin1) + " de " + str(coin1)

        coin2cambio_label['text'] = str(vueltocoin2) + " de " + str(coin2)

        coin3cambio_label['text'] = str(vueltocoin3) + " de " + str(coin3)

        bill1cambio_label['text'] = str(vueltobill1) + " de " + str(bill1)

        bill2cambio_label['text'] = str(vueltobill2) + " de " + str(bill2)

        bill3cambio_label['text'] = str(vueltobill3) + " de " + str(bill3)

        bill4cambio_label['text'] = str(vueltobill4) + " de " + str(bill4)

        bill5cambio_label['text'] = str(vueltobill5) + " de " + str(bill5)

        if  (vueltocoin3 * coin3+ vueltocoin2 * coin2+ vueltocoin1 * coin1) >= 10:
            cambiomonto_label['text'] = str(vueltobill5 * bill5 + vueltobill4 * bill4 + vueltobill3 * bill3 + vueltobill2 * bill2 + vueltobill1 * bill1) +"." + str(vueltocoin3 * coin3+ vueltocoin2 * coin2+ vueltocoin1 * coin1)
        else:
            cambiomonto_label['text'] = str(vueltobill5 * bill5 + vueltobill4 * bill4 + vueltobill3 * bill3 + vueltobill2 * bill2 + vueltobill1 * bill1) +".0" + str(vueltocoin3 * coin3+ vueltocoin2 * coin2+ vueltocoin1 * coin1)
    
    def pagar(denominacion, tipo,placa):
        global montoapagar
        global configuracion
        global parqueo
        global pagado
        global tiempocobrado

        global saldocoin1 # Los saldos contienen la cantidad de billetes
        global saldocoin2
        global saldocoin3

        global saldobill1
        global saldobill2
        global saldobill3
        global saldobill4
        global saldobill5

        if montoapagar == -1:
            return      
        if tipo == "C":
            pagado += (denominacion / 100)
            pagado = "{:.2f}".format(pagado)
            pagado= float(pagado)
        elif tipo == "B":
            pagado += denominacion
        
        pagadomonto_label['text'] = pagado
        i = 0
        if pagado >= montoapagar:
            while i <= len(parqueo):
                if i in parqueo:
                    if parqueo[i][0] == placa:
                        print(parqueo[i][2])
                        if  parqueo[i][2] == "":
                            now = datetime.now()
                            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                            parqueo[i][2] = dt_string
                            parqueo[i][3] = montoapagar
                            sepuede = vuelto()
                            if sepuede == False:
                                return
                            
                            print(parqueo)
                            messagebox.showinfo("Éxito", "SE HA REGISTRADO SU PAGO") # Se despliega un error si no es válido
                            imprimir_recibo(montoapagar, parqueo[i][1], dt_string, tiempocobrado, placa)
                            montoapagar = -1
                        else:
                            messagebox.showinfo("Error", "ESTA PLACA YA PAGÓ") # Se despliega un error si no es válido
                            return
                        break
                i += 1        
            if i > len(parqueo):
                print(parqueo)
                print(detalle_de_uso)
                messagebox.showinfo("Error", "ESA PLACA NO ESTÁ EN EL PARQUEO") # Se despliega un error si no es válido   
    
    def pagartarjeta(placa, tarjeta):
        global pagado
        global montoapagar
        global configuracion
        global parqueo
        global ingresotarjeta

        if tarjeta == "":
            return

        if montoapagar == -1:
            return      

        pagado = montoapagar
        print("t", pagado)
        print("t",montoapagar)
        pagadomonto_label['text'] = pagado
        i = 0
        if pagado >= montoapagar:
            while i <= len(parqueo):
                if i in parqueo:
                    if parqueo[i][0] == placa:
                        print(parqueo[i][2])
                        if  parqueo[i][2] == "":
                            now = datetime.now()
                            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                            parqueo[i][2] = dt_string
                            parqueo[i][3] = montoapagar
                            sepuede = vuelto()
                            if sepuede == False:
                                return
                            montoapagar = -1
                            print(parqueo)
                            ingresotarjeta.append([montoapagar, placa])
                            messagebox.showinfo("Éxito", "SE HA REGISTRADO SU PAGO") # Se despliega un error si no es válido
                        else:
                            messagebox.showinfo("Error", "ESTA PLACA YA PAGÓ") # Se despliega un error si no es válido
                            return
                        break
                i += 1        
            if i > len(parqueo):
                print(parqueo)
                print(detalle_de_uso)
                messagebox.showinfo("Error", "ESA PLACA NO ESTÁ EN EL PARQUEO") # Se despliega un error si no es válido   

    def anular_pago(window):
        cerrarventana(window)
        cajero()
    global saldocoin1 # Los saldos contienen la cantidad de billetes
    global saldocoin2
    global saldocoin3

    global saldobill1
    global saldobill2
    global saldobill3
    global saldobill4
    global saldobill5
    global configuracion
    global parqueo
    global pagado
    global montoapagar

    montoapagar= -1
    pagado = 0
    coin1 = configuracion[5]
    coin2 = configuracion[6]
    coin3 = configuracion[7]

    bill1 = configuracion[8]
    bill2 = configuracion[9]
    bill3 = configuracion[10]
    bill4 = configuracion[11]
    bill5 = configuracion[12]


    cajero_ventana = tk.Toplevel(ventana)
    cajero_ventana.title("Cajero")
    cajero_ventana.geometry("900x700")
    cajero_ventana.configure(bg = blanco)
    cajero_Label = tk.Label(cajero_ventana, text =  "CAJERO DEL PARQUEO", font = ("Microsoft YaHei", 20),bg = blanco) 
    cajero_Label.grid(row = 0, column = 0, columnspan = 2)

    pagoporhoratext = str(configuracion[1]) + " POR HORA"
    pagoporhora_label = tk.Label(cajero_ventana, text = pagoporhoratext, font = ("Microsoft YaHei", 14),bg = blanco) 
    pagoporhora_label.grid(row = 0, column = 3)
    
    paso1_label = tk.Label(cajero_ventana, text = "Paso 1: SU PLACA", font = ("Microsoft YaHei", 14),bg = blanco) 
    paso1_label.grid(row = 1, column = 0)

    placa = tk.IntVar()
    placaentry = tk.Entry(cajero_ventana, textvariable = placa)
    placaentry.grid(row = 1, column = 1)
       
    horadeentrada_label = tk.Label(cajero_ventana, text = "HORA DE ENTRADA", font = ("Microsoft YaHei", 14),bg = blanco) 
    horadeentrada_label.grid(row = 2, column = 0)
    horadesalida_label = tk.Label(cajero_ventana, text = "HORA DE SALIDA", font = ("Microsoft YaHei", 14),bg = blanco) 
    horadesalida_label.grid(row = 3, column = 0)
    tiempocobrado_label = tk.Label(cajero_ventana, text = "TIEMPO COBRADO", font = ("Microsoft YaHei", 14),bg = blanco) 
    tiempocobrado_label.grid(row = 4, column = 0)
        
    tiempo1_label = tk.Label(cajero_ventana, text = "DD/MM/AAAA HH:MM:SS", font = ("Microsoft YaHei", 14),bg = blanco) 
    tiempo1_label.grid(row = 2, column = 1)
    tiempo2_label = tk.Label(cajero_ventana, text = "DD/MM/AAAA HH:MM:SS", font = ("Microsoft YaHei", 14),bg = blanco) 
    tiempo2_label.grid(row = 3, column = 1)
    tiempousado_label = tk.Label(cajero_ventana, text = "XXh YYm ZZs", font = ("Microsoft YaHei", 14),bg = blanco) 
    tiempousado_label.grid(row = 4, column = 1)

    seleccionarplaca_button = tk.Button(cajero_ventana, text = "Seleccionar", command = lambda: selectplate(placa.get()), bg = blanco, height = 2, width = 12)
    seleccionarplaca_button.grid(row = 1, column = 2, padx = 4, pady = 4)  

    paso2_label = tk.Label(cajero_ventana, text = "Paso 2: SU PAGO EN:", font = ("Microsoft YaHei", 14),bg = blanco) 
    paso2_label.grid(row = 5, column = 0)

    monedas_label = tk.Label(cajero_ventana, text = "MONEDAS", font = ("Microsoft YaHei", 14),bg = blanco) 
    monedas_label.grid(row = 5, column = 1)

    billetes_label = tk.Label(cajero_ventana, text = "BILLETES", font = ("Microsoft YaHei", 14),bg = blanco) 
    billetes_label.grid(row = 5, column = 2)

    tarjeta_label = tk.Label(cajero_ventana, text = "TARJETA DE CRÉDITO", font = ("Microsoft YaHei", 14),bg = blanco) 
    tarjeta_label.grid(row = 5, column = 3)

    coin1_button = tk.Button(cajero_ventana, text = coin1, command = lambda: pagar(coin1,"C",placa.get()), bg = "#ad8911", height = 2, width = 12)
    coin1_button.grid(row = 6, column = 1, padx = 4, pady = 4)  

    coin2_button = tk.Button(cajero_ventana, text = coin2, command = lambda: pagar(coin2,"C",placa.get()), bg = "#ad8911", height = 2, width = 12)
    coin2_button.grid(row = 7, column = 1, padx = 4, pady = 4)  

    coin3_button = tk.Button(cajero_ventana, text = coin3, command = lambda: pagar(coin3,"C",placa.get()), bg = "#ad8911", height = 2, width = 12)
    coin3_button.grid(row = 8, column = 1, padx = 4, pady = 4)  

    billete1_button = tk.Button(cajero_ventana, text = bill1, command = lambda: pagar(bill1,"B",placa.get()), bg = "#29c440", height = 2, width = 12)
    billete1_button.grid(row = 6, column = 2, padx = 4, pady = 4)  

    billete2_button = tk.Button(cajero_ventana, text = bill2, command = lambda: pagar(bill2,"B",placa.get()), bg = "#29c440", height = 2, width = 12)
    billete2_button.grid(row = 7, column = 2, padx = 4, pady = 4)  

    billete3_button = tk.Button(cajero_ventana, text = bill3, command = lambda: pagar(bill3,"B",placa.get()), bg = "#29c440", height = 2, width = 12)
    billete3_button.grid(row = 8, column = 2, padx = 4, pady = 4)  

    billete4_button = tk.Button(cajero_ventana, text = bill4, command = lambda: pagar(bill4,"B",placa.get()), bg = "#29c440", height = 2, width = 12)
    billete4_button.grid(row = 9, column = 2, padx = 4, pady = 4)  

    billete5_button = tk.Button(cajero_ventana, text = bill5, command = lambda: pagar(bill5,"B",placa.get()), bg = "#29c440", height = 2, width = 12)
    billete5_button.grid(row = 10, column = 2, padx = 4, pady = 4)  

    tarjeta = tk.StringVar()
    tarjetaentry = tk.Entry(cajero_ventana, textvariable = tarjeta)
    tarjetaentry.grid(row = 6, column = 3)

    seleccionartarjeta_button = tk.Button(cajero_ventana, text = "Aceptar", command = lambda: pagartarjeta(placa.get(),tarjeta.get()), bg = blanco, height = 2, width = 12)
    seleccionartarjeta_button.grid(row = 7, column = 3, padx = 4, pady = 4)  


    apagar_label = tk.Label(cajero_ventana, text = "A PAGAR", font = ("Microsoft YaHei", 14),bg = blanco) 
    apagar_label.grid(row = 2, column = 4)

    apagarmonto_label = tk.Label(cajero_ventana, text = "XXXXX", font = ("Microsoft YaHei", 18),bg = "#d4020d") 
    apagarmonto_label.grid(row = 3, column = 4)

    pagado_label = tk.Label(cajero_ventana, text = "Pagado", font = ("Microsoft YaHei", 14),bg = blanco) 
    pagado_label.grid(row = 4, column = 4)

    pagadomonto_label = tk.Label(cajero_ventana, text = "XXXXX", font = ("Microsoft YaHei", 14),bg = "#90de93") 
    pagadomonto_label.grid(row = 5, column = 4)

    cambio_label = tk.Label(cajero_ventana, text = "Cambio", font = ("Microsoft YaHei", 14),bg = blanco) 
    cambio_label.grid(row = 6, column = 4)

    cambiomonto_label = tk.Label(cajero_ventana, text = "XXXXX", font = ("Microsoft YaHei", 14),bg = "#90de93") 
    cambiomonto_label.grid(row = 7, column = 4)

    paso3_label = tk.Label(cajero_ventana, text = "Paso 3: SU CAMBIO EN", font = ("Microsoft YaHei", 14),bg = blanco) 
    paso3_label.grid(row = 11, column = 0)

    monedascambio_label = tk.Label(cajero_ventana, text = "MONEDAS", font = ("Microsoft YaHei", 14),bg = blanco) 
    monedascambio_label.grid(row = 11, column = 1)

    billetescambio_label = tk.Label(cajero_ventana, text = "BILLETES", font = ("Microsoft YaHei", 14),bg = blanco) 
    billetescambio_label.grid(row = 11, column = 2)
    
    coin1text = "XXX de " + str(coin1) 
    coin1cambio_label = tk.Label(cajero_ventana, text = coin1text, font = ("Microsoft YaHei", 14),bg = blanco) 
    coin1cambio_label.grid(row = 12, column = 1)

    coin2text = "XXX de " + str(coin2) 
    coin2cambio_label = tk.Label(cajero_ventana, text = coin2text, font = ("Microsoft YaHei", 14),bg = blanco) 
    coin2cambio_label.grid(row = 13, column = 1)

    coin3text = "XXX de " + str(coin3) 
    coin3cambio_label = tk.Label(cajero_ventana, text = coin3text, font = ("Microsoft YaHei", 14),bg = blanco) 
    coin3cambio_label.grid(row = 14, column = 1)

    bill1text = "XXX de " + str(bill1) 
    bill1cambio_label = tk.Label(cajero_ventana, text = bill1text, font = ("Microsoft YaHei", 14),bg = blanco) 
    bill1cambio_label.grid(row = 12, column = 2)

    bill2text = "XXX de " + str(bill2) 
    bill2cambio_label = tk.Label(cajero_ventana, text = bill2text, font = ("Microsoft YaHei", 14),bg = blanco) 
    bill2cambio_label.grid(row = 13, column = 2)

    bill3text = "XXX de " + str(bill3) 
    bill3cambio_label = tk.Label(cajero_ventana, text = bill3text, font = ("Microsoft YaHei", 14),bg = blanco) 
    bill3cambio_label.grid(row = 14, column = 2)

    bill4text = "XXX de " + str(bill4) 
    bill4cambio_label = tk.Label(cajero_ventana, text = bill4text, font = ("Microsoft YaHei", 14),bg = blanco) 
    bill4cambio_label.grid(row = 15, column = 2)

    bill5text = "XXX de " + str(bill5) 
    bill5cambio_label = tk.Label(cajero_ventana, text = bill5text, font = ("Microsoft YaHei", 14),bg = blanco) 
    bill5cambio_label.grid(row = 16, column = 2)

    anularpago_button = tk.Button(cajero_ventana, text = "Anular pago", command = lambda: anular_pago(cajero_ventana), bg = blanco, height = 2, width = 12)
    anularpago_button.grid(row = 17, column = 0, padx = 4, pady = 4)  



def salida():
    
    def guardarsalida(window, placa):
        global configuracion
        global parqueo
        global detalle_de_uso
        print(placa)
        seborro = False
        i = 1
        while i <= len(parqueo):
            if i in parqueo:
                if parqueo[i][0] == placa:
                    if  parqueo[i][2] == "":
                        messagebox.showinfo("Error", "ESTA PLACA NO HA PAGADO") # Se despliega un error si no es válido
                        return
                    
                    fecha = parqueo[i][2]
                    fechalista = fecha.split()
                    fecha = fechalista[0].split("/")
                    tiempo=fechalista[1].split(":")
                    date1 = datetime(int(fecha[2]), int(fecha[1]), int(fecha[0]), int(tiempo[0]), int(tiempo[1]), int(tiempo[2]))
                    now = datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    fechalista = dt_string.split()
                    fecha = fechalista[0].split("/")
                    tiempo=fechalista[1].split(":")
                    date2 = datetime(int(fecha[2]), int(fecha[1]), int(fecha[0]), int(tiempo[0]), int(tiempo[1]), int(tiempo[2]))
                    print(date1)
                    print(date2)
                    difference = date2 - date1
                    print(difference)
                    difference = difference.total_seconds() / 60
                    print(difference)
                    nuevodetalle = parqueo[i].copy()
                    nuevodetalle += [dt_string] + [i]
                    detalle_de_uso.append(nuevodetalle)
                    if difference <= configuracion[4]:
                        print("se borro")
                        seborro = True
                        del parqueo[i]
                        print(parqueo)
                        print(detalle_de_uso)
                        
                    else:
                        texto = "No puede salir porque excedió el tiempo permitido para ello \n"
                        texto += "Tiempo máximo para salir luego del pago "
                        texto += str(configuracion[4])
                        texto += "\n Tiempo que usted ha tardado \n"
                        texto += str(difference)
                        texto += "\n Debe regresar al cajero a pagar la diferencia. "
                        nuevoparqueo = []
                        nuevoparqueo = nuevoparqueo + [parqueo[i][0]] + [parqueo[i][2]] + [""] + [0]
                        del parqueo[i]
                        parqueo[i] = nuevoparqueo
                        messagebox.showinfo("Error", texto) # Se despliega un error si no es válido
                    break
            i += 1        
        if i > len(parqueo) and seborro == False:
            print(parqueo)
            print(detalle_de_uso)
            messagebox.showinfo("Error", "ESA PLACA NO ESTÁ EN EL PARQUEO") # Se despliega un error si no es válido   

    salida_ventana = tk.Toplevel(ventana)
    salida_ventana.title("Salida")
    salida_ventana.geometry("550x200")
    salida_ventana.configure(bg = blanco)
    salida_Label = tk.Label(salida_ventana, text = "PARQUEO - SALIDA DE VEHÍCULO", font = ("Microsoft YaHei", 20),bg = blanco) 
    salida_Label.grid(row = 0, column = 0,columnspan = 2)
    placa_Label = tk.Label(salida_ventana, text = "SU PLACA", font = ("Microsoft YaHei", 14),bg = blanco) 
    placa_Label.grid(row = 1, column = 0)

    placa = tk.IntVar()
    placaentry = tk.Entry(salida_ventana, textvariable = placa)
    placaentry.grid(row = 1, column = 1)

    oksalida_button = tk.Button(salida_ventana, text = "OK", command = lambda: guardarsalida(salida_ventana, placa.get()), bg = blanco, height = 2, width = 12)
    oksalida_button.grid(row = 2, column = 0, padx = 4, pady = 4)  


def ayuda():
    path = 'manual_de_usuario_parqueo.pdf'
    os.system(path)
ventana = tk.Tk()
# C:\\Users\\dandi\\OneDrive-EstudiantesITCR\\Documentos\\TEC\\ISemestre\\Tallerdeprogramación\\Parqueo\\Parqueo\\
ventana.geometry("1000x1000")
ventana.title("Parqueo")
ventana.configure(bg = blanco)

titulo = tk.Label(ventana, text = "Parqueo", font = ("Microsoft YaHei", 30), bg = blanco)
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
cajero_button.grid(row = 1, column = 5, padx = 4, pady = 4)
salida_button = tk.Button(ventana, text = "Salida del \n vehículo", command = lambda: salida(), bg = select_color, height = 2, width = 10)
salida_button.grid(row = 1, column = 6, padx = 4, pady = 4)
ayuda_button = tk.Button(ventana, text = "Ayuda", command = lambda: ayuda(), bg = select_color, height = 2, width = 10)
ayuda_button.grid(row = 1, column = 7, padx = 4, pady = 4)


ventana.mainloop()


