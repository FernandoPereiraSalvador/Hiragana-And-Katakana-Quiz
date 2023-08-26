import tkinter as tk
import webbrowser
from tkinter import messagebox
from datos import borrar_datos

class Configuracion:
    def __init__(self, root, menu_principal):
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
        # Mostrar ventana emergente de confirmación
        confirmacion = messagebox.askyesno("Confirmación", "¿Estás seguro de borrar los datos de progreso?")
        if confirmacion:
            self.borrar_progreso()
        else:
            print("Cancelado")

    def borrar_progreso(self):
        borrar_datos()
        messagebox.showinfo("Borrado Exitoso", "Datos de progreso borrados exitosamente.")

    def cerrar_ventana(self):
        self.menu_principal.deiconify()  # Vuelve a mostrar la ventana principal
        self.root.destroy()  # Cierra la ventana de configuración

    def abrir_repositorio(self):
        url = "https://www.google.com"
        webbrowser.open(url)

def main(menu_principal):
    root = tk.Toplevel(menu_principal)
    Configuracion(root, menu_principal)
