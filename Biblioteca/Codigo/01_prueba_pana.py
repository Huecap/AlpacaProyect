# from sqlite3 import Error
# import HR_formatos as formats
from datetime import datetime
from DB_tabla_libros import TablaLibros
from DB_tabla_socios import TablaSocios
from DB_tabla_prestamos import TablaPrestamos
from NG_libro import Libro
from NG_socio import Socio
from NG_prestamo import Prestamo
from DB_create_tables import create_tables

# print(create_tables())

# socio = Socio('Matias', 'Pana', 11223344, 3511234567, 'elpana@gmail.com', 'Juarez 126 CBA')

for n in range(7):
    #TablaLibros.delete_libro(19+n)
    libro = Libro(f'Harry Potter {n}', 2000)
    libro.modificar_estado(1)
#print(socio)
#print(libro)

# print(TablaSocios())
# print(TablaLibros())

# socio = TablaSocios.create_socio(1)
# print(socio)
# libro = TablaLibros.create_libro(1)
# print(libro)

# socio.nuevo_prestamo(libro, 5)
# print(socio.prestamos)

# print(TablaPrestamos())

# print(TablaLibros())
