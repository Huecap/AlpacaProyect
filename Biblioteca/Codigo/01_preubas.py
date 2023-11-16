
import tkinter as tk
from tkinter import ttk, messagebox
from functools import partial 
from datetime import datetime

# - Import Lógica de negocio - # 
from NG_socio import Socio
from NG_libro import Libro
from NG_prestamo import Prestamo

# - Import Intefaz - # 
from IN_tabla import Tabla
from IN_barra_busqueda import Barra_busqueda
from IN_botonera import Botonera
from IN_campo_datos import Campos_datos

# - Import  Base de datos - #
from DB_tabla_prestamos import TablaPrestamos
from DB_tabla_libros import TablaLibros
from DB_tabla_socios import TablaSocios

class Prestamo_in(ttk.Frame):
    def __init__(self, notebook):
        ttk.Frame.__init__(self, notebook)
        
        self._notebook = notebook
        
        # Hacemos el frame Responsive 
        self.grid_columnconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=1)
        self.grid_columnconfigure(index=1, weight=1)
        
        #self._tabla_base = TablaLibros
        self._tabla_base = TablaPrestamos
        
        # ? Valores del menú desplegable 
        self._combo = {"codigo":"i","libroCodigo":"i", "cantidadDias":"i", "estado":"s", "socioID":"i"}

            #         self._combo = ["Codigo_libro", "Titulo", "Fecha_prestamo", "Dias_prestados", "Fecha_devolucion", "Estado", "ID_Socio"]

        # fechaPrestamo, cantidadDias, fechaDevolucion, estado, socioID, libroCodigo
        # ? Valores default del campo de datos 
        # Formato "Nombre_campo":(Valor,tipo) 
        # self._campos_default = {"libro":(None, "i") ,"Nombre":("","s"), "Apellido":("","s"), "DNI":("", "i"), "Telefono":("", "i"), "Mail":("","s"), "Direccion":("","s")}
        self._campos_default = {"Codigo":(None, "i") ,"Fecha_prestamo":("","d"), "Dias_prestados":("", "i"), "Codigo Socio":("", "i"), "Estado":("",("En Fecha",
            "Vencido",
            "Devuelto",
            "Extraviado",
        )), "Codigo Libro":("", "i")}
        
        # self._campos_mostrar = {"Codigo":(None,"i"), "Titulo":("","s"), "Estado":("","s"), "Precio":("","f")}
        
        # ? ------- Variables de control ---------

        ## ------ Barra de Busqueda ----- ##
        ### Valores de la barra de busqueda 
        self._valores_barra_busqueda = ('Codigo', '')

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
            valores = {"Codigo":(t[0], "i"), "Fecha_prestamo":(t[1],"d"), "Dias_prestados":(t[2], "i"), "Fecha_devolucion":(t[3],"d"), "Estado":(t[4],("En Fecha",
            "Vencido",
            "Devuelto",
            "Extraviado",
        )), "ID_Socio":(t[5], "i"), "libroCodigo":(t[6], "i")}
            self.datos_socio.actualizar_contenido(valores)
            # Forzamos a que cada vez que se actualicen los datos sea en la vista de datos no en modo edicion
            self._campos_datos_estado = tk.BooleanVar(value=True)
            self.modificar_estado_campos()
        
    #def mostrar_valor_tabla(self):
    #    """
    #    Nos muestar el 
    #    """
    #    self.actualizar_layout()
    
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
            self.datos_socio.editar_campos()
            self.datos_socio.pack()
            botones_valores = {"Cancelar":{"Fila":0, 
                                                "Columna":0, 
                                                "Comando":lambda:self.cancelar_operacion()}, 
                                    "Guardar Cambios":{"Fila":0, 
                                                "Columna":1, 
                                                "Comando":lambda:self.guardar_libro()}}
            self._campos_datos_estado.set(value=True)
        else:
            # Setear configuración modo visualización 
            self.datos_socio.ver_campos()
            self.datos_socio.pack()
            botones_valores = {"Nuevo Prestamo":{"Fila":0, 
                                                "Columna":0,
                                                "Comando":lambda:self.nuevo_pres()}, 
                                    "Modificar Prestamo":{"Fila":0, 
                                                "Columna":1, 
                                                "Comando":lambda:self.modificar_prestamo()}}
            self._campos_datos_estado.set(value=False)
        self.botones_nuevo_editar.editar_botonera(botones_valores)
    
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
        for widget in self.datos_socio.winfo_children():
            if (type(widget) is not ttk.Label):
                datos.append(widget.get())  
                
                self._valores_obtenidos_campo = datos  
        # self.modificar_estado_campos()

    ###### APLICANDO LOGICA DE NEGOCIO ###### 

    def nuevo_pres(self):
        """
        Funcion para el boton nuevo libro
        - Limpia los campos de entrada de datos
        - Cambia los botones a "cancelar" "Guardar"

        :param botonera: pasamos la botonera a modificar 
        :type botonera: _type_
        """
        self._bandera_nuevo = True
        self.datos_socio.actualizar_contenido(self._campos_default)
        self.modificar_estado_campos(modificar=False)

    
    def eliminar_socio(self):
        """
        Elimina el socio seleccionado, si no hay ninguno lo informa  
        """
        # Obtenemos los campos 
        self.obtener_campos()
        if self._valores_obtenidos_campo == [] or ("" in self._valores_obtenidos_campo):
            # No hay libro que eliminar 
            self.abrir_ventana_emergente(mensaje="Error No hay ningun Socio seleccionado")
        else:
            valor = self.abrir_ventana_emergente(mensaje="¿Esta seguro que quiere eliminar este Socio?", tipo=1)
            if valor:
            # Aca me tiene que eliminar el libro 
                libro = self._tabla_base.create_prestamo(int(self._valores_tabla[0]))
                libro.eliminar_prestamo()
                self._valores_barra_busqueda = ('Codigo', '')   
                self.actualizar_por_busqueda()
                self.abrir_ventana_emergente("Eliminación correcta", mensaje="Se elimino el Prestamo correctamente", tipo=2)
                self._valores_obtenidos_campo = []
                self._campos_datos_estado = tk.BooleanVar(value=True)
                self.modificar_estado_campos()

                #self.modificar_estado_campos()
        # Me tiene que salir una ventana que me digo "Esta seguro que desea eliminar el libro"
    
    def guardar_libro(self):
        """
        Guarda el estado del libro 
        """
        self.obtener_campos()
        if self._valores_obtenidos_campo == [] or ("" in self._valores_obtenidos_campo):
            self.abrir_ventana_emergente(mensaje="Error No se puede guardar el Socio, hay campos vacios")
        else:
            # ! Arregalr esto 
            # Esto es para la creacion de los libros 
                
                # Tenemos que verificar si existe el socio , si no existe salta una ventana 
                    # SI existe el socio lo isntanciamos 
                # Tenemo que verificar si exsite el libro, si no existe salta una ventana
            if not self._bandera_nuevo:
                id_socio = self._valores_tabla[5]
                id_libro = self._valores_tabla[6]
            else: 
                id_socio = self._valores_obtenidos_campo[3]
                id_libro = self._valores_obtenidos_campo[4]
            if TablaLibros.show(int(id_libro)):
                libro = TablaLibros.create_libro(int(id_libro)) 
                print(id_socio)
                if TablaSocios.show(int(id_socio)):
                    socio = TablaSocios.create_socio(int(id_socio))
                    if TablaPrestamos.show(int(id_socio), "socioID"):
                            
                            # Si existe lo instanciamos 
                        self.obtener_campos()
                        # libro = self._tabla_base.create_libro(int(self._valores_tabla[0]))
                        #prestamo = Socio(self._valores_obtenidos_campo[0], self._valores_obtenidos_campo[1],
                        #              int(self._valores_obtenidos_campo[2]), int(self._valores_obtenidos_campo[3]),
                        
                        if self._bandera_nuevo:
                        #              self._valores_obtenidos_campo[4], self._valores_obtenidos_campo[5]
                            #              )
                            contador = 0
                            for n in (TablaPrestamos.show(int(id_socio), "socioID")):
                                if n[4] == 'Vencido' or n[4] == 'Extraviado':
                                    contador += 1
                            if contador < 3:
                                fecha = datetime.strptime((self._valores_obtenidos_campo[0]), '%d/%m/%y').date()
                                prestamo = Prestamo(fecha,
                                                    self._valores_obtenidos_campo[1],
                                                    socio, 
                                                    libro)                                    
                                self._bandera_nuevo = False
                            else:
                                self.abrir_ventana_emergente("Error", mensaje="Este socio tiene demasiados prestamos")
                                self._bandera_nuevo = False
                        else: 
                            print(self._valores_obtenidos_campo)
                            self.obtener_campos()
                            prestamo = self._tabla_base.create_prestamo(int(self._valores_tabla[0]))
                            fecha = datetime.strptime((self._valores_obtenidos_campo[0]), '%d/%m/%y').date()
                            print('HPOLL', self._valores_obtenidos_campo[3])
                            if self._valores_obtenidos_campo[3] != 'Devuelto':
                                self._valores_obtenidos_campo[2]  = None
                            fecha2 = self._valores_obtenidos_campo[2] 
                            if self._valores_obtenidos_campo[2] != None:
                                fecha2 = datetime.strptime((self._valores_obtenidos_campo[2]), '%d/%m/%y').date()
                            else:
                                fecha2 = None
                            prestamo.modificar_datos(int(self._valores_tabla[0]), fecha,
                                        int(self._valores_obtenidos_campo[1]), fecha2,
                                        (self._valores_obtenidos_campo[3]), socio, libro)
                            self.abrir_ventana_emergente("Modificacion correcta", mensaje="Se modifico el socio correctamente", tipo=2)
                    else:
                        self.abrir_ventana_emergente("Error", mensaje="Este socio tiene demasiados prestamos")

                else:
                    self.abrir_ventana_emergente("Error", mensaje="No Existe ese socio")
                
            else: 
                self.abrir_ventana_emergente("Error", mensaje="No existe el libro")
                

        self._campos_datos_estado = tk.BooleanVar(value=True)
        self.datos_socio.actualizar_contenido(self._campos_default)
        self.modificar_estado_campos()

        self._valores_barra_busqueda = ('Codigo', '')
        self.actualizar_por_busqueda()
    
    def modificar_prestamo(self):
        """
        Modifica los campos para poder modificar el contenido de un socio
        """
        if self._valores_tabla != []:
            self.modificar_estado_campos()
        else:
            self.abrir_ventana_emergente("Error", mensaje="Error no hay ningun campo seleccionado")
    
    def cancelar_operacion(self):
        """
        Cancela la operacion
        """
        self.modificar_estado_campos()
        
    ##### LOGICA DE NEGOCIO PRESTAMOS 
    
    def devolver_prestamo(self):
            """
            Elimina el socio seleccionado, si no hay ninguno lo informa  
            """
            # Obtenemos los campos 
            self.obtener_campos()
            if self._valores_obtenidos_campo == [] or ("" in self._valores_obtenidos_campo):
                # No hay libro que eliminar 
                self.abrir_ventana_emergente(mensaje="Error No hay ningun Socio seleccionado")
            else:
                valor = self.abrir_ventana_emergente(mensaje="¿Esta seguro que quiere devolver este Socio?", tipo=1)
                if valor:
                # Aca me tiene que eliminar el libro 
                    prestamo = self._tabla_base.create_prestamo(int(self._valores_tabla[0]))
                    print(prestamo)
                    prestamo.modificar_estado(3)
                    print(prestamo)
                    self._valores_barra_busqueda = ('Codigo', '')   
                    self.actualizar_por_busqueda()
                    self.abrir_ventana_emergente("Devolucion Registrada", mensaje="Se registro la devolucion correctamente", tipo=2)
                    self._valores_obtenidos_campo = []
                    self._campos_datos_estado = tk.BooleanVar(value=True)
                    self.modificar_estado_campos()

                    #self.modificar_estado_campos()
            # Me tiene que salir una ventana que me digo "Esta seguro que desea eliminar el libro"
        
        
    def ver_prestamo(self):
        #self._notebook.select(0)
        pass


    def actualizar_por_busqueda(self):
        """
        Actualiza la tabla con los valores obtenidos de la barra de busqueda 
        """
        # Aca me tiene que actualizar la tabla (hacer un filter)
        # Y si existe una sola coincidencia me la tiene que mostrar
        campo =  self._valores_barra_busqueda[0]
        valor = self._valores_barra_busqueda[1]
        if (campo == 'socioID' or campo =="dni" or campo == "telefono" or campo == "codigo")and valor!="":
            v = (campo, int(valor))
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
        self.datos_socio = Campos_datos(self.bloque_izquierda, self._campos_default)
        self.datos_socio.pack(expand=True, fill="both")
        
        
        # Creamos la botonera 
        ## - Funcionalidades de los botones - ##

        ## - Valores de la botonera - ##
        botones_nuevo_editar = {"Nuevo Prestamo":{"Fila":0, 
                                               "Columna":0,
                                               "Comando":lambda:self.nuevo_pres()}, 
                                "Modificar Prestamo":{"Fila":0, 
                                                   "Columna":1, 
                                                   "Comando":lambda:self.modificar_prestamo()}}
        ### BOTONES nuevo y editar
        self.botones_nuevo_editar = Botonera(self.bloque_izquierda, botones_nuevo_editar)
        self.botones_nuevo_editar.pack(expand=True, fill="both")

        ### Registrar devolucion### 
        botones_devolver = {"Registrar Devolucion":{"Fila":0, 
                                              "Columna":0,
                                              "Comando":lambda:self.devolver_prestamo()}}
        self.botones_nuevoPrestamo_verPrestamos = Botonera(self.bloque_izquierda, botones_devolver)
        self.botones_nuevoPrestamo_verPrestamos.pack()        
        
        ### BOTONES eliminar
        botones_eliminar = {"Eliminar Prestamo":{"Fila":0, 
                                              "Columna":0,
                                              "Comando":lambda:self.eliminar_socio()}}
        self.botones_nuevoPrestamo_verPrestamos = Botonera(self.bloque_izquierda, botones_eliminar)
        self.botones_nuevoPrestamo_verPrestamos.pack()
        
        
        ## Frame derecho 
        self.bloque_derecha = ttk.Frame(self, padding=10)
        self.bloque_derecha.grid(row=0, column=1, rowspan=2, sticky="snew")
        self.bloque_derecha.grid_columnconfigure(index=1, weight=2)
        
        # Tabla 
        
        campos = ("Codigo", "Titulo", "Id Socio", "Fecha Prestamo", "Dias Prestados", "Fecha Devolcion","Estado")
        campos = ("Codigo Prestamo","Fecha Prestamo","cantidadDias", "FechaDevolucion", "Estado" , "socioID", "Codigo Libro")
        self.tabla = Tabla(self.bloque_derecha, campos, self)
        self.tabla.pack(expand=True, fill="both")
        
        
if __name__ == "__main__":
    ventana = tk.Tk()

    # Definimos la resolucion por defecto
    ventana.geometry("1280x640")

    # Seteamos el tema
    ventana.tk.call("source", "azure.tcl")
    ventana.tk.call("set_theme", "dark")

    # Creamos el Frame principal
    programa = Prestamo_in(ventana)
    programa.pack(expand=True, fill="both")

    ventana.mainloop()