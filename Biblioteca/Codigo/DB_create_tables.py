from sqlite3 import Error
from DB_conexion import DBConnection

def create_tables():
    conn = DBConnection("biblioteca.db").dbconnection
    cursor = conn.cursor()
    resultado = ''

    try:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS Libros
                        (codigo INTEGER PRIMARY KEY,
                        titulo TEXT,
                        estado VARCHAR,
                        precio FLOAT)"""
        )
        resultado += "Se creo la tabla 'Libros' con exito\n"
    except Error as er:
        resultado += f"Error {er} al crear la tabla 'Libros'\n"

    try:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS Socios
                        (socioID INTEGER PRIMARY KEY,
                        nombre VARCHAR,
                        apellido VARCHAR,
                        dni INTEGER,
                        telefono INTEGER,
                        mail TEXT,
                        direccion TEXT)"""
        )
        resultado += "Se creo la tabla 'Socios' con exito\n"
    except Error as er:
        resultado += f"Error {er} al crear la tabla 'Socios'\n"

    try:
        # Foreign kays: libroCodigo & socioID
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS Prestamos
                        (codigo INTEGER PRIMARY KEY,
                        fechaPrestamo DATETIME,
                        cantidadDias INTEGER,
                        fechaDevolucion DATETIME,
                        estado VARCHAR,
                        socioID INTEGER,
                        libroCodigo INTEGER,
                        FOREIGN KEY (SocioID) REFERENCES Socios (SocioID),
                        FOREIGN KEY (libroCodigo) REFERENCES Libros (codigo))"""
        )
        resultado += "Se creo la tabla 'Prestamos' con exito\n"
    except Error as er:
        resultado += f"Error {er} al crear la tabla 'Prestamos'\n"

    cursor.close()
    conn.commit()

    return resultado
