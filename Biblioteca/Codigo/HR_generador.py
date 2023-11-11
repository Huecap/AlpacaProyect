from Programs.DAO.TP.Codigo.Herramientas.HR_datos import libros_famosos_50
import csv
import random


def generarLibros(nombre_archivo):
    estado = ["Disponible", "Prestado", "Extraviado"]
    libros = []
    for _ in range(0, 1000):
        libro = {
            "Titulo": random.choice(libros_famosos_50),
            "Estado": random.choice(estado),
            "Precio": random.randrange(5000, 15000),
        }
        libros.append(libro)
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=["Titulo", "Estado", "Precio"])

        # escribir el encabezado
        writer.writeheader()

        # escribir lineas
        writer.writerows(libros)


def main():
    generarLibros("Libros.csv")


if __name__ == "__main__":
    main()
