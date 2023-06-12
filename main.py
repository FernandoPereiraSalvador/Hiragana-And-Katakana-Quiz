import tkinter as tk
from tkinter import PhotoImage


def menu_principal():
    def decision_hiragana():
        print("Se ha hecho clic en Hiragana")

    def decision_katakana():
        print("Se ha hecho clic en Katakana")

    def mostrar_registro():
        print("Se ha hecho clic en Registro")

    # Crear la ventana principal
    menu = tk.Tk()
    menu.geometry("900x550+300+100")
    menu.resizable(False, False)
    menu.title("Menu")
    menu.iconbitmap("menu_imagenes/icono.ico")

    # Cargar las imágenes
    imagen_hiragana = PhotoImage(file="menu_imagenes/hiragana.png")
    imagen_katakana = PhotoImage(file="menu_imagenes/katakana.png")
    imagen_registro = PhotoImage(file="menu_imagenes/registro.png")

    # Crear los botones
    hiragana_button = tk.Button(
        menu,
        command=lambda: [menu.destroy(), decision_hiragana()],
        width=325, height=325, image=imagen_hiragana
    )
    hiragana_button.place(x=65, y=50)

    katakana_button = tk.Button(
        menu,
        command=lambda: [menu.destroy(), decision_katakana()],
        width=325, height=325, image=imagen_katakana
    )
    katakana_button.place(x=500, y=50)

    registro_button = tk.Button(
        menu,
        command=lambda: [mostrar_registro()],
        image=imagen_registro, width=40, height=40
    )
    registro_button.pack(side=tk.TOP)

    # Iniciar el bucle principal de la ventana
    menu.mainloop()


if __name__ == "__main__":

    menu_principal()


else:
    print("Error")
