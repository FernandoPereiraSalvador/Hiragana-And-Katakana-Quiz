import tkinter as tk
from tkinter import PhotoImage, messagebox

import configuracion
from datos import GestionDatos
import menu_juego


# Definición de la clase MenuPrincipal
class MenuPrincipal:
    """
    Clase que representa la ventana principal del menú de la aplicación.

    Esta clase se encarga de crear y gestionar la interfaz del menú principal de la aplicación. Proporciona opciones
    para seleccionar modos de juego, mostrar el registro de progreso del jugador y acceder a la configuración de la
    aplicación.

    Atributos:
        root (Tk): La ventana principal de la aplicación.
        imagen_hiragana (PhotoImage): Imagen para el botón de selección de modo Hiragana.
        imagen_katakana (PhotoImage): Imagen para el botón de selección de modo Katakana.
        imagen_registro (PhotoImage): Imagen para el botón de mostrar registro.
        configuracion (PhotoImage): Imagen para el botón de acceso a configuración.

    Métodos:
        __init__(self, root): Inicializa la ventana principal, carga imágenes y crea los botones.
        decision_hiragana(self): Abre el menú de selección de modo Hiragana.
        decision_katakana(self): Abre el menú de selección de modo Katakana.
        mostrar_registro(self): Muestra un gráfico de progreso del jugador a lo largo del tiempo.
        abrir_configuracion(self): Abre la ventana de configuración.
        crear_botones(self): Crea los botones en la ventana principal.
    """

    def __init__(self, root):
        """
        Inicializa una ventana principal, establece sus propiedades, carga imágenes y crea los botones.

        Parámetros:
        root (Tk): La ventana principal o ventana raíz de la aplicación. Es la ventana de nivel superior
        que contiene todos los demás widgets. En este código, el parámetro "root" se pasa al constructor
        de la clase para inicializar la ventana principal de la aplicación.

        Detalles:
        Esta función establece las propiedades de la ventana, carga imágenes necesarias y llama a la
        función que crea los botones para la interfaz del menú.

        :return: None
        """

        # Inicialización de la ventana principal
        self.root = root
        self.root.geometry("900x550+300+100")
        self.root.resizable(False, False)
        self.root.title("Menu")
        self.root.iconbitmap("menu_imagenes/icono.ico")

        # Carga de las imágenes
        self.imagen_hiragana = PhotoImage(file="menu_imagenes/hiragana.png")
        self.imagen_katakana = PhotoImage(file="menu_imagenes/katakana.png")
        self.imagen_registro = PhotoImage(file="menu_imagenes/registro.png")
        self.configuracion = PhotoImage(file="menu_imagenes/configuracion.png")

        # Creación de los botones en la ventana
        self.crear_botones()

    def decision_hiragana(self):
        """
        Oculta la ventana principal y llama a la función de menú del juego para elegir el modo de juego.

        Detalles:
        Esta función se activa al hacer click en el boton hiragana. Y oculta la ventana principal y abre el
        menú de selección de modo de juego. Se le pasa un parámetro booleano para indicar si el modo de juego
        seleccionado es Hiragana (True).

        :return: None
        """

        self.root.withdraw()
        menu_juego.main(True, self.root)

    def decision_katakana(self):
        """
        Oculta la ventana principal y llama a la función de menú del juego para elegir el modo de juego.

        Detalles:
        Esta función se activa al hacer click en el boton katakana. Y oculta la ventana principal y abre el
        menú de selección de modo de juego. Se le pasa un parámetro booleano para indicar si el modo de juego
        seleccionado es Katakana (False).

        :return: None
        """
        self.root.withdraw()
        menu_juego.main(False, self.root)

    def mostrar_registro(self):
        """
        Oculta la ventana principal y muestra un gráfico del progreso del jugador a lo largo del tiempo
        utilizando la función 'mostrar_grafico_tkinter' de la clase 'GestionDatos'.

        Detalles:
        Esta función utiliza la clase 'GestionDatos' para mostrar un gráfico del progreso del jugador a lo
        largo del tiempo en una ventana secundaria utilizando la librería Tkinter. Primero, oculta la ventana
        principal actual y luego crea una instancia de la clase 'GestionDatos' para acceder a la función
        'mostrar_grafico_tkinter'. Dicha función es responsable de mostrar el gráfico en una ventana secundaria. El
        parámetro 'self.root' se pasa a la función 'mostrar_grafico_tkinter' para asegurarse de que el gráfico se
        muestre en la misma ventana principal después de ocultarla.

        :return: None
        """
        self.root.withdraw()
        registro = GestionDatos()
        registro.mostrar_grafico_tkinter(self.root)

    def abrir_configuracion(self):
        """
        Oculta la ventana principal y abre la ventana de configuración.

        Detalles:
        Esta función oculta la ventana principal actual utilizando el método 'withdraw' y luego llama a la
        función 'main' del módulo 'configuracion' para abrir la ventana de configuración. La instancia actual de la
        ventana principal, 'self.root', se pasa a la función 'main' para asegurarse de que la configuración se
        realice en la misma ventana principal después de ocultarla.

        :return: None
        """
        self.root.withdraw()
        configuracion.main(self.root)

    def crear_botones(self):
        """
        Crea los botones para seleccionar modos de juego y acceder a funciones adicionales.

        Esta función crea varios botones en la ventana principal para interactuar con el programa. Los botones
        incluyen opciones para seleccionar el alfabeto para el juego (Hiragana o Katakana), mostrar el registro de
        progreso del jugador y acceder a la configuración de la aplicación.

        Detalles:
        Esta función utiliza la librería Tkinter para crear y posicionar los botones en la ventana principal. Cada
        botón está asociado a una función específica (como 'decision_hiragana', 'decision_katakana', 'mostrar_registro',
        y 'abrir_configuracion') y se configura para llamar a la función correspondiente cuando se hace clic en él.

        :return: None
        """
        # Creación del botón para seleccionar Hiragana
        hiragana_button = tk.Button(
            self.root,
            command=lambda: [self.decision_hiragana()],
            width=325, height=325, image=self.imagen_hiragana
        )
        hiragana_button.place(x=65, y=50)

        # Creación del botón para seleccionar Katakana
        katakana_button = tk.Button(
            self.root,
            command=lambda: [self.decision_katakana()],
            width=325, height=325, image=self.imagen_katakana
        )
        katakana_button.place(x=500, y=50)

        # Creación del botón para mostrar el registro
        registro_button = tk.Button(
            self.root,
            command=lambda: [self.mostrar_registro()],
            image=self.imagen_registro, width=40, height=40
        )
        registro_button.place(x=395, y=0)

        # Creación del botón para mostrar la configuración
        configuracion_button = tk.Button(
            self.root,
            command=lambda: [self.abrir_configuracion()],
            image=self.configuracion, width=40, height=40
        )
        configuracion_button.place(x=455, y=0)


def main():
    """
    Inicia la aplicación del menú principal.

    Esta función es el punto de entrada de la aplicación. Crea una ventana principal de Tkinter, instancia la clase
    'MenuPrincipal' para gestionar el menú y luego inicia el bucle principal de la aplicación, que se encarga de
    mostrar la interfaz y responder a eventos del usuario.

    Detalles:
    Esta función crea la ventana principal utilizando la librería Tkinter y luego crea una instancia de la clase
    'MenuPrincipal', que se encarga de gestionar la interfaz del menú. Después de configurar todo, inicia el bucle
    principal de la aplicación llamando al método 'mainloop' de la ventana. Esto permite que la aplicación se ejecute
    y responda a eventos de manera interactiva.

    :return: None
    """
    # Crear la ventana principal de Tkinter
    root = tk.Tk()

    # Crear una instancia de la clase MenuPrincipal
    MenuPrincipal(root)

    # Iniciar el bucle principal de la aplicación
    root.mainloop()


# Verificar si este módulo es el programa principal
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        messagebox.showinfo(
            "Error", "No se ha podido iniciar el programa. Intentelo de nuevo.\nError: " + str(e))
