import tkinter as tk
from datetime import datetime
from tkinter import messagebox
import random
from datos import GestionDatos
from custom_message_box import custom_message_box


class Juego:
    def __init__(self, menu_principal):
        self.menu = None
        self.numeroErrores = 0
        self.errores = {}
        self.salida = True
        self.menu_principal = menu_principal
        self.num_letras_conseguidas = 0

    def jugar(self, caracteres, modo_juego, alfabeto_elegido, menu_principal):
        keys = list(caracteres.keys())
        indice_clave_actual = 0

        while indice_clave_actual < len(keys):
            indice_clave_actual += 1

        if modo_juego:
            self.japones_a_espanol(caracteres, alfabeto_elegido, menu_principal)
        else:
            self.espanol_a_japones(caracteres, alfabeto_elegido, menu_principal)

    def japones_a_espanol(self, caracteres, alfabeto_elegido, menu_principal):
        caracteres_copia = caracteres.copy()
        self.num_letras_conseguidas = 1

        while caracteres_copia and self.salida:
            self.crear_ventana(caracteres)

            caracter_al_azar = random.choice(list(caracteres_copia.items()))
            caracter_japones = caracter_al_azar[1]
            caracter_espanol = caracter_al_azar[0]

            respuesta_var = tk.StringVar()

            def submit():
                respuesta = respuesta_var.get()

                if respuesta == caracter_espanol:
                    del caracteres_copia[caracter_espanol]
                    self.num_letras_conseguidas += 1
                    self.menu.withdraw()
                else:
                    messagebox.showerror("Te has equivocado", f"La respuesta correcta era: {caracter_espanol}")
                    self.numeroErrores += 1
                    self.errores[caracter_espanol] = caracter_japones

                self.menu.destroy()
                respuesta_var.set("")

            respuesta_label = tk.Label(self.menu, text=f"¿Cual es el siguiente caracter?", font=("Arial", 20))
            letra_elegida = tk.Label(self.menu, text=f"{caracter_japones}", font=("Arial", 175))
            respuesta_entry = tk.Entry(self.menu, textvariable=respuesta_var, width=30)
            sub_btn = tk.Button(self.menu, text="Continuar", command=submit)

            respuesta_label.place(x=250, y=50)

            if len(caracter_japones) == 1:
                letra_elegida.place(x=300, y=125)
            else:
                letra_elegida.place(x=200, y=125)

            respuesta_entry.place(x=335, y=400)
            sub_btn.place(x=400, y=440)

            self.menu.wait_window()

        if self.salida:
            datos = GestionDatos()
            datos.guardar(self.numeroErrores, self.errores, alfabeto_elegido)
            self.repetir(caracteres, alfabeto_elegido, menu_principal, True, self.numeroErrores, self.errores)

    def espanol_a_japones(self, caracteres, alfabeto_elegido, menu_principal):
        respuesta = None
        caracteres_copia = caracteres.copy()
        self.num_letras_conseguidas = 1

        while caracteres and self.salida:

            self.crear_ventana(caracteres_copia)

            opciones_posibles = self.generar_opciones(caracteres_copia, caracteres)

            opcion_escogida = random.choice(opciones_posibles)
            while opcion_escogida[0] not in caracteres:
                opcion_escogida = random.choice(opciones_posibles)

            def respuesta_comprobar():
                e = opcion_escogida[1]
                v = opcion_escogida[0]
                if respuesta == opcion_escogida:
                    del caracteres[v]
                    self.num_letras_conseguidas += 1
                else:
                    messagebox.showerror("Te has equivocado", f"La respuesta correcta era: {e}")
                    self.numeroErrores += 1
                    self.errores[e] = v
                self.menu.destroy()

            def opcion_eleccion(eleccion):
                nonlocal respuesta
                respuesta = eleccion
                respuesta_comprobar()

            titulo_label = tk.Label(self.menu, text=f"Introduce el caracter correcto", font=("Arial", 20))
            opcion_escogida_label = tk.Label(self.menu, text=opcion_escogida[0], font=("Arial", 40))

            opcion_buttons = []
            for opcion in opciones_posibles:
                button = tk.Button(self.menu, text=opcion[1], font=("Arial", 30), height=2, width=4,
                                   command=lambda o=opcion: opcion_eleccion(o))
                opcion_buttons.append(button)

            titulo_label.place(x=275, y=50)
            opcion_escogida_label.place(x=425, y=125)

            x_positions = [100, 400, 700]
            for i in range(3):
                opcion_buttons[i].place(x=x_positions[i], y=250)

            self.menu.wait_window()

        if self.salida:
            datos = GestionDatos()
            datos.guardar(self.numeroErrores, self.errores, alfabeto_elegido)
            self.repetir(caracteres_copia, alfabeto_elegido, menu_principal, False, self.numeroErrores, self.errores)

    @staticmethod
    def generar_opciones(caracteres_copia, caracteres_originales):
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

    def repetir(self, caracteres, alfabeto_elegido, menu_principal, modo, numero_errores, errores):
        self.menu = tk.Toplevel(menu_principal)
        self.menu.geometry("900x550+300+100")
        self.menu.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.menu.resizable(False, False)
        self.menu.title("¿Quieres repetir?")
        self.menu.iconbitmap("menu_imagenes/icono.ico")

        # Agregar texto "¿Quieres repetir?" arriba del contenido con un tamaño de fuente más grande
        titulo_label = tk.Label(self.menu, text="¿Quieres repetir?", font=("Helvetica", 20))
        titulo_label.pack(pady=30)

        # Colocar los botones "Sí" y "No" en el centro uno al lado del otro
        botones_frame = tk.Frame(self.menu)
        botones_frame.pack()

        boton_si = tk.Button(botones_frame, text="Sí", width=15, height=2,
                             command=lambda: self.repetir_si(caracteres, alfabeto_elegido, menu_principal, modo),
                             font=("Helvetica", 14))
        boton_si.pack(side="left", padx=20)

        boton_no = tk.Button(botones_frame, text="No", width=15, height=2,
                             command=lambda: self.repetir_no(menu_principal),
                             font=("Helvetica", 14))
        boton_no.pack(side="right", padx=20)

        # Mostrar número de errores en un tamaño de fuente más grande
        errores_label = tk.Label(self.menu, text="Número de errores: " + str(numero_errores), font=("Helvetica", 16))
        errores_label.pack(pady=15)

        # Mostrar la fecha actual en un tamaño de fuente más grande
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        fecha_label = tk.Label(self.menu, text="Fecha actual: " + fecha_actual, font=("Helvetica", 16))
        fecha_label.pack(pady=15)

        # Agregar botón para ver los errores en forma de cuadro de mensaje
        def ver_errores():
            if not errores:
                custom_message_box("Errores", "No hay errores", 16)
            else:
                mensaje_errores = "\n".join([f"{clave}: {valor}" for clave, valor in errores.items()])
                custom_message_box("Errores", mensaje_errores, 16)

        boton_errores = tk.Button(self.menu, text="Ver Errores", width=20, height=2,
                                  command=ver_errores, font=("Helvetica", 14))
        boton_errores.pack(pady=30)

    def repetir_si(self, letras, alfabeto, menu_principal, modo):
        if modo:
            self.menu.destroy()
            self.japones_a_espanol(letras, alfabeto, menu_principal)
        else:
            self.menu.destroy()
            self.espanol_a_japones(letras, alfabeto, menu_principal)

    def repetir_no(self, menu_principal):
        self.menu.destroy()
        menu_principal.deiconify()

    def cerrar_ventana(self):
        self.salida = False
        self.menu.withdraw()
        self.menu.destroy()
        self.menu_principal.deiconify()

    def crear_contador(self, num_letras_conseguidas, num_letras_faltantes):
        contador_frame = tk.Frame(self.menu, bg="white")
        contador_frame.place(x=750, y=20)

        contador_label = tk.Label(contador_frame,
                                  text=f"{num_letras_conseguidas} / {num_letras_faltantes}",
                                  font=("Arial", 20))
        contador_label.pack()

        return contador_label

    def crear_ventana(self, num_letras_faltantes):
        self.menu = tk.Toplevel(self.menu_principal)
        self.menu.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.menu.geometry("900x550+300+100")
        self.menu.resizable(False, False)
        self.menu.title("Japones")
        self.menu.iconbitmap("menu_imagenes/icono.ico")
        self.crear_contador(self.num_letras_conseguidas, len(num_letras_faltantes))


def main(letras, modo_juego, alfabeto, menu_principal):
    juego = Juego(menu_principal)
    juego.jugar(letras, modo_juego, alfabeto, menu_principal)
