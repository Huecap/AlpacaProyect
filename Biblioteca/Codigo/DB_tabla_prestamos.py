"""
Tabla de prestamos
"""

from sqlite3 import Error
from datetime import datetime
from DB_conexion import DBConnection
from DB_tabla_libros import TablaLibros
from DB_tabla_socios import TablaSocios
import HR_formatos as formats


#! Revisar y probar luego de hacer NG_prestamo
class TablaPrestamos:
    """
    Clase que representa y se comunica con la Tabla Prestamos de la base de datos
    """

    conn = DBConnection().dbconnection

    #! ELIMINAR
    @staticmethod
    def __str__() -> str:
        """
        Muestra de forma simple la tabla completa
        :return: Una cadena de caracteres que
        lista cada registro de la tabla Prestamos de la base de datos
        :rtype: str
        """

        prestamos = TablaPrestamos.show_table()
        cadena = formats.tabla_list_tuple(
            prestamos,
            0,
            "Codigo",
            "Fecha de Prestamo",
            "Cantidad de Dias",
            "Fecha de Devolucion",
            "Estado",
            "socioID",
            "Codigo de Libro",
        )

        return cadena

    @staticmethod
    def save(prestamo) -> bool:
        """
        Guarda el prestamo pasado por parametro en la tabla de la base de datos
        :param prestamo: Prestamo que se desea guardar en la base de datos
        :type prestamo: Prestamo
        :return: Devuelve un True o un False dependiendo si la consulta se realizo con exito o no
        :rtype: bool
        """

        if not TablaPrestamos.validar_codigo(prestamo.codigo):
            try:
                cursor = TablaPrestamos.conn.cursor()
                codigo = cursor.execute(
                    """INSERT INTO Prestamos (fechaPrestamo, cantidadDias, fechaDevolucion, estado, socioID, libroCodigo)
                                        VALUES (?, ?, ?, ?, ?, ?)
                                        returning codigo""",
                    (
                        prestamo.fechaPrestamo,
                        prestamo.cantidadDias,
                        prestamo.fechaDevolucion,
                        prestamo.estado,
                        prestamo.socio.socioID,
                        prestamo.libro.codigo,
                    ),
                )
                prestamo.codigo = codigo.fetchall()[0][0]
                TablaPrestamos.conn.commit()
                resultado = True
            except Error as er:
                resultado = False
                print(er)
            finally:
                cursor.close()
        else:
            resultado = False

        return resultado

    @staticmethod
    def create_prestamo(codigo: int):
        """
        Permite acceder a un registro de la tabla e instanciarlo como un objeto de la clase Prestamo
        :param codigo: Codigo del registro que se esta buscando
        :type codigo: int
        :return: Devuelve el objeto Prestamo ya instanciado
        sin volverlo a almacenar en la base de datos
        """
        #! Para evitar la importacion ciclica
        from NG_prestamo import Prestamo

        if TablaPrestamos.validar_codigo(codigo):
            registro = TablaPrestamos.show(codigo)

            if registro:
                socio = TablaSocios.create_socio(registro[0][5])
                libro = TablaLibros.create_libro(registro[0][6])
                print(socio)
                print(libro)
                prestamo = Prestamo(
                    registro[0][1], registro[0][2], socio, libro, crear=False
                )
                prestamo.codigo = registro[0][0]
                prestamo.fechaDevolucion = registro[0][3]
                prestamo.estado = registro[0][4]
                print(prestamo)

                resultado = prestamo
        else:
            resultado = False

        return resultado

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

        if not TablaPrestamos.validar_campos(campos) and len(campos) != 0:
            resultado = False
        else:
            if len(campos) == 0:
                seleccion = "*"
            elif TablaPrestamos.validar_campos(campos):
                for elem in campos:
                    seleccion += f"{elem},"
                seleccion = seleccion[:-1]

            try:
                cursor = TablaPrestamos.conn.cursor()
                # Se valida previamente el valor de 'seleccion' para evitar SQLI
                cursor.execute(f"SELECT {seleccion} FROM Prestamos")
                resultado = cursor.fetchall()
            except Error:
                resultado = False
            finally:
                cursor.close()

        return resultado

    @staticmethod
    def show(valor, campo: str = "codigo") -> list:
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
        if TablaPrestamos.validar_campos((campo,)):
            # Si el campo seleccionado es codigo,
            # valida que valor sea un codigo existente en la tabla
            if campo == "codigo" and not TablaPrestamos.validar_codigo(valor):
                resultado = False
            else:
                try:
                    cursor = TablaPrestamos.conn.cursor()
                    cursor.execute(
                        f"""SELECT codigo, fechaPrestamo, cantidadDias, fechaDevolucion, estado, socioID, libroCodigo
                                    FROM Prestamos
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
    # Crear metodo con SELECT que devuelva los prestamos segun el estado
    # REPORTES
    # Crear metodos con SELECT para crear los reportes
    # Por ejemplo:
    #   SELECT id,estado,socioID FROM Prestamos ORDER BY socioID
    #   SELECT id,estado,COUNT(*) FROM Prestamos ORDER BY estado DESC

    @staticmethod
    def update_prestamo(
        fechaPrestamo: datetime,
        cantidadDias: int,
        fechaDevolucion: datetime,
        estado: str,
        socioID: int,
        libroCodigo: int,
        codigo: int,
    ) -> bool:
        """
        Modifica un registro de la tabla Prestamos
        :param fechaPrestamo: Fecha inicial del prestamo nueva del prestamo a actualizar
        :type fechaPrestamo: datetime
        :param cantidadDias: Cantidad de dias nueva del prestamo a actualizar
        :type cantidadDias: int
        :param fechaDevolucion: Fecha de devolucion nueva del prestamo a actualizar
        :type fechaDevolucion: datetime
        :param estado: Estado nuevo del prestamo a actualizar
        :type estado: str
        :param socioID: socioID nuevo del prestamo a actualizar
        :type socioID: int
        :param libroCodigo: libroCodigo nuevo del prestamo a actualizar
        :type libroCodigo: int
        :param codigo: Codigo del prestamo a actualizar
        :type codigo: int
        :return: Devuelve un True o un False dependiendo si la consulta se realizo con exito o no
        :rtype: bool
        """

        if TablaPrestamos.validar_codigo(codigo):
            try:
                cursor = TablaPrestamos.conn.cursor()
                cursor.execute(
                    """UPDATE Prestamos
                                SET fechaPrestamo=?, cantidadDias=?, fechaDevolucion=?, estado=?, socioID=?, libroCodigo=?
                                WHERE codigo=?""",
                    (
                        fechaPrestamo,
                        cantidadDias,
                        fechaDevolucion,
                        estado,
                        socioID,
                        libroCodigo,
                        codigo,
                    ),
                )
                TablaPrestamos.conn.commit()
                resultado = True
            except Error:
                resultado = False
            finally:
                cursor.close()
        else:
            resultado = False

        return resultado

    @staticmethod
    def delete_prestamo(codigo: int) -> bool:
        """
        Eliminar un registro de la tabla Prestamos
        :param codigo: Codigo del prestamo a eliminar
        :type codigo: int
        :return: Devuelve un True o un False dependiendo si la consulta se realizo con exito o no
        :rtype: bool
        """

        if TablaPrestamos.validar_codigo(codigo):
            try:
                cursor = TablaPrestamos.conn.cursor()
                cursor.execute("""DELETE FROM Prestamos WHERE codigo=?""", (codigo,))
                TablaPrestamos.conn.commit()
                resultado = True
            except Error:
                resultado = False
            finally:
                cursor.close()
        else:
            resultado = False

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
                    "codigo",
                    "fechaPrestamo",
                    "cantidadDias",
                    "fechaDevolucion",
                    "estado",
                    "socioID",
                    "libroCodigo",
                )
                for campo in campos
            ]
            if len(campos) > 0
            else [False]
        )

        return all(existen)

    @staticmethod
    def validar_codigo(codigo: int) -> bool:
        """
        Valida que el codigo pasado como parametro pertenezca a un registro de la tabla
        :param codigo: Entero a ser validado como un codigo de un registro de la tabla Prestamos
        :type codigo: int
        :return: Devuelve un True en caso de que el valor sea un codigo de un registro de la tabla
        :rtype: bool
        """

        lista_codigos = TablaPrestamos.show_table("codigo")
        var = [tup[0] == codigo for tup in lista_codigos]

        return any(var)

if __name__ == "__main__":
    # print(TablaLibros.__str__())
    #print(TablaLibros.show_table(('codigo', '1')))
    
    a = ('socioID', '1')
    print((TablaPrestamos.show(a[1], campo=a[0])))
    contador = 0
    for n in (TablaPrestamos.show(a[1], campo=a[0])):
        if n[4] == 'En Fecha' or n[4] == 'Extraviado':
            contador += 1
    print(contador)
    print(TablaPrestamos.show_table())
        