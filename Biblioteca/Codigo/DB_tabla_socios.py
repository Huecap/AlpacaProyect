"""
Tabla de socios
"""

from sqlite3 import Error
from DB_conexion import DBConnection


class TablaSocios(DBConnection):
    """
    Clase que representa y se comunica con la Tabla Socios de la base de datos
    """

    conn = DBConnection("biblioteca.db").dbconnection
    try:
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXIST Socios
                        (socioID INTEGER PRIMARY KEY,
                        nombre VARCHAR,
                        apellido VARCHAR,
                        dni INTEGER,
                        telefono INTEGER,
                        mail TEXT,
                        direccion TEXT)"""
        )
    except Error as er:
        print(er)

    def __str__(self):
        cadena = "|---|---|---|\n"
        socios = self.show_table()
        for reg in socios:
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
            cursor.execute("""SELECT * FROM Socios""")
            resultado = cursor.fetchall()
        except Error as er:
            resultado = er
        finally:
            cursor.close()

        return resultado

    def show_socio(self, identificador: int) -> tuple:
        """
        Descripcion
        :param identificador: ID del socio que se esta buscando
        :type identificador: int
        :return: Una tupla que contiene los datos del registro encontrado
        :rtype: tuple
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """SELECT nombre, apellido, dni, telefono, mail, direccion
                              FROM Socios
                              WHERE socioID=?""",
                (identificador,),
            )
            resultado = cursor.fetchall()
        except Error as er:
            resultado = er
        finally:
            cursor.close()

        return resultado[0]

    def save(self, socio) -> None:
        """
        Descripcion
        :param socio: Socio que se desea guardar en la base de datos
        :type socio: Socio
        """
        try:
            cursor = self.conn.cursor()
            identificador = cursor.execute(
                """INSERT INTO Socios (nombre, apellido, dni, telefono, mail, direccion)
                                       VALUES (?, ?, ?, ?, ?, ?)
                                       returning socioID""",
                (
                    socio.nombre,
                    socio.apellido,
                    socio.dni,
                    socio.telefono,
                    socio.mail,
                    socio.direccion,
                ),
            )
            socio.socioId = identificador
            self.conn.commit()
        except Error as er:
            self.conn.rollback()
            print(er)
        finally:
            cursor.close()

    def update_socio(
        self,
        nombre: str,
        apellido: str,
        dni: int,
        telefono: int,
        mail: str,
        direccion: str,
        identificador: int,
    ) -> None:
        """
        Descripcion
        :param nombre: Nombre nuevo del socio a actualizar
        :type nombre: str
        :param apellido: Apellido nuevo del socio a actualizar
        :type apellido: str
        :param dni: DNI nuevo del socio a actualizar
        :type dni: int
        :param telefono: Telefono nuevo del socio a actualizar
        :type telefono: int
        :param mail: Mail nuevo del socio a actualizar
        :type mail: str
        :param direccion: Direccion nueva del socio a actualizar
        :type direccion: str
        :param identificador: ID del socio a actualizar
        :type identificador: int
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """UPDATE Socios
                              SET nombre=?, apellido=?, dni=?, telefono=?, mail=?, direccion=?
                              WHERE socioID=?""",
                (nombre, apellido, dni, telefono, mail, direccion, identificador),
            )
            self.conn.commit()
        except Error as er:
            self.conn.rollback()
            print(er)
        finally:
            cursor.close()

    def delete_libro(self, identificador: int) -> None:
        """
        Descripcion
        :param identificador: ID del socio a eliminar
        :type identificador: int
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("""DELETE FROM Socios WHERE socioID=?""", (identificador,))
            self.conn.commit()
        except Error as er:
            self.conn.rollback()
            print(er)
