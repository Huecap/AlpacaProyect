"""
Dar formato str a diferentes estructuras
"""

def listado_list_tuple(lista: list, orden=0, *encabezado) -> str:
    """
    Estructura en formato listado str una lista que contiene tuplas
    :param lista: 
    """
    cadena = ''
    if orden == 1:
        may = len_mayor_list_tuple(lista)
    else:
        may = 0

    cadena += armar_encabezado(encabezado, may)

    for tupla in lista:
        for campo in tupla:
            cadena += f"- {campo:<{may}} "
        cadena += '\n'

    return cadena


def cuadro_list_tuple(lista: list, orden=0, *encabezado) -> str:
    cadena = ''
    if orden == 1:
        may = len_mayor_list_tuple(lista)
    else:
        may = 0

    cadena += armar_encabezado(encabezado, may)

    for tupla in lista:
        for campo in tupla:
            cadena += f"| {campo:<{may}} "
        cadena += '|\n'

    return cadena

def len_mayor_list_tuple(lista: list) -> int:
    may = 0

    for tupla in lista:
        for campo in tupla:
            if len(str(campo)) > may:
                may = len(str(campo))

    return may

def armar_encabezado(campos, espaciado):
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

    #? Otros formatos:
    # print(listado_list_tuple(personas))
    # print(cuadro_list_tuple(personas))
    # print(listado_list_tuple(personas, 1))
    # print(cuadro_list_tuple(personas, 1))
    # print(listado_list_tuple(personas, 0, 'Nombre', 'Apellido', 'DNI'))
    # print(cuadro_list_tuple(personas, 0, 'Nombre', 'Apellido', 'DNI'))
    # print(listado_list_tuple(personas, 1, 'Nombre', 'Apellido', 'DNI'))
    #! RECOMENDADO:
    print(cuadro_list_tuple(personas, 1, 'Nombre', 'Apellido', 'DNI'))
