import json
from tkinter import messagebox

import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import matplotlib.dates as mdates

import main


def guardar(numeroErrores, errores, alfabeto_elegido):
    data = {"fecha": str(datetime.now()), "numeroErrores": numeroErrores, "errores": errores,
            "alfabeto_elegido": alfabeto_elegido}

    try:
        with open('datos_partidas.json', 'r') as archivo_lectura:
            contenido = json.load(archivo_lectura)
    except FileNotFoundError:
        contenido = []

    contenido.insert(0, data)

    with open('datos_partidas.json', 'w') as archivo_escritura:
        json.dump(contenido, archivo_escritura, indent=4)


def leer_datos():
    try:
        with open('datos_partidas.json', 'r') as archivo_lectura:
            contenido = json.load(archivo_lectura)
            return contenido
    except FileNotFoundError:
        return []


def generar_grafico():
    datos = leer_datos()

    if not datos:
        messagebox.showinfo("No hay datos", "No se han encontrado datos de progreso")
        return

    df = pd.DataFrame(datos)
    df['fecha'] = pd.to_datetime(df['fecha'])

    df_hiragana = df[df['alfabeto_elegido'] == True]
    df_katakana = df[df['alfabeto_elegido'] == False]

    fig, ax = plt.subplots(figsize=(10, 6))

    hiragana_plot, = ax.plot(df_hiragana['fecha'], df_hiragana['numeroErrores'], marker='o', label='Hiragana',
                             color='blue')
    katakana_plot, = ax.plot(df_katakana['fecha'], df_katakana['numeroErrores'], marker='o', label='Katakana',
                             color='red')

    ax.set_xlabel('Fecha')
    ax.set_ylabel('Número de Errores')
    ax.set_title('Progreso del Jugador')
    ax.legend()
    ax.grid(True)

    # Configurar el formato de fecha en el eje x
    date_format = mdates.DateFormatter('%d/%m/%Y')
    ax.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()

    return fig


def mostrar_grafico_tkinter(menu_principal):
    grafico = generar_grafico()
    if grafico:
        root = tk.Toplevel(menu_principal)
        root.title("Gráfico de Progreso")
        root.geometry("900x550+300+100")
        root.resizable(False, False)
        root.iconbitmap("menu_imagenes/icono.ico")

        canvas = FigureCanvasTkAgg(grafico, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack()

        root.protocol("WM_DELETE_WINDOW", lambda: cerrar_ventana_registro(root, menu_principal))

    else:menu_principal.deiconify()



def cerrar_ventana_registro(ventana_registro, ventana_principal):
    ventana_registro.destroy()
    ventana_principal.deiconify()


def borrar_datos():
    try:
        with open('datos_partidas.json', 'w') as archivo:
            archivo.write('[]')
    except Exception as e:
        mensaje_error = f"Error al borrar los datos: {str(e)}"
        print(mensaje_error)
        messagebox.showerror("Error", mensaje_error)
