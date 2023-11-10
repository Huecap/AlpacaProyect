import sqlite3
from abc import ABC
from collections import namedtuple
from sqlite3 import Error
from rich import print as printr

class Empleados(namedtuple('Empleados', ['nombre', 'salario'])):

    def __str__(self):
        return f"-> Nombre: {self.nombre:<6} | Salario: {self.salario}"

class DataBase(ABC):

    def __init__(self) -> None:
        self.conexion = sqlite3.connect("empresa2.db")

    def mostrarTabla(self):
        pass

class TablaEmpleados(DataBase):

    def mostrarTabla(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT nombre, salario FROM empleados")
            resultado = cursor.fetchall()
            cursor.close()
        except Error as er:
            resultado = er

        return resultado

miDB_TablaEmpleados = TablaEmpleados()
result = miDB_TablaEmpleados.mostrarTabla()
for emp in map(Empleados._make, result):
    printr(emp.__str__())
