from HR_validaciones import validar_entero, validar_flotante, validar_string
from PR_observers import Observer


class Libro(Observer):

    estados = ("Disponible", "Prestado", "Extraviado")

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
        return self._codigo

    @property
    def titulo(self) -> str:
        return self._titulo

    @property
    def estado(self) -> str:
        return self._estado

    @property
    def precio(self) -> float:
        return self._precio

    # Setters 
    
    @codigo.setter
    def codigo(self, codigo : int):
        """
        Metodo setter para el atributo self._codigo
        :param codigo: valor al que queremos cambiar el atributo codigo 
        :type codigo: int
        """
        if validar_entero(codigo):
            self._codigo = int(codigo)

    @titulo.setter
    def titulo(self, titulo : str):
        """
        Metodo setter para el atributo self._titulo 

        :param titulo: titulo al que queremos cambiar 
        :type titulo: str
        """
        if validar_string(titulo):
            self._titulo = titulo

    @estado.setter
    def estado(self, estado : str):
        """
        ! En este caso no defini el setter de estado, porque definí 3 funciones más abajo para cambiar los estados posibles
        ! De esa manera los unicos estados posibles estan controlados 
        """
        pass

  
    @precio.setter
    def precio(self, precio : float):
        
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
        cadena = f"Codigo: {self._codigo}\n"
        cadena += f"Titulo: {self._titulo}\n"
        cadena += f"Estado: {self._estado}\n"
        cadena += f"Precio: {self._precio}"
        return cadena
    
    
    # Validaciones de los campos de la clase # Pana

    # Metodos específicos para el cambio de estado 
    
    def prestar(self) -> None:
        """ 
        Permite cambiar el estado del objeto libro a Prestado 
        """
        self._estado = "Prestado"
    
    def devolver(self):
        """
        Permite cambiar el estado del objeto libro a "Disponible"
        """
        self._estado = "Disponible"
    
    def extraviar(self):
        """
        Permite cambiar el estado del objeto libro a "Extraviado"
        """
        self._estado = "Extraviado"
        
        
    def guardar_libro():
        pass
    
    
    # Metodos update 
    def update(self, opcion: int):
        """
        Método update de observer. 
        Mediante la recepcion del mensaje del Subject Prestamo, dependiendo del parametro que reciba cambia el estado del libro

        :param opcion: recibe un entero 
            1 = El libro cambia su estado a prestado 
            2 = El libro cambia su estado a Disponible (es decir se devuelve el libro)
            3 = El libro cambia su estado a extraviado
        :type opcion: int
        """
        if opcion == 1:
            self.prestar()
        elif opcion == 2:
            self.devolver()
        elif opcion == 3:
            self.extraviar()



if __name__ == '__main__':
    
    libro = Libro('Harry popoter', 1000)
    print(libro)
    print()
    print(libro.codigo)
    print(libro.titulo)
    print(libro.estado)

    print(validar_entero("1"))