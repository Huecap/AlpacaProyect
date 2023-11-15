
import tkinter as tk
from tkinter import ttk

class Barra_busqueda(ttk.Frame):
    def __init__(self, parent, valores, objeto=None):
        """

        :param parent: Objeto contenedor (padre)
        :type parent: _type_
        :param valores: Valores del menú desplegable
        :type valores: list
        :param objeto: objeto que contiene variables a retornar 
        :type comando: ttk.Frame 
        """
        ttk.Frame.__init__(self, parent, padding=10)
        
        # Metodos Responsive 
        self.columnconfigure(index=0, weight=1)
        #self.rowconfigure(index=0, weight=1)
        
        ## ---- Variables de estado ---- ##

        # Valores del menu desplegable 
        self._combo = valores
        
        # Objeto con variables: valores_barra_busqueda
        self._object = objeto
        
        self.configurar_barra()
            
    def obtener_valor_seleccionado(self):
        # Obtiene valor del combobox #
        filtro = self.filtro.get()

        # Obtiene el valor del entry # 
        campo = self.campo_busqueda.get()
        valores = (filtro, campo)
        if self._object is not None:
            self._object.valores_barra_busqueda = valores
            # Avisa al objeto que actualice 
            self._object.actualizar_por_busqueda()
            # La idea aca es que te filtre la tabla por estos valores entonces 
            
    def configurar_barra(self):
        # Metodos Responsive 
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=5)
        self.columnconfigure(index=2, weight=1)
        self.rowconfigure(index=0, weight=0)
        
        # Menu deplegable 
        self.filtro = ttk.Combobox(self, state="readonly", values=self._combo, width=10)
        self.filtro.grid(row=0, column=0, padx=(0,5), pady=(0,10), sticky="ew")
        self.filtro.current(0)
        
        # Campo para ingresar texto 
        self.campo_busqueda = ttk.Entry(self, width=30)
        self.campo_busqueda.grid(row=0, column=1, padx=(5,0),pady=(0,10), sticky="ew")
        
        # Botón Buscar 
        self.boton_buscar = ttk.Button(self, text=">", width=5, command=self.obtener_valor_seleccionado)
        self.boton_buscar.grid(row=0, column=2, padx=(5,0) , pady=(0,10), sticky="we")
        

if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.geometry("800x640")
    
    # Seteando el tema 
    ventana.tk.call("source", "azure.tcl")
    ventana.tk.call("set_theme", "dark")

    
    campos = ["Id", "Nombre", "Apellido", "DNI", "Telefono", "Mail", "Direccion"]
    # bloque_izquierda.columnconfigure(index=0, weight=1)
    
    barra = Barra_busqueda(ventana, campos)
    barra.pack(expand=True, fill="both")
    ventana.mainloop()
    
