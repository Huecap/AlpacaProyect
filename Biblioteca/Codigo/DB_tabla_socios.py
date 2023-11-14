"""
Tabla de socios
"""

from sqlite3 import Error
from DB_conexion import DBConnection
import HR_formatos as formats


class TablaSocios:
    """
    Clase que representa y se comunica con la Tabla Socios de la base de datos
    """

    conn = DBConnection().dbconnection

    #! ELIMINAR
    @staticmethod
    def __str__() -> str:
        """
        Muestra de forma simple la tabla completa
        :return: Una cadena de caracteres que
        lista cada registro de la tabla Socios de la base de datos
        :rtype: str
        """

        socio = TablaSocios.show_table()
        cadena = formats.cuadro_list_tuple(
            socio,
            1,
            "socioID",
            "Nombre",
            "Apellido",
            "DNI",
            "Telefono",
            "Mail",
            "Direccion",
        )

        return cadena

    @staticmethod
    def show_table(*campos: tuple):
        """
        Trae de la base de datos todos los registros de la tabla
        o solo los campos/columnas deseados y especificados por parametro
        :param campos: Contiene los campos deseados a seleccionar
        o vacia en caso de querer seleccionar todos los campos
        :type campos: tuple
        :return: Devuelve los registros seleccionados
        en caso de que los campos especificados sean correctos
        :rtype: ??
        """

        seleccion = ""
        resultado = None

        if not TablaSocios.validar_campos(campos) and len(campos) != 0:
            resultado = False
        else:
            if len(campos) == 0:
                seleccion = "*"
            elif TablaSocios.validar_campos(campos):
                for elem in campos:
                    seleccion += f"{elem},"
                seleccion = seleccion[:-1]

            try:
                cursor = TablaSocios.conn.cursor()
                # Se valida previamente el valor de 'seleccion' para evitar SQLI
                cursor.execute(f"SELECT {seleccion} FROM Socios")
                resultado = cursor.fetchall()
            except Error:
                resultado = False
            finally:
                cursor.close()

        return resultado

    @staticmethod
    def validar_campos(campos: tuple) -> bool:
        """
        Valida que los campos pasados como parametros pertenezcan a la tabla
        :param campos: Contiene valores en formato str
        a ser validados como los nombres de los campos de la tabla
        :type campos: tuple
        :return: Devuelve un True en caso de que todos los valores
        sean exactamente iguales / pertenezcan a los campos de la tabla
        :rtype: bool
        """

        existen = (
            [
                campo
                in (
                    "socioID",
                    "nombre",
                    "apellido",
                    "dni",
                    "telefono",
                    "mail",
                    "direccion",
                )
                for campo in campos
            ]
            if len(campos) > 0
            else [False]
        )

        return all(existen)

    @staticmethod
    def show_socio(valor, campo: str = "socioID") -> list:
        """
        Busca en la tabla Socios por campo especificado por parametro,
        un registro especifico o varios
        :param valor: Valor del campo por el cual se esta buscando
        :type valor: any
        :param campo: Campo por el cual se desea buscar en la tabla Socios. Por defecto 'socioID'
        :type campo: str
        :return: Devuelve los datos de los registros encontrados
        o un False en caso de no encontrar ningun registro
        :rtype: ??
        """

        # Valida que el campo seleccionado exista en la tabla
        if TablaSocios.validar_campos((campo,)):
            # Si el campo seleccionado es codigo,
            # valida que valor sea un codigo existente en la tabla
            if campo == "socioID" and not TablaSocios.validar_id(valor):
                resultado = False
            else:
                try:
                    cursor = TablaSocios.conn.cursor()
                    cursor.execute(
                        f"""SELECT socioID, nombre, apellido, dni, telefono, mail, direccion
                                    FROM Socios
                                    WHERE {campo}
                                    LIKE '%{valor}%'"""
                    )
                    resultado = cursor.fetchall()
                except Error:
                    resultado = False
                finally:
                    cursor.close()
        else:
            resultado = False

        return resultado

    # Pana
    # REPORTES
    # Crear metodos con SELECT para crear los reportes
    # Por ejemplo:
    #   SELECT id,nombre,telefono FROM Socios ORDER BY nombre
    #   SELECT id,nombre,COUNT(*) FROM Socios ORDER BY id DESC

    @staticmethod
    def save(socio) -> bool:
        """
        Guarda el socio pasado por parametro en la tabla de la base de datos
        :param socio: Socio que se desea guardar en la base de datos
        :type socio: Socio
        :return: Devuelve un True o un False dependiendo si la consulta se realizo con exito o no
        :rtype: bool
        """

        try:
            cursor = TablaSocios.conn.cursor()
            codigo = cursor.execute(
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
            socio.socioID = codigo.fetchall()[0][0]
            TablaSocios.conn.commit()
            resultado = True
        except Error:
            resultado = False
        finally:
            cursor.close()

        return resultado

    @staticmethod
    def update_socio(
        nombre: str,
        apellido: str,
        dni: int,
        telefono: int,
        mail: str,
        direccion: str,
        socioID: int,
    ) -> bool:
        """
        Modifica un registro de la tabla Socios
        :param nombre: Nombre nuevo del socio a actualizar
        :type nombre: str
        :param apellido: Apellido nuevo del socio a actualizar
        :type apellido: str
        :param dni: DNI nuevo del socio a actualizar
        :type dni: int
        :param telefono: Telefono del socio a actualizar
        :type telefono: int
        :param mail: Mail nuevo del socio a actualizar
        :type mail: str
        :param direccion: Direccion nuevo del socio a actualizar
        :type direccion: str
        :return: Devuelve un True o un False dependiendo si la consulta se realizo con exito o no
        :rtype: bool
        """

        if TablaSocios.validar_id(socioID):
            try:
                cursor = TablaSocios.conn.cursor()
                cursor.execute(
                    """UPDATE Socios
                                SET nombre=?, apellido=?, dni=?, telefono=?, mail=?, direccion=?
                                WHERE socioID=?""",
                    (nombre, apellido, dni, telefono, mail, direccion, socioID),
                )
                TablaSocios.conn.commit()
                resultado = True
            except Error:
                resultado = False
            finally:
                cursor.close()
        else:
            resultado = False

        return resultado

    @staticmethod
    def delete_socio(socioID: int) -> bool:
        """
        Eliminar un registro de la tabla Socios
        :param socioID: socioID del socio a eliminar
        :type socioID: int
        :return: Devuelve un True o un False dependiendo si la consulta se realizo con exito o no
        :rtype: bool
        """

        if TablaSocios.validar_id(socioID):
            try:
                cursor = TablaSocios.conn.cursor()
                cursor.execute("""DELETE FROM Socios WHERE socioID=?""", (socioID,))
                TablaSocios.conn.commit()
                resultado = True
            except Error:
                resultado = False
            finally:
                cursor.close()
        else:
            resultado = False

        return resultado

    @staticmethod
    def validar_id(codigo: int) -> bool:
        """
        Valida que el codigo pasado como parametro pertenezca a un registro de la tabla
        :param codigo: Entero a ser validado como un codigo de un registro de la tabla Socios
        :type codigo: int
        :return: Devuelve un True en caso de que el valor sea un codigo de un registro de la tabla
        :rtype: bool
        """

        lista_ids = TablaSocios.show_table("socioID")
        var = [tup[0] == codigo for tup in lista_ids]

        return any(var)
