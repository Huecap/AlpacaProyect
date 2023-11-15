
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
            
            
        for nombre, configuracion in self._botones.items(): 
            if configuracion.get("Comando") is not None:
                self.boton = ttk.Button(self, text=nombre, width=15, command=configuracion["Comando"])
            else:
                self.boton = ttk.Button(self, text=nombre, width=15)
            self.boton.grid(row=configuracion["Fila"], column=configuracion["Columna"], padx=(5) , pady=(0,5), sticky="we")
        
    def actualizar(self):
        # Destruir widgets actuales
        for widget in self.winfo_children():
            widget.destroy()
            
    def editar_botonera(self, configuracion_nueva):
        self.actualizar()
        for nombre, configuracion in configuracion_nueva.items(): 
            if configuracion.get("Comando") is not None:
                self.boton = ttk.Button(self, text=nombre, width=15, command=configuracion["Comando"])
            else:
                self.boton = ttk.Button(self, text=nombre, width=15)
            self.boton.grid(row=configuracion["Fila"], column=configuracion["Columna"], padx=(5) , pady=(0,5), sticky="we")
        
            
bandera = True
if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.geometry("1320x640")
    
    # Seteando el tema 
    ventana.tk.call("source", "azure.tcl")
    ventana.tk.call("set_theme", "dark")

    
    #campos = {"Nuevo":(0,0), "Modificar":(0, 1), "Ver Prestamos":(1, 1), "Nuevo Prestamo": (1,0)}
    def funcion(botonera):
        global bandera
        if bandera:
            bandera = False
            campos2 = {"Otro":{"Columna":0, "Fila":0, "Comando":lambda:funcion(botonera)}, "Otro2":{"Columna":1, "Fila":0}}
            botonera.editar_botonera(campos2)
            botonera.pack(expand=True, fill="both")
        else:
            bandera = True        
            campos2 = {"Nuevo":{"Columna":0, "Fila":0, "Comando":lambda:funcion(botonera)}, "Nuevo2":{"Columna":1, "Fila":0}}
            botonera.editar_botonera(campos2)
            botonera.pack(expand=True, fill="both")
    campos = {"Nuevo":{"Columna":0, "Fila":0, "Comando":lambda:funcion(botonera)}, "Nuevo2":{"Columna":0, "Fila":1}}
    # bloque_izquierda.columnconfigure(index=0, weight=1)
    botonera = Botonera(ventana, campos)
    
    # botonera.editar_botonera(campos2)
    botonera.pack(expand=True, fill="both")
    ventana.mainloop()
    