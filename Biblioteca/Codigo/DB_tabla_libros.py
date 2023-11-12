"""
Tabla de libros
"""

from sqlite3 import Error
from DB_conexion import DBConnection


class TablaLibros:
    """
    Clase que representa y se comunica con la Tabla Libros de la base de datos
    """

    conn = DBConnection("biblioteca.db").dbconnection

    # Colocarle formato # Pana
    def __str__(self):
        cadena = "|---|---|---|\n"
        libros = self.show_table()
        for reg in libros:
            cadena += f"{reg}\n"
        cadena += "|---|---|---|\n"
        return cadena

    def show_table(self, *campos):
        """
        Descripcion
        """
        aux = ""
        resultado = None

        if not self.validar_show_table(campos) and len(campos) != 0:
            resultado = 'Campos invalidos'
        else:
            if len(campos) == 0:
                aux = "*"
            elif self.validar_show_table(campos):
                for elem in campos:
                    aux += f"{elem},"
                aux = aux[:-1]

            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT {} FROM Libros".format(aux))
                resultado = cursor.fetchall()
            except Error as er:
                resultado = er
            finally:
                cursor.close()

        return resultado

    def validar_show_table(self, tupla):
        var = (
            [campo in ("codigo", "titulo", "estado", "precio") for campo in tupla]
            if len(tupla) > 0
            else [False]
        )
        return all(var)

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
                              WHERE codigo=?""",
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
