import tkinter as tk


class Tooltip:
    """
    Clase que maneja la creación y visualización de tooltips (información emergente) en widgets.

    Attributes:
    - tooltip: Ventana emergente que muestra el tooltip.

    Métodos:
    - __init__(self): Inicializa una nueva instancia de Tooltip.
    - mostrar_tooltip(self, widget, text_dict): Muestra un tooltip en un widget específico.
    - ocultar_tooltip(self): Oculta el tooltip si está visible.
    """
    def __init__(self):
        """
        Inicializa una nueva instancia de la clase Tooltip.
        """
        self.tooltip = None

    def mostrar_tooltip(self, widget, text_dict):
        """
        Muestra un tooltip en un widget específico con información proporcionada en text_dict.

        Parámetros:
        :param widget: El widget en el que se mostrará el tooltip.
        :param text_dict: Un diccionario que contiene la información a mostrar en el tooltip.

        Detalles:
        La función calcula las coordenadas en las que se debe mostrar el tooltip cerca del widget.
        Crea una nueva ventana emergente (Toplevel) y configura su apariencia y contenido utilizando
        el contenido de text_dict. El tooltip se ajusta automáticamente en tamaño para acomodar su contenido.

        :return: None
        """
        # Obtener las coordenadas del cursor dentro del widget

        # Ajustar las coordenadas para que el tooltip se muestre ligeramente desplazado desde el cursor
        x, y, _, _ = widget.bbox("insert")
        x += widget.winfo_rootx() + 25
        y += widget.winfo_rooty() + 25

        # Obtener las coordenadas actuales del puntero del mouse
        x_mouse = widget.winfo_pointerx()
        y_mouse = widget.winfo_pointery()

        # Crear la ventana emergente para el tooltip
        self.tooltip = tk.Toplevel(widget)
        self.tooltip.wm_overrideredirect(True)

        # Dividir el contenido del diccionario en filas de texto
        items = list(text_dict.items())
        rows = [", ".join([f"{key}: {value}" for key, value in items[i:i + 5]]) for i in range(0, len(items), 5)]

        # Crear una etiqueta para mostrar el contenido del tooltip
        tooltip_label = tk.Label(self.tooltip, text="\n".join(rows), wraplength=300, justify='left', background="white",
                                 relief="solid", borderwidth=1)
        tooltip_label.pack()

        # Ajustar el tamaño del tooltip según su contenido
        tooltip_width = min(tooltip_label.winfo_reqwidth(), 300)
        tooltip_height = min(tooltip_label.winfo_reqheight(), 200)

        # Posicionar el tooltip cerca del puntero del mouse
        self.tooltip.geometry(f"{tooltip_width}x{tooltip_height}+{x_mouse}+{y_mouse}")

    def ocultar_tooltip(self):
        """
        Oculta el tooltip si está visible.

        Detalles:
        La función verifica si hay un tooltip mostrándose en la ventana actual. Si es así,
        se destruye la ventana del tooltip, ocultándolo.

        :return: None
        """
        if self.tooltip is not None:
            self.tooltip.destroy()
