def validar_entero(valor):
    try:
        int(valor)
        resultado = True
    except ValueError:
        resultado = False
    return resultado
    

def validar_flotante(valor):
    try:
        float(valor)
        resultado = True
    except ValueError:
        resultado = False
    return resultado

def validar_string(valor):
    if type(valor) == str:
        resultado = True
    else:
        resultado = False
    return resultado


def validar_validaciones(validacion):
    a = 0
    while a != 'M': 
        a = input('Ingrese un valor: ')
        resultado = validacion(a)
        if type(resultado) == float:
            print('La operacion fue exitosa')
        else:
            print(resultado)


if __name__ == '__main__':
    validar_validaciones(validar_string)
    pass