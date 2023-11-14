from sqlite3 import Error
from DB_tabla_libros import TablaLibros
from NG_libro import Libro
import HR_formatos as formats

print(TablaLibros())

resultado = TablaLibros.show_table('titulo')

if resultado:
    for tupla in resultado:
        for campo in tupla:
            print(campo)
