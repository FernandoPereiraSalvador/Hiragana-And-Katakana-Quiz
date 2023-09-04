import tkinter as tk
from tkinter import PhotoImage

import pkg_resources

import alfabeto.hiragana
import alfabeto.katakana
import juego
from tooltip import Tooltip


class MenuJuego:
    """
    Clase que representa el menú principal del juego.

    Esta clase crea una ventana de menú donde el jugador puede elegir entre los modos
    de juego "Japonés a Español" o "Español a Japonés".

    Parámetros:
    :param alfabeto_usado: Booleano que indica si se usará el alfabeto hiragana (True) o katakana (False).
    :param menu_principal: Objeto Tkinter de la ventana principal del programa.

    Métodos:
    - __init__(self, alfabeto_usado, menu_principal): Constructor que inicializa la ventana y otros atributos.
    - japones_a_espanol(self): Método que inicia el juego en el modo "Japonés a Español".
    - espanol_a_japones(self): Método que inicia el juego en el modo "Español a Japonés".
    - crear_interfaz(self): Método que crea la interfaz gráfica del menú.
    """

    def __init__(self, alfabeto_usado, menu_principal):
        """
        Constructor de la clase MenuJuego.

        Este constructor inicializa una instancia de MenuJuego, creando la interfaz gráfica para que el jugador elija
        entre los modos "Japonés a Español" y "Español a Japonés".

        Parámetros:
        :param alfabeto_usado: Booleano que indica si se usará el alfabeto hiragana (True) o katakana (False).
        :param menu_principal: Objeto Tkinter de la ventana principal del programa.

        Detalles:
        La función constructora crea una ventana secundaria (`Toplevel`) que actúa como el menú de selección de modo.
        Si `alfabeto_usado` es True, se cargarán imágenes correspondientes al alfabeto hiragana para los botones.
        Si es False, se cargarán imágenes para el alfabeto katakana.

        La ventana de menú se configura con un tamaño fijo y una posición en la pantalla. Se establece la acción a
        realizar cuando se intenta cerrar la ventana mediante el protocolo "WM_DELETE_WINDOW", que llamará a la
        función `cerrar_ventana` para ocultar y destruir la ventana de menú y restaurar la ventana principal.

        Finalmente, se llama a la función `crear_interfaz` para generar la interfaz gráfica de selección de modo.

        :return: None
        """

        # Atributo que almacenará la decisión del modo de juego elegido
        self.decision = None
        self.menu_principal = menu_principal

        # Crear la ventana de menú como una ventana secundaria (Toplevel) de la ventana principal
        self.menu = tk.Toplevel(menu_principal)

        # Cargar imágenes para los botones del menú según el alfabeto utilizado
        if alfabeto_usado:
            self.imagen_japones_a_espanol = PhotoImage(file=pkg_resources.resource_filename(__name__, 'menu_imagenes/japonesHiragana.png'))
            self.imagen_espanol_a_japones = PhotoImage(file=pkg_resources.resource_filename(__name__, 'menu_imagenes/españolHiragana.png'))
        else:
            self.imagen_japones_a_espanol = PhotoImage(file=pkg_resources.resource_filename(__name__, 'menu_imagenes/japonesKatakana.png'))
            self.imagen_espanol_a_japones = PhotoImage(file=pkg_resources.resource_filename(__name__, 'menu_imagenes/españolKatakana.png'))

        # Configurar la ventana de menú
        self.menu.geometry("900x550+300+100")
        self.menu.protocol("WM_DELETE_WINDOW", lambda: cerrar_ventana(self.menu, self.menu_principal))
        self.menu.resizable(False, False)
        self.menu.title("Modo")
        self.menu.iconbitmap("menu_imagenes/icono.ico")

        # Almacenar la decisión del alfabeto y crear la interfaz gráfica del menú
        self.alfabeto = alfabeto_usado
        self.crear_interfaz()

    def japones_a_espanol(self):
        """
        Cambia la decisión de modo a "Japonés a Español" y abre la ventana de selección de caracteres.

        Esta función se activa cuando el jugador elige el modo "Japonés a Español" en el menú de selección de modo.
        Cambia el atributo `decision` de la clase a `True`, indicando que se ha seleccionado el modo "Japonés a
        Español".

        Detalles:
        La función establece `self.decision` en `True` para indicar que el modo de juego seleccionado es
        "Japonés a Español". Luego, utiliza el método `destroy()` en `self.menu` para cerrar la ventana actual del
        menú.

        Se crea una instancia de la clase `CaracteresSelector`, pasando los parámetros `self.alfabeto` (decisión del
        alfabeto), `self.decision` (decisión de modo) y `self.menu_principal` (ventana principal del programa). Esto
        abre la ventana de selección de caracteres para que el jugador elija qué caracteres utilizar en el juego.

        :return: None
        """

        # Cambiar la decisión a "Japonés a Español"
        self.decision = True

        # Destruir la ventana de menú actual
        self.menu.destroy()

        # Crear una instancia de la clase CaracteresSelector para la selección de caracteres
        CaracteresSelector(self.alfabeto, self.decision, self.menu_principal)

    def espanol_a_japones(self):
        """
        Cambia la decisión de modo a "Español a Japonés" y abre la ventana de selección de caracteres.

        Esta función se activa cuando el jugador elige el modo "Español a Japonés" en el menú de selección de modo.
        Cambia el atributo `decision` de la clase a `False`, indicando que se ha seleccionado el modo "Español a
        Japonés".

        Detalles:
        La función establece `self.decision` en `False` para indicar que el modo de juego seleccionado es
        "Español a Japonés". Luego, utiliza el método `destroy()` en `self.menu` para cerrar la ventana actual del
        menú.

        Se crea una instancia de la clase `CaracteresSelector`, pasando los parámetros `self.alfabeto` (decisión del
        alfabeto), `self.decision` (decisión de modo) y `self.menu_principal` (ventana principal del programa). Esto
        abre la ventana de selección de caracteres para que el jugador elija qué caracteres utilizar en el juego.

        :return: None
        """

        # Cambiar la decisión a "Español a Japonés"
        self.decision = False

        # Destruir la ventana de menú actual
        self.menu.destroy()

        # Crear una instancia de la clase CaracteresSelector para la selección de caracteres
        CaracteresSelector(self.alfabeto, self.decision, self.menu_principal)

    def crear_interfaz(self):

        """
        Crea y muestra la interfaz gráfica para la selección de modo de juego.

        Esta función se encarga de crear y mostrar la interfaz gráfica en la ventana de selección de modo de juego.
        La interfaz incluye dos botones con imágenes correspondientes a los modos de juego disponibles: "Japonés a
        Español" y "Español a Japonés".

        Detalles:
        La función crea dos botones de la clase `tk.Button` para los modos de juego "Japonés a Español" y
        "Español a Japonés". Cada botón tiene una imagen asociada (`self.imagen_japones_a_espanol` o
        `self.imagen_espanol_a_japones`), un comando que se activará cuando se haga clic en el botón y dimensiones de
        ancho y alto.

        Los botones se posicionan en la ventana utilizando el método `place()` y las coordenadas `(x, y)` especificadas.
        El botón "Japonés a Español" se coloca en la posición `(65, 50)` y el botón "Español a Japonés" se coloca en la
        posición `(500, 50)`.

        Cuando se hace clic en cualquiera de los botones, se ejecutará el comando correspondiente (
        `self.japones_a_espanol` o `self.espanol_a_japones`) para cambiar el modo de juego y abrir la ventana de
        selección de caracteres.

        :return: None
        """

        # Crear botón para el modo "Japonés a Español"
        hiragana_button = tk.Button(
            self.menu,
            command=self.japones_a_espanol,
            width=325, height=325, image=self.imagen_japones_a_espanol
        )
        hiragana_button.place(x=65, y=50)

        # Crear botón para el modo "Español a Japonés"
        katakana_button = tk.Button(
            self.menu,
            command=self.espanol_a_japones,
            width=325, height=325, image=self.imagen_espanol_a_japones
        )
        katakana_button.place(x=500, y=50)


