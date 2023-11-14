"""
Objeto libro
"""

from HR_validaciones import validar_entero, validar_flotante, validar_string
from DB_tabla_libros import TablaLibros


class Libro:
    """
    Clase que representa un libro
    """

    def __init__(self, titulo: str, precio: float) -> None:
        """_summary_

        :param titulo: Titulo del libro
        :type titulo: str
        :param precio: Precio del libro
        :type precio: float
        """
        self._codigo = None
        self._titulo = titulo
        self._estado = "Disponible"
        self._precio = precio

    # Getters

    @property
    def codigo(self) -> int:
        """
        :return: Devuelve el codigo del libro
        :rtype: int
        """
        return self._codigo

    @property
    def titulo(self) -> str:
        """
        :return: Devuelve el titulo del libro
        :rtype: str
        """
        return self._titulo

    @property
    def estado(self) -> str:
        """
        :return: Devuelve el estado del libro
        :rtype: str
        """
        return self._estado

    @property
    def precio(self) -> float:
        """
        :return: Devuelve el precio del libro
        :rtype: float
        """
        return self._precio

    # Setters

    @codigo.setter
    def codigo(self, codigo: int):
        """
        Metodo setter para el atributo self._codigo
        :param codigo: valor al que queremos cambiar el atributo codigo
        :type codigo: int
        """
        if validar_entero(codigo):
            self._codigo = int(codigo)

    @titulo.setter
    def titulo(self, titulo: str):
        """
        Metodo setter para el atributo self._titulo

        :param titulo: titulo al que queremos cambiar
        :type titulo: str
        """
        if validar_string(titulo):
            self._titulo = titulo

    @estado.setter
    def estado(self, estado: str):
        """
        ! En este caso no defini el setter de estado,
        porque definí 3 funciones más abajo para cambiar los estados posibles
        ! De esa manera los unicos estados posibles estan controlados
        """
        if validar_string(estado) and estado in ['Prestado', 'Disponible', 'Extraviado']:
            self._estado = estado

    @precio.setter
    def precio(self, precio: float):
        """
        Metodo setter para el atributo self._precio

        :param precio: recibe parametro un str, que valida utilizando el metodo validar_flotante().
        En caso que el mismo retorne True, convierte el str en un float y lo asigna a la variable
        :type precio: float
        """
        if validar_flotante(precio):
            self._precio = float(precio)

    def __str__(self) -> str:
        """Retorna una cadena con la información del objeto libro

        :return: Cadena de caracteres con la información del obejto libro
        :rtype: str
        """
        cadena = f"Codigo: {self._codigo} - "
        cadena += f"Titulo: {self._titulo} - "
        cadena += f"Estado: {self._estado} - "
        cadena += f"Precio: {self._precio}"
        return cadena

    #TODO: Validaciones de los campos de la clase # Pana

    # Metodos específicos para el cambio de estado

    def prestar(self) -> None:
        """
        Permite cambiar el estado del objeto libro a Prestado
        """
        self.estado = "Prestado"

    def devolver(self) -> None:
        """
        Permite cambiar el estado del objeto libro a "Disponible"
        """
        self.estado = "Disponible"

    def extraviar(self) -> None:
        """
        Permite cambiar el estado del objeto libro a "Extraviado"
        """
        self.estado = "Extraviado"

    def guardar_libro(self) -> None:
        """
        Guardar el libro en la tabla Libros de la base de datos
        """
        #! No se si esta bien planteado # Pana
        TablaLibros.save(self)

    # Metodos
    def modificar_estado(self, opcion: int):
        """
        Modifica el estado del libro

        :param opcion: recibe un entero
            1 = El libro cambia su estado a prestado
            2 = El libro cambia su estado a Disponible (es decir se devuelve el libro)
            3 = El libro cambia su estado a extraviado
        :type opcion: int
        """
        if validar_entero(opcion) and 0 < opcion < 4:
            if opcion == 1:
                self.prestar()
            elif opcion == 2:
                self.devolver()
            elif opcion == 3:
                self.extraviar()


if __name__ == "__main__":
    libro = Libro("Harry popoter", 1000)
    print(libro)
    print()
    print(libro.codigo)
    print(libro.titulo)
    print(libro.estado)
