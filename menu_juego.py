import tkinter as tk
from tkinter import PhotoImage

import alfabeto.hiragana
import alfabeto.katakana
import juego


def menu_juego(alfabetoUsado):
    decision = None

    def japones_a_español():
        print("Japones a español")
        nonlocal decision
        decision = True

    def español_a_japones():
        print("Español a japones")
        nonlocal decision
        decision = False

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

    caracteres = seleccionar_caracteres(alfabetoUsado)
    juego.jugar(caracteres,decision)


def seleccionar_caracteres(decisionAlfabeto):
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
    vocales = tk.Checkbutton(menu, text="Vocales", command=lambda: toggle_opcion("Vocales"))
    basico = tk.Checkbutton(menu, text="Basico", command=lambda: toggle_opcion("Basico"))
    compuesto = tk.Checkbutton(menu, text="Compuesto", command=lambda: toggle_opcion("Compuesto"))
    combinado1 = tk.Checkbutton(menu, text="Combinado 1", command=lambda: toggle_opcion("Combinado 1"))
    combinado2 = tk.Checkbutton(menu, text="Combinado 2", command=lambda: toggle_opcion("Combinado 2"))

    # Posicionar las opciones en la ventana
    vocales.pack()
    basico.pack()
    compuesto.pack()
    combinado1.pack()
    combinado2.pack()

    # Crear el botón de continuar
    boton_continuar = tk.Button(menu, text="Continuar", command=continuar)
    boton_continuar.pack()

    # Iniciar el bucle principal de la ventana
    menu.mainloop()

    caracteres = {}

    if decisionAlfabeto:
        if vocales: caracteres |= alfabeto.hiragana.vocales
        if basico: caracteres |= alfabeto.hiragana.basico
        if compuesto: caracteres |= alfabeto.hiragana.compuesto
        if combinado1: caracteres |= alfabeto.hiragana.combinado_1
        if combinado2: caracteres |= alfabeto.hiragana.combinados_2
    else:
        if vocales: caracteres |= alfabeto.katakana.vocales
        if basico: caracteres |= alfabeto.katakana.basico
        if compuesto: caracteres |= alfabeto.katakana.compuesto
        if combinado1: caracteres |= alfabeto.katakana.combinado_1
        if combinado2: caracteres |= alfabeto.katakana.combinados_2

    return caracteres
