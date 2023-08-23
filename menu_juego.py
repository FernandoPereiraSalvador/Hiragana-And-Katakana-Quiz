import tkinter as tk
from tkinter import PhotoImage

import alfabeto.hiragana
import alfabeto.katakana
import juego


def MenuJuego(alfabetoUsado):
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
    if alfabetoUsado:
        imagen_japones_a_español = PhotoImage(file="menu_imagenes/japonesHiragana.png")
    else:
        imagen_japones_a_español = PhotoImage(file="menu_imagenes/japonesKatakana.png")

    if alfabetoUsado:
        imagen_español_a_japones = PhotoImage(file="menu_imagenes/españolHiragana.png")
    else:
        imagen_español_a_japones = PhotoImage(file="menu_imagenes/españolKatakana.png")

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
    juego.jugar(caracteres,decision,alfabetoUsado)


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
    opciones_frame = tk.Frame(menu)
    opciones_frame.pack(pady=20)

    vocales = tk.Checkbutton(opciones_frame, text="Vocales", command=lambda: toggle_opcion("Vocales"), font=("Arial", 14))
    basico = tk.Checkbutton(opciones_frame, text="Basico", command=lambda: toggle_opcion("Basico"), font=("Arial", 14))
    compuesto = tk.Checkbutton(opciones_frame, text="Compuesto", command=lambda: toggle_opcion("Compuesto"), font=("Arial", 14))
    combinado1 = tk.Checkbutton(opciones_frame, text="Combinado 1", command=lambda: toggle_opcion("Combinado 1"), font=("Arial", 14))
    combinado2 = tk.Checkbutton(opciones_frame, text="Combinado 2", command=lambda: toggle_opcion("Combinado 2"), font=("Arial", 14))

    vocales.pack(pady=5)
    basico.pack(pady=5)
    compuesto.pack(pady=5)
    combinado1.pack(pady=5)
    combinado2.pack(pady=5)

    # Crear el botón de continuar
    boton_frame = tk.Frame(menu)
    boton_frame.pack(pady=20)

    boton_continuar = tk.Button(boton_frame, text="Continuar", command=continuar, font=("Arial", 16), padx=20, pady=10)
    boton_continuar.pack()

    # Centrar la ventana en la pantalla
    menu.update_idletasks()
    menu.geometry("900x550+300+100")

    # Iniciar el bucle principal de la ventana
    menu.mainloop()

    caracteres = {}

    if decisionAlfabeto:
        if opcion_vocales: caracteres |= alfabeto.hiragana.vocales
        if opcion_basico: caracteres |= alfabeto.hiragana.basico
        if opcion_compuesto: caracteres |= alfabeto.hiragana.compuesto
        if opcion_combinado1: caracteres |= alfabeto.hiragana.combinado_1
        if opcion_combinado2: caracteres |= alfabeto.hiragana.combinado_2
    else:
        if opcion_vocales: caracteres |= alfabeto.katakana.vocales
        if opcion_basico: caracteres |= alfabeto.katakana.basico
        if opcion_compuesto: caracteres |= alfabeto.katakana.compuesto
        if opcion_combinado1: caracteres |= alfabeto.katakana.combinado_1
        if opcion_combinado2: caracteres |= alfabeto.katakana.combinado_2

    return caracteres
