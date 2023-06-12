import tkinter as tk
from tkinter import PhotoImage

def menu_juego():
    def japones_a_español():
        print("Japones a español")
        return True

    def español_a_japones():
        print("Español a japones")
        return False

    # Crear la ventana principal
    menu = tk.Tk()
    menu.geometry("900x550+300+100")
    menu.resizable(False, False)
    menu.title("Modo")
    menu.iconbitmap("menu_imagenes/icono.ico")

    # Cargar las imágenes
    imagen_japones_a_español = PhotoImage(file="menu_imagenes/japones.png")
    imagen_español_a_japones = PhotoImage(file="menu_imagenes/español.png")

    # Crear los botones
    hiragana_button = tk.Button(
        menu,
        command=lambda: [menu.destroy(), japones_a_español()],
        width=325, height=325, image=imagen_japones_a_español
    )
    hiragana_button.place(x=65, y=50)

    katakana_button = tk.Button(
        menu,
        command=lambda: [menu.destroy(), español_a_japones()],
        width=325, height=325, image=imagen_español_a_japones
    )
    katakana_button.place(x=500, y=50)

    # Iniciar el bucle principal de la ventana
    menu.mainloop()

def seleccionar_caracteres():
    opcion_vocales = False
    opcion_basico = False
    opcion_compuesto = False
    opcion_combinado1 = False
    opcion_combinado2 = False

    def toggle_opcion(opcion):
        nonlocal opcion_vocales, opcion_basico, opcion_compuesto, opcion_combinado1, opcion_combinado2
        if opcion == "Vocales":
            opcion_vocales = not opcion_vocales
        if opcion == "Basico":
            opcion_basico = not opcion_basico
        if opcion == "Compuesto":
            opcion_compuesto = not opcion_compuesto
        if opcion == "Combinado 1":
            opcion_combinado1 = not opcion_combinado1
        if opcion == "Combinado 2":
            opcion_combinado2 = not opcion_combinado2

    def continuar():
        print("Continuar")
        print(opcion_combinado2)
        print(opcion_vocales)
        menu.destroy()

    # Crear la ventana principal
    menu = tk.Tk()
    menu.title("Caracteres")
    menu.geometry("900x550+300+100")
    menu.resizable(False, False)
    menu.title("Menu")
    menu.iconbitmap("menu_imagenes/icono.ico")

    # Crear los widgets de las opciones
    Vocales = tk.Checkbutton(menu, text="Vocales", command=lambda: toggle_opcion("Vocales"))
    Basico = tk.Checkbutton(menu, text="Basico", command=lambda: toggle_opcion("Basico"))
    Compuesto = tk.Checkbutton(menu, text="Compuesto", command=lambda: toggle_opcion("Compuesto"))
    Combinado1 = tk.Checkbutton(menu, text="Combinado 1", command=lambda: toggle_opcion("Combinado 1"))
    Combinado2 = tk.Checkbutton(menu, text="Combinado 2", command=lambda: toggle_opcion("Combinado 2"))

    # Posicionar las opciones en la ventana
    Vocales.pack()
    Basico.pack()
    Compuesto.pack()
    Combinado1.pack()
    Combinado2.pack()

    # Crear el botón de continuar
    boton_continuar = tk.Button(menu, text="Continuar", command=continuar)
    boton_continuar.pack()

    # Iniciar el bucle principal de la ventana
    menu.mainloop()

seleccionar_caracteres()