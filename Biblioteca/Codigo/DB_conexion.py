"""
Conexion a la base de datos
"""

import sqlite3

class DBConnection:
    """
    Clase que contiene la conexion a la base de datos
    """
    _instance = None
    dbconnection = None

    def __new__(cls, connection_string):
        if not cls._instance:
            cls._instance = super(DBConnection, cls).__new__(cls)
            cls.dbconnection = sqlite3.connect(connection_string)

        return cls._instance
