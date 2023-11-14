# from sqlite3 import Error
# import HR_formatos as formats
from datetime import datetime
from DB_tabla_libros import TablaLibros
from DB_tabla_socios import TablaSocios
from DB_tabla_prestamos import TablaPrestamos
from NG_libro import Libro
from NG_socio import Socio
from NG_prestamo import Prestamo

# print(TablaLibros())
# print(TablaSocios())
# print(TablaPrestamos())

# libro = Libro('Hola Python', 2000)
# print(libro)
# socio = Socio('Matias', 'Pana', 11223344, 3511234567, 'elpana@gmail.com', 'Juarez 126 CBA')
# print(socio)
# prestamo = Prestamo(datetime.today(), 5, socio, libro)
# print(prestamo)

# print(TablaPrestamos.show_table('estado'))
# print(TablaPrestamos.show_prestamo('2023-11-14', 'fechaPrestamo'))

# result = TablaPrestamos.update_prestamo(datetime.today(), 10, None, 'En Fecha', 1, 1, 2)
# print(result)
# result = TablaPrestamos.update_prestamo(datetime.today(), 10, None, 'En Fecha', 1, 1, 1)
# print(result)
# print(TablaPrestamos.show_table())

# result = TablaPrestamos.delete_prestamo(2)
# print(result)
# result = TablaPrestamos.delete_prestamo(1)
# print(result)
# print(TablaPrestamos())
