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

    #! ELIMINAR
    @staticmethod
    def __str__() -> str:
        """
        Muestra de forma simple la tabla completa
        :return: Una cadena de caracteres que
        lista cada registro de la tabla Libros de la base de datos
        :rtype: str
        """

        cadena = "> ------------------------- +\n"
        libros = TablaLibros.show_table()
        for reg in libros:
            cadena += f"{reg}\n"
        cadena += "> ------------------------- +\n"

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

        if not TablaLibros.validar_campos(campos) and len(campos) != 0:
            resultado = False
        else:
            if len(campos) == 0:
                seleccion = "*"
            elif TablaLibros.validar_campos(campos):
                for elem in campos:
                    seleccion += f"{elem},"
                seleccion = seleccion[:-1]

            try:
                cursor = TablaLibros.conn.cursor()
                # Se valida previamente el valor de 'seleccion' para evitar SQLI
                cursor.execute(f"SELECT {seleccion} FROM Libros")
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
            [campo in ("codigo", "titulo", "estado", "precio") for campo in campos]
            if len(campos) > 0
            else [False]
        )

        return all(existen)

    @staticmethod
    def show_libro(valor, campo: str = "codigo") -> list:
        """
        Busca en la tabla Libros por campo especificado por parametro,
        un registro especifico o varios
        :param valor: Valor del campo por el cual se esta buscando
        :type valor: any
        :param campo: Campo por el cual se desea buscar en la tabla Libros. Por defecto 'codigo'
        :type campo: str
        :return: Devuelve los datos de los registros encontrados
        o un False en caso de no encontrar ningun registro
        :rtype: ??
        """

        # Valida que el campo seleccionado exista en la tabla
        if TablaLibros.validar_campos((campo,)):
            # Si el campo seleccionado es codigo,
            # valida que valor sea un codigo existente en la tabla
            if campo == "codigo" and not TablaLibros.validar_codigo(valor):
                resultado = False
            else:
                try:
                    cursor = TablaLibros.conn.cursor()
                    cursor.execute(
                        f"""SELECT codigo, titulo, estado, precio
                                    FROM Libros
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
    # Crear metodo con SELECT que devuelva los libros segun el estado
    # REPORTES
    # Crear metodos con SELECT para crear los reportes
    # Por ejemplo:
    #   SELECT id,nombre,autor FROM Libros ORDER BY nombre
    #   SELECT id,autor,COUNT(*) FROM Libros ORDER BY id DESC

    @staticmethod
    def save(libro) -> bool:
        """
        Guarda el liblo pasado por parametro en la tabla de la base de datos
        :param libro: Libro que se desea guardar en la base de datos
        :type libro: Libro
        :return: Devuelve un True o un False dependiendo si la consulta se realizo con exito o no
        :rtype: bool
        """

        try:
            cursor = TablaLibros.conn.cursor()
            codigo = cursor.execute(
                """INSERT INTO Libros (titulo, estado, precio)
                                       VALUES (?, ?, ?)
                                       returning codigo""",
                (libro.titulo, libro.estado, libro.precio),
            )
            libro.codigo = codigo.fetchall()[0][0]
            TablaLibros.conn.commit()
            resultado = True
        except Error:
            resultado = False
        finally:
            cursor.close()

        return resultado

    @staticmethod
    def update_libro(titulo: str, estado: str, precio: float, codigo: int) -> bool:
        """
        Modifica un registro de la tabla Libros
        :param titulo: Titulo nuevo del libro a actualizar
        :type titulo: str
        :param estado: Estado nuevo del libro a actualizar
        :type estado: str
        :param precio: Precio nuevo del libro a actualizar
        :type precio: float
        :param codigo: Codigo del libro a actualizar
        :type codigo: int
        :return: Devuelve un True o un False dependiendo si la consulta se realizo con exito o no
        :rtype: bool
        """

        if TablaLibros.validar_codigo(codigo):
            try:
                cursor = TablaLibros.conn.cursor()
                cursor.execute(
                    """UPDATE Libros
                                SET titulo=?, estado=?, precio=?
                                WHERE codigo=?""",
                    (titulo, estado, precio, codigo),
                )
                TablaLibros.conn.commit()
                resultado = True
            except Error:
                resultado = False
            finally:
                cursor.close()
        else:
            resultado = False

        return resultado

    @staticmethod
    def delete_libro(codigo: int) -> bool:
        """
        Eliminar un registro de la tabla Libros
        :param codigo: Codigo del libro a eliminar
        :type codigo: int
        :return: Devuelve un True o un False dependiendo si la consulta se realizo con exito o no
        :rtype: bool
        """

        if TablaLibros.validar_codigo(codigo):
            try:
                cursor = TablaLibros.conn.cursor()
                cursor.execute("""DELETE FROM Libros WHERE codigo=?""", (codigo,))
                TablaLibros.conn.commit()
                resultado = True
            except Error:
                resultado = False
            finally:
                cursor.close()
        else:
            resultado = False

        return resultado

    @staticmethod
    def validar_codigo(codigo: int) -> bool:
        """
        Valida que el codigo pasado como parametro pertenezca a un registro de la tabla
        :param codigo: Entero a ser validado como un codigo de un registro de la tabla Libros
        :type codigo: int
        :return: Devuelve un True en caso de que el valor sea un codigo de un registro de la tabla
        :rtype: bool
        """

        lista_codigos = TablaLibros.show_table("codigo")
        var = [tup[0] == codigo for tup in lista_codigos]

        return any(var)
