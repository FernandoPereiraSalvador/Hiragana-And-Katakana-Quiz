import tkinter as tk
import webbrowser
from tkinter import messagebox
from datos import GestionDatos


class Configuracion:
    """
    Clase para gestionar la ventana de configuración.

    Esta clase define una ventana de configuración que permite al usuario borrar
    los datos de progreso del juego o abrir el repositorio en línea del proyecto.

    Parámetros:
    :param root: Objeto Tkinter representando la ventana principal.
    :param menu_principal: Objeto Tkinter de la ventana principal del programa.

    Detalles:
    La ventana contiene dos opciones: una para borrar los datos de progreso del jugador
    y otra para abrir un enlace al repositorio de GitHub del proyecto.
    """
    
    def __init__(self, root, menu_principal):
        """
        Inicializa la ventana de configuración.

        Esta función realiza la configuración inicial de la ventana de configuración,
        estableciendo su apariencia y elementos interactivos.

        Parámetros:
        :param root: Objeto Tkinter representando la ventana principal.
        :param menu_principal: Objeto Tkinter de la ventana principal del programa.

        Detalles: Contiene dos opciones. La primera borrara los datos del progreso del jugador y la segunda abrira un
        link al repositorio de github del proyecto.

        :return: None
        """
        # Inicialización de la ventana principal
        self.root = root
        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.root.geometry("900x550+300+100")
        self.root.resizable(False, False)
        self.root.title("Configuración")
        self.root.iconbitmap("menu_imagenes/icono.ico")

        self.menu_principal = menu_principal  # Ventana principal

        # Crear el título
        titulo = tk.Label(root, text="Configuración", font=("Helvetica", 20))
        titulo.pack(pady=20)

        # Crear el botón "Borrar Datos de Progreso"
        borrar_bot = tk.Button(root, text="Borrar datos", command=self.mostrar_confirmacion, height=5, width=25,
                               font=("Helvetica", 20))
        borrar_bot.pack(pady=20)

        # Crear el botón "Repositorio"
        repositorio_bot = tk.Button(root, text="Repositorio", command=self.abrir_repositorio, height=5, width=25,
                                    font=("Helvetica", 20))
        repositorio_bot.pack()

    def mostrar_confirmacion(self):
        """
        Muestra una ventana emergente de confirmación para borrar los datos de progreso.

        Detalles:
        Esta función muestra una ventana emergente de confirmación con un mensaje preguntando
        al usuario si está seguro de borrar los datos de progreso. Si el usuario confirma,
        se llama al método `borrar_progreso` para realizar la acción de borrado.

        :return: None
        """
        # Mostrar ventana emergente de confirmación
        confirmacion = messagebox.askyesno("Confirmación", "¿Estás seguro de borrar los datos de progreso?")
        if confirmacion:
            self.borrar_progreso()

    @staticmethod
    def borrar_progreso():
        """
        Borra los datos de progreso.

        Detalles: Esta función crea una instancia de la clase `GestionDatos` para borrar los datos de progreso
        almacenados y llama a la función `borrar_datos`. Luego, muestra una ventana informativa para indicar que el
        borrado se realizó exitosamente.

        :return: None
        """
        borrar = GestionDatos()
        borrar.borrar_datos()
        messagebox.showinfo("Borrado Exitoso", "Datos de progreso borrados exitosamente.")

    def cerrar_ventana(self):
        """
        Cierra la ventana actual y restaura la ventana principal.

        Detalles:
        Esta función restaura la ventana principal del programa al invocar el método
        `deiconify()` en el objeto `menu_principal`. Luego, cierra la ventana actual
        de configuración al invocar el método `destroy()` en el objeto `root`.

        :return: None
        """
        self.menu_principal.deiconify()  # Vuelve a mostrar la ventana principal
        self.root.destroy()  # Cierra la ventana de configuración

    @staticmethod
    def abrir_repositorio():
        """
        Abre un navegador web para mostrar el repositorio en línea.

        Detalles:
        Esta función utiliza la biblioteca `webbrowser` para abrir un navegador web
        y mostrar la URL proporcionada. En este caso, la URL es para un repositorio
        en línea. La URL puede ser modificada según se desee.

        :return: None
        """
        url = "https://github.com/FernandoPereiraSalvador/Hiragana-And-Katakana-Quiz"
        webbrowser.open(url)


def main(menu_principal):
    """
    Función principal para iniciar la ventana de configuración.

    Esta función crea una nueva ventana secundaria (`Toplevel`) utilizando
    la instancia `menu_principal`. Luego, instancia la clase `Configuracion`
    para crear y mostrar la ventana de configuración en la nueva ventana.

    Parámetros:
    :param menu_principal: Objeto Tkinter de la ventana principal del programa.
    
    :return: None
    """
    root = tk.Toplevel(menu_principal)
    Configuracion(root, menu_principal)
