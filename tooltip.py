import tkinter as tk

class Tooltip:
    def __init__(self):
        self.tooltip = None

    def mostrar_tooltip(self, widget, text_dict):
        x, y, _, _ = widget.bbox("insert")
        x += widget.winfo_rootx() + 25
        y += widget.winfo_rooty() + 25

        x_mouse = widget.winfo_pointerx()
        y_mouse = widget.winfo_pointery()

        self.tooltip = tk.Toplevel(widget)
        self.tooltip.wm_overrideredirect(True)

        items = list(text_dict.items())
        rows = [", ".join([f"{key}: {value}" for key, value in items[i:i + 5]]) for i in range(0, len(items), 5)]

        tooltip_label = tk.Label(self.tooltip, text="\n".join(rows), wraplength=300, justify='left', background="white",
                                 relief="solid", borderwidth=1)
        tooltip_label.pack()

        tooltip_width = min(tooltip_label.winfo_reqwidth(), 300)
        tooltip_height = min(tooltip_label.winfo_reqheight(), 200)

        self.tooltip.geometry(f"{tooltip_width}x{tooltip_height}+{x_mouse}+{y_mouse}")

    def ocultar_tooltip(self):
        if self.tooltip is not None:
            self.tooltip.destroy()


