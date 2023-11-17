"""
Dar formato str a diferentes estructuras
"""

def listado_list_tuple(lista: list, orden=False, *encabezado) -> str:
    """
    Estructura en formato listado str de una lista que contiene tuplas
    :param lista: Lista de tuplas donde cada tupla es un conjunto de datos de una entidad
    :type lista: list
    :param orden: Indica si las filas se amoldaran a las demas automaticamente
    :type orden: bool
    :param encabezado: Encabezados que se peuden poner al formato lista
    :type encabezado: tuple
    :return: Devuelve una cadena donde
    se formateo toda la lista de tuplas como una lista de elementos
    :rtype: str
    """
    cadena = ''
    if orden:
        may = len_mayor_list_tuple(lista)
    else:
        may = 0

    cadena += armar_encabezado(encabezado, may)

    for tupla in lista:
        for campo in tupla:
            if campo is None:
                campo = 'None'
            cadena += f"- {campo:<{may}} "
        cadena += '\n'

    return cadena


def tabla_list_tuple(lista: list, orden=False, *encabezado) -> str:
    """
    Estructura en formato tabla str de una lista que contiene tuplas
    :param lista: Lista de tuplas donde cada tupla es un conjunto de datos de una entidad
    :type lista: list
    :param orden: Indica si las filas se amoldaran a las demas automaticamente
    :type orden: bool
    :param encabezado: Encabezados que se peuden poner al formato tabla
    :type encabezado: tuple
    :return: Devuelve una cadena donde
    se formateo toda la lista de tuplas como una tabla de elementos
    :rtype: str
    """
    cadena = ''
    if orden:
        may = len_mayor_list_tuple(lista)
    else:
        may = 0

    cadena += armar_encabezado(encabezado, may)

    for tupla in lista:
        for campo in tupla:
            if campo is None:
                campo = 'None'
            cadena += f"| {campo:<{may}} "
        cadena += '|\n'

    return cadena

def len_mayor_list_tuple(lista: list) -> int:
    """
    Calcula el elemento de mayor tamaño de la lista de tuplas
    :param lista: Lista de tuplas donde cada tupla es un conjunto de datos de una entidad
    :type lista: list
    :return: tamaño del elemento con mayor longitud
    :rtype: int
    """
    may = 0

    for tupla in lista:
        for campo in tupla:
            if len(str(campo)) > may:
                may = len(str(campo))

    return may

def armar_encabezado(campos, espaciado):
    """
    Formatea los encabezados con un espaciado especifico
    :param campos: Campos que representan cada columna
    :type campos: tuple
    :param espaciado: Espaciado que se pondra dentro de cada campo para igualar sus tamaños
    :type espaciado: int
    :return: Devuelve una cadena con los encabezados formateados
    :rtype: str
    """
    cadena = ''
    if len(campos) > 0:
        may = espaciado
        for campo in campos:
            cadena += f"| {campo:^{may}} "
        cadena += '|\n'
        cadena += f"+{'-' * (len(cadena) - 3)}+\n"

    return cadena

if __name__ == "__main__":

    personas = [('Matias', 'Pana', 11223344), ('Huenu', 'Cap', 55667788), ('Other', 'Person', 11001100)]
