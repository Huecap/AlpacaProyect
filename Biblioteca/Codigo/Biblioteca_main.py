import tkinter as tk
from tkinter import ttk
from screeninfo import get_monitors

from IN_socio import Socio_in
from IN_prestamo import Prestamo_in
from IN_libro import Libro_in
from IN_reportes import Reportes_in




class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, master=parent)

        self.columnconfigure(index=0, weight=1)
        self.rowconfigure(index=0, weight=1)

        # Create widgets :)
        self.configuracion_widgets()

    def cambiar_pestana(self, pestana_index):
        self.notebook.select(pestana_index)
        
    def accion_al_cambiar_pestana(event):
        print('Hola Mundo')

    def configuracion_widgets(self):
        # Creamos el Notebook
        self.notebook = ttk.Notebook(self)

        # Creamos los frames correspondientes a cada pestaña
        tab_prestamos = Prestamo_in(self.notebook)  # Frame para la pestaña prestamos
        tb_socios = Socio_in(self.notebook)  # Frame para la pestaña socios
        tab_libros = Libro_in(self.notebook)  # Frame para la pesaña libros
        tab_reportes = Reportes_in(self.notebook)  # Frame para la pesaña libros

        # Añadimos las pestañas
        self.notebook.add(tab_prestamos, text="PRESTAMOS")
        self.notebook.add(tb_socios, text="SOCIOS")
        self.notebook.add(tab_libros, text="LIBROS")
        self.notebook.add(tab_reportes, text="Reportes")
        self.notebook.bind("<FocusIn>", self.accion_al_cambiar_pestana)
        self.notebook.pack(expand=True, fill="both")

        


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
