from datetime import datetime, date
from NG_libro import Libro
from PR_observers import Observer
from HR_validaciones import (
    validar_entero,
    validar_string,
    validar_fecha,
)
from DB_tabla_prestamos import TablaPrestamos

class Prestamo(Observer):
    def __init__(
        self,
        fechaPrestamo: datetime,
        cantidadDias: int,
        socioID: int,
        libro: Libro
        # ? Huenu : Esto lo tenemos que poner como objeto ya que tiene que interactuar con el objeto, si ponemos el Id solo no tiene como conocerlo
        # ? Mi idea aca es: definir despues el metodo guardar prestamo en base de datos que te guarde el prestamo con el id del libro (en vez del objeto)
        # ? Definir un metodo que sea cargar prestamo que busque en la base de datos el id del libro, lo instancie, e instancie el objeto prestamo referenciando a ese objeto libro
    ) -> None:
        self._codigo = None
        self._fechaPrestamo = fechaPrestamo
        self._cantidadDias = cantidadDias
        self._fechaDevolucion = None
        self._estado = "En Fecha"
        self._socioID = socioID
        self._libro = libro
        self.libro.modificar_estado(1)

    @property
    def codigo(self) -> int:
        """
        :return: Devuelve el codigo del prestamo
        :rtype: int
        """
        return self._codigo

    @property
    def fechaPrestamo(self) -> datetime:
        """
        :return: Devuelve la fecha del prestamo
        :rtype: datetime
        """
        return self._fechaPrestamo

    @property
    def cantidadDias(self) -> int:
        """
        :return: Devuelve la cantidad de dias del prestamo
        :rtype: int
        """
        return self._cantidadDias

    @property
    def fechaDevolucion(self) -> datetime:
        """
        :return: Devuelve la fecha de devolucion del prestamo
        :rtype: datetime
        """
        return self._fechaDevolucion

    @property
    def estado(self) -> str:
        """
        :return: Devuelve el estado del prestamo
        :rtype: str
        """
        return self._estado

    @property
    def socioID(self) -> int:
        """
        :return: Devuelve socioID del prestamo
        :rtype: int
        """
        return self._socioID

    #? Aca podriamos devolver el libro a partir de una busqueda en la base de datos
    #? teniendo previamente el codigo
    @property
    def libro(self) -> Libro:
        """
        :return: Devuelve el Libro del prestamo
        :rtype: Libro
        """
        #* Pana
        #* Si esta variable contiene solo el codigo del Libro:
        #* previamente... from DB_tabla_libros import TablaLibros

        #* libro_tuple = TablaLibros.show_libro(libroCodigo)
        #* if libro_tuple:
        #*      libro = Libro(libro_tuple[0][1], libro_tuple[0][3])
        #*      libro.codigo = libro_tuple[0][0]
        #*      libro.estado = libro_tuple[0][2]
        #*      return libro
        return self._libro

    @codigo.setter
    def codigo(self, valor: int):
        if validar_entero(valor):
            self._codigo = int(valor)


    @fechaPrestamo.setter
    def fechaPrestamo(self, fecha: date):
        if validar_fecha(fecha):
            self._fechaPrestamo = fecha

    @cantidadDias.setter
    def cantidadDias(self, cantidad: int):
        if validar_entero(cantidad):
            self._cantidadDias = int(cantidad)

    @fechaDevolucion.setter
    def fechaDevolucion(self, fecha: date):
        if validar_fecha(fecha):
            self._fechaDevolucion = fecha

    @estado.setter
    def estado(self, estado: str):
        if validar_string(estado) and estado in ['En Fecha', 'Vencido', 'Devuelto', 'Extraviado']:
            self._estado = estado

    @socioID.setter
    def socioID(self, identificador: int):
        if validar_entero(identificador):
            self._socioID = int(identificador)

    @libro.setter
    def libro(self, libro: Libro):
        if isinstance(libro, Libro):
            #* Pana
            #* self._libro = libro.codigo
            self._libro = libro

    # --- Metodos --- #
    def fecha_prestamo_string(self):
        """
        Obtenemos la fecha de prestamo en formato "Año - Mes - Día"
        """
        fecha = self._fechaPrestamo
        cadena = fecha.strftime(
            "%Y-%m-%d"
        )
        return cadena

    def prestamo_en_fecha(self):
        """
        Modificar el estado del prestamo a 'En Fecha'
        """
        self.estado = "En Fecha"
        self._libro.modificar_estado(1)

    def prestamo_vencido(self):
        """
        Modificar el estado del prestamo a 'Vencido'
        """
        self.estado = "Vencido"
        self._libro.modificar_estado(1)

    def prestamo_devuelto(self):
        """
        Modificar el estado del prestamo a 'Devuelto'
        """
        self.estado = "Devuelto"
        self._libro.modificar_estado(2)
        self._fechaDevolucion = date.today()

    def prestamo_extraviado(self):
        """
        Modificar el estado del prestamo a 'Extraviado'
        """
        self.estado = "Extraviado"
        self._libro.modificar_estado(3)

    def modificar_estado(self, estado: int):
        """Modifica el estado del Prestamo

        :param estado: Valor numérico que representa el estado del prestamo
            1 = Prestamo en Fecha
            2 = Prestamo vencido (es decir se paso de la cantidad de días establecidas para el prestamo pero es menor a 30)
            3 = El prestamo fue devuelto
            4 = El prestamo no fue devuelto más de 30 días
        :type estado: int
        """
        if validar_entero(estado) and 0 < estado < 5:
            if estado == 1:
                self.prestamo_en_fecha()
            elif estado == 2:
                self.prestamo_vencido()
            elif estado == 3:
                self.prestamo_devuelto()
            elif estado == 4:
                self.prestamo_extraviado()

    def guardar_prestamo(self):
        """
        Guardar prestamo en la base de datos
        """
        #! No se si esta bien planteado # Pana
        TablaPrestamos.save(self)

    # --- Métodos de observer ---- #

    def update(self):  # Metodo para update de observers
        """
        Verifica si el prestamo se vencio , permite cambiar de estado al prestamo en caso que si

        :param estado: _description_
        :type estado: _type_
        """
        fecha_estimada = self._fechaPrestamo + self._cantidadDias
        if date.today() > fecha_estimada:
            if (date.today() - fecha_estimada).day > 30:
                self.modificar_estado(4)
            else:
                self.modificar_estado(2)

    def __str__(self) -> str:
        cadena = "----Infomracion de Prestamo----\n"
        cadena += f"-Libro Prestado-\n{self._libro} \n"
        cadena += "-Datos sobre prestamo-\n"
        cadena += f"Fecha prestamo: {self._fechaPrestamo}\n"
        cadena += f"Cantidad días: {self._cantidadDias}\n"
        cadena += f"Fecha Devolucion: {self._fechaDevolucion}\n"
        cadena += f"Estado: {self._estado}\n"
        cadena += f"socioID: {self._socioID}\n"
        return cadena
