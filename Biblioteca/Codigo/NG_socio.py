import time
from datetime import date, timedelta
from NG_prestamo import Prestamo
from NG_libro import Libro
from PR_observers import Sujeto
from HR_validaciones import validar_entero, validar_flotante, validar_string


class Socio(Sujeto):
    def __init__(
        self,
        nombre: str,
        apellido: str,
        dni: int,
        telefono: int,
        mail: str,
        direccion: str,
    ) -> None:
        super().__init__() # Heredemos de la clase Subject del modulo observer 
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
    def prestamos(self) -> list:
        return self._prestamos

    @property
    def socioId(self) -> int:
        return self._socioId

    @nombre.setter
    def nombre(self, nombre : str):
        """
        Metodo setter para el atributo self._nombre

        :param nombre: Nombre que queremos establecer
        :type nombre: str
        """
        if validar_string(nombre):
            self._nombre = nombre

    @apellido.setter
    def apellido(self, apellido : str):
        """
        Metodo setter para el atributo self._apellido

        :param apellido: Nombre que queremos establecer
        :type apellido: str
        """
        if validar_string(apellido):
            self._apellido = apellido

    @dni.setter
    def dni(self, dni : int):
        """
        Metodo setter para el atributo self._dni

        :param dni: Numero de dni que queremos establecer
        :type dni: int
        """
        if validar_entero(dni):
            self._dni = int(dni)


    @telefono.setter
    def telefono(self, telefono:int):
        """
        Metodo setter para el atributo self._telefono

        :param telefono: telefono que queremos establecer
        :type telefono: int
        """
        if validar_entero(telefono):
            self._telefono = int(telefono)

    @mail.setter
    def mail(self, mail : str):
        """
        Metodo setter para el atributo self._mail

        :param mail: mail que queremos establecer
        :type mail: str
        """
        if validar_string(mail):
            self._mail = mail

    @direccion.setter
    def direccion(self, direccion : str):
        """
        Metodo setter para el atributo self._direccion

        :param direccion: direccion que queremos establecer
        :type direccion: str
        """
        if validar_string(direccion):
            self._direccion = direccion

    @socioId.setter
    def socioId(self, id : int):
        """
        Metodo setter para el atributo self._

        :param id: Id de socio que queremos establecer 
        :type id: int
        """
        if validar_entero(id):
            self._socioId = id # Pana

    # --- Metodos --- #
    
    def nuevo_prestamo(self, libro, cantidadDias):
        if len(self._prestamos) <= 2:
            fechaPrestamo = date.today()  # nos toma la fecha actual
            delta = timedelta(days=cantidadDias)  # Definimos el intervalo de tiempo para poder operar con este
            # Creamos el objeto Prestamo
            prestamo = Prestamo(libro, fechaPrestamo, delta, socioID=self._socioId)
            # Agremos el prestamo el Socio
            self._prestamos.append(prestamo)

            return "El prestamo se registro con éxito"
        else:
            return "El socio no puede solicitar más prestamos"
        

    def registrar_devolucion(self, prestamo):
        prestamo.update(3)
        self._prestamos.remove(prestamo)
        return "La devolucion se registro con Exito"


    def guardar_socio(self):
        pass 
    
    
    
    def __str__(self) -> str:
        cadena = f"Nombre: {self._nombre} \n"
        cadena += f"Apellido: {self._apellido}\n"
        cadena += f"Dni {self._dni}\n"
        cadena += f"Telefono {self._telefono}\n"
        cadena += f"Mail: {self._mail}\n"
        cadena += f"Dirección: {self._direccion}\n"
        cadena += f"Id: {self._socioId}\n"
        for prestamo in self._prestamos: cadena += f"{prestamo}"
        return cadena

    ## ! --- Métodos de prueba despues BORRAR --- ##  


if __name__ == '__main__':
    
    socio1 = Socio('Juan', 'Carlos', 43061739, 99999, 'Juancho01@gmail.com', 'Av.Marcelo T de alvear 1123')
    libro = Libro('Harry popoter', 1000)
    libro.codigo = 1111
    
    socio1.socioId = 1
    print()
    print(socio1.nuevo_prestamo(libro, 10))
    print(socio1)
    # socio1.mostrar_prestamos()
    print(socio1.registrar_devolucion(socio1.prestamos[0]))
    print(socio1)
    