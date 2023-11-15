import tkinter as tk
from tkinter import ttk
from screeninfo import get_monitors

from IN_socio import Socio
from IN_prestamo import Prestamo
from IN_libro import Libro


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, master=parent)

        self.columnconfigure(index=0, weight=1)
        self.rowconfigure(index=0, weight=1)

        # Create widgets :)
        self.configuracion_widgets()

    def configuracion_widgets(self):
        # Creamos el Notebook
        notebook = ttk.Notebook(self)

        # Creamos los frames correspondientes a cada pestaña
        tab_libros = Libro(notebook)  # Frame para la pesaña libros
        #tb_socios = Socio(notebook)  # Frame para la pestaña socios
        #tab_prestamos = Prestamo(notebook)  # Frame para la pestaña prestamos

        # Añadimos las pestañas
        notebook.add(tab_libros, text="LIBROS")
        #notebook.add(tb_socios, text="SOCIOS")
        #notebook.add(tab_prestamos, text="PRESTAMOS")
        notebook.pack(expand=True, fill="both")


if __name__ == "__main__":
    # Creamos la ventana
    ventana = tk.Tk()

    # Definimos la resolucion por defecto
    ventana.geometry("1320x640")

    # Seteamos el tema
    ventana.tk.call("source", "azure.tcl")
    ventana.tk.call("set_theme", "dark")

    # Creamos el Frame principal
    programa = App(ventana)
    programa.pack(expand=True, fill="both")

    # Actualizamos cualquier cambio de la ventana
    ventana.update()

    # Limitamos el tamaño mínimo de la ventana
    ventana.minsize(ventana.winfo_width(), ventana.winfo_height())

    # Localizamos el monitor principal
    monitor = get_monitors()[0]

    # Centramos la ventana
    x_cordinate = int((monitor.width / 2) - (ventana.winfo_width() / 2))
    y_cordinate = int((monitor.height / 2) - (ventana.winfo_height() / 2))
    ventana.geometry("+{}+{}".format(x_cordinate, y_cordinate - 20))

    # Creamos el mainloop
    ventana.mainloop()
