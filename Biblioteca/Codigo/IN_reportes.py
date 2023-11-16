# Reporte que importa de las tablas los SELECTs que le sirven
# Crear el reporte como un archivo
# Mostrar el archivo en una ventana aparte
# (no crear interfaz de usuario para el reporte mas que mostrar el archivo anteriormente creado)
# Pueden crearse clases hijas para hacer diferentes reportes


import tkinter as tk
from tkinter import ttk, messagebox
from functools import partial 

# - Import Lógica de negocio - # 
from NG_libro import Libro

# - Import Intefaz - # 
from IN_tabla import Tabla
from IN_barra_busqueda import Barra_busqueda
from IN_botonera import Botonera
from IN_campo_datos import Campos_datos

# - Import  Base de datos - #
from DB_tabla_libros import TablaLibros
from DB_tabla_socios import TablaSocios
from DB_tabla_prestamos import TablaPrestamos

class Reportes_in(ttk.Frame):
    def __init__(self, notebook):
        ttk.Frame.__init__(self, notebook)
        
        self._notebook = notebook
        
        # Hacemos el frame Responsive 
        self.grid_columnconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=1)
        self.grid_columnconfigure(index=1, weight=1)
        
        # Método utilizado para configurar todo el layout del Frame 
        self.setup_widgets()
        

    def abrir_ventana_emergente(self, titulo="Error", mensaje="Aca va un mensaje de error", tipo=0):
        #ventana_emergente = #tk.Toplevel(self)
        #ventana_emergente.title("Ventana Emergente")

        #etiqueta = tk.Label(ventana_emergente, text="¡Esta es una ventana emergente!")
        #etiqueta.pack(padx=10, pady=10)
        #ventana_emergente.wait_window(ventana_emergente)
        #self.focus_set()
        if tipo == 0 :
            ventana_emergente =  messagebox.showerror(titulo, mensaje)
            print(ventana_emergente)
        elif tipo == 1:
            ventana_emergente = messagebox.askyesno(titulo, mensaje)
        elif tipo == 2:
            ventana_emergente = messagebox.showinfo(titulo, mensaje)
        return ventana_emergente
    ###### APLICANDO LOGICA DE NEGOCIO ###### 

    def mostrar_ventana_informativa(self, texto_largo):
    # Crear una nueva ventana
        ventana_info = tk.Toplevel(self)
        ventana_info.title("Ventana Informativa")

        # Crear un widget de texto
        cuadro_texto = tk.Text(ventana_info, wrap="word", width=40, height=10)
        cuadro_texto.pack(padx=10, pady=10)

        # Insertar el texto largo en el widget de texto
        cuadro_texto.insert("1.0", texto_largo)

    def cant_lib_est(self):
        lib_dispo = len(TablaLibros.show("Disponible", "estado"))
        lib_extr = len(TablaLibros.show("Extraviado", "estado"))
        lib_Pres = len(TablaLibros.show("Prestado", "estado"))
        
        message =f"- Libros Disponibles: {lib_dispo} \n - Libros Extraviados: {lib_extr} \n - Libros Prestados: {lib_Pres}"
        self.mostrar_ventana_informativa(message)
        # self.abrir_ventana_emergente(titulo="Cantidad de libros estado", mensaje="message", tipo=2)
    def libros_estado(self):
        prec_tot = 0
        for n in (TablaLibros.show("Extraviado", "estado")):
            prec_tot += n[3]
        self.abrir_ventana_emergente(titulo="Precio Libros extraviados", mensaje=f"El precio de la suma de libros extraviados son de:    {prec_tot}", tipo=2)

    
        
        

    ## ---------- Metodos para configuración de Layout ---------- ##      
    def setup_widgets(self):

        ## ------ Frame izquierdo ------ ## 
        self.bloque_izquierda = ttk.Frame(self, padding=(10))
        self.bloque_izquierda.grid(row=0,column=0, sticky="nsew")
        
        
        
        

        ## - Valores de la botonera - ##
        botones_nuevo_editar = {"Cantidad de libros en cada estado":{"Fila":0, 
                                               "Columna":0,
                                               "Comando":lambda:self.cant_lib_est()}, 
                                "Precio Extraviados":{"Fila":0, 
                                                   "Columna":1, 
                                                   "Comando":lambda:self.libros_estado()}}
        ### BOTONES nuevo y editar
        self.botones_nuevo_editar = Botonera(self.bloque_izquierda, botones_nuevo_editar)
        self.botones_nuevo_editar.pack(expand=True, fill="both")
        


        
        
        ## Frame derecho 
        self.bloque_derecha = ttk.Frame(self, padding=10)
        self.bloque_derecha.grid(row=0, column=1, rowspan=2, sticky="snew")
        self.bloque_derecha.grid_columnconfigure(index=1, weight=2)
        
        message = 'No llegamos a completar todas las funcionalidades que queríamos, así que consideramos esta nuestra versión 0.8 \
            \n\nReferente a los reportes nos gustaría en un futuro implementar las librerias presentadas en clase para obtener reportes de manera mas "Presentable " y "Util":\
               \n 1) Listado de Prestamos "Vecidos" se pueden obtener en la pesataña Prestamos \
               \n \
               \n 2) Nombre de todos los socios que solicitaron un Libro, se pueden obtener en la pestaña Libros \
               \n \
               \n 3) Listado de Prestamos de socios identificado por numero de socio'
        cuadro_texto = tk.Text(self.bloque_derecha, wrap="word", width=80, height=15, )
        cuadro_texto.pack(padx=10, pady=10)

        # Insertar el texto largo en el widget de texto
        cuadro_texto.insert("1.0", message)
        cuadro_texto.config(state="disabled")
        # self.mostrar_ventana_informativa(message)
        
        ### BOTONES Nuevo y ver prestamos
        #self.botones_nuevoPrestamo_verPrestamos = Botonera(self.bloque_derecha, botones_nuevoPrestamo_verPrestamos)
        #self.botones_nuevoPrestamo_verPrestamos.pack(expand=True, fill="both")

        
        
        
if __name__ == "__main__":
    ventana = tk.Tk()

    # Definimos la resolucion por defecto
    ventana.geometry("1280x480")

    # Seteamos el tema
    ventana.tk.call("source", "azure.tcl")
    ventana.tk.call("set_theme", "dark")

    # Creamos el Frame principal
    programa = Reportes_in(ventana)
    programa.pack(expand=True, fill="both")

    ventana.mainloop()