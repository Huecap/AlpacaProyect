from datetime import datetime, date
from NG_libro import Libro
from PR_observers import Observer
from HR_validaciones import validar_entero, validar_flotante, validar_string, validar_fecha


class Prestamo( Observer):

    def __init__(
        self,
        libro: Libro, # libroCodigo: int # Pana 
        # ? Huenu : Esto lo tenemos que poner como objeto ya que tiene que interactuar con el objeto, si ponemos el Id solo no tiene como conocerlo 
        # ? Mi idea aca es: definir despues el metodo guardar prestamo en base de atos que te guarde el prestamo con el id del libro (en vez del objeto)
        # ? Definir un metodo que sea cargar prestamo que busque en la base de datos el id del libro, lo instancie, e instancie el objeto prestamo referenciando a ese objeto libro 
        fechaPrestamo: datetime,
        cantidadDias: int,
        socioID: int,
    ) -> None:
        self._libro = libro
        self._fechaPrestamo = fechaPrestamo
        self._cantidadDias = cantidadDias
        self._fechaDevolucion = None
        self._estado = "En Fecha"
        self._socioID = socioID
        self.libro.update(1)

    @property
    def libro(self) -> Libro:
        return self._libro

    @property
    def fechaPrestamo(self) -> datetime:
        return self._fechaPrestamo

    @property
    def cantidadDias(self) -> int:
        return self._cantidadDias

    @property
    def fechaDevolucion(self) -> datetime:
        return self._fechaDevolucion

    @property
    def estado(self) -> str:
        return self._estado

    @property
    def socioId(self) -> int:
        return self._socioID

    @libro.setter
    def libro(self, libro : Libro):
        if type(libro) == Libro:
            self._libro = libro

    @fechaPrestamo.setter
    def fechaPrestamo(self, fecha : date):
        if validar_fecha(fecha):
            self._fechaPrestamo = fecha

    @cantidadDias.setter
    def cantidadDias(self, cantidad : int):
        if validar_entero(cantidad):
            self._cantidadDias = int(cantidad)

    @fechaDevolucion.setter
    def fechaDevolucion(self, fecha : date):
        if validar_fecha(fecha):
            self._fechaDevolucion = fecha

    @estado.setter
    def estado(self, estado : str):
        if validar_string(estado):
            self._estado = estado

    @socioId.setter
    def socioId(self, id : int):
        if validar_entero(id):
            self._socioID = int(id)

    # --- Metodos --- #
    def fecha_prestamo_string(self):
        fecha = self._fechaPrestamo
        cadena = fecha.strftime("%Y-%m-%d") # Obtenemos la fecha en formato "Año - Mes - Día"
        return cadena
    
    def prestamo_en_fecha(self):
        self._estado = "En Fecha"
        self._libro.update(1)
    
    def prestamo_vencido(self):
        self._estado = "Vencido"
        self._libro.update(1)
        
    def prestamo_devuelto(self):
        self._estado = "Devuelto"  
        self._libro.update(2)      
        self._fechaDevolucion = date.today()
        
    def prestamo_extraviado(self):
        self._estado = "Extraviado"
        self._libro.update(3)
    
    
    def modificar_estado(self, estado : int):
        """Modifica el estado del Prestamo

        :param estado: Valor numérico que representa el estado del prestamo 
            1 = Prestamo en Fecha
            2 = Prestamo vencido (es decir se paso de la cantidad de días establecidas para el prestamo pero es menor a 30)
            3 = El prestamo fue devuelto 
            4 = El prestamo no fue devuelto más de 30 días 
        :type estado: int
        """
        if estado == 1:
            self.prestamo_en_fecha()
        elif estado == 2:
            self.prestamo_vencido()
        elif estado == 3:
            self.prestamo_devuelto()
        elif estado == 4:
            self.prestamo_extraviado()
    
    
    def guardar_prestamo():
        pass
    
    # --- Métodos de observer ---- #
    
    def update(self, estado):  # Metodo para update de observers
        self.modificar_estado(estado)

    def __str__(self) -> str:
        cadena = "----Infomracion de Prestamo----\n"
        cadena += f"-Libro Prestado-\n{self._libro} \n"
        cadena += "-Datos sobre prestamo-\n"
        cadena += f"Fecha prestamo:{self._fechaPrestamo}\n"
        cadena += f"Cantidad días:{self._cantidadDias.days}\n"
        cadena += f"Fecha Devolucion:{self._fechaDevolucion}\n"
        cadena += f"Estado:{self._estado}\n"
        cadena += f"SocioID:{self._socioID}\n"
        return cadena
