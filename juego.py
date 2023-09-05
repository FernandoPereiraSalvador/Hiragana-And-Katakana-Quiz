import tkinter as tk
from datetime import datetime
from tkinter import messagebox
import random
from datos import GestionDatos
from custom_message_box import custom_message_box


class Juego:
    """
    Clase que representa el juego de aprendizaje de caracteres japoneses.

    Esta clase implementa el juego de aprendizaje de caracteres japoneses. Los caracteres se presentan al jugador,
    quien debe adivinar su significado en diferentes modos de juego: 'japonés a español' o 'español a japonés'.

    Atributos:
    - menu (None or Tkinter object): Almacena la ventana de juego en la que se mostrarán los caracteres y respuestas.
    - numeroErrores (int): Contador del número de errores cometidos durante la partida actual.
    - errores (dict): Diccionario que registra los errores cometidos, donde las claves son los caracteres japoneses
    equivocados y los valores son sus significados.
    - salida (bool): Indica si el juego ha terminado. Si es True, el juego continúa; si es False, el juego se detiene.
    - menu_principal (Tkinter object): Objeto Tkinter de la ventana principal del programa desde la cual se invocó el
    juego.
    - num_letras_conseguidas (int): Número de letras acertadas por el jugador en la partida actual, utilizado para
    el seguimiento del progreso.

    Métodos:
    - __init__(self, menu_principal): Inicializa una nueva instancia del juego.
    - jugar(self, caracteres, modo_juego, alfabeto_elegido, menu_principal): Inicia el juego de aprendizaje.
    - japones_a_espanol(self, caracteres, alfabeto_elegido, menu_principal): Inicia el juego en el modo japonés a
    español.
    - espanol_a_japones(self, caracteres, alfabeto_elegido, menu_principal): Inicia el juego en el modo español a
    japonés.
    - generar_opciones(caracteres_copia, caracteres_originales): Genera una lista de opciones posibles para el juego de
    traducción.
    - repetir(self, caracteres, alfabeto_elegido, menu_principal, modo, numero_errores, errores): Muestra una ventana
    emergente que pregunta al jugador si desea repetir el juego.
    - repetir_si(self, letras, alfabeto, menu_principal, modo): Reinicia el juego para continuar jugando.
    - repetir_no(self, menu_principal): Finaliza el juego y muestra el menú principal.
    - cerrar_ventana(self): Cierra la ventana de juego y restaura la ventana principal.
    - crear_contador(self, num_letras_conseguidas, num_letras_faltantes): Crea y muestra un contador de progreso en la
    ventana de juego.
    - crear_ventana(self, num_letras_faltantes): Crea y muestra una nueva ventana de juego.
    """

    def __init__(self, menu_principal):
        """
        Inicia una nueva instancia del juego.

        Esta función inicializa una nueva instancia del juego con los valores y atributos iniciales necesarios para
        el funcionamiento del juego.

        Parámetros:
        :param menu_principal: Objeto Tkinter de la ventana principal del programa desde la cual se está
        invocando el juego.

        Atributos:
        - menu (None or Tkinter object): Almacena la ventana de juego en la que se mostrarán los caracteres y
        respuestas.
        - numeroErrores (int): Contador del número de errores cometidos durante la partida actual.
        - errores (dict): Diccionario que registra los errores cometidos, donde las claves son los caracteres japoneses
        equivocados y los valores son sus significados.
        - salida (bool): Indica si el juego ha terminado o no. Si es True, el juego continúa; si es False, el juego se
        detiene.
        - menu_principal (Tkinter object): Objeto Tkinter de la ventana principal del programa desde la cual se invocó
        el juego.
        - num_letras_conseguidas (int): Número de letras acertadas por el jugador en la partida actual, utilizado para
        el seguimiento del progreso.

        Detalles:
        La función establece los atributos iniciales para rastrear el estado del juego. El atributo 'menu'
        se utiliza para almacenar la ventana de juego. 'numeroErrores' y 'errores' se utilizan para llevar un
        registro de los errores cometidos. 'salida' se utiliza para controlar si el juego está en curso.
        'menu_principal' se guarda para restaurar la ventana principal cuando se cierre la ventana del juego.
        'num_letras_conseguidas' se utiliza para rastrear el progreso del jugador durante la partida.

        :return: None
        """
        self.menu = None
        self.numeroErrores = 0
        self.errores = {}
        self.salida = True
        self.menu_principal = menu_principal
        self.num_letras_conseguidas = 0

    def jugar(self, caracteres, modo_juego, alfabeto_elegido, menu_principal):
        """
        Inicia el juego de aprendizaje de caracteres japoneses.

        Esta función inicia el juego de aprendizaje de caracteres japoneses. Los caracteres se presentan al jugador,
        quien debe adivinar su significado cos dos modos: 'modo japonés a español' o 'modo español a japonés'.

        Parámetros:
        :param caracteres: Un diccionario de caracteres japoneses como claves y sus significados o
        pronunciaciones como valores.
        :param modo_juego: Un valor booleano que indica si el juego se ejecuta en modo
        japonés a español (True) o español a japonés (False).
        :param alfabeto_elegido: El alfabeto elegido para el
        juego, como hiragana o katakana.
        :param menu_principal: Objeto Tkinter de la ventana principal del programa.

        Detalles:
        La función recibe el diccionario 'caracteres' que contiene los caracteres japoneses y sus
        significados o pronunciaciones. 'modo_juego' determina el modo de juego (japonés a español o español a
        japonés). 'alfabeto_elegido' especifica el alfabeto seleccionado para el juego.

        La función itera a través de los caracteres presentados en el diccionario 'caracteres', mostrando cada uno al
        jugador. Dependiendo del modo de juego, llama a la función 'japones_a_espanol' o 'espanol_a_japones' para
        manejar la interacción y la validación de respuestas.

        :return: None
        """

        # Obtener las claves (caracteres) del diccionario de caracteres
        keys = list(caracteres.keys())
        indice_clave_actual = 0

        # Iterar a través de las claves (caracteres)
        while indice_clave_actual < len(keys):
            indice_clave_actual += 1

        # Dependiendo del modo de juego, llamar a la función correspondiente
        if modo_juego:
            self.japones_a_espanol(caracteres, alfabeto_elegido, menu_principal)
        else:
            self.espanol_a_japones(caracteres, alfabeto_elegido, menu_principal)

    def japones_a_espanol(self, caracteres, alfabeto_elegido, menu_principal):
        """
        Inicia el juego en el modo japonés a español.

        Donde se muestran caracteres japoneses y el jugador debe adivinar su significado en español.

        Parámetros:
        :param caracteres: Un diccionario de caracteres japoneses como claves y sus significados como valores.
        :param alfabeto_elegido: El alfabeto elegido para el juego, como hiragana o katakana.
        :param menu_principal: Objeto Tkinter de la ventana principal del programa.

        Detalles:
        La función recibe el diccionario 'caracteres' que contiene caracteres japoneses y sus significados
        en español. 'alfabeto_elegido' especifica el alfabeto seleccionado para el juego, y 'menu_principal' es el
        objeto Tkinter de la ventana principal del programa.

        La función itera a través de los caracteres presentados en el diccionario 'caracteres', mostrando cada uno al
        jugador. El jugador debe adivinar el significado en español del carácter japonés presentado. Si la respuesta
        es correcta, el carácter se elimina del diccionario y el jugador avanza al siguiente. Si la respuesta es
        incorrecta, se muestra un mensaje de error y se almacena la respuesta incorrecta en el diccionario de errores.

        Luego de completar todos los caracteres o si el jugador decide salir, se guardan los datos de progreso
        utilizando la instancia de la clase 'GestionDatos' y se ofrece la opción de repetir el juego o volver al menú
        principal.

        :return: None
        """
        caracteres_copia = caracteres.copy()
        self.num_letras_conseguidas = 1
        self.numeroErrores = 0
        self.errores = {}

        def submit():
            """
            Procesa la respuesta del jugador y maneja la lógica del juego.

            Esta función se activa cuando el jugador hace clic en el botón "Continuar" para enviar su respuesta.
            Procesa la respuesta ingresada por el jugador y determina si es correcta o incorrecta. En caso de
            respuesta incorrecta, se muestra un mensaje de error con la respuesta correcta. En caso de respuesta
            correcta, se actualiza el juego, eliminando el carácter actual del diccionario de caracteres a
            adivinar.

            Detalles: La función obtiene la respuesta ingresada por el jugador utilizando la variable
            `respuesta_var`. Luego, compara la respuesta con el significado en español del carácter japonés
            presentado (`caracter_espanol`). Si la respuesta es correcta, se elimina el carácter del diccionario
            de caracteres a adivinar (`caracteres_copia`), se actualiza el número de letras conseguidas y se
            oculta la ventana del juego actual (`self.menu`).

            Si la respuesta es incorrecta, se muestra un mensaje de error utilizando la función
            `messagebox.showerror`, indicando la respuesta correcta en español. Además, se incrementa el número
            de errores y se agrega el carácter japonés a la lista de errores (`self.errores`).

            Finalmente, se destruye la ventana del juego actual y se restablece la variable `respuesta_var` a una
            cadena vacía.

            :return: None
            """
            # Obtener la respuesta ingresada por el jugador desde la variable respuesta_var
            respuesta = respuesta_var.get()

            # Comprobar si la respuesta del jugador es correcta
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

        # Bucle principal del juego
        while caracteres_copia and self.salida:
            # Crear la ventana del juego y mostrar el carácter japonés
            self.crear_ventana(caracteres)

            # Elegir un carácter al azar para adivinar
            caracter_al_azar = random.choice(list(caracteres_copia.items()))
            caracter_japones = caracter_al_azar[1]
            caracter_espanol = caracter_al_azar[0]

            respuesta_var = tk.StringVar()

            # Crear elementos de la ventana: etiquetas, entrada y botón "Continuar"
            respuesta_label = tk.Label(self.menu, text=f"¿Cuál es el siguiente carácter?", font=("Arial", 20))
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

            # Esperar hasta que el jugador responda o cierre la ventana
            self.menu.wait_window()

        # Si el juego no ha sido detenido y no quedan caracteres por adivinar
        if self.salida:
            # Guardar datos y dar la opción de repetir el juego
            datos = GestionDatos()
            datos.guardar(self.numeroErrores, self.errores, alfabeto_elegido)
            self.repetir(caracteres, alfabeto_elegido, menu_principal, True, self.numeroErrores, self.errores)

    def espanol_a_japones(self, caracteres, alfabeto_elegido, menu_principal):
        """
        Inicia el modo de juego de traducción de español a japonés.

        Esta función implementa el modo de juego en el que el jugador debe traducir palabras o frases del
        español al japonés. Muestra una ventana con una palabra o frase en español y varias opciones en japonés,
        de las cuales el jugador debe elegir la traducción correcta.

        Parámetros:
        :param caracteres: Un diccionario de palabras/frases en español y sus traducciones en japonés.
        :param alfabeto_elegido: El alfabeto elegido para el juego (hiragana o katakana).
        :param menu_principal: Objeto Tkinter de la ventana principal del programa.

        Detalles:
        La función inicializa variables y ajusta la configuración para el modo de juego.
        Luego, inicia un ciclo en el cual se presentan palabras/frases en español junto con varias opciones
        en japonés. El jugador debe seleccionar la opción correcta y se verifica su respuesta.

        Si el jugador elige correctamente, se elimina la palabra/frase del diccionario de caracteres a adivinar
        (`caracteres`). Si elige incorrectamente, se muestra un mensaje de error con la respuesta correcta.

        Al finalizar el juego, se guardan los datos de progreso y se ofrece al jugador la opción de repetir el juego.

        :return: None
        """

        def respuesta_comprobar():
            """
            Comprueba la respuesta del jugador y actualiza el juego en consecuencia.

            Esta función se activa cuando el jugador selecciona una opción en japonés como su respuesta.
            Verifica si la respuesta es correcta y realiza las actualizaciones necesarias en función del resultado.

            Detalles:
            La función toma la opción elegida por el jugador (`opcion_escogida`) y extrae la traducción
            en español (`caracter_espanol`) y la traducción en japonés (`caracter_japones`). Luego, compara la
            respuesta del jugador con la opción escogida para determinar si es correcta.

            Si la respuesta es correcta, se elimina la palabra/frase del diccionario de caracteres (`caracteres`),
            se incrementa el contador de letras conseguidas y se cierra la ventana de juego (`menu`).

            Si la respuesta es incorrecta, se muestra un mensaje de error con la respuesta correcta en español y se
            actualizan las estadísticas de errores. Luego, se cierra la ventana de juego.

            :return: None
            """
            # Extraer la traducción en español y la traducción en japonés de la opción escogida
            caracter_espanol = opcion_escogida[1]
            caracter_japones = opcion_escogida[0]

            # Verificar si la respuesta del jugador es correcta
            if respuesta == opcion_escogida:
                del caracteres[caracter_japones]
                self.num_letras_conseguidas += 1
            else:
                messagebox.showerror("Te has equivocado", f"La respuesta correcta era: {caracter_espanol}")
                self.numeroErrores += 1
                self.errores[caracter_espanol] = caracter_japones

            # Cerrar la ventana del juego actual
            self.menu.destroy()

        def opcion_eleccion(eleccion):
            """
            Procesa la elección del jugador y llama a la función para comprobar la respuesta.

            Esta función se activa cuando el jugador elige una opción en español como su respuesta.
            Captura la opción seleccionada y llama a la función `respuesta_comprobar()` para verificar la respuesta.

            Parámetros:
            :param eleccion: La opción elegida por el jugador.

            Detalles:
            La función toma la opción elegida por el jugador como parámetro (`eleccion`) y la asigna
            a la variable no local `respuesta`. Luego, llama a la función `respuesta_comprobar()` para
            realizar la comprobación y actualización del juego en función de la respuesta.

            :return: None
            """
            nonlocal respuesta  # Acceder a la variable 'respuesta' fuera del ámbito de la función
            respuesta = eleccion  # Asignar la opción elegida como respuesta
            respuesta_comprobar()  # Llamar a la función para comprobar la respuesta del jugador

        respuesta = None
        caracteres_copia = caracteres.copy()
        self.numeroErrores = 0
        self.errores = {}

        # Inicializa el contador de letras conseguidas en 1, ya que el jugador aún no ha adivinado ninguna.
        # Se inicia en 1 en lugar de 0 para que el marcador de letras actual esté adelantado por 1,
        # de manera que coincida con la primera letra que se presenta al jugador.
        self.num_letras_conseguidas = 1

        while caracteres and self.salida:

            # Crea la ventana de juego y presenta las opciones
            self.crear_ventana(caracteres_copia)

            # Genera las opciones posibles para la traducción en japonés
            opciones_posibles = self.generar_opciones(caracteres_copia, caracteres)

            # Elige una opción al azar para presentar al jugador
            opcion_escogida = random.choice(opciones_posibles)
            while opcion_escogida[0] not in caracteres:
                opcion_escogida = random.choice(opciones_posibles)

            # Configuración de la ventana de juego y opciones
            titulo_label = tk.Label(self.menu, text=f"Introduce el carácter correcto", font=("Arial", 20))
            opcion_escogida_label = tk.Label(self.menu, text=opcion_escogida[0], font=("Arial", 40))

            opcion_buttons = []
            for opcion in opciones_posibles:
                button = tk.Button(self.menu, text=opcion[1], font=("Arial", 30), height=2, width=4,
                                   command=lambda o=opcion: opcion_eleccion(o))
                opcion_buttons.append(button)

            # Posicionamiento de elementos en la ventana de juego
            titulo_label.place(x=275, y=50)
            opcion_escogida_label.place(x=425, y=125)

            x_positions = [100, 400, 700]
            for i in range(3):
                opcion_buttons[i].place(x=x_positions[i], y=250)

            self.menu.wait_window()

        # Si el juego no ha sido detenido y no quedan caracteres por adivinar
        if self.salida:
            # Guardar datos y ofrecer repetir el juego
            datos = GestionDatos()
            datos.guardar(self.numeroErrores, self.errores, alfabeto_elegido)
            self.repetir(caracteres_copia, alfabeto_elegido, menu_principal, False, self.numeroErrores, self.errores)

    @staticmethod
    def generar_opciones(caracteres_copia, caracteres_originales):
        """
        Genera una lista de opciones posibles para el juego de traducción.

        Esta función crea una lista de opciones posibles para que el jugador elija durante el juego
        de traducción de español a japonés. Estas opciones incluyen dos caracteres seleccionados al azar
        de los caracteres copia y uno de los caracteres originales.

        Parámetros:
        :param caracteres_copia: Un diccionario que contiene los caracteres disponibles para el juego.
        :param caracteres_originales: Un diccionario que contiene todos los caracteres originales.

        Detalles:
        La función elige al azar una opción original del diccionario de caracteres originales.
        Luego, selecciona dos opciones al azar del diccionario de caracteres copia, asegurándose de que
        sean diferentes de la opción original. Estas opciones se combinan en una lista llamada `opciones_copia`.

        Finalmente, la opción original se agrega a la lista `opciones_copia`, y la lista resultante se
        mezcla al azar utilizando `random.shuffle()` para asegurar que las opciones no estén en un orden predecible.

        :return: Una lista de opciones posibles para que el jugador elija durante el juego.
        """
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
        """
        Muestra una ventana emergente que pregunta al jugador si desea repetir el juego.

        Esta función crea una ventana emergente que pregunta al jugador si desea repetir el juego
        con los mismos caracteres y configuración. El jugador puede elegir "Sí" o "No" en función
        de su elección.

        Parámetros:
        :param caracteres: Un diccionario que contiene los caracteres para el juego.
        :param alfabeto_elegido: El alfabeto elegido para el juego (hiragana o katakana).
        :param menu_principal: Objeto Tkinter de la ventana principal del programa.
        :param modo: Un valor booleano que indica el modo de juego (True para japonés a español, False para español a
        japonés).
        :param numero_errores: El número de errores cometidos durante el juego.
        :param errores: Un diccionario que contiene los errores cometidos y sus valores.

        Detalles:
        La función crea una nueva ventana emergente utilizando `Toplevel`, con el título "¿Quieres repetir?"
        y un tamaño fijo. Se agregan etiquetas para mostrar el texto "¿Quieres repetir?", el número de errores
        cometidos y la fecha actual. Luego, se colocan dos botones "Sí" y "No" en el centro de la ventana.

        Los botones "Sí" y "No" están asociados a las funciones `repetir_si()` y `repetir_no()` respectivamente,
        que manejan la lógica de repetir el juego o regresar al menú principal.

        :return: None
        """

        def ver_errores():
            """
            Muestra una ventana emergente con los errores cometidos durante el juego.

            Esta función crea una ventana emergente que muestra los errores cometidos durante el juego.
            Si no hay errores, se muestra un mensaje indicando que no hay errores. Si hay errores, se
            muestra una lista de errores en formato clave-valor.

            Detalles:
            La función verifica si hay errores en el diccionario `errores`. Si no hay errores,
            se muestra un cuadro de mensaje con el título "Errores" y el mensaje "No hay errores".

            Si hay errores, se genera un mensaje con el formato "clave: valor" para cada par clave-valor
            en el diccionario de errores. Luego, se muestra un cuadro de mensaje con el título "Errores"
            y el mensaje que contiene la lista de errores formateados.

            :return: None
            """
            if not errores:
                custom_message_box("Errores", "No hay errores", 16)
            else:
                # Generar un mensaje con los errores en formato clave: valor
                mensaje_errores = "\n".join([f"{clave}: {valor}" for clave, valor in errores.items()])
                custom_message_box("Errores", mensaje_errores, 16)

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

        boton_errores = tk.Button(self.menu, text="Ver Errores", width=20, height=2,
                                  command=ver_errores, font=("Helvetica", 14))
        boton_errores.pack(pady=30)

    def repetir_si(self, letras, alfabeto, menu_principal, modo):
        """
        Reinicia el juego para continuar jugando.

        Esta función reinicia el juego para continuar jugando con los mismos parámetros que
        se utilizaron en la partida anterior. Puede reiniciar el juego en modo japonés-español
        o español-japonés, según el modo en que se estaba jugando.

        Parámetros:
        :param letras: El diccionario de letras o caracteres a utilizar en el juego.
        :param alfabeto: El alfabeto elegido para el juego (hiragana o katakana).
        :param menu_principal: Objeto Tkinter de la ventana principal del programa.
        :param modo: Indicador del modo de juego (True para japonés-español, False para español-japonés).

        Detalles:
        La función destruye la ventana actual del juego utilizando el método `destroy()`, lo que
        cierra la ventana emergente del juego actual.

        Luego, si el modo es japonés-español (`True`), llama a la función `japones_a_espanol` para
        iniciar un nuevo juego en modo japonés-español. Si el modo es español-japonés (`False`),
        llama a la función `espanol_a_japones` para iniciar un nuevo juego en modo español-japonés.

        :return: None
        """
        if modo:
            self.menu.destroy()
            self.japones_a_espanol(letras, alfabeto, menu_principal)
        else:
            self.menu.destroy()
            self.espanol_a_japones(letras, alfabeto, menu_principal)

    def repetir_no(self, menu_principal):
        """
        Finaliza el juego y muestra el menú principal.

        Esta función finaliza el juego y muestra nuevamente el menú principal del programa.
        Se invoca cuando el jugador decide no repetir el juego y regresar al menú principal.

        Parámetros:
        :param menu_principal: Objeto Tkinter de la ventana principal del programa.

        Detalles:
        La función destruye la ventana actual del juego utilizando el método `destroy()`, lo que
        cierra la ventana emergente del juego actual.

        Luego, utiliza el método `deiconify()` en el objeto `menu_principal` para restaurar la
        visibilidad y el enfoque en la ventana principal del programa.

        :return: None
        """
        self.menu.destroy()
        menu_principal.deiconify()

    def cerrar_ventana(self):
        """
        Cierra la ventana de juego y restaura la ventana principal.

        Esta función se invoca cuando el jugador decide cerrar la ventana de juego en medio de una partida.
        Cierra la ventana del juego actual, restaura la visibilidad de la ventana principal y detiene la partida.

        Detalles:
        La función establece el atributo `salida` en `False`, lo que detiene la partida actual. Luego, utiliza
        los métodos `withdraw()` y `destroy()` en el objeto `menu` para cerrar la ventana de juego actual.

        Finalmente, utiliza `deiconify()` en el objeto `menu_principal` para restaurar la visibilidad de la
        ventana principal que pudo haber sido ocultada cuando se abrió la ventana de juego.

        :return: None
        """
        self.salida = False
        self.menu.withdraw()
        self.menu.destroy()
        self.menu_principal.deiconify()

    def crear_contador(self, num_letras_conseguidas, num_letras_faltantes):
        """
        Crea y muestra un contador de progreso en la ventana de juego.

        Esta función crea y muestra un contador de progreso en la ventana de juego actual.
        El contador muestra la cantidad de letras conseguidas y el total de letras faltantes
        en el juego.

        Parámetros:
        :param num_letras_conseguidas: El número de letras conseguidas hasta el momento.
        :param num_letras_faltantes: El número total de letras faltantes en el juego.

        Detalles:
        La función crea un marco (`contador_frame`) en la ventana de juego donde se mostrará
        el contador. Luego, crea una etiqueta (`contador_label`) en el marco para mostrar
        la información del contador en el formato "letras_conseguidas / letras_faltantes".

        Los parámetros `num_letras_conseguidas` y `num_letras_faltantes` se utilizan para
        mostrar los valores actuales en el contador.

        :return: La etiqueta del contador creada.
        """
        contador_frame = tk.Frame(self.menu, bg="white")
        contador_frame.place(x=750, y=20)

        contador_label = tk.Label(contador_frame,
                                  text=f"{num_letras_conseguidas} / {num_letras_faltantes}",
                                  font=("Arial", 20))
        contador_label.pack()

        return contador_label

    def crear_ventana(self, num_letras_faltantes):
        """
        Crea y muestra una nueva ventana de juego.

        Esta función crea y muestra una nueva ventana de juego utilizando la librería Tkinter.
        La ventana muestra la interfaz gráfica del juego, incluyendo letras o caracteres
        que el jugador debe identificar y una barra de progreso.

        Parámetros:
        :param num_letras_faltantes: El número total de letras faltantes en el juego.

        Detalles:
        La función utiliza la clase Toplevel para crear una nueva ventana secundaria que
        contendrá la interfaz gráfica del juego. Se configuran varias propiedades de la ventana,
        como su tamaño, posición, título y el ícono que se muestra en la barra de título.

        Luego, se llama a la función `crear_contador` para crear y mostrar un contador de progreso
        en la ventana de juego. El contador mostrará la cantidad de letras conseguidas y el total
        de letras faltantes.

        :return: None
        """
        self.menu = tk.Toplevel(self.menu_principal)
        self.menu.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.menu.geometry("900x550+300+100")
        self.menu.resizable(False, False)
        self.menu.title("Japones")
        self.menu.iconbitmap("menu_imagenes/icono.ico")
        self.crear_contador(self.num_letras_conseguidas, len(num_letras_faltantes))


def main(letras, modo_juego, alfabeto, menu_principal):
    """
    Función principal que inicia el juego.

    Esta función crea una instancia de la clase Juego y la utiliza para iniciar
    y controlar el flujo del juego. El juego se juega de acuerdo al modo especificado
    (japonés a español o español a japonés) y utiliza las letras y el alfabeto
    proporcionados.

    Parámetros:
    :param letras: Un diccionario que contiene las letras o caracteres del juego.
    :param modo_juego: Un valor booleano que indica el modo de juego (japonés a español o español a japonés).
    :param alfabeto: El alfabeto elegido para el juego (hiragana o katakana).
    :param menu_principal: Objeto Tkinter de la ventana principal del programa.

    Detalles:
    La función crea una instancia de la clase Juego llamada 'juego' y luego invoca el método
    'jugar' de la instancia creada. Este método controlará el flujo del juego y lo jugará según
    el modo y los datos proporcionados.

    :return: None
    """
    juego = Juego(menu_principal)
    juego.jugar(letras, modo_juego, alfabeto, menu_principal)
