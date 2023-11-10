"""
Tabla de libros
"""

from sqlite3 import Error
from conexion import DBConnection


class TablaLibros(DBConnection):
    """
    Clase que representa y se comunica con la Tabla Libros de la base de datos
    """

    conn = DBConnection("biblioteca.db").dbconnection
    # Creacion de las tablas en un modulo aparte luego de crear la conexion # Pana
    try:
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXIST Libros
                        (codigo INTEGER PRIMARY KEY,
                        titulo TEXT,
                        estado VARCHAR,
                        precio FLOAT)"""
        )
    except Error as er:
        print(er)

    def __str__(self):
        cadena = "|---|---|---|\n"
        libros = self.show_table()
        for reg in libros:
            cadena += f"{reg}\n"
        cadena += "|---|---|---|\n"
        return cadena

    # Se puede unificar el metodo tomando otro parameto que filtre por un campo especifico, concatenando "WHERE campo=?" # Pana
    def show_table(self) -> list:
        """
        Descripcion
        :return: Una lista de tuplas que contienen los datos de cada registro
        :rtype: list
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("""SELECT * FROM Libros""")
            resultado = cursor.fetchall()
        except Error as er:
            resultado = er
        finally:
            cursor.close()

        return resultado

    def show_libro(self, codigo: int) -> tuple:
        # RETORNAR EL ID # Pana
        """
        Descripcion
        :param codigo: Codigo del libro que se esta buscando
        :type codigo: int
        :return: Una tupla que contiene los datos del registro encontrado
        :rtype: tuple
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """SELECT codigo, titulo, estado, precio
                              FROM Libros
                              WHERE id=?""",
                (codigo,),
            )
            resultado = cursor.fetchall()
        except Error as er:
            resultado = er
        finally:
            cursor.close()

        return resultado[0]

    # Crear metodo con SELECT que devuelva los libros segun el estado # Pana
    # REPORTES
    # Crear metodos con SELECT para crear los reportes # Pana
    # Por ejemplo:
    #   SELECT id,nombre,autor FROM Libros ORDER BY nombre
    #   SELECT id,autor,COUNT(*) FROM Libros ORDER BY id DESC

    def save(self, libro) -> None:
        """
        Descripcion
        :param libro: Libro que se desea guardar en la base de datos
        :type libro: Libro
        """
        try:
            cursor = self.conn.cursor()
            codigo = cursor.execute(
                """INSERT INTO Libros (titulo, estado, precio)
                                       VALUES (?, ?, ?)
                                       returning codigo""",
                (libro.titulo, libro.estado, libro.precio),
            )
            libro.codigo = codigo
            self.conn.commit()
        except Error as er:
            print(er)
        finally:
            cursor.close()

    def update_libro(
        self, titulo: str, estado: str, precio: float, codigo: int
    ) -> None:
        """
        Descripcion
        :param titulo: Titulo nuevo del libro a actualizar
        :type titulo: str
        :param estado: Estado nuevo del libro a actualizar
        :type estado: str
        :param precio: Precio nuevo del libro a actualizar
        :type precio: float
        :param codigo: Codigo del libro a actualizar
        :type codigo: int
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """UPDATE Libros
                              SET titulo=?, estado=?, precio=?
                              WHERE codigo=?""",
                (titulo, estado, precio, codigo),
            )
            self.conn.commit()
        except Error as er:
            print(er)
        finally:
            cursor.close()

    def delete_libro(self, codigo: int) -> None:
        """
        Descripcion
        :param codigo: Codigo del libro a eliminar
        :type codigo: int
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("""DELETE FROM Libros WHERE codigo=?""", (codigo,))
            self.conn.commit()
        except Error as er:
            print(er)
