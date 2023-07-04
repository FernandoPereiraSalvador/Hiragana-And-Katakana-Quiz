import tkinter as tk
from tkinter import PhotoImage, messagebox
import random

# japones a español: true
# español a japones: false
import main


def jugar(caracteres, modoJuego):
    keys = list(caracteres.keys())
    index = 0

    while index < len(keys):
        key = keys[index]
        value = caracteres[key]
        print(key, ":", value)
        index += 1

    if modoJuego:
        print('hola')
        japones_a_español(caracteres)
    else:
        print('hola3')
        español_a_japones(caracteres)


def japones_a_español(caracteres):
    while caracteres:

        print('hola')
        menu = tk.Tk()
        menu.geometry("900x550+300+100")
        menu.resizable(False, False)
        menu.title("Japones")
        menu.iconbitmap("menu_imagenes/icono.ico")

        def boton_salida():
            global salida, caracteres
            salida = "salir"
            caracteres = {}
            menu.destroy()
            main.menu_principal()
            breakpoint()

        caracter_al_azar = random.choice(list(caracteres.items()))

        print(caracter_al_azar)
        v = caracter_al_azar[1]
        e = caracter_al_azar[0]

        respuesta_var = tk.StringVar()

        def submit():
            global numero_de_errores
            global errores
            numero_de_errores = 0
            errores = {}

            respuesta = respuesta_var.get()

            print("La respuesta es: " + respuesta)
            if (respuesta == e):

                print("Has acertado")
                del caracteres[e]

            else:
                ventana_error = messagebox.showerror("Te has equivocado", f"La respuesta correcta era: {e}")
                numero_de_errores += 1
                errores[e] = v

            menu.destroy()

            respuesta_var.set("")

        respuesta_label = tk.Label(menu, text=f"¿Cual es el siguiente caracter?", font=("Arial", 20))
        letra_elegida = tk.Label(menu, text=f"{v}", font=("Arial", 175))
        respuesta_entry = tk.Entry(menu, textvariable=respuesta_var, width=30)
        salida_button = tk.Button(menu, text="Salir", command=lambda: [boton_salida(), menu.destroy()])
        salida_button.pack()
        sub_btn = tk.Button(menu, text="Submit", command=submit)

        respuesta_label.place(x=250, y=50)
        letra_elegida.place(x=300, y=125)
        respuesta_entry.place(x=335, y=400)
        sub_btn.place(x=400, y=440)
        menu.mainloop()


def español_a_japones(caracteres):
    respuesta = None
    while caracteres:

        def boton_salida():
            global salida, caracteres, respuesta
            salida = "salir"
            caracteres = {}
            menu.destroy()
            main.menu_principal()
            breakpoint()

        menu = tk.Tk()
        menu.geometry("900x550+300+100")
        menu.resizable(False, False)
        menu.title("Japones")
        menu.iconbitmap("menu_imagenes/icono.ico")

        caracter_al_azar = random.choice(list(caracteres.items()))
        v = caracter_al_azar[1]

        opcion_1 = random.choice(list(caracteres.items()))
        opcion_2 = random.choice(list(caracteres.items()))
        opcion_3 = random.choice(list(caracteres.items()))

        opciones_posibles = dict([opcion_1] + [opcion_2] + [opcion_3])
        opcion_escogida = random.choice(list(opciones_posibles.items()))

        def respuesta_comprobar():
            global numero_de_errores, errores, respuesta
            numero_de_errores = 0
            errores = {}
            e = opcion_escogida[1]
            v = opcion_escogida[0]
            if respuesta == opcion_escogida:
                e = opcion_escogida[1]
                del caracteres[v]
            else:
                ventana_error = messagebox.showerror("Te has equivocado", f"La respuesta correcta era: {e}")
                numero_de_errores += 1
                errores[e] = v
            menu.destroy()

        def opcion_1_eleccion():
            global respuesta
            respuesta = opcion_1
            print(f"La respuesta es {respuesta}")
            respuesta_comprobar()

        def opcion_2_eleccion():
            global respuesta
            respuesta = opcion_2
            print(f"La respuesta es {respuesta}")
            respuesta_comprobar()

        def opcion_3_eleccion():
            global respuesta
            respuesta = opcion_3
            print(f"La respuesta es {respuesta}")
            respuesta_comprobar()

        # imagen_salida = PhotoImage(file="menu_imagenes/salida.png")

        titulo_label = tk.Label(menu, text=f"Introduce el caracter correcto", font=("Arial", 20))
        opcion_escogida_label = tk.Label(menu, text=opcion_escogida[0], font=("Arial", 40))

        opcion_1_button = tk.Button(menu, text=opcion_1[1], font=("Arial", 30), height=2, width=4,
                                    command=lambda: [opcion_1_eleccion()])
        opcion_2_button = tk.Button(menu, text=opcion_2[1], font=("Arial", 30), height=2, width=4,
                                    command=lambda: [opcion_2_eleccion()])
        opcion_3_button = tk.Button(menu, text=opcion_3[1], font=("Arial", 30), height=2, width=4,
                                    command=lambda: [opcion_3_eleccion()])
        salida_button = tk.Button(menu, text="Salir", command=lambda: [boton_salida(), menu.destroy()])

        titulo_label.place(x=275, y=50)
        opcion_escogida_label.place(x=425, y=125)
        opcion_1_button.place(x=100, y=250)
        opcion_2_button.place(x=400, y=250)
        opcion_3_button.place(x=700, y=250)
        salida_button.pack()

        print(f"La respuesta era {respuesta} y la opcion elegida {opcion_escogida}")
        print(caracteres)

        menu.mainloop()
