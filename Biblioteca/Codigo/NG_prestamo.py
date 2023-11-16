from datetime import datetime, date, timedelta
from DB_tabla_prestamos import TablaPrestamos
from HR_validaciones import (
    validar_entero,
    validar_string,
    validar_fecha,
)
from NG_libro import Libro
from NG_socio import Socio
from PR_observers import Observer


#! Observer de la Ventana Prestamos
class Prestamo(Observer):
    def __init__(
        self,
        fechaPrestamo: datetime,
        cantidadDias: int,
        socio: int , # Socio id
        libro: int, # libro id
        crear=True,
    ) -> None:
        self._codigo = None
        self._fechaPrestamo = fechaPrestamo
        self._cantidadDias = cantidadDias
        self._fechaDevolucion = None
        self._estado = "En Fecha"
        self._socio = socio
        self._libro = libro
        self.libro.modificar_estado(1)
        if crear:
            self.guardar_prestamo()

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
    def socio(self) -> Socio:
        """
        :return: Devuelve socio del prestamo
        :rtype: Socio
        """
        return self._socio

    # ? Aca podriamos devolver el libro a partir de una busqueda en la base de datos
    # ? teniendo previamente el codigo
    @property
    def libro(self) -> Libro:
        """
        :return: Devuelve el Libro del prestamo
        :rtype: Libro
        """
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
        if validar_string(estado) and estado in [
            "En Fecha",
            "Vencido",
            "Devuelto",
            "Extraviado",
        ]:
            self._estado = estado

    @socio.setter
    def socio(self, socio: Socio):
        if isinstance(socio, Socio):
            self._socio = socio

    @libro.setter
    def libro(self, libro: Libro):
        if isinstance(libro, Libro):
            self._libro = libro

    # --- Metodos --- #

    def __str__(self) -> str:
        cadena = f"\n> --- Infomracion del Prestamo: codigo {self._codigo}\n"
        cadena += f"> --- Libro Prestado{self._libro}"
        cadena += "> --- Datos sobre prestamo\n"
        cadena += f"Fecha del prestamo:  {self._fechaPrestamo}\n"
        cadena += f"Cantidad de días:    {self._cantidadDias}\n"
        cadena += f"Fecha de devolucion: {self._fechaDevolucion}\n"
        cadena += f"Estado: {self._estado}\n"
        cadena += f"socioID: {self._socio.socioID}\n"
        return cadena

    def guardar_prestamo(self):
        """
        Guardar prestamo en la base de datos
        """
        TablaPrestamos.save(self)

    def fecha_prestamo_string(self):
        """
        Obtenemos la fecha de prestamo en formato "Año - Mes - Día"
        """
        fecha = self._fechaPrestamo
        cadena = fecha.strftime("%Y-%m-%d")
        return cadena

    def modificar_estado(self, estado: int):
        """Modifica el estado del Prestamo

        :param estado: Valor numérico que representa el estado del prestamo
            1 = Prestamo en Fecha
            2 = Prestamo vencido (se paso de la cantidad de días establecidos para el prestamo pero es menor a 30)
            3 = El prestamo fue devuelto
            4 = El prestamo no fue devuelto más de 30 días
        :type estado: int
        """
        if validar_entero(estado) and 0 < estado < 5:
            if estado == 1:
                self.estado = "En Fecha"
                self._libro.modificar_estado(1)
            elif estado == 2:
                self.estado = "Vencido"
                self._libro.modificar_estado(1)
            elif estado == 3:
                self.estado = "Devuelto"
                self._libro.modificar_estado(2)
                self._fechaDevolucion = date.today()
            elif estado == 4:
                self.estado = "Extraviado"
                self._libro.modificar_estado(3)
            self.update_prestamo()
    # --- Métodos de observer ---- #

    def update(self):  # Metodo para update de observers
        """
        Verifica si el prestamo se vencio , permite cambiar de estado al prestamo en caso que si

        :param estado: _description_
        :type estado: _type_
        """
        fecha_prestamo = datetime.strptime(self._fechaPrestamo, "%Y-%m-%d")
        delta = timedelta(days=float(self._cantidadDias))
        fecha_estimada = fecha_prestamo + delta
        if datetime.today() > fecha_estimada:
            if (date.today() - fecha_estimada).day > 30:
                self.modificar_estado(4)
            else:
                self.modificar_estado(2)

    def update_prestamo(self) -> None:
        """
        Actualiza el valor del libro en la base de datos
        """
        
        TablaPrestamos.update_prestamo(self.fechaPrestamo,
        self.cantidadDias,
        self.fechaDevolucion,
        self.estado,
        self.socio.socioID,
        self.libro.codigo,
        self.codigo)

        if self.estado == "En Fecha":
            self._libro.modificar_estado(1)
        elif self.estado == "Vencido":
            self._libro.modificar_estado(1)
        elif self.estado == "Devuelto":
            self._libro.modificar_estado(2)
            self._fechaDevolucion = date.today()
        elif self.estado == "Extraviado":
            self._libro.modificar_estado(3)

    def eliminar_prestamo(self):
        TablaPrestamos.delete_prestamo(self._codigo)

    def modificar_datos(self, codigo, fechaPrestamo,
        cantidadDias,
        fechaDevolucion,
        estado,
        socio,
        libro):
        
        self.codigo = codigo
        self.fechaPrestamo = fechaPrestamo
        self.cantidadDias = cantidadDias
        self.fechaDevolucion = fechaDevolucion
        self.estado = estado
        self.socio = socio
        self.libro = libro
         
        self.update_prestamo()
        