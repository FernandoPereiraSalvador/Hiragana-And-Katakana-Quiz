import tkinter as tk
from tkinter import PhotoImage, messagebox

import configuracion
import datos
import menu_juego


# Definición de la clase MenuPrincipal
class MenuPrincipal:
    def __init__(self, root):
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
        # Llamada a función de otro módulo
        self.root.withdraw()
        menu_juego.main(True, self.root)

    def decision_katakana(self):
        # Llamada a función de otro módulo
        self.root.withdraw()
        menu_juego.main(False, self.root)

    def mostrar_registro(self):
        # Llamada a función de otro módulo
        self.root.withdraw()
        datos.mostrar_grafico_tkinter(self.root)

    def abrir_configuracion(self):
        self.root.withdraw()
        configuracion.main(self.root)

    def crear_botones(self):
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

        configuracion_button = tk.Button(
            self.root,
            command=lambda: [self.abrir_configuracion()],
            image=self.configuracion, width=40, height=40
        )
        configuracion_button.place(x=455, y=0)


# Función principal para iniciar la aplicación
def main():
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
        messagebox.showinfo("Error", "No se ha podido iniciar el programa. Intentelo de nuevo.\nError: " + str(e))
