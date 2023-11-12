
# Formato de documentacion 


#### Nombres 

> Nombres de archivos = **XX_Nombre**

**XX** = es un prefijo que indica la clasificación del archivo 
- DB = Base de datos
- HR = Herramientas 
- IN = Interfaz 
- NG = Lógica de Negocio 
- RP = Reporte 


> Nombres clases = Mayúsculas + Camelcase

> Nombres funciones = minúsculas + snake_case 

---
#### docstring:
> Utilizamos el formato rest(Sphinx) 
Línea de Resumen: La primera línea del docstring debería ser una breve descripción de la función.

- Descripción Detallada: A continuación de la línea de resumen, puedes proporcionar una descripción más detallada de la función.

- Parámetros: Después de la descripción, puedes listar los parámetros de la función utilizando la sintaxis :param nombre_parametro: Descripción del parámetro.. 
- Tipo esperado del parámetro utilizando :type nombre_parametro: Tipo del parámetro..

- Valor Devuelto: Puedes describir el valor devuelto utilizando :return: Descripción del valor devuelto. y :rtype: Tipo del valor devuelto..

```python
def validar_entero(valor : any):
    """
    Valida que el valor ingresado sea un entero 

    :param valor: Valor a verificar  
    :type valor: any
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
```
---
#### cometarios en docstring con Better comments 
```python 

""" 
! = Información Importante, cosas con las que tener cuidado 
    ! Ojo que esta funcion solo funcion con esa funcion 

? = Comentario de una persona 
    ? Pana = En esta funcion la funcion funciona
    ? Huecap = En esta funcion la funcion funciona

TODO: = Indica alguna funcionalidad o cosa que tenemos que hacer o nos falta 
    TODO: En esta funcion me falta hacer que la funcion funcione
"""
```