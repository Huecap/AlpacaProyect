
import tkinter as tk
from tkinter import ttk 
from functools import partial 

# - Import Lógica de negocio - # 
from NG_libro import Libro

# - Import Intefaz - # 
from IN_tabla import Tabla
from IN_barra_busqueda import Barra_busqueda
from IN_botonera import Botonera
from IN_campo_datos import Campos_datos

class Libro(ttk.Frame):
    def __init__(self, notebook):
        ttk.Frame.__init__(self, notebook)
        
        # Hacemos el frame Responsive 
        self.grid_columnconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=1)
        self.grid_columnconfigure(index=1, weight=1)
        
        
        
        # ? Valores del menú desplegable 
        self._combo = ["Codigo", "Titulo", "Estado", "Precio"]
        
        # ? Valores default del campo de datos 
        # Formato "Nombre_campo":(Valor,tipo) 
        
        self._campos_default = {"Codigo":(None,"i"), "Titulo":("","s"), "Estado":("","s"), "Precio":("","f")}
        self._campos_mostrar = {"Codigo":(None,"i"), "Titulo":("","s"), "Estado":("","s"), "Precio":("","f")}
        
        # ? ------- Variables de control ---------

        ## ------ Barra de Busqueda ----- ##
        ### Valores de la barra de busqueda 
        self._valores_barra_busqueda = ('Id', '')

        ## ------ Campos de datos ------- ## 
        ### Estado del campo de datos 
            ### Es una variable que alterna su estado para saber
            ### si el campo de estados se encuentra en modo edicion o en modo visualziación 
                #### False = Visualización 
                #### True = Edición 
        self._campos_datos_estado = tk.BooleanVar(value=False)
        ### -  Valores obtenidos de campos 
            ### Es una lista que contiene los valores obtenidos de los ttk.Entry de los campos de datos
        self._valores_obtenidos_campo = []
    
        ## ------ Tabla ------- ##
            ### - Valores fila de tabla 
            ### Variable que contiene los valores de la fila de la tabla seleccionada
        self._valores_tabla = [] 
        
        
        # Método utilizado para configurar todo el layout del Frame 
        self.setup_widgets()
        
    @property
    def valores_barra_busqueda(self):
        return self._valores_barra_busqueda    
        
    @property
    def valores_tabla(self):
        return self._valores_tabla    
    
    @valores_barra_busqueda.setter
    def valores_barra_busqueda(self, valores):
        self._valores_barra_busqueda = valores
        
    @valores_tabla.setter
    def valores_tabla(self, valores):
        self._valores_tabla = valores
    
    
    def actualizar_layout(self):
        t = self._valores_tabla
        valores = {"Codigo":(t[0],"i"), "Titulo":(t[1],"s"), "Estado":(t[2],"s"), "Precio":(t[3],"f")}
        self.datos_libro.actualizar_contenido(valores)
        # Forzamos a que cada vez que se actualicen los datos sea en la vista de datos no en modo edicion
        self._campos_datos_estado = tk.BooleanVar(value=True)
        self.modificar_estado_campos()
        
    
    def modificar_estado_campos(self):
        """
        Modifica los valores de los campos de datos 
        Modifica los botones que interactuan con los campos de datos 
        Solo modifican el estado (Es decir la visualizacion)
        Recibe como parametros los campos

        :param campos: Frame que contiene los campos a modificar 
        :type campos: ttk.Frame
        :param botonera: Frame que contiene la botonera a modificar
        :type botonera: ttk.Frame
        """
        if not self._campos_datos_estado.get():
            #Setear configuración modo edición 
            self.datos_libro.editar_campos()
            self.datos_libro.pack()
            botones_valores = {"Cancelar":{"Fila":0, 
                                                "Columna":0, 
                                                "Comando":lambda:self.modificar_estado_campos()}, 
                                    "Guardar Cambios":{"Fila":0, 
                                                   "Columna":1, 
                                                   "Comando":lambda:self.obtener_campos()}}
            self._campos_datos_estado.set(value=True)
        else:
            # Setear configuración modo visualización 
            self.datos_libro.ver_campos()
            self.datos_libro.pack()
            botones_valores = {"Nuevo Libro":{"Fila":0, 
                                                   "Columna":0,
                                                   "Comando":lambda:self.nuevo_libro()}, 
                                    "Modificar Libro":{"Fila":0, 
                                                   "Columna":1, 
                                                   "Comando":lambda:self.modificar_estado_campos()}}
            self._campos_datos_estado.set(value=False)
        
        self.botones_nuevo_editar.editar_botonera(botones_valores)
        print(self._campos_datos_estado)
    
    def obtener_campos(self):
        """
        Asigna a la variable self._valores_obtenidos_campo los valores colocados en los ttk.Entry (verifica que los widgets
        que contenga el Frame sean del tipo ttk.Entry y devuelven su contenido)
        

        :param campos: Frame que contiene a los campos de datos
        :type campos: ttk.Frame
        :param botonera: Frame que contiene a los botones que interactuan con los campos de datos
        :type botonera: ttk.Frame
        """
        datos = []
        for widget in self.datos_libro.winfo_children():
            if type(widget) is ttk.Entry:
                datos.append(widget.get())  
                
                self._valores_obtenidos_campo = datos  
        self.modificar_estado_campos()

    def nuevo_libro(self):
        """
        Funcion para el boton nuevo libro
        - Limpia los campos de entrada de datos
        - Cambia los botones a "cancelar" "Guardar"

        :param botonera: pasamos la botonera a modificar 
        :type botonera: _type_
        """
        # self._campos_datos_estado = tk.BooleanVar(value=False)
        self.datos_libro.actualizar_contenido(self._campos_default)
        self.modificar_estado_campos()
        
    
    def eliminar_libro(self, campo, botonera):
        pass
    
    def guardar_libro(self, campo, botonera):
        pass
    
    def actualizar_tabla(self):
        pass
        
    def actualizar_por_busqueda(self):
        # Aca me tiene que actualizar la tabla (hacer un filter)
        # Y si existe una sola coincidencia me la tiene que mostrar
        print(self._valores_barra_busqueda)
    
    def mostrar_valor_tabla(self):
        self.actualizar_layout()
        print(self._valores_tabla)

    ## ---------- Metodos para configuración de Layout ---------- ##      
    def setup_widgets(self):
        
        # ! Creo que esto hay que borrarlo 
        #fram2 = ttk.Frame(self)
        #fram2.grid(row=1, column=0, sticky="nsew")

        ## ------ Frame izquierdo ------ ## 
        self.bloque_izquierda = ttk.Frame(self, padding=(10))
        self.bloque_izquierda.grid(row=0,column=0, sticky="nsew")
        #self.bloque_izquierda.grid_columnconfigure(index=0, weight=1)
        
        
        # Creamos la barra de busqueda y la colocamos 
        
        # self.barra_busqueda = Barra_busqueda(self.bloque_izquierda, self._combo, lambda:self.obtener_barra(self.barra_busqueda))
        # Barra busqueda recibe "El frame Padre", "Los valores para el menú", "El objeto que contiene la variable a retornar el valor"
        self.barra_busqueda = Barra_busqueda(self.bloque_izquierda, self._combo, self)
        self.barra_busqueda.pack(expand=True, fill="both")
        
        
        
        # Creamos los campos para ver la información del socio 
        self.datos_libro = Campos_datos(self.bloque_izquierda, self._campos_default)
        self.datos_libro.pack(expand=True, fill="both")
        
        
        
        # Creamos la botonera 
        ## - Funcionalidades de los botones - ##
        
        # ! Esto hay que borrarlo creo 
        # modificar = partial(self.modificar_estado_campos , campos=self.datos_libro)

        ## - Valores de la botonera - ##
        botones_nuevo_editar = {"Nuevo Libro":{"Fila":0, 
                                               "Columna":0,
                                               "Comando":lambda:self.nuevo_libro()}, 
                                "Modificar Libro":{"Fila":0, 
                                                   "Columna":1, 
                                                   "Comando":lambda:self.modificar_estado_campos()}}

        self.botones_nuevo_editar = Botonera(self.bloque_izquierda, botones_nuevo_editar)
        self.botones_nuevo_editar.pack(expand=True, fill="both")
        
        
        botones_nuevoPrestamo_verPrestamos = {"Nuevo Prestamo":{"Fila":0, 
                                                                "Columna":0}, 
                                              "Ver Prestamos Libro":{"Fila":0, 
                                                                     "Columna":1}}
        self.botones_nuevoPrestamo_verPrestamos = Botonera(self.bloque_izquierda, botones_nuevoPrestamo_verPrestamos)
        self.botones_nuevoPrestamo_verPrestamos.pack(expand=True, fill="both")
        
        
        botones_eliminar = {"Eliminar Libro":{"Fila":0, 
                                              "Columna":0}}
        self.botones_nuevoPrestamo_verPrestamos = Botonera(self.bloque_izquierda, botones_eliminar)
        self.botones_nuevoPrestamo_verPrestamos.pack()
        
        
        ## Frame derecho 
        self.bloque_derecha = ttk.Frame(self, padding=10)
        self.bloque_derecha.grid(row=0, column=1, rowspan=2, sticky="snew")
        self.bloque_derecha.grid_columnconfigure(index=1, weight=2)
        # self.bloque_derecha.grid_rowconfigure(index=0, weight=1)
        
        # Tabla 
        campos = ("Codigo", "Titulo", "Estado", "Precio")
        self.tabla = Tabla(self.bloque_derecha, campos, self)
        self.tabla.pack(expand=True, fill="both")
        
        
if __name__ == "__main__":
    ventana = tk.Tk()

    # Definimos la resolucion por defecto
    ventana.geometry("1320x640")

    # Seteamos el tema
    ventana.tk.call("source", "azure.tcl")
    ventana.tk.call("set_theme", "dark")

    # Creamos el Frame principal
    programa = Libro(ventana)
    programa.pack(expand=True, fill="both")

    ventana.mainloop()