import tkinter as tk


def custom_message_box(title, message, font_size):
    """
    Crea una ventana emergente personalizada con un mensaje.

    Esta función crea una nueva ventana emergente utilizando la biblioteca Tkinter,
    mostrando un título y un mensaje proporcionados. El tamaño de fuente del mensaje
    se puede personalizar con el parámetro `font_size`.

    Parámetros:
    :param title: El título de la ventana emergente.
    :param message: El mensaje que se mostrará en la ventana.
    :param font_size: El tamaño de fuente del mensaje.

    Detalles:
    La función crea la ventana emergente con un título y un mensaje utilizando la
    fuente "Helvetica" y el tamaño de fuente proporcionado. Luego, calcula la posición
    para centrar la ventana en la pantalla y ajusta la geometría de la ventana en consecuencia.

    :return: None
    """
    # Crea una nueva ventana emergente
    window = tk.Toplevel()
    window.title(title)

    # Configura el tamaño de fuente del mensaje y muestra el texto
    label = tk.Label(window, text=message, font=("Helvetica", font_size))
    label.pack(padx=20, pady=20)

    # Actualiza la ventana para calcular su tamaño
    window.update_idletasks()

    # Calcula la posición para centrar la ventana en la pantalla
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width() + 100  # Ajusta el ancho de la ventana
    window_height = window.winfo_height()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    # Ajusta la geometría de la ventana para centrarla en la pantalla
    window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

