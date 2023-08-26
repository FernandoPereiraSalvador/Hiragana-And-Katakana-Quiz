import tkinter as tk
from datetime import datetime
from tkinter import messagebox
import random
import datos


class Juego:
    def __init__(self, menu_principal):
        self.numeroErrores = 0
        self.errores = {}
        self.salida = True
        self.menu_principal = menu_principal

    def boton_salida(self):
        self.salida = False
        self.caracteres = {}
        self.menu.destroy()
        self.menu_principal.deiconify()

    def jugar(self, caracteres, modoJuego, alfabeto_elegido, menu_principal):
        self.keys = list(caracteres.keys())
        self.index = 0

        while self.index < len(self.keys):
            key = self.keys[self.index]
            value = caracteres[key]
            print(key, ":", value)
            self.index += 1

        if modoJuego:
            self.japones_a_español(caracteres, alfabeto_elegido, menu_principal)
        else:
            self.español_a_japones(caracteres, alfabeto_elegido, menu_principal)

    def japones_a_español(self, caracteres, alfabeto_elegido, menu_principal):
        caracteres_copia = caracteres.copy()
        while caracteres_copia and self.salida:
            self.menu = tk.Toplevel(menu_principal)
            self.menu.geometry("900x550+300+100")
            self.menu.resizable(False, False)
            self.menu.title("Japones")
            self.menu.iconbitmap("menu_imagenes/icono.ico")

            caracter_al_azar = random.choice(list(caracteres_copia.items()))
            v = caracter_al_azar[1]
            e = caracter_al_azar[0]

            respuesta_var = tk.StringVar()

            def submit():
                respuesta = respuesta_var.get()

                if respuesta == e:
                    del caracteres_copia[e]
                    self.menu.withdraw()
                else:
                    ventana_error = messagebox.showerror("Te has equivocado", f"La respuesta correcta era: {e}")
                    self.numeroErrores += 1
                    self.errores[e] = v

                self.menu.destroy()
                respuesta_var.set("")

            respuesta_label = tk.Label(self.menu, text=f"¿Cual es el siguiente caracter?", font=("Arial", 20))
            letra_elegida = tk.Label(self.menu, text=f"{v}", font=("Arial", 175))
            respuesta_entry = tk.Entry(self.menu, textvariable=respuesta_var, width=30)
            salida_button = tk.Button(self.menu, text="Salir", command=self.boton_salida)
            sub_btn = tk.Button(self.menu, text="Submit", command=submit)

            respuesta_label.place(x=250, y=50)

            if len(v) == 1:
                letra_elegida.place(x=300, y=125)
            else:
                letra_elegida.place(x=200, y=125)

            respuesta_entry.place(x=335, y=400)
            sub_btn.place(x=400, y=440)
            salida_button.pack()

            self.menu.wait_window()

        if self.salida:
            datos.guardar(self.numeroErrores, self.errores, alfabeto_elegido)
            self.repetir(caracteres, alfabeto_elegido, menu_principal, True, self.numeroErrores)

    def español_a_japones(self, caracteres, alfabeto_elegido, menu_principal):
        respuesta = None
        caracteres_copia = caracteres.copy()

        while caracteres and self.salida:
            self.menu = tk.Toplevel(menu_principal)
            self.menu.geometry("900x550+300+100")
            self.menu.resizable(False, False)
            self.menu.title("Japones")
            self.menu.iconbitmap("menu_imagenes/icono.ico")

            opciones_posibles = self.generar_opciones(caracteres_copia,caracteres)

            opcion_escogida = random.choice(opciones_posibles)
            while opcion_escogida[0] not in caracteres:
                opcion_escogida = random.choice(opciones_posibles)

            def respuesta_comprobar():
                e = opcion_escogida[1]
                v = opcion_escogida[0]
                if respuesta == opcion_escogida:
                    e = opcion_escogida[1]
                    del caracteres[v]
                else:
                    ventana_error = messagebox.showerror("Te has equivocado", f"La respuesta correcta era: {e}")
                    self.numeroErrores += 1
                    self.errores[e] = v
                self.menu.destroy()

            def opcion_eleccion(opcion):
                nonlocal respuesta
                respuesta = opcion
                respuesta_comprobar()

            titulo_label = tk.Label(self.menu, text=f"Introduce el caracter correcto", font=("Arial", 20))
            opcion_escogida_label = tk.Label(self.menu, text=opcion_escogida[0], font=("Arial", 40))

            opcion_buttons = []
            for opcion in opciones_posibles:
                button = tk.Button(self.menu, text=opcion[1], font=("Arial", 30), height=2, width=4,
                                   command=lambda o=opcion: opcion_eleccion(o))
                opcion_buttons.append(button)

            salida_button = tk.Button(self.menu, text="Salir", command=self.boton_salida)

            titulo_label.place(x=275, y=50)
            opcion_escogida_label.place(x=425, y=125)

            x_positions = [100, 400, 700]
            for i in range(3):
                opcion_buttons[i].place(x=x_positions[i], y=250)

            salida_button.pack()
            self.menu.wait_window()

        if self:
            datos.guardar(self.numeroErrores, self.errores, alfabeto_elegido)
            self.repetir(caracteres, alfabeto_elegido, menu_principal, False, self.numeroErrores)

    def generar_opciones(self, caracteres_copia, caracteres_originales):
        opciones_posibles = []

        # Elegir un valor al azar de caracteres originales
        opcion_original = random.choice(list(caracteres_originales.items()))

        # Elegir dos valores al azar de caracteres copia que sean diferentes de la opción original
        opciones_copia = random.sample([item for item in caracteres_copia.items() if item != opcion_original], 2)

        opciones_posibles.extend(opciones_copia)
        opciones_posibles.append(opcion_original)

        # Mezclar las opciones
        random.shuffle(opciones_posibles)

        return opciones_posibles
    def repetir(self, caracteres, alfabeto_elegido, menu_principal, modo, numero_errores):
        self.menu = tk.Toplevel(menu_principal)
        self.menu.geometry("900x550+300+100")
        self.menu.resizable(False, False)
        self.menu.title("¿Quieres repetir?")
        self.menu.iconbitmap("menu_imagenes/icono.ico")

        # Agregar los botones "Sí" y "No"
        boton_si = tk.Button(self.menu, text="Sí", command=lambda: self.repetir_si(caracteres,alfabeto_elegido,menu_principal,modo))
        boton_si.pack(pady=20)
        boton_no = tk.Button(self.menu, text="No", command=lambda: self.repetir_no(menu_principal))
        boton_no.pack()

        # Mostrar número de errores
        errores_label = tk.Label(self.menu, text="Número de errores: " + str(numero_errores))
        errores_label.pack(pady=10)

        # Mostrar la fecha actual
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        fecha_label = tk.Label(self.menu, text="Fecha actual: " + fecha_actual)
        fecha_label.pack(pady=10)

    def repetir_si(self, caracteres, alfabeto_elegido, menu_principal, modo):
        if modo:
            self.menu.destroy()
            self.japones_a_español(caracteres, alfabeto_elegido, menu_principal)
        else:
            self.menu.destroy()
            self.español_a_japones(caracteres, alfabeto_elegido, menu_principal)

    def repetir_no(self, menu_principal):
        self.menu.destroy()
        menu_principal.deiconify()


def main(caracteres, modoJuego, alfabeto_elegido, menu_principal):
    juego = Juego(menu_principal)
    juego.jugar(caracteres, modoJuego, alfabeto_elegido, menu_principal)


if __name__ == "__main__":
    caracteres = {...}  # Define your character dictionary here
    modoJuego = True  # Set to True or False based on game mode
    alfabeto_elegido = "hiragana"  # Set the alphabet choice
    main(caracteres, modoJuego, alfabeto_elegido)
