
import tkinter as tk
from tkinter import ttk 

from tabla import Tabla
from barra_busqueda import Barra_busqueda
from botonera import Botonera
from campo_datos import Campos_datos

class Socio(ttk.Frame):
    def __init__(self, notebook):
        ttk.Frame.__init__(self, notebook)
        
        # Hacemos el frame Responsive 
        self.grid_columnconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=1)
        self.grid_columnconfigure(index=1, weight=1)
        
        # Valores del menú desplegable 
        self._combo = ["Codigo", "Nombre", "Apellido", "DNI", "Telefono", "Mail", "Direccion"]
        
        # Valores default del campo de datos 
        #self._campos_default = {"Id":None, "Nombre":None, "Apellido":None, "DNI":None, "Telefono":None, "Mail":None, "Direccion":None}
        self._campos_default = {"Codigo":None, "Nombre":"", "Apellido":"", "DNI":"", "Telefono":"", "Mail":"", "Direccion":""}

        self.setup_widgets()
        
    
    def setup_widgets(self):
        fram2 = ttk.Frame(self)
        fram2.grid(row=1, column=0, sticky="nsew")
        ## Frame izquierdo 
        self.bloque_izquierda = ttk.Frame(self, padding=(10))
        self.bloque_izquierda.grid(row=0,column=0, sticky="nsew")
        #self.bloque_izquierda.grid_columnconfigure(index=0, weight=1)
        
        # Creamos la barra de busqueda y la colocamos 
        self.barra_busqueda = Barra_busqueda(self.bloque_izquierda, self._combo)
        self.barra_busqueda.pack(expand=True, fill="both")
        
        # Creamos los campos para ver la información del socio 
        self.datos_socio = Campos_datos(self.bloque_izquierda, self._campos_default)
        self.datos_socio.pack(expand=True, fill="both")
        
        # Creamos la botonera 
        botones_nuevo_editar = {"Nuevo":(0,0), "Modificar":(0, 1)}
        self.botones_nuevo_editar = Botonera(self.bloque_izquierda, botones_nuevo_editar)
        self.botones_nuevo_editar.pack(expand=True, fill="both")
        
        botones_nuevoPrestamo_verPrestamos = {"Nuevo Prestamo":(0,0), "Ver Prestamos":(0, 1)}
        self.botones_nuevoPrestamo_verPrestamos = Botonera(self.bloque_izquierda, botones_nuevoPrestamo_verPrestamos)
        self.botones_nuevoPrestamo_verPrestamos.pack(expand=True, fill="both")
        
        botones_eliminar = {"Eliminar":(0,0)}
        self.botones_nuevoPrestamo_verPrestamos = Botonera(self.bloque_izquierda, botones_eliminar)
        self.botones_nuevoPrestamo_verPrestamos.pack()
        
        
        ## Frame derecho 
        self.bloque_derecha = ttk.Frame(self, padding=10)
        self.bloque_derecha.grid(row=0, column=1, rowspan=2, sticky="snew")
        self.bloque_derecha.grid_columnconfigure(index=1, weight=2)
        # self.bloque_derecha.grid_rowconfigure(index=0, weight=1)
        
        # Tabla 
        campos = ("Id", "Nombre", "Apellido", "DNI", "Telefono", "Mail", "Direccion")
        self.tabla = Tabla(self.bloque_derecha, campos)
        self.tabla.pack(expand=True, fill="both")