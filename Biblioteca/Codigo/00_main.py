
"""Mas o menos voy estructurando las funcionalidades que tiene
que tiene que tener la interfaz"""

import schedule
import time 
import threading

# -- Ventana Libros -- # 
def cargar_libro():
    pass

def cambiar_titulo():
    pass

def cambiar_estado():
    pass

def cambiar_precio():
    pass

def mostrar_libro():
    pass 


# -- Ventan socios -- # 
def cargar_socio():
    pass

def cambiar_datos():
    # Te permite cambiar 
    # - nombre 
    # apellido 
    # dni 
    # telefono 
    # mail 
    # direccion 
    pass

def registrar_prestamo():
    pass 

def registrar_devolucion():
    pass

def mostrar_socio():
    pass

# -- Ventan prestamos -- # 
def crear_prestamo():
    pass 

def cambiar_estado_prestamo():
    pass 

def cambiar_datos_prestamo():
    pass 

def mostrar_prestamo():
    pass

def job():
    print('Holi')
    
def validar():
    print("hola")

def validar_prestamos():
    pass
def ejecutar_tareas_programadas():
    # Las ejecuta cada 1 hs, 
    while True:
        schedule.run_pending()
        time.sleep(120)

if __name__ == '__main__':
    schedule.every().day.at("03:16").do(validar)
    # schedule.every(1).hour.do(validar)
    threading.Thread(target=ejecutar_tareas_programadas, daemon=True).start()
    a = input('Terminar programa presione enter')
