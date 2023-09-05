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
    """
    Clase para gestionar la recopilación, almacenamiento y visualización de datos de progreso del jugador.

    Esta clase proporciona métodos para guardar y leer datos de partidas en un archivo JSON,
    generar gráficos de progreso y mostrarlos en ventanas emergentes, y borrar los datos almacenados.

    Atributos:
    data_file: Ruta al archivo JSON donde se almacenan los datos de las partidas.
    """

    def __init__(self):
        """
        Inicializa una instancia de la clase GestionDatos.

        Esta función es el constructor de la clase GestionDatos. Al crear una instancia
        de esta clase, se establece el atributo `data_file` con la ruta al archivo JSON
        donde se almacenarán los datos de las partidas.

        Detalles:
        La ruta al archivo JSON puede ser modificada según se desee. Este atributo
        será utilizado por otros métodos de la clase para acceder y manipular los datos
        almacenados en el archivo.

        :return: None
        """
        self.data_file = 'datos/datos_partidas.json'

    def guardar(self, numero_errores, errores, alfabeto_elegido):
        """
        Guarda los datos de una partida en el archivo JSON de datos.

        Esta función almacena los datos de una partida en el archivo JSON designado,
        incluyendo la fecha, el número de errores cometidos, los errores cometidos
        durante la partida y el alfabeto elegido.

        Parámetros:
        :param numero_errores: El número de errores cometidos durante la partida.
        :param errores: Un diccionario que contiene los errores cometidos y sus valores.
        :param alfabeto_elegido: El alfabeto elegido para la partida (por ejemplo, hiragana o katakana).

        Detalles:
        La función crea un diccionario `data` con los detalles de la partida, incluyendo la fecha
        actual, el número de errores, los errores y el alfabeto elegido. Luego, intenta cargar
        el contenido del archivo JSON existente. Si el archivo no existe, crea una lista vacía.
        La partida actual se inserta en la primera posición de la lista. Finalmente, se guarda
        la lista actualizada en el archivo JSON.

        :return: None
        """
        data = {"fecha": str(datetime.now()), "numeroErrores": numero_errores, "errores": errores,
                "alfabeto_elegido": alfabeto_elegido}

        try:
            # Intenta cargar el contenido del archivo JSON existente
            with open(self.data_file, 'r') as archivo_lectura:
                contenido = json.load(archivo_lectura)
        except FileNotFoundError:
            # Si el archivo no existe, crea una lista vacía
            contenido = []

        # Inserta los datos de la partida en la primera posición de la lista
        contenido.insert(0, data)

        # Guarda la lista actualizada en el archivo JSON
        with open(self.data_file, 'w') as archivo_escritura:
            json.dump(contenido, archivo_escritura, indent=4)

    def leer_datos(self):
        """
        Lee y devuelve los datos almacenados en el archivo JSON de datos.

        Esta función lee los datos almacenados en el archivo JSON designado y devuelve
        el contenido en forma de una lista de diccionarios. Cada diccionario representa
        los detalles de una partida, incluyendo la fecha, el número de errores, los errores
        cometidos y el alfabeto elegido.

        Detalles:
        La función intenta cargar el contenido del archivo JSON existente. Si el archivo
        no existe, devuelve una lista vacía. En caso contrario, retorna el contenido
        del archivo JSON, que consiste en una lista de diccionarios.

        :return: Una lista de diccionarios representando los datos de las partidas almacenadas.
        """
        try:
            # Intenta cargar el contenido del archivo JSON existente
            with open(self.data_file, 'r') as archivo_lectura:
                contenido = json.load(archivo_lectura)
                return contenido
        except FileNotFoundError:
            # Si el archivo no existe, devuelve una lista vacía
            return []

    def generar_grafico(self):
        """
        Genera y devuelve un gráfico de progreso del jugador.

        Esta función utiliza los datos almacenados en el archivo JSON de datos para
        crear un gráfico de líneas que muestra el progreso del jugador a lo largo
        del tiempo, con los errores cometidos en el eje 'y' y las fechas en el eje 'x'.

        Detalles:
        La función lee los datos almacenados en el archivo JSON utilizando el método
        `leer_datos`. Si no hay datos, la función devuelve `None`. Luego, crea un DataFrame
        de pandas con los datos leídos y convierte la columna 'fecha' en un objeto de tipo
        fecha. Los datos se dividen en dos conjuntos según el alfabeto elegido (hiragana o katakana).
        Se crea un gráfico de líneas con los datos de errores para cada conjunto y se personaliza
        con etiquetas, título y formato de fecha en el eje x. Finalmente, se ajusta la apariencia
        de los ejes y se devuelve la figura del gráfico.

        :return: Una figura de matplotlib que representa el gráfico de progreso del jugador.
        """

        datos = self.leer_datos()

        if not datos:
            return

        # Crear un DataFrame de pandas y convertir la columna 'fecha' en tipo datetime
        df = pd.DataFrame(datos)
        df['fecha'] = pd.to_datetime(df['fecha'])

        # Dividir los datos en conjuntos de hiragana y katakana
        df_hiragana = df[df['alfabeto_elegido']]
        df_katakana = df[~df['alfabeto_elegido']]

        # Crear una figura y ejes para el gráfico
        fig, ax = plt.subplots(figsize=(10, 6))

        # Trazar líneas para los conjuntos de hiragana y katakana
        ax.plot(df_hiragana['fecha'], df_hiragana['numeroErrores'], marker='o', label='Hiragana', color='blue')
        ax.plot(df_katakana['fecha'], df_katakana['numeroErrores'], marker='o', label='Katakana', color='red')

        # Personalizar etiquetas y título del gráfico
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

        # Configurar los ticks del eje y para mostrar valores enteros positivos de forma escalonada
        y_ticks = np.arange(min_error_value, max_error_value + 1, 1)
        ax.set_yticks(y_ticks)

        return fig

    def mostrar_grafico_tkinter(self, menu_principal):
        """
        Muestra un gráfico de progreso del jugador en una ventana emergente.

        Esta función genera un gráfico de progreso utilizando el método `generar_grafico`
        y lo muestra en una ventana emergente de Tkinter.

        Parámetros:
        :param menu_principal: Objeto Tkinter de la ventana principal del programa.

        Detalles:
        La función llama al método `generar_grafico` para obtener la figura del gráfico de progreso.
        Si se obtiene una figura, se crea una nueva ventana secundaria utilizando `Toplevel`,
        y se configura su título, tamaño y apariencia.

        Luego, se crea un widget de lienzo (`FigureCanvasTkAgg`) que contiene el gráfico y se lo
        empaqueta en la ventana secundaria.

        Se configura un manejo especial para el evento de cierre de ventana (`WM_DELETE_WINDOW`),
        de modo que cuando el usuario cierre la ventana emergente, se restaure la ventana
        principal `menu_principal`.

        Si no hay datos para generar un gráfico, se muestra un mensaje emergente utilizando la
        función `custom_message_box` para informar al usuario que no hay datos de progreso.

        :return: None
        """
        grafico = self.generar_grafico()
        if grafico:
            root = tk.Toplevel(menu_principal)
            root.title("Gráfico de Progreso")
            root.geometry("900x550+300+100")
            root.resizable(False, False)
            root.iconbitmap("imagenes/icono.ico")

            # Crear un widget de lienzo con el gráfico y empaquetarlo en la ventana
            canvas = FigureCanvasTkAgg(grafico, master=root)
            canvas.draw()
            canvas.get_tk_widget().pack()

            # Configurar el manejo del evento de cierre de ventana
            root.protocol("WM_DELETE_WINDOW", lambda: self.cerrar_ventana_registro(root, menu_principal))
        else:
            # Mostrar un mensaje emergente si no hay datos para el gráfico
            menu_principal.deiconify()
            custom_message_box("No hay datos", "No se han encontrado datos de progreso", 16)

    @staticmethod
    def cerrar_ventana_registro(ventana_registro, ventana_principal):
        """
        Cierra la ventana de registro y restaura la ventana principal.

        Esta función cierra la ventana de registro (ventana emergente) y restaura
        la visibilidad de la ventana principal.

        Parámetros:
        :param ventana_registro: Objeto Tkinter de la ventana de registro (ventana emergente).
        :param ventana_principal: Objeto Tkinter de la ventana principal del programa.

        Detalles:
        La función cierra la ventana de registro invocando el método `destroy()` en
        el objeto `ventana_registro`, lo que provoca su cierre.

        Luego, se utiliza `deiconify()` en el objeto `ventana_principal` para restaurar
        la visibilidad de la ventana principal que pudo haber sido ocultada cuando se
        abrió la ventana de registro.

        :return: None
        """
        ventana_registro.destroy()
        ventana_principal.deiconify()

    def borrar_datos(self):
        """
        Borra todos los datos almacenados en el archivo de datos.

        Esta función borra todos los datos almacenados en el archivo de datos, dejando el archivo en blanco.

        Detalles:
        La función utiliza un bloque de código 'try...except' para manejar posibles errores durante la operación
        de borrado de datos.

        En el bloque 'try', se abre el archivo de datos en modo de escritura ('w') y se escribe un corchete
        cuadrado vacío ('[]') en el archivo, lo que efectivamente borra todos los datos previamente almacenados.

        Si se produce un error durante la operación, se muestra un mensaje de error emergente utilizando la función
        'custom_message_box', indicando el tipo de error que ocurrió.

        :return: None
        """
        try:
            with open(self.data_file, 'w') as archivo:
                archivo.write('[]')  # Escribir un corchete cuadrado vacío para borrar todos los datos
        except Exception as error:
            # Mostrar un mensaje de error emergente en caso de falla
            custom_message_box("Error", f'Error al borrar los datos: {str(error)}', 16)
