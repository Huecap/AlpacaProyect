
import tkinter as tk
from tkinter import ttk

class Campos_datos(ttk.LabelFrame):
    def __init__(self, parent, valores):
        ttk.LabelFrame.__init__(self, parent, text="Datos")
        
        # Valores del menu desplegable 
        self._valores = valores
                
        # Metodos Responsive 
        #for n in range(0,len(valores)):
         #   self.columnconfigure(index=n, weight=1)
          #  self.rowconfigure(index=n, weight=1)
        
        self.editar_campos()
        
    def editar_campos(self):
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)
        
        self.label_socioID = ttk.Label(self, text="ID", anchor="center")
        self.label_socioID.grid(row=0, column=0, padx=5, pady=(0,10), sticky="nswe")
        
        self.label_numero_socioID = ttk.Label(self, text=self._valores["Codigo"], anchor="center")
        self.label_numero_socioID.grid(row=0, column=1, pady=(0,10),  sticky="nswe")
        
        n = 0 
        for key, value in self._valores.items():
            if n!=0:
                self.label_nombre = ttk.Label(self, text=key, anchor="center")
                self.label_nombre.grid(row=n, column=0, padx=5, pady=(0,10), sticky="we")
                self.campo_dato1 = ttk.Entry(self, width=10, justify="center")
                self.campo_dato1.insert(n, value)
                self.campo_dato1.grid(row=n, column=1, padx= (5, 20), pady=(0,20), sticky="ew")
            self.rowconfigure(index=n, weight=1)
            n += 1

    def ver_campos(self):

        
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)
        
        n = 0 
        for key, value in self._valores.items():
            self.label_nombre = ttk.Label(self, text=key, anchor="center")
            self.label_nombre.grid(row=n, column=0, padx=5, pady=(0,10), sticky="we")
            self.campo_dato1 = ttk.Label(self, text=value,width=11, anchor="center")
            self.campo_dato1.grid(row=n, column=1, padx= (5, 20), pady=(0,29), sticky="ew")
            self.rowconfigure(index=n, weight=1)

            n += 1

    def eliminar_contenido(self):
        # Eliminar widgets actuales dentro del Frame
        for widget in self.winfo_children():
            widget.destroy()

    def actualizar_contenido1(self):
        self.eliminar_contenido()
        self.ver_campos()

    def actualizar_contenido2(self):
        self.eliminar_contenido()
        self.editar_campos()
            
if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.geometry("600x400")
    
    # Seteando el tema 
    ventana.tk.call("source", "azure.tcl")
    ventana.tk.call("set_theme", "dark")

    
    campos = {"Codigo":12, "Nombre":"Juancho", "Apellido":"Perez", "DNI":1233321, "Telefono":12313, "Mail":"Hudfa@gadg", "Direccion":"Una direccion xxx"}
    # bloque_izquierda.columnconfigure(index=0, weight=1)
    campos = Campos_datos(ventana, campos)
    campos.pack(expand=True, fill="both")
    boton1 = ttk.Button(ventana, text="Ver campos", command=campos.actualizar_contenido1)
    boton1.pack()
    boton2 = ttk.Button(ventana, text="Modificar", command=campos.actualizar_contenido2)
    boton2.pack()
    
    ventana.mainloop()
    
