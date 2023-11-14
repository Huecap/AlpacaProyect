import tkinter as tk
from tkinter import ttk

class Tabla(ttk.Frame):
    def __init__(self, parent, columnas: tuple):
        ttk.Frame.__init__(self, parent, padding=10)
        
        self.columnconfigure(index=0, weight=1)
        self.rowconfigure(index=0, weight=1)
        
        self.columnas = columnas
        
        self.configurar_tabla()
        self.llenar_tabla()
        
    def configurar_tabla(self):
        
        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self)
        self.scrollbar.pack(side="right", fill="y", padx=5)  # Utilizar grid en lugar de pack

        # Crear el Treeview
        self.tabla = ttk.Treeview(
            self,
            selectmode="browse",
            yscrollcommand=self.scrollbar.set,
            columns=self.columnas,
            show="headings",
        )

        # Crear columnas 
        for columna in self.columnas:
            self.tabla.column(columna, anchor="w", width=120)
            self.tabla.heading(columna, text=columna)

        # Centrar columnas 
        for col in self.tabla["columns"]:
            self.tabla.column(col, anchor="center")

        # Configurar expansión del Treeview
        # self.tabla.grid(row=0, column=0, sticky="nsew")  # Utilizar grid en lugar de pack

        # Configurar expansión de la fila y columna del Treeview
        self.tabla.pack(expand=True, fill="both")

         # Asociar evento de selección a la función
        self.tabla.bind("<ButtonRelease-1>", self.obtener_valor_seleccionado)


    def obtener_valor_seleccionado(self, event):
        item_seleccionado = self.tabla.item(self.tabla.selection())
        valores_seleccionados = item_seleccionado['values']
        print("Valor seleccionado:", valores_seleccionados)
        
    
    def llenar_tabla(self):
        for n in range(0, 100):
            self.tabla.insert("", index="end", values=(f"{123+n}", "Juan", "Perez", "4323234", "12344123", "juanchi@gmail.com", "Maristreen 12341"))



if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.geometry("1320x640")

    # Seteando el tema 
    ventana.tk.call("source", "azure.tcl")
    ventana.tk.call("set_theme", "dark")
    
    campos = ("Id", "Nombre", "Apellido", "DNI", "Telefono", "Mail", "Direccion")
    tabla = Tabla(ventana, campos)
    tabla.pack(expand=True, fill="both")
    
    ventana.mainloop()
    