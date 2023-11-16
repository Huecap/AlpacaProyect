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
        
        self._tabla_base = TablaLibros
        
        # ? Valores del menú desplegable 
        self._combo = {"codigo":"i", "titulo":"s", "estado":"s", "precio":"f"}
        
        # ? Valores default del campo de datos 
        # Formato "Nombre_campo":(Valor,tipo) 
        
        self._campos_default = {"Codigo":(None,"i"), "Titulo":("","s"), "Precio":("","f"), "Estado":("",("Disponible", "Prestado", "Extraviado"))}
        # self._campos_mostrar = {"Codigo":(None,"i"), "Titulo":("","s"), "Estado":("","s"), "Precio":("","f")}
        
        # ? ------- Variables de control ---------

        ## ------ Barra de Busqueda ----- ##
        ### Valores de la barra de busqueda 
        self._valores_barra_busqueda = ('codigo', '')

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
    
        ## ------ Botones ------## 
        self._bandera_nuevo = False

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
    
    @property
    def tabla_base(self):
        return self._tabla_base
    
    
    @valores_barra_busqueda.setter
    def valores_barra_busqueda(self, valores):
        self._valores_barra_busqueda = valores
        
    @valores_tabla.setter
    def valores_tabla(self, valores):
        self._valores_tabla = valores
    
    
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
            
    def actualizar_layout(self, valor=None, campo=None):
        """
        Funcion para actualizar los campos de datos recibiendo como paremetro un valor 

        :param valor: Los valores a los que queremos actualizar los datos del libro 
        :type valor: _type_, optional
        :param campo: _description_, defaults to None
        :type campo: _type_, optional
        """
        if valor is None:
            t = self._valores_tabla
            self._valores_obtenidos_campo = self._valores_tabla
            valores = {"Codigo":(t[0],"i"), "Titulo":(t[1],"s"), "Precio":(t[3],"f"), "Estado":(t[2],("Disponible", "Prestado", "Extraviado"))}
            self.datos_libro.actualizar_contenido(valores)
            # Forzamos a que cada vez que se actualicen los datos sea en la vista de datos no en modo edicion
            self._campos_datos_estado = tk.BooleanVar(value=True)
            self.modificar_estado_campos()
        
    def mostrar_valor_tabla(self):
        self.actualizar_layout()
        # print(self._valores_tabla)
    
    def modificar_estado_campos(self, modificar=True):
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
                                                "Comando":lambda:self.cancelar_operacion()}, 
                                    "Guardar Cambios":{"Fila":0, 
                                                "Columna":1, 
                                                "Comando":lambda:self.guardar_libro()}}
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
                                                "Comando":lambda:self.modificar_libro()}}
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
            if type(widget) is ttk.Entry or (type(widget) is ttk.Combobox):
                datos.append(widget.get())  
                
                self._valores_obtenidos_campo = datos  
        # self.modificar_estado_campos()
        print(self._valores_obtenidos_campo)

    ###### APLICANDO LOGICA DE NEGOCIO ###### 

    def nuevo_libro(self):
        """
        Funcion para el boton nuevo libro
        - Limpia los campos de entrada de datos
        - Cambia los botones a "cancelar" "Guardar"

        :param botonera: pasamos la botonera a modificar 
        :type botonera: _type_
        """
        print('Nuevo Librooo')
        self._bandera_nuevo = True
        #self._campos_default = {"Codigo":(None,"i"), "Titulo":("","s"), "Precio":("","f")}
        self.datos_libro.actualizar_contenido({"Codigo":(None,"i"), "Titulo":("","s"), "Precio":("","f")})
        #self.obtener_campos()
        self.modificar_estado_campos(modificar=False)
        self.datos_libro.actualizar_contenido(self._campos_default)
        #self._campos_default = {"Codigo":(None,"i"), "Titulo":("","s"), "Estado":("","s"), "Precio":("","f")}
        #self.modificar_estado_campos()
        # print(self._valores_obtenidos_campo)
        # self._campos_datos_estado = tk.BooleanVar(value=False)
        
    
    def eliminar_libro(self):
        """
        Elimina el libro seleccionado, si no hay ninguno no hace nada 
        """
        # Obtenemos los campos 
        self.obtener_campos()
        print(self._valores_obtenidos_campo)
        if self._valores_obtenidos_campo == [] or ("" in self._valores_obtenidos_campo):
            # No hay libro que eliminar 
            self.abrir_ventana_emergente(mensaje="Error No hay ningun libro seleccionado")
        else:
            valor = self.abrir_ventana_emergente(mensaje="¿Esta seguro que quiere eliminar este libro?", tipo=1)
            if valor:
            # Aca me tiene que eliminar el libro 
                print(self._valores_tabla)
                libro = self._tabla_base.create_libro(int(self._valores_tabla[0]))
                libro.eliminar_libro()
                self._valores_barra_busqueda = ('codigo', '')   
                self.actualizar_por_busqueda()
                self.abrir_ventana_emergente("Eliminación correcta", mensaje="Se elimino el Libro correctamente", tipo=2)

                self._valores_obtenidos_campo = []
                self._campos_datos_estado = tk.BooleanVar(value=True)
                self.modificar_estado_campos()
                #self.modificar_estado_campos()
        self._campos_datos_estado = tk.BooleanVar(value=True)
        self.datos_libro.actualizar_contenido(self._campos_default)
        self.modificar_estado_campos()
        # Me tiene que salir una ventana que me digo "Esta seguro que desea eliminar el libro"
    
    def guardar_libro(self):
        """
        Guarda el estado del libro 
        """
        self.obtener_campos()
        if self._valores_obtenidos_campo == [] or ("" in self._valores_obtenidos_campo):
            self.abrir_ventana_emergente(mensaje="Error No se puede guardar el libro, hay campos vacios")
            print('No hya nada')
            #libro = Libro(self._valores_obtenidos_campo)
        else:
            # ! Arregalr esto 
            # Esto es para la creacion de los libros 
            # print(self._valores_obtenidos_campo)
            if self._bandera_nuevo:
                libro = Libro(self._valores_obtenidos_campo[0], float(self._valores_obtenidos_campo[1]))
                self._bandera_nuevo = False
                self.abrir_ventana_emergente(titulo="Libro creado", mensaje="Libro creado con exito", tipo=2)
                
            else: 
                libro = self._tabla_base.create_libro(int(self._valores_tabla[0]))
                #print(self._valores_obtenidos_campo)
                libro.modificar_datos(self._valores_obtenidos_campo[0], float(self._valores_obtenidos_campo[1]), self._valores_obtenidos_campo[2])
                self.abrir_ventana_emergente("Modificacion correcta", mensaje="Se modifico el libro correctamente", tipo=2)
        
        self._campos_datos_estado = tk.BooleanVar(value=True)
        self.datos_libro.actualizar_contenido(self._campos_default)
        self.modificar_estado_campos()

        self._valores_barra_busqueda = ('codigo', '')
        self.actualizar_por_busqueda()
    
    def modificar_libro(self):
        """
        Modifica los campos para poder modificar el contenido de un libro 
        """
        self.modificar_estado_campos()
        print('Se modificooo')
    
    def cancelar_operacion(self):
        """
        Cancela la operacion
        """
        self.modificar_estado_campos()
        
    ##### LOGICA DE NEGOCIO PRESTAMOS 
    
    def nuevo_prestamo(self):
        self._notebook.select(0)

        
    def ver_prestamo(self):
        self._notebook.select(0)



    def actualizar_por_busqueda(self):
        """
        Actualiza la tabla con los valores obtenidos de la barra de busqueda 
        """
        # Aca me tiene que actualizar la tabla (hacer un filter)
        # Y si existe una sola coincidencia me la tiene que mostrar
        print(self._valores_barra_busqueda)
        campo =  self._valores_barra_busqueda[0]
        valor = self._valores_barra_busqueda[1]
        if campo == 'codigo' and valor != "":
            v = (campo, int(valor))
        elif campo == 'precio' and valor !="":
            v = (campo, float(valor))
        else:
            v = (campo, valor)
        
        self.tabla.cargar_tabla(valor=v[1], camp=v[0])
    

    ## ---------- Metodos para configuración de Layout ---------- ##      
    def setup_widgets(self):

        ## ------ Frame izquierdo ------ ## 
        self.bloque_izquierda = ttk.Frame(self, padding=(10))
        self.bloque_izquierda.grid(row=0,column=0, sticky="nsew")
        
        
        # Creamos la barra de busqueda y la colocamos 
        
        # Barra busqueda recibe "El frame Padre", "Los valores para el menú", "El objeto que contiene la variable a retornar el valor"
        self.barra_busqueda = Barra_busqueda(self.bloque_izquierda, self._combo, self)
        self.barra_busqueda.pack(expand=True, fill="both")
        
        
        
        # Creamos los campos para ver la información del socio 
        self.datos_libro = Campos_datos(self.bloque_izquierda, self._campos_default)
        self.datos_libro.pack(expand=True, fill="both")
        
        
        
        # Creamos la botonera 
        ## - Funcionalidades de los botones - ##

        ## - Valores de la botonera - ##
        botones_nuevo_editar = {"Nuevo Libro":{"Fila":0, 
                                               "Columna":0,
                                               "Comando":lambda:self.nuevo_libro()}, 
                                "Modificar Libro":{"Fila":0, 
                                                   "Columna":1, 
                                                   "Comando":lambda:self.modificar_estado_campos()}}
        ### BOTONES nuevo y editar
        self.botones_nuevo_editar = Botonera(self.bloque_izquierda, botones_nuevo_editar)
        self.botones_nuevo_editar.pack(expand=True, fill="both")
        
        botones_nuevoPrestamo_verPrestamos = {"Nuevo Prestamo":{"Fila":0, 
                                                                "Columna":0,
                                                                "Comando":lambda:self.nuevo_prestamo()}, 
                                              "Ver Prestamos Libro":{"Fila":0, 
                                                                     "Columna":1,
                                                                    "Comando":lambda:self.ver_prestamo()}}
        ### BOTONES Nuevo y ver prestamos
        self.botones_nuevoPrestamo_verPrestamos = Botonera(self.bloque_izquierda, botones_nuevoPrestamo_verPrestamos)
        self.botones_nuevoPrestamo_verPrestamos.pack(expand=True, fill="both")
        
        ### BOTONES eliminar
        botones_eliminar = {"Eliminar Libro":{"Fila":0, 
                                              "Columna":0,
                                              "Comando":lambda:self.eliminar_libro()}}
        self.botones_nuevoPrestamo_verPrestamos = Botonera(self.bloque_izquierda, botones_eliminar)
        self.botones_nuevoPrestamo_verPrestamos.pack()
        
        
        ## Frame derecho 
        self.bloque_derecha = ttk.Frame(self, padding=10)
        self.bloque_derecha.grid(row=0, column=1, rowspan=2, sticky="snew")
        self.bloque_derecha.grid_columnconfigure(index=1, weight=2)
        
        # Tabla 

        
        
        
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