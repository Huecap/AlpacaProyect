"""
Objeto socio
"""

from datetime import date
from DB_tabla_socios import TablaSocios
from HR_validaciones import validar_entero, validar_string


class Socio:
    """
    Clase que representa un socio
    """

    def __init__(
        self,
        nombre: str,
        apellido: str,
        dni: int,
        telefono: int,
        mail: str,
        direccion: str,
        crear=True,
    ) -> None:
        super().__init__()  # Heredemos de la clase Subject del modulo observer
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._telefono = telefono
        self._mail = mail
        self._direccion = direccion
        self._prestamos = []
        self._socioID = None
        if crear:
            self.guardar_socio()

    @property
    def nombre(self) -> str:
        """
        :return: Devuelve el nombre del socio
        :rtype: str
        """
        return self._nombre

    @property
    def apellido(self) -> str:
        """
        :return: Devuelve el apellido del socio
        :rtype: str
        """
        return self._apellido

    @property
    def dni(self) -> int:
        """
        :return: Devuelve el dni del socio
        :rtype: int
        """
        return self._dni

    @property
    def telefono(self) -> int:
        """
        :return: Devuelve el telefono del socio
        :rtype: int
        """
        return self._telefono

    @property
    def mail(self) -> str:
        """
        :return: Devuelve el mail del socio
        :rtype: str
        """
        return self._mail

    @property
    def direccion(self) -> str:
        """
        :return: Devuelve el direccion del socio
        :rtype: str
        """
        return self._direccion

    @property
    def prestamos(self) -> list:
        """
        :return: Devuelve los prestamos del socio
        :rtype: list
        """
        return self._prestamos

    @property
    def socioID(self) -> int:
        """
        :return: Devuelve el ID del socio
        :rtype: int
        """
        return self._socioID

    @nombre.setter
    def nombre(self, nombre: str):
        """
        Metodo setter para el atributo self._nombre

        :param nombre: Nombre que queremos establecer
        :type nombre: str
        """
        if validar_string(nombre):
            self._nombre = nombre

    @apellido.setter
    def apellido(self, apellido: str):
        """
        Metodo setter para el atributo self._apellido

        :param apellido: Nombre que queremos establecer
        :type apellido: str
        """
        if validar_string(apellido):
            self._apellido = apellido

    @dni.setter
    def dni(self, dni: int):
        """
        Metodo setter para el atributo self._dni

        :param dni: Numero de dni que queremos establecer
        :type dni: int
        """
        if validar_entero(dni):
            self._dni = int(dni)

    @telefono.setter
    def telefono(self, telefono: int):
        """
        Metodo setter para el atributo self._telefono

        :param telefono: telefono que queremos establecer
        :type telefono: int
        """
        if validar_entero(telefono):
            self._telefono = int(telefono)

    @mail.setter
    def mail(self, mail: str):
        """
        Metodo setter para el atributo self._mail

        :param mail: mail que queremos establecer
        :type mail: str
        """
        if validar_string(mail):
            self._mail = mail

    @direccion.setter
    def direccion(self, direccion: str):
        """
        Metodo setter para el atributo self._direccion

        :param direccion: direccion que queremos establecer
        :type direccion: str
        """
        if validar_string(direccion):
            self._direccion = direccion

    @socioID.setter
    def socioID(self, identificador: int):
        """
        Metodo setter para el atributo self._socioID

        :param identificador: Id de socio que queremos establecer
        :type identificador: int
        """
        if validar_entero(identificador):
            self._socioID = identificador  # Pana

    # --- Metodos --- #

    def __str__(self) -> str:
        cadena = f"\nNombre:    {self._nombre} \n"
        cadena += f"Apellido:  {self._apellido}\n"
        cadena += f"Dni:       {self._dni}\n"
        cadena += f"Telefono:  {self._telefono}\n"
        cadena += f"Mail:      {self._mail}\n"
        cadena += f"Dirección: {self._direccion}\n"
        cadena += f"Id:        {self._socioID}\n"
        for prestamo in self._prestamos:
            cadena += f"{prestamo}"
        return cadena

    def guardar_socio(self):
        """
        Guardar el socio en la tabla Socios de la base de datos
        """
        TablaSocios.save(self)


    def update_socio(self) -> None:
        """
        Actualiza el valor del libro en la base de datos
        """
        TablaSocios.update_socio(self.nombre, self.apellido, self.dni, self.telefono, self.mail, self.direccion, self.socioID)


    def eliminar_socio(self):
        TablaSocios.delete_socio(self._socioID)

    def modificar_datos(self,nombre, apellido, dni, telefono, mail, direccion):
        self.nombre = nombre  
        self.apellido = apellido 
        self.dni = dni 
        self.telefono = telefono 
        self.mail = mail 
        self.direccion = direccion 
        self.update_socio()

    def nuevo_prestamo(self, libro, cantidadDias):
        """
        Crear un nuevo prestamo del socio
        :param libro: Libro pedido por el socio
        :type libro: Libro
        :param cantidadDias: Cantidad de dias del prestamo
        :type cantidadDias: int
        :return: Devuelve una cadena de texto que informa si el prestamo fue creado con exito o no
        :rtype: str
        """
        #! Para evitar la importacion ciclica
        from NG_prestamo import Prestamo

        if len(self._prestamos) < 3:
            # Toma la fecha actual
            fechaPrestamo = date.today()
            # Definimos el intervalo de tiempo para poder operar con este
            #! delta = timedelta(days=cantidadDias)
            # Creamos el objeto Prestamo
            prestamo = Prestamo(fechaPrestamo, cantidadDias, self, libro)
            # Agremos el prestamo al Socio
            self._prestamos.append(prestamo)

            return "El prestamo se registro con éxito"
        else:
            return "El socio no puede solicitar más prestamos"

    def registrar_devolucion(self, prestamo):
        """
        Registra que el prestamo fue cumplido en tiempo y forma
        :param prestamo: Prestamo al cual actualizar el estado
        :type prestamo: Prestamo
        """
        prestamo.modificar_estado(3)
        self._prestamos.remove(prestamo)
        return "La devolucion se registro con Exito"
