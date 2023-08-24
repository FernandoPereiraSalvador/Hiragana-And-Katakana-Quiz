import tkinter as tk
from tkinter import messagebox
import random
import datos

class Juego:
    def __init__(self):
        self.numeroErrores = 0
        self.errores = {}
        self.salida = True

    def boton_salida(self):
        self.salida = False
        self.caracteres = {}
        self.menu.destroy()
        from main import main
        main()

    def jugar(self, caracteres, modoJuego, alfabeto_elegido):
        self.keys = list(caracteres.keys())
        self.index = 0

        while self.index < len(self.keys):
            key = self.keys[self.index]
            value = caracteres[key]
            print(key, ":", value)
            self.index += 1

        if modoJuego:
            self.japones_a_español(caracteres, alfabeto_elegido)
        else:
            self.español_a_japones(caracteres, alfabeto_elegido)

    def japones_a_español(self, caracteres, alfabeto_elegido):
        while caracteres and self.salida:
            self.menu = tk.Tk()
            self.menu.geometry("900x550+300+100")
            self.menu.resizable(False, False)
            self.menu.title("Japones")
            self.menu.iconbitmap("menu_imagenes/icono.ico")

            caracter_al_azar = random.choice(list(caracteres.items()))
            v = caracter_al_azar[1]
            e = caracter_al_azar[0]

            respuesta_var = tk.StringVar()

            def submit():
                respuesta = respuesta_var.get()

                if respuesta == e:
                    del caracteres[e]
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
            letra_elegida.place(x=300, y=125)
            respuesta_entry.place(x=335, y=400)
            sub_btn.place(x=400, y=440)
            salida_button.pack()

            self.menu.mainloop()

        datos.guardar(self.numeroErrores, self.errores, alfabeto_elegido)

    def español_a_japones(self, caracteres, alfabeto_elegido):
        respuesta = None

        while caracteres and self.salida:
            self.menu = tk.Tk()
            self.menu.geometry("900x550+300+100")
            self.menu.resizable(False, False)
            self.menu.title("Japones")
            self.menu.iconbitmap("menu_imagenes/icono.ico")

            opciones_posibles = self.generar_opciones(caracteres)

            opcion_escogida = opciones_posibles[0]

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

            self.menu.mainloop()

        datos.guardar(self.numeroErrores, self.errores, alfabeto_elegido)

    def generar_opciones(self, caracteres):
        copia_caracteres_juego = caracteres.copy()
        opciones_posibles = []

        while len(opciones_posibles) < 3:
            opcion_key = random.choice(list(copia_caracteres_juego.keys()))
            opcion_value = copia_caracteres_juego[opcion_key]
            opciones_posibles.append((opcion_key, opcion_value))
            del copia_caracteres_juego[opcion_key]

        random.shuffle(opciones_posibles)
        return opciones_posibles

def main(caracteres, modoJuego, alfabeto_elegido):
    juego = Juego()
    juego.jugar(caracteres, modoJuego, alfabeto_elegido)

if __name__ == "__main__":
    caracteres = {...}  # Define your character dictionary here
    modoJuego = True  # Set to True or False based on game mode
    alfabeto_elegido = "hiragana"  # Set the alphabet choice
    main(caracteres, modoJuego, alfabeto_elegido)
