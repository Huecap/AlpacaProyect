from datetime import date

def validar_entero(valor : any):
    """
    Valida que el valor ingresado sea un entero 

    :param valor: Valor a verificar  
    :type valor: int
    :return: Si el valor ingresado es un entero o una cadena de caracteres que puede ser
            transformada a un entero, retorna True, si el valor ingresado no es un entero o es
            una cadena que no puede ser transformada a un entero retorna False 
    :rtype: bool 
    """
    try:
        valor = str(valor)
        int(valor)
        resultado = True
    except ValueError:
        resultado = False
    return resultado
    

def validar_flotante(valor : float):
    """
    Valida que el valor ingresado sea un flotante

    :param valor: Valor a verificar 
    :type valor: float
    :return: Si el valor ingresado es un flotante o una cadena de caracteres que puede ser
            transformada a un flotante, retorna True, si el valor ingresado no es un flotante o es
            una cadena que no puede ser transformada a un flotante retorna False 
    :rtype: bool
    """
    if not validar_entero(valor):
        try:
            float(valor)
            resultado = True
        except ValueError:
            resultado = False
    else: resultado = False
    return resultado

def validar_string(valor : str):
    """
    Valida que el valor ingresado sea un str

    :param valor: Valor a verificar 
    :type valor: str
    :return: Si el valor ingresado es una cadena de Caracteres, entonces retorna true, caso contrario retorna False
    :rtype: bool
    """
    
    if type(valor) == str:
        resultado = True
    else:
        resultado = False
    return resultado


def validar_fecha(valor : date):
    """
    Valida que el valor ingresado sea un objeto del tipo date

    :param valor: Valor a verificar 
    :type valor: date
    :return: Si el valor ingresado es una fecha de del tipo date, entonces retorna true, caso contrario retorna False
    :rtype: bool
    """
    if type(valor) == date:
        resultado = True
    else:
        resultado = False
    return resultado


def validar_validaciones(validacion):
    """
    Funcion que recibe como parametro "validacion" una funcion que permite validar valores
    Es útil para probar los distintos tipos de errores que puede arrojar la validación en si
    para posteriormente agregarlos a la funcion 

    :param validacion: funcion que queremos encontar los distintos tipos de errores que puede arrojar 
    :type validacion: function
    """
    a = 0
    while a != 'M': 
        a = input('Ingrese un valor: ')
        resultado = validacion(a)
        if type(resultado) == float:
            print('La operacion fue exitosa')
        else:
            print(resultado)


if __name__ == '__main__':
    # validar_validaciones(validar_string)
    pass