# Importar librerías de manejo de datos y visualización
import json

import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Importar librerías de interfaz gráfica
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from custom_message_box import custom_message_box


class GestionDatos:
    def __init__(self):
        self.data_file = 'datos/datos_partidas.json'

    def guardar(self, numero_errores, errores, alfabeto_elegido):
        data = {"fecha": str(datetime.now()), "numeroErrores": numero_errores, "errores": errores,
                "alfabeto_elegido": alfabeto_elegido}

        try:
            with open(self.data_file, 'r') as archivo_lectura:
                contenido = json.load(archivo_lectura)
        except FileNotFoundError:
            contenido = []

        contenido.insert(0, data)

        with open(self.data_file, 'w') as archivo_escritura:
            json.dump(contenido, archivo_escritura, indent=4)

    def leer_datos(self):
        try:
            with open(self.data_file, 'r') as archivo_lectura:
                contenido = json.load(archivo_lectura)
                return contenido
        except FileNotFoundError:
            return []

    def generar_grafico(self):
        datos = self.leer_datos()

        if not datos:
            return

        df = pd.DataFrame(datos)
        df['fecha'] = pd.to_datetime(df['fecha'])

        df_hiragana = df[df['alfabeto_elegido']]
        df_katakana = df[~df['alfabeto_elegido']]

        fig, ax = plt.subplots(figsize=(10, 6))

        ax.plot(df_hiragana['fecha'], df_hiragana['numeroErrores'], marker='o', label='Hiragana', color='blue')
        ax.plot(df_katakana['fecha'], df_katakana['numeroErrores'], marker='o', label='Katakana', color='red')

        ax.set_xlabel('Fecha')
        ax.set_ylabel('Número de Errores')
        ax.set_title('Progreso del Jugador')
        ax.legend()
        ax.grid(True)

        # Configurar el formato de fecha en el eje x
        date_format = mdates.DateFormatter('%d/%m/%Y')
        ax.xaxis.set_major_formatter(date_format)
        fig.autofmt_xdate()

        # Configurar ticks en el eje y para mostrar solo valores enteros positivos
        min_error_value = df['numeroErrores'].min()
        max_error_value = df['numeroErrores'].max()

        y_ticks = np.arange(0, max_error_value + 1, 1)
        ax.set_yticks(y_ticks)

        return fig

    def mostrar_grafico_tkinter(self, menu_principal):
        grafico = self.generar_grafico()
        if grafico:
            root = tk.Toplevel(menu_principal)
            root.title("Gráfico de Progreso")
            root.geometry("900x550+300+100")
            root.resizable(False, False)
            root.iconbitmap("menu_imagenes/icono.ico")

            canvas = FigureCanvasTkAgg(grafico, master=root)
            canvas.draw()
            canvas.get_tk_widget().pack()

            root.protocol("WM_DELETE_WINDOW", lambda: self.cerrar_ventana_registro(root, menu_principal))
        else:
            menu_principal.deiconify()
            custom_message_box("No hay datos", "No se han encontrado datos de progreso", 16)

    @staticmethod
    def cerrar_ventana_registro(ventana_registro, ventana_principal):
        ventana_registro.destroy()
        ventana_principal.deiconify()

    def borrar_datos(self):
        try:
            with open(self.data_file, 'w') as archivo:
                archivo.write('[]')
        except Exception as error:
            custom_message_box("Error", f'Error al borrar los datos: {str(error)}', 16)