class CaracteresSelector:
    """
    Clase que representa la ventana de selección de caracteres del juego.

    Esta clase se encarga de manejar la ventana de selección de caracteres del juego, permitiendo al jugador
    elegir diferentes conjuntos de caracteres para practicar.

    Parámetros:
    :param decision_alfabeto (bool): Indica si se usará el alfabeto de hiragana (True) o katakana (False).
    :param decision_modo (bool): Indica el modo de juego: Japonés a Español (True) o Español a Japonés (False).
    :param menu_principal: La ventana principal del menú.

    Attributos:
        opcion_vocales (bool): Indica si la opción de caracteres de vocales está seleccionada.
        opcion_basico (bool): Indica si la opción de caracteres básicos está seleccionada.
        opcion_compuesto (bool): Indica si la opción de caracteres compuestos está seleccionada.
        opcion_combinado1 (bool): Indica si la opción de caracteres combinados tipo 1 está seleccionada.
        opcion_combinado2 (bool): Indica si la opción de caracteres combinados tipo 2 está seleccionada.
        opcion_vocales_var: Variable booleana asociada a la opción de vocales.
        opcion_basico_var: Variable booleana asociada a la opción de caracteres básicos.
        opcion_compuesto_var: Variable booleana asociada a la opción de caracteres compuestos.
        opcion_combinado1_var: Variable booleana asociada a la opción de caracteres combinados tipo 1.
        opcion_combinado2_var: Variable booleana asociada a la opción de caracteres combinados tipo 2.
        menu_principal: La ventana principal del menú.
        decisionAlfabeto (bool): La decisión sobre qué alfabeto se usará.
        decisionModo (bool): La decisión sobre el modo de juego.
        caracteres (dict): Un diccionario que almacenará los caracteres seleccionados.

    Métodos:
        __init__(decision_alfabeto, decision_modo, menu_principal): Inicializa la clase
        toggle_opcion(opcion): Cambia el estado de una opción de caracteres.
        continuar(): Oculta la ventana actual y abre la ventana de selección de caracteres.
        crear_interfaz(alfabeto_usado): Crea la interfaz gráfica para la selección de opciones de caracteres.
        seleccionar_caracteres(): Procesa las opciones seleccionadas y almacena los caracteres correspondientes.
        iniciar_juego(): Inicia el juego con los caracteres seleccionados.
    """

    def __init__(self, decision_alfabeto, decision_modo, menu_principal):
        """
        Inicializa la clase CaracteresSelector con las opciones y configuraciones de la ventana de selección de
        caracteres.

        Parámetros:
        :param decision_alfabeto (bool): Indica si se usará el alfabeto de hiragana (True) o katakana (False).
        :param decision_modo (bool): Indica el modo de juego: Japonés a Español (True) o Español a Japonés (False).
        :param menu_principal: La ventana principal del menú.

        Atributos:
            opcion_vocales (bool): Indica si se ha seleccionado la opción de caracteres "Vocales".
            opcion_basico (bool): Indica si se ha seleccionado la opción de caracteres "Básico".
            opcion_compuesto (bool): Indica si se ha seleccionado la opción de caracteres "Compuesto".
            opcion_combinado1 (bool): Indica si se ha seleccionado la opción de caracteres "Combinado 1".
            opcion_combinado2 (bool): Indica si se ha seleccionado la opción de caracteres "Combinado 2".
            opcion_vocales_var: Variable booleana asociada a la opción "Vocales".
            opcion_basico_var: Variable booleana asociada a la opción "Básico".
            opcion_compuesto_var: Variable booleana asociada a la opción "Compuesto".
            opcion_combinado1_var: Variable booleana asociada a la opción "Combinado 1".
            opcion_combinado2_var: Variable booleana asociada a la opción "Combinado 2".
            menu_principal: La ventana principal del menú.
            decisionAlfabeto (bool): El valor de la decisión sobre el alfabeto.
            decisionModo (bool): El valor de la decisión sobre el modo de juego.
            caracteres (dict): Diccionario para almacenar los caracteres seleccionados.

        Detalles:
        Esta función constructora inicializa una instancia de la clase CaracteresSelector con las opciones
        de configuración y las decisiones tomadas por el usuario en la ventana de selección de caracteres. Los
        parámetros `decision_alfabeto` y `decision_modo` determinan el alfabeto utilizado y el modo de juego,
        respectivamente. El parámetro `menu_principal` es la ventana principal del menú que llamó a esta instancia.

        La función también crea y muestra la interfaz gráfica de la ventana de selección de caracteres, que incluye
        opciones para seleccionar los tipos de caracteres a utilizar en el juego. Las variables de opción y las
        imágenes asociadas a las opciones se configuran en esta función.

        Las variables de opción (`opcion_vocales`, `opcion_basico`, etc.) se utilizan para rastrear si se ha
        seleccionado cada opción de caracteres. Las variables de tipo `tk.BooleanVar` (como `opcion_vocales_var`) se
        asocian a los botones de selección de opciones en la interfaz gráfica.

        Los atributos `decisionAlfabeto` y `decisionModo` almacenan las decisiones tomadas sobre el alfabeto y el
        modo de juego.

        El diccionario `caracteres` se utilizará posteriormente para almacenar los caracteres seleccionados por el
        usuario para jugar.

        :return: None
        """

        # Inicialización de variables de opción para el tipo de caracteres
        self.opcion_vocales = False
        self.opcion_basico = False
        self.opcion_compuesto = False
        self.opcion_combinado1 = False
        self.opcion_combinado2 = False

        # Inicialización de variables de tipo BooleanVar para asociar a los botones de selección
        self.opcion_vocales_var = tk.BooleanVar()
        self.opcion_basico_var = tk.BooleanVar()
        self.opcion_compuesto_var = tk.BooleanVar()
        self.opcion_combinado1_var = tk.BooleanVar()
        self.opcion_combinado2_var = tk.BooleanVar()

        # Asignación de la ventana principal del menú
        self.menu_principal = menu_principal

        # Almacenamiento de decisiones tomadas sobre alfabeto y modo de juego
        self.decisionAlfabeto = decision_alfabeto
        self.decisionModo = decision_modo
        self.caracteres = {}

        # Creación de la ventana de selección de caracteres
        self.menu = tk.Toplevel(menu_principal)
        self.menu.title("Caracteres")
        self.menu.protocol("WM_DELETE_WINDOW", lambda: cerrar_ventana(self.menu, self.menu_principal))
        self.menu.geometry("900x550+300+100")
        self.menu.resizable(False, False)
        self.menu.title("Menu")
        self.menu.iconbitmap("menu_imagenes/icono.ico")

        self.crear_interfaz(decision_alfabeto)

    def toggle_opcion(self, opcion):
        """
        Cambia el estado de una opción de caracteres.

        Parámetros:
        :param opcion: (str) La opción de caracteres cuyo estado se cambiará.

        Detalles:
        Esta función se utiliza para cambiar el estado de una opción de caracteres. Recibe como argumento una cadena que
        representa la opción ("Vocales", "Basico", etc.) y cambia el valor correspondiente en las variables de estado
        (`opcion_vocales`, `opcion_basico`, etc.).

        Si la opción estaba en `True`, cambiará a `False`, y viceversa. Esto permite al usuario seleccionar y
        deseleccionar las opciones según sea necesario para el juego.

        :return: None
        """

        # Cambio del estado de la opción correspondiente
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
        """
        Oculta la ventana actual y procede a la selección de caracteres.

        Detalles:
        Esta función se activa cuando el botón "Continuar" en la ventana de selección de caracteres es presionado.
        Su propósito es ocultar la ventana actual (ventana de selección de caracteres) utilizando el método `withdraw()`
        y luego proceder a la selección de caracteres invocando la función `seleccionar_caracteres()`.

        La función `seleccionar_caracteres()` es responsable de determinar qué opciones de caracteres fueron
        seleccionadas y construir el conjunto final de caracteres a utilizar en el juego.

        :return: None
        """

        self.menu.withdraw()
        self.seleccionar_caracteres()

    def crear_interfaz(self, alfabeto_usado):
        """
        Crea la interfaz gráfica de la ventana de selección de opciones de caracteres.

        Parámetros:
        :param alfabeto_usado: Indica si se usará el alfabeto de hiragana (True) o katakana (False).

        Detalles:
        Esta función es responsable de crear la interfaz gráfica de la ventana de selección de opciones de
        caracteres. Utiliza la biblioteca tkinter para crear los elementos gráficos, como los botones de selección y
        los checkbuttons. También se encarga de establecer los comandos asociados a los checkbuttons y de mostrar
        tooltips informativos cuando el cursor del mouse pasa sobre ellos.

        Después de construir la interfaz gráfica, establece las dimensiones y la posición de la ventana mediante el
        método `geometry()` y empaqueta los elementos en la ventana. Finalmente, muestra la ventana con las opciones de
        selección de caracteres.

        :return: None
        """

        # Crea un frame para las opciones
        opciones_frame = tk.Frame(self.menu)
        opciones_frame.pack(pady=20)

        # Crea una instancia de Tooltip para mostrar información adicional
        tooltip = Tooltip()

        # Define las opciones de caracteres basándose en el alfabeto usado
        if alfabeto_usado:
            vocales = alfabeto.hiragana.vocales
            basico = alfabeto.hiragana.basico
            compuesto = alfabeto.hiragana.compuesto
            combinado_1 = alfabeto.hiragana.combinado_1
            combinado_2 = alfabeto.hiragana.combinado_2
        else:
            vocales = alfabeto.hiragana.vocales
            basico = alfabeto.hiragana.basico
            compuesto = alfabeto.hiragana.compuesto
            combinado_1 = alfabeto.hiragana.combinado_1
            combinado_2 = alfabeto.hiragana.combinado_2

        # Lista de opciones con sus variables asociadas y textos tooltip
        opciones = [
            ("Vocales", self.opcion_vocales_var, vocales),
            ("Básico", self.opcion_basico_var, basico),
            ("Compuesto", self.opcion_compuesto_var, compuesto),
            ("Combinado 1", self.opcion_combinado1_var, combinado_1),
            ("Combinado 2", self.opcion_combinado2_var, combinado_2)
        ]

        checkbuttons = []

        # Itera sobre las opciones para crear checkbuttons y asociarles comandos y tooltips
        for opcion, var, tooltip_text in opciones:
            checkbutton = tk.Checkbutton(
                opciones_frame, text=opcion, command=lambda op=opcion: self.toggle_opcion(op),
                font=("Arial", 14), variable=var
            )
            # Asocia tooltips a los eventos de entrada y salida del mouse
            checkbutton.bind("<Enter>", lambda event, text=tooltip_text: tooltip.mostrar_tooltip(checkbutton, text))
            checkbutton.bind("<Leave>", lambda event: tooltip.ocultar_tooltip())
            checkbutton.pack(pady=5)
            checkbuttons.append(checkbutton)

        # Crea un frame para el botón "Continuar"
        boton_frame = tk.Frame(self.menu)
        boton_frame.pack(pady=20)

        # Crea el botón "Continuar" y le asigna un comando
        boton_continuar = tk.Button(
            boton_frame, text="Continuar", command=self.continuar, font=("Arial", 16), padx=20, pady=10
        )
        boton_continuar.pack()

        # Establece las dimensiones y posición de la ventana
        self.menu.geometry("900x550+300+100")

    def seleccionar_caracteres(self):
        """
        Selecciona los caracteres basados en las opciones elegidas por el usuario.

        Detalles: Esta función determina qué caracteres se incluirán en el juego en función de las opciones
        seleccionadas por el usuario en la ventana de selección de caracteres. Primero, verifica si se va a utilizar
        el alfabeto de hiragana o katakana según la decisión de alfabeto.

        Luego, utiliza las variables de opción (opcion_vocales, opcion_basico, etc.) para decidir qué conjuntos de
        caracteres se deben agregar al diccionario 'caracteres'. Cada conjunto se agrega utilizando la operación de
        unión (|) para combinar los conjuntos de caracteres seleccionados.

        Una vez que se han seleccionado los caracteres, se llama a la función 'iniciar_juego()' para comenzar el
        juego con los caracteres seleccionados.

        :return: None
        """

        # Determinar qué conjunto de caracteres utilizar según la decisión de alfabeto
        if self.decisionAlfabeto:
            caracteres_usados = alfabeto.hiragana
        else:
            caracteres_usados = alfabeto.katakana

        # Agregar conjuntos de caracteres seleccionados al diccionario 'caracteres'
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

        # Iniciar el juego con los caracteres seleccionados
        self.iniciar_juego()

    def iniciar_juego(self):
        """
        Inicia el juego con las configuraciones y caracteres seleccionados.

        Detalles: Esta función cierra la ventana actual de selección de caracteres y llama a la función 'main' del
        módulo 'juego' para iniciar el juego con las configuraciones y caracteres seleccionados. Se pasan como
        argumentos el diccionario de caracteres seleccionados, la decisión sobre el modo de juego y la decisión sobre
        el alfabeto a utilizar.

        :return: None
        """

        # Cerrar la ventana de selección de caracteres
        self.menu.destroy()

        # Llamar a la función principal del módulo 'juego' para iniciar el juego
        juego.main(self.caracteres, self.decisionModo, self.decisionAlfabeto, self.menu_principal)


