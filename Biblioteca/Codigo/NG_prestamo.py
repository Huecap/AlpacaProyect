from datetime import datetime
from Programs.DAO.TP.Codigo.Clases.NG_libro import Libro
from ..Patrones.PR_observers import Observer


class Prestamo(Observer):
    def __init__(
        self,
        libro: Libro, # libroCodigo: int # Pana
        fechaPrestamo: datetime,
        cantidadDias: int,
        estado: str,
        socioID: int,
    ) -> None:
        super().__init__()
        self._libro = libro
        self._fechaPrestamo = fechaPrestamo
        self._cantidadDias = cantidadDias
        self._fechaDevolucion = None
        self._estado = estado
        self._socioID = socioID

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
    def libro(self):
        pass

    @fechaPrestamo.setter
    def fechaPrestamo(self):
        pass

    @cantidadDias.setter
    def cantidadDias(self):
        pass

    @fechaDevolucion.setter
    def fechaDevolucion(self):
        pass

    @estado.setter
    def estado(self):
        pass

    @socioId.setter
    def socioId(self):
        pass

    # --- Metodos --- #
    def update(self):  # Metodo para update de observers
        pass

    def __str__(self) -> str:
        pass
