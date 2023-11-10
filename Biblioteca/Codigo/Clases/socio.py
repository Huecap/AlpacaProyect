from datetime import date, timedelta
from prestamo import Prestamo
from ..Patrones.observers import Sujeto


class Socio:
    def __init__(
        self,
        nombre: str,
        apellido: str,
        dni: int,
        telefono: int,
        mail: str,
        direccion: str,
    ) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._telefono = telefono
        self._mail = mail
        self._direccion = direccion
        self._prestamos = []
        self._socioId = None # socioID # Pana

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def apellido(self) -> str:
        return self._apellido

    @property
    def dni(self) -> int:
        return self._dni

    @property
    def telefono(self) -> int:
        return self._telefono

    @property
    def mail(self) -> str:
        return self._mail

    @property
    def direccion(self) -> str:
        return self._direccion

    @property
    def socioId(self) -> int:
        return self._socioId

    @nombre.setter
    def nombre(self):
        pass

    @apellido.setter
    def apellido(self):
        pass

    @dni.setter
    def dni(self):
        pass

    @telefono.setter
    def telefono(self):
        pass

    @mail.setter
    def mail(self):
        pass

    @direccion.setter
    def direccion(self):
        pass

    @socioId.setter
    def socioId(self, new_id):
        # self._socioId = new_id # Pana
        pass

    # --- Metodos --- #
    def nuevo_prestamo(self, libro, cantidadDias):
        if len(self._prestamos) <= 2:
            fechaPrestamo = date.today  # nos toma la fecha actual
            delta = timedelta(
                days=cantidadDias
            )  # Definimos el intervalo de tiempo para poder operar con este
            estado = "Prestado"
            # Creamos el objeto Prestamo
            prestamo = Prestamo(
                libro, fechaPrestamo, delta, estado, socioID=self._socioId
            )
            # Agremos el prestamo el Socio
            self._prestamos.append(prestamo)

            return "El prestamo se registro con éxito"
        else:
            return "El socio no puede solicitar más prestamos"

    def registrar_devolucion(self):
        pass

    def __str__(self) -> str:
        pass