def cerrar_ventana(menu, menu_principal):
    """
    Cierra una ventana secundaria y restaura la visibilidad de la ventana principal.

    Parámetros:
    :param menu: La ventana secundaria a cerrar.
    :param menu_principal: La ventana principal que se restaurará a la visibilidad.

    Detalles:
    Esta función oculta la ventana secundaria ('menu') utilizando el método 'withdraw()', luego la destruye con el
    método 'destroy()'. Posteriormente, hace visible la ventana principal ('menu_principal') utilizando el método
    'deiconify()', lo que permite que la ventana principal sea nuevamente visible para el usuario.

    :return: None
    """

    # Ocultar y destruir la ventana secundaria
    menu.withdraw()
    menu.destroy()

    # Restaurar la visibilidad de la ventana principal
    menu_principal.deiconify()


def main(alfabeto_usado, menu_principal):
    """
    Función principal para iniciar la aplicación del juego.

    Detalles:
    Esta función es el punto de entrada para iniciar la aplicación del juego. Toma dos argumentos: 'alfabeto_usado'
    que indica si se utilizará el alfabeto de hiragana o katakana, y 'menu_principal' que es la ventana principal
    del menú.

    Parámetros:
    :param alfabeto_usado: Un valor booleano que indica si se usará el alfabeto de hiragana (True) o katakana (False).
    :param menu_principal: La ventana principal del menú.

    La función crea una instancia de la clase 'MenuJuego', pasando los valores de 'alfabeto_usado' y 'menu_principal'
    como argumentos. Esto inicia la ventana del menú del juego.

    :return: None
    """
    MenuJuego(alfabeto_usado, menu_principal)
