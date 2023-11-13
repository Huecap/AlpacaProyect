
import tkinter as tk
from tkinter import ttk

class Botonera(ttk.Frame):
    def __init__(self, parent, botones):
        ttk.Frame.__init__(self, parent, padding=10)
        
        # Valores de los botones 
        self._botones = botones
                
        # Metodos Responsive 
        self.columnconfigure(index=0, weight=1)
        #self.rowconfigure(index=0, weight=1)
        
        self.configurar_botonera_doble()
        
        
    def configurar_botonera_doble(self):
        for n in range(0,2):
            self.columnconfigure(index=n, weight=1)
            #self.rowconfigure(index=n, weight=1)
            
            
        for nombre, posicion in self._botones.items(): 
            self.boton = ttk.Button(self, text=nombre, width=15)
            self.boton.grid(row=posicion[0], column=posicion[1], padx=(5) , pady=(0,5), sticky="we")
            
            
            
if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.geometry("1320x640")
    
    # Seteando el tema 
    ventana.tk.call("source", "azure.tcl")
    ventana.tk.call("set_theme", "dark")

    
    campos = {"Nuevo":(0,0), "Modificar":(0, 1), "Ver Prestamos":(1, 1), "Nuevo Prestamo": (1,0)}
    # bloque_izquierda.columnconfigure(index=0, weight=1)
    botonera = Botonera(ventana, campos)
    botonera.pack(expand=True, fill="both")
    ventana.mainloop()
    