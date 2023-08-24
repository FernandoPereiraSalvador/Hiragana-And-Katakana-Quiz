import tkinter as tk
from tkinter import PhotoImage
import alfabeto.hiragana
import alfabeto.katakana
import juego

class MenuJuego:
    def __init__(self,alfabetoUsado):
        self.decision = None

        self.menu = tk.Tk()
        self.menu.geometry("900x550+300+100")
        self.menu.resizable(False, False)
        self.menu.title("Modo")
        self.menu.iconbitmap("menu_imagenes/icono.ico")
        self.alfabeto = alfabetoUsado
        self.crear_interfaz()

    def japones_a_español(self):
        self.decision = True
        self.menu.destroy()

    def español_a_japones(self):
        self.decision = False
        self.menu.destroy()

    def crear_interfaz(self):
        if self.alfabeto:
            imagen_japones_a_español = PhotoImage(file="menu_imagenes/japonesHiragana.png")
        else:
            imagen_japones_a_español = PhotoImage(file="menu_imagenes/japonesKatakana.png")

        if self.alfabeto:
            imagen_español_a_japones = PhotoImage(file="menu_imagenes/españolHiragana.png")
        else:
            imagen_español_a_japones = PhotoImage(file="menu_imagenes/españolKatakana.png")

        hiragana_button = tk.Button(
            self.menu,
            command=self.japones_a_español,
            width=325, height=325, image=imagen_japones_a_español
        )
        hiragana_button.place(x=65, y=50)

        katakana_button = tk.Button(
            self.menu,
            command=self.español_a_japones,
            width=325, height=325, image=imagen_español_a_japones
        )
        katakana_button.place(x=500, y=50)

        self.menu.mainloop()

class CaracteresSelector:
    def __init__(self, decisionAlfabeto, decisionModo):
        self.opcion_vocales = False
        self.opcion_basico = False
        self.opcion_compuesto = False
        self.opcion_combinado1 = False
        self.opcion_combinado2 = False

        self.decisionAlfabeto = decisionAlfabeto
        self.decisionModo = decisionModo
        self.caracteres = {}

        self.menu = tk.Tk()
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
        self.menu.destroy()
        self.seleccionar_caracteres()

    def crear_interfaz(self):
        opciones_frame = tk.Frame(self.menu)
        opciones_frame.pack(pady=20)

        opciones = ["Vocales", "Basico", "Compuesto", "Combinado 1", "Combinado 2"]
        checkbuttons = []

        for opcion in opciones:
            checkbutton = tk.Checkbutton(
                opciones_frame, text=opcion, command=lambda op=opcion: self.toggle_opcion(op),
                font=("Arial", 14)
            )
            checkbutton.pack(pady=5)
            checkbuttons.append(checkbutton)

        boton_frame = tk.Frame(self.menu)
        boton_frame.pack(pady=20)

        boton_continuar = tk.Button(
            boton_frame, text="Continuar", command=self.continuar, font=("Arial", 16), padx=20, pady=10
        )
        boton_continuar.pack()

        self.menu.update_idletasks()
        self.menu.geometry("900x550+300+100")
        self.menu.mainloop()

    def seleccionar_caracteres(self):
        if self.decisionAlfabeto:
            caracteres_usados = alfabeto.hiragana
        else:
            caracteres_usados = alfabeto.katakana

        if self.opcion_vocales: self.caracteres |= caracteres_usados.vocales
        if self.opcion_basico: self.caracteres |= caracteres_usados.basico
        if self.opcion_compuesto: self.caracteres |= caracteres_usados.compuesto
        if self.opcion_combinado1: self.caracteres |= caracteres_usados.combinado_1
        if self.opcion_combinado2: self.caracteres |= caracteres_usados.combinado_2

        self.iniciar_juego()

    def iniciar_juego(self):
        juego.main(self.caracteres, self.decisionModo, self.decisionAlfabeto)

def main(alfabetoUsado):
    modo_selector = MenuJuego(alfabetoUsado)
    caracteres_selector = CaracteresSelector(alfabetoUsado, modo_selector.decision)

if __name__ == "__main__":
    main()
else:
    print("error")