"""
Tabla de prestamos
"""

from sqlite3 import Error
from datetime import datetime
from conexion import DBConnection


class TablaPrestamos(DBConnection):
    """
    Clase que representa y se comunica con la Tabla Prestamos de la base de datos
    """

    conn = DBConnection("biblioteca.db").dbconnection
    try:
        cursor = conn.cursor()
        # Foreign kays: libroCodigo & socioID
        cursor.execute(
            """CREATE TABLE IF NOT EXIST Prestamos
                        (id INTEGER PRIMARY KEY,
                        fechaPrestamo DATETIME,
                        cantidadDias INTEGER,
                        estado VARCHAR,
                        socioID INTEGER,
                        libroCodigo INTEGER,
                        FOREIGN KEY (SocioID) REFERENCES Socios (SocioID),
                        FOREIGN KEY (libroCodigo) REFERENCES Libros (codigo))"""
        )
    except Error as er:
        print(er)

    def __str__(self):
        cadena = "|---|---|---|\n"
        prestamos = self.show_table()
        for reg in prestamos:
            cadena += f"{reg}\n"
        cadena += "|---|---|---|\n"
        return cadena

    def show_table(self) -> list:
        """
        Descripcion
        :return: Una lista de tuplas que contienen los datos de cada registro
        :rtype: list
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("""SELECT * FROM Prestamos""")
            resultado = cursor.fetchall()
        except Error as er:
            resultado = er
        finally:
            cursor.close()

        return resultado

    def show_prestamo(self, identificador: int) -> tuple:
        """
        Descripcion
        :param identificador: ID del presatmos, socio o libro que se esta buscando
        :type identificador: int
        :return: Una tupla que contiene los datos del registro encontrado
        :rtype: tuple
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """SELECT fechaPrestamo, cantidadDias, estado, socioID, libroCodigo
                              FROM Prestamos
                              WHERE id=? OR socioID=? OR libroCodigo=?""",
                (identificador,),
            )
            resultado = cursor.fetchall()
        except Error as er:
            resultado = er
        finally:
            cursor.close()

        return resultado[0]

    # Crear metodo que devuelva los prestamos segun el estado # Pana

    def save(self, prestamo) -> None:
        """
        Descripcion
        :param prestamo: Prestamos que se desea guardar en la base de datos
        :type prestamo: Prestamo
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """INSERT INTO Prestamos (fechaPrestamo, cantidadDias, estado, socioID, libroCodigo)
                                       VALUES (?, ?, ?, ?, ?)""",
                (
                    prestamo.fechaPrestamo,
                    prestamo.cantidadDias,
                    prestamo.estado,
                    prestamo.socioID,
                    prestamo.libroCodigo,
                ),
            )
            self.conn.commit()
        except Error as er:
            self.conn.rollback()
            print(er)
        finally:
            cursor.close()

    def update_prestamo(
        self,
        fechaPrestamo: datetime,
        cantidadDias: int,
        estado: str,
        socioID: int,
        libroCodigo: int,
        identificador: int,
    ) -> None:
        """
        Descripcion
        :param fechaPrestamo: Fecha del prestamo nueva del prestamo a actualizar
        :type fechaPrestamo: datetime
        :param cantidadDias: Cantidad de dias nuevos del prestamo a actualizar
        :type cantidadDias: int
        :param estado: Estado nuevo del prestamo a actualizar
        :type estado: str
        :param socioID: ID del socio nuevo del prestamo a actualizar
        :type socioID: int
        :param socioCodigo: Codigo del libro nuevo del prestamo a actualizar
        :type socioCodigo: int
        :param identificador: ID del prestamo a actualizar
        :type identificador: int
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """UPDATE Prestamos
                              SET fechaPrestamo=?, cantidadDias=?, estado=?, socioID=?, libroCodigo=?
                              WHERE id=?""",
                (
                    fechaPrestamo,
                    cantidadDias,
                    estado,
                    socioID,
                    libroCodigo,
                    identificador,
                ),
            )
            self.conn.commit()
        except Error as er:
            self.conn.rollback()
            print(er)
        finally:
            cursor.close()

    def delete_prestamo(self, identificador: int) -> None:
        """
        Descripcion
        :param identificador: ID del prestamo a eliminar
        :type identificador: int
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("""DELETE FROM Prestamos WHERE id=?""", (identificador,))
            self.conn.commit()
        except Error as er:
            self.conn.rollback()
            print(er)
