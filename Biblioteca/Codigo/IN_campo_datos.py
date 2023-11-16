import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

from HR_validaciones_interfaz import validar_entry_int, validar_entry_str, validar_entry_float

class Campos_datos(ttk.LabelFrame):
    def __init__(self, parent, valores):
        ttk.LabelFrame.__init__(self, parent, text="Datos")
        
        # Valores tupla 
            # valores[0] = Texto a mostrar
            # valores[1] = Tipo de dato 
        self._valores = valores
                
                
        # Validacion de campos 
        self.vcmd_int = self.register(lambda P: validar_entry_int(P))
        self.vcmd_str = self.register(lambda P: validar_entry_str(P))
        self.vcmd_float = self.register(lambda P: validar_entry_float(P))        
        # Metodos Responsive 
        #for n in range(0,len(valores)):
         #   self.columnconfigure(index=n, weight=1)
          #  self.rowconfigure(index=n, weight=1)
       # if default == 1:
        # self.editar_campos()
        #elif default == 2:
        self.ver_campos()
            
    def eliminar_contenido(self):
        # Eliminar widgets actuales dentro del Frame
        for widget in self.winfo_children():
            widget.destroy()    
        
    def editar_campos(self):
        self.eliminar_contenido()
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)
        
        self.label_socioID = ttk.Label(self, text="Codigo", anchor="center")
        self.label_socioID.grid(row=0, column=0, padx=5, pady=(0,10), sticky="nswe")
        
        self.label_numero_socioID = ttk.Label(self, text=self._valores["Codigo"][0], anchor="center")
        self.label_numero_socioID.grid(row=0, column=1, pady=(0,10),  sticky="nswe")
        
        
        n = 0 
        for key, value in self._valores.items():
            if n!=0:
                if key == "Estado":
                    self.label_nombre = ttk.Label(self, text=key, anchor="center")
                    self.label_nombre.grid(row=n, column=0, padx=5, pady=(0,10), sticky="we")
                    
                    self.filtro = ttk.Combobox(self, state="readonly", values=value[1], width=10)
                    self.filtro.grid(row=n, column=1, padx=5, pady=(0,10), sticky="we")
                    self.filtro.current(0)
                    n += 1
                    continue
                elif "Fecha" in key:
                    self.label_nombre = ttk.Label(self, text=key, anchor="center")
                    self.label_nombre.grid(row=n, column=0, padx=(5,10), pady=(0,10), sticky="we")
                    
                    if "devolucion" in key:
                        self.entry_fecha = DateEntry(self, width=12, background="darkblue", foreground="white",date=None, borderwidth=2, state='readonly', 
                                                     selectmode='day',year=2000,month=1,day=1)
                    else:
                        self.entry_fecha = DateEntry(self, width=12, background="darkblue", foreground="white",date=None, borderwidth=2, state='readonly')

                    self.entry_fecha.grid(row=n, column=1, padx=(5, 10), pady=(0,10), sticky="we")
                    n += 1
                    continue
                
                elif ("ID" in key )or (key == "Codigo"):
                    self.label_socioID = ttk.Label(self, text=key, anchor="center")
                    self.label_socioID.grid(row=n, column=0, padx=5, pady=(0,10), sticky="nswe")
                    
                    self.label_numero_socioID = ttk.Label(self, text=value[0], anchor="center")
                    self.label_numero_socioID.grid(row=n, column=1, pady=(0,10),  sticky="nswe")
                    n += 1
                    continue
                    #self.campo_dato1 = ttk.Combobox(self, width=10, justify="center",  validate="key", validatecommand=(self.vcmd_int, '%P'))
                    # self.campo_dato1.insert(n, value[0])
                    
                self.label_nombre = ttk.Label(self, text=key, anchor="center")
                self.label_nombre.grid(row=n, column=0, padx=5, pady=(0,10), sticky="we")
                if value[1] == "i":
                    self.campo_dato1 = ttk.Entry(self, width=10, justify="center",  validate="key", validatecommand=(self.vcmd_int, '%P'))
                    self.campo_dato1.insert(n, value[0])

                elif value[1] == "s":
                    self.campo_dato1 = ttk.Entry(self, width=10, justify="center")
                    self.campo_dato1.insert(n, value[0])

                elif value[1] == "f":
                    self.campo_dato1 = ttk.Entry(self, width=10, justify="center",  validate="key", validatecommand=(self.vcmd_float, '%P'))
                    self.campo_dato1.insert(n, value[0])

                self.campo_dato1.grid(row=n, column=1, padx= (5, 20), pady=(0,20), sticky="ew")
            self.rowconfigure(index=n, weight=1)
            n += 1

    def ver_campos(self):

        self.eliminar_contenido()
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)
        
        n = 0 
        for key, value in self._valores.items():
            self.label_nombre = ttk.Label(self, text=key, anchor="center")
            self.label_nombre.grid(row=n, column=0, padx=5, pady=(0,10), sticky="we")
            self.campo_dato1 = ttk.Label(self, text=value[0],width=11, anchor="center")
            self.campo_dato1.grid(row=n, column=1, padx= (5, 20), pady=(0,29), sticky="ew")
            self.rowconfigure(index=n, weight=1)

            n += 1

    def obtener_datos(self):
        """
        Recorre todos los entry y retorna una lista con el contenido de estos 
        :return: lista de contenido de entry
        :rtype: list
        """
        datos = []
        for widget in self.winfo_children():
            if (type(widget) is ttk.Entry) or (type(widget) is ttk.Combobox):
                datos.append(widget.get())
        print(f"camposss {datos}")
        return datos 
        

    def actualizar_contenido(self, valores):
        self._valores = valores
        # self.ver_campos()

    def actualizar_contenido2(self):
        self.eliminar_contenido()
        self.editar_campos()
        self.obtener_datos()
        
        
if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.geometry("600x400")
    
    # Seteando el tema 
    ventana.tk.call("source", "azure.tcl")
    ventana.tk.call("set_theme", "dark")

    
    campos = {"Codigo":(None,"i"), "Titulo":("","s"), "Estado":("","s"), "Precio":("","f")}
 # bloque_izquierda.columnconfigure(index=0, weight=1)
    campos = Campos_datos(ventana, campos)
    campos.pack(expand=True, fill="both")
    boton1 = ttk.Button(ventana, text="Ver campos", command=campos.actualizar_contenido1)
    boton1.pack()
    boton2 = ttk.Button(ventana, text="Modificar", command=campos.actualizar_contenido2)
    boton2.pack()
    
    ventana.mainloop()
    
