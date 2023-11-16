"""import tkinter as tk
from tkinter import ttk

def cambiar_pestana(pestana_index):
    notebook.select(pestana_index)

root = tk.Tk()
root.title("Cambiar Pestaña")

notebook = ttk.Notebook(root)

# Pestaña 1
frame_1 = ttk.Frame(notebook)
label_1 = tk.Label(frame_1, text="Contenido de la Pestaña 1")
label_1.pack(padx=10, pady=10)
notebook.add(frame_1, text="Pestaña 1")

# Pestaña 2
frame_2 = ttk.Frame(notebook)
label_2 = tk.Label(frame_2, text="Contenido de la Pestaña 2")
label_2.pack(padx=10, pady=10)
notebook.add(frame_2, text="Pestaña 2")

notebook.pack(pady=10)

# Botones para cambiar de pestaña
boton_pestana_1 = tk.Button(root, text="Ir a Pestaña 1", command=lambda: cambiar_pestana(0))
boton_pestana_1.pack(side=tk.LEFT, padx=5)

boton_pestana_2 = tk.Button(root, text="Ir a Pestaña 2", command=lambda: cambiar_pestana(1))
boton_pestana_2.pack(side=tk.LEFT, padx=5)

root.mainloop()"""
"""
import tkinter as tk
from tkcalendar import Calendar

def mostrar_fecha():
    fecha_seleccionada = cal.get_date()
    label_fecha.config(text=f"Fecha seleccionada: {fecha_seleccionada}")

root = tk.Tk()
root.title("Selector de Fecha")

cal = Calendar(root, selectmode="day", year=2023, month=11, day=12)
cal.pack(pady=10)

boton_mostrar_fecha = tk.Button(root, text="Mostrar Fecha", command=mostrar_fecha)
boton_mostrar_fecha.pack(pady=10)

label_fecha = tk.Label(root, text="Fecha seleccionada: ")
label_fecha.pack(pady=10)

root.mainloop()"""

import tkinter as tk
from tkcalendar import DateEntry

def mostrar_fecha():
    fecha_seleccionada = entry_fecha.get_date()
    label_fecha.config(text=f"Fecha seleccionada: {fecha_seleccionada}")

root = tk.Tk()
root.title("Selector de Fecha")

entry_fecha = DateEntry(root, width=12, background="darkblue", foreground="white", borderwidth=2, state='readonly')
entry_fecha.pack(pady=10)

boton_mostrar_fecha = tk.Button(root, text="Mostrar Fecha", command=mostrar_fecha)
boton_mostrar_fecha.pack(pady=10)

label_fecha = tk.Label(root, text="Fecha seleccionada: ")
label_fecha.pack(pady=10)

root.mainloop()

import tkinter as tk
from tkcalendar import DateEntry
from datetime import date
def obtener_fecha():
    fecha_seleccionada = entry_fecha.get_date()
    print("Fecha seleccionada:", type(fecha_seleccionada))

# Crear la ventana
root = tk.Tk()
root.title("DateEntry con Fecha por Defecto")

# Utilizar una fecha inicial poco probable para indicar ninguna selección
fecha_por_defecto = date(1900, 1, 1)

# Crear el widget DateEntry con la fecha por defecto
entry_fecha = DateEntry(root, date_pattern='dd/MM/y', selectmode='day',year=2021,month=8,day=17)
entry_fecha.delete(0, "end")
entry_fecha.pack(pady=10)

# Botón para obtener la fecha seleccionada
boton_obtener_fecha = tk.Button(root, text="Obtener Fecha", command=obtener_fecha)
boton_obtener_fecha.pack(pady=10)

root.mainloop()