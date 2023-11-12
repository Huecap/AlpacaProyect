from HR_validaciones import validar_entero, validar_flotante, validar_string
class Libro:

    estados = ("Disponible", "Prestado", "Extraviado")

    def __init__(self, titulo: str, precio: int) -> None:
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

    @codigo.setter
    def codigo(self, codigo):
        if validar_entero(codigo):
            self._codigo = int(codigo)
            resultado = "El codigo de libro se ha registrado correctamente: {codigo}"
        else: 
            resultado = "No se ha podido registrar el codigo del libro"
        return resultado

    @titulo.setter
    def titulo(self, titulo):
        if validar_string(titulo):
            self._titulo = titulo
            resultado = "El titulo del libro se ha registrado correctamente: {titulo}"
        else:
            resultado = "No se ha podido registrar el nuevo titulo del libro"
        return resultado

    @estado.setter
    def estado(self, estado):
        if validar_entero(estado):
            self._estado = int(estado)
            resultado = f'El estado del libro se ha registrado correctamente: {estado}'
        else:
            resultado = 'No se ha podido registrar el estado del libro'
        return resultado             

    @precio.setter
    def precio(self, precio):
        if validar_flotante(precio):
            self._precio = float(precio)
            resultado = f"El Precio del libro se ha registrado correctamente: {precio}"
        else:
            resultado = "No se ha podido registrar el precio del libro"
        return resultado 

    def __str__(self) -> str:
        cadena = f"Codigo: {self._codigo}\n"
        cadena += f"Titulo: {self._titulo}\n"
        cadena += f"Estado: {self._estado}\n"
        cadena += f"Precio: {self._precio}"
        return cadena
    # Validaciones de los campos de la clase # Pana

if __name__ == '__main__':
    
    libro = Libro('Harry popoter', 1000)
    print(libro)
    libro.codigo = 12
    libro.titulo = 12
    libro.estado = 12
    print(libro.codigo)