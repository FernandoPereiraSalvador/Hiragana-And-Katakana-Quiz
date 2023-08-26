import tkinter as tk
from tkinter import PhotoImage
import alfabeto.hiragana
import alfabeto.katakana
import juego


class MenuJuego:
    def __init__(self, alfabeto_usado, menu_principal):
        self.decision = None
        self.menu_principal = menu_principal

        self.menu = tk.Toplevel(menu_principal)

        if alfabeto_usado:
            self.imagen_japones_a_espanol = PhotoImage(file="menu_imagenes/japonesHiragana.png")
            self.imagen_espanol_a_japones = PhotoImage(file="menu_imagenes/españolHiragana.png")
        else:
            self.imagen_japones_a_espanol = PhotoImage(file="menu_imagenes/japonesKatakana.png")
            self.imagen_espanol_a_japones = PhotoImage(file="menu_imagenes/españolKatakana.png")

        self.menu.geometry("900x550+300+100")
        self.menu.resizable(False, False)
        self.menu.title("Modo")
        self.menu.iconbitmap("menu_imagenes/icono.ico")
        self.alfabeto = alfabeto_usado
        self.crear_interfaz()

    def japones_a_espanol(self):
        self.decision = True
        self.menu.destroy()
        CaracteresSelector(self.alfabeto, self.decision, self.menu_principal)

    def espanol_a_japones(self):
        self.decision = False
        self.menu.destroy()
        CaracteresSelector(self.alfabeto, self.decision, self.menu_principal)

    def crear_interfaz(self):

        hiragana_button = tk.Button(
            self.menu,
            command=self.japones_a_espanol,
            width=325, height=325, image=self.imagen_japones_a_espanol
        )
        hiragana_button.place(x=65, y=50)

        katakana_button = tk.Button(
            self.menu,
            command=self.espanol_a_japones,
            width=325, height=325, image=self.imagen_espanol_a_japones
        )
        katakana_button.place(x=500, y=50)


class CaracteresSelector:
    def __init__(self, decision_alfabeto, decision_modo, menu_principal):
        self.opcion_vocales = False
        self.opcion_basico = False
        self.opcion_compuesto = False
        self.opcion_combinado1 = False
        self.opcion_combinado2 = False

        self.opcion_vocales_var = tk.BooleanVar()
        self.opcion_basico_var = tk.BooleanVar()
        self.opcion_compuesto_var = tk.BooleanVar()
        self.opcion_combinado1_var = tk.BooleanVar()
        self.opcion_combinado2_var = tk.BooleanVar()

        self.menu_principal = menu_principal

        self.decisionAlfabeto = decision_alfabeto
        self.decisionModo = decision_modo
        self.caracteres = {}

        self.menu = tk.Toplevel(menu_principal)
        self.menu.title("Caracteres")
        self.menu.geometry("900x550+300+100")
        self.menu.resizable(False, False)
        self.menu.title("Menu")
        self.menu.iconbitmap("menu_imagenes/icono.ico")

        self.crear_interfaz()

    def toggle_opcion(self, opcion):
        if opcion == "Vocales":
            self.opcion_vocales = not self.opcion_vocales
        if opcion == "Basico":
            self.opcion_basico = not self.opcion_basico
        if opcion == "Compuesto":
            self.opcion_compuesto = not self.opcion_compuesto
        if opcion == "Combinado 1":
            self.opcion_combinado1 = not self.opcion_combinado1
        if opcion == "Combinado 2":
            self.opcion_combinado2 = not self.opcion_combinado2

    def continuar(self):
        self.menu.withdraw()
        self.seleccionar_caracteres()

    def crear_interfaz(self):
        opciones_frame = tk.Frame(self.menu)
        opciones_frame.pack(pady=20)

        opciones = [
            ("Vocales", self.opcion_vocales_var),
            ("Basico", self.opcion_basico_var),
            ("Compuesto", self.opcion_compuesto_var),
            ("Combinado 1", self.opcion_combinado1_var),
            ("Combinado 2", self.opcion_combinado2_var)
        ]

        checkbuttons = []

        for opcion, var in opciones:
            checkbutton = tk.Checkbutton(
                opciones_frame, text=opcion, command=lambda op=opcion: self.toggle_opcion(op),
                font=("Arial", 14), variable=var
            )
            checkbutton.pack(pady=5)
            checkbuttons.append(checkbutton)

        boton_frame = tk.Frame(self.menu)
        boton_frame.pack(pady=20)

        boton_continuar = tk.Button(
            boton_frame, text="Continuar", command=self.continuar, font=("Arial", 16), padx=20, pady=10
        )
        boton_continuar.pack()

        self.menu.geometry("900x550+300+100")

    def seleccionar_caracteres(self):
        if self.decisionAlfabeto:
            caracteres_usados = alfabeto.hiragana
        else:
            caracteres_usados = alfabeto.katakana

        if self.opcion_vocales:
            self.caracteres |= caracteres_usados.vocales
        if self.opcion_basico:
            self.caracteres |= caracteres_usados.basico
        if self.opcion_compuesto:
            self.caracteres |= caracteres_usados.compuesto
        if self.opcion_combinado1:
            self.caracteres |= caracteres_usados.combinado_1
        if self.opcion_combinado2:
            self.caracteres |= caracteres_usados.combinado_2

        self.iniciar_juego()

    def iniciar_juego(self):
        self.menu.destroy()
        juego.main(self.caracteres, self.decisionModo, self.decisionAlfabeto, self.menu_principal)


def main(alfabeto_usado, menu_principal):
    MenuJuego(alfabeto_usado, menu_principal)
