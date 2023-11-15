
import tkinter as tk
from tkinter import ttk

from HR_validaciones_interfaz import validar_entry_float, validar_entry_int, validar_entry_str

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
        
        self._valores = valores
        ## ---- Variables de estado ---- ##

        self._combo = []    
        
        # Valores del menu desplegable 
        for key in valores.keys():
            self._combo.append(key)
            
        # self._validaciones_campos = valores[1]
        
        # Objeto con variables: valores_barra_busqueda
        self._object = objeto
        
        # Validacion de campos 
        self.vcmd_int = self.register(lambda P: validar_entry_int(P))
        self.vcmd_str = self.register(lambda P: validar_entry_str(P))
        self.vcmd_float = self.register(lambda P: validar_entry_float(P))     
        
        self.configurar_barra()
    
        
    def validar_campos(self, event):
        filtro = self.filtro.get()
        self.campo_busqueda.destroy()
        if self._valores[filtro] == "i":
            self.campo_busqueda = ttk.Entry(self, width=10, justify="center",  validate="key", validatecommand=(self.vcmd_int, '%P'))
        elif self._valores[filtro] == "s":
            self.campo_busqueda = ttk.Entry(self, width=10, justify="center",  validate="key", validatecommand=(self.vcmd_str, '%P'))
        elif self._valores[filtro] == "f":
            self.campo_busqueda = ttk.Entry(self, width=10, justify="center",  validate="key", validatecommand=(self.vcmd_float, '%P'))
        self.campo_busqueda.grid(row=0, column=1, padx=(5,0),pady=(0,10), sticky="ew")
    
    def obtener_valor_seleccionado(self):
        # Obtiene valor del combobox #
        filtro = self.filtro.get()
        #self.validar_campos(filtro)

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
        # Entry 
        #self.campo_busqueda = ttk.Entry(self, width=30)
        self.campo_busqueda = ttk.Entry(self, width=10, justify="center",  validate="key", validatecommand=(self.vcmd_int, '%P'))
        self.campo_busqueda.grid(row=0, column=1, padx=(5,0),pady=(0,10), sticky="ew")
        self.filtro.bind("<<ComboboxSelected>>", lambda event: self.validar_campos(event))
        
        # Botón Buscar 
        self.boton_buscar = ttk.Button(self, text=">", width=5, command=self.obtener_valor_seleccionado)
        self.boton_buscar.grid(row=0, column=2, padx=(5,0) , pady=(0,10), sticky="we")
        

if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.geometry("800x640")
    
    # Seteando el tema 
    ventana.tk.call("source", "azure.tcl")
    ventana.tk.call("set_theme", "dark")

    
    campos = {"codigo":"i", "titulo":"s", "estado":"s", "precio":"f"}
    # bloque_izquierda.columnconfigure(index=0, weight=1)
    
    barra = Barra_busqueda(ventana, campos)
    barra.pack(expand=True, fill="both")
    ventana.mainloop()
    
