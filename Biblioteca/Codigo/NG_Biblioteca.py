from datetime import date, timedelta
from PR_observers import Sujeto
from NG_libro import Libro
from NG_socio import Socio
from NG_prestamo import Prestamo
from DB_tabla_libros import TablaLibros


class Biblioteca(Sujeto):
    def __init__(self):
        super().__init__()
        self._libros = dict()
        self._socios = dict()
        self._prestamos = dict()

    @property
    def libros(self):
        return self._libros

    @property
    def socios(self):
        return self._socios

    @property
    def prestamos(self):
        return self._prestamos

    def notify(self):
        for observer in self._observers:
            observer.update()

    def crear_libro(self, titulo, precio):
        libro = Libro(titulo, precio)
        TablaLibros.save(libro)
        self._libros[libro.codigo] = libro

    def modificar_libro(self):
        pass

    def mostrar_libro(self, idLibro):
        if idLibro in self._libros:
            aux = self._libros[idLibro]
        else:
            aux = "No existe ese id"
        return aux

    def mostrar_libros(self):
        cadena = ""
        for libro in self._libros.values():
            cadena += str(libro) + "\n"
        return cadena

    def crear_socio(
        self,
        nombre: str,
        apellido: str,
        dni: int,
        telefono: int,
        mail: str,
        direccion: str,
    ):
        socio = Socio(nombre, apellido, dni, telefono, mail, direccion)
        socio.socioId = len(self._socios) + 1
        self._socios[socio.socioId] = socio

    def mostrar_socio(self, idSocio):
        return self._socios[idSocio]

    def crear_prestamo(self, libro, fechaPrestamo, cantidadDias, socioId):
        prestamo = Prestamo(libro, fechaPrestamo, cantidadDias, socioId)
        self._prestamos[libro.codigo] = prestamo

    def mostrar_prestamo(self, idLibro):
        return self._prestamos[idLibro]


def menu():
    biblioteca = Biblioteca()
    op = 5
    while op != 0:
        print("--- Menu ---")
        print("1)Libros")
        print("2)Socios")
        print("3) Prestamos")
        op = "1"
        match op:
            case "1":
                print("--- Menu Libros ---")
                print("1) Registrar Libro")
                print("2) Modificar datos libro")
                print("3) Datos libro")
                print("4) Mostrar Libros")
                print("5) Buscar libro")
                print("3) Eliminar Libro")
                biblioteca.crear_libro("Harry potter 1", 1000)
                biblioteca.crear_libro("Harry potter 2", 1000)
                biblioteca.crear_libro("Harry potter 3", 1000)
                print()
                print(biblioteca.mostrar_libro(0))
                print()
                print(biblioteca.mostrar_libros())
                break

            case "2":
                biblioteca.crear_socio(
                    "Juan",
                    "Carlos",
                    421222,
                    3511233212,
                    "Juanchi_112@gmail.com",
                    "Av. Carlos altamirano 1123",
                )
                print()
                print(biblioteca.mostrar_socio(1))

            case "3":
                biblioteca.crear_libro("Harry potter", 1000)
                print(biblioteca.mostrar_libro(1))
                biblioteca.crear_socio(
                    "Juan",
                    "Carlos",
                    421222,
                    3511233212,
                    "Juanchi_112@gmail.com",
                    "Av. Carlos altamirano 1123",
                )
                print(biblioteca.mostrar_socio(1))
                biblioteca.crear_prestamo(
                    biblioteca.libros[1],
                    date.today(),
                    timedelta(days=10),
                    biblioteca.socios[1],
                )
                print(biblioteca.prestamos[1])
            case _:
                break


if __name__ == "__main__":
    menu()
    pass
