"""
Imaginá que estás a cargo de organizar una pequeña biblioteca de la escuela en una base de datos.
Los datos que se quieren registrar incluyen el título del libro, el autor, la fecha de publicación 
y el género. 

Definí:

Un nombre adecuado para la tabla.
Los campos que incluirías en la tabla, sus tipos de datos y por qué.
Qué campo sería la clave primaria y por qué.

"""

# importe modulo
import sqlite3

# conecte y/o cree la base de datos
conexion = sqlite3.connect(
    r"C:\Users\Mauro\Desktop\talento_tech_Python\programas_py\Clase13\Ejercicios\biblioteca.db"
)


# hice el puntero o cursor para usar de comando
cursor = conexion.cursor()

# Crear la tabla dentro de la base de datos
# la clave primaria es un numero autoincremental, que se llama id
# es asi por que puede haber dos libros con el mismo nombre pero no con el mismo id
# de esa manera los identifico

cursor.execute(
    """ CREATE TABLE IF NOT EXISTS libros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    fecha_publicacion DATE NOT NULL,
    genero TEXT NOT NULL
    );
"""
)
# lista vacia, que se convierte en una lista de tuplas
datos_para_tabla = []

# datos para la tabla
# while True:
#     nombre = input("ingrese el nombre del libro ")
#     autor = input("ingrese el autor del libro ")
#     fecha_publicacion = int(input("ingrese la fecha de publicacion del libro "))
#     genero = input("ingrese el genero del libro ")
#     temporal = (nombre, autor, fecha_publicacion, genero)
#     datos_para_tabla.append(temporal)
#     opcion = input("¿Desea agregar otro libro? si/no ")
#     if opcion.lower() == "no":
#         break


print(datos_para_tabla)

# insertar datos en la tabla
# para insertar mas de una tupla , se usa un for para recorrer la lista

for datos in datos_para_tabla:
    cursor.execute(
        "INSERT INTO libros (titulo, autor, fecha_publicacion, genero) VALUES (?, ?, ?, ?)",
        datos,
    )

conexion.commit()

# mostrar los datos de la tabla
cursor.execute("SELECT * FROM libros")
# pero solo lo ejecuta en memoria, crear varible

consulta = cursor.fetchall()

for i in consulta:
    print(i)

# cuenta la cantidad de registros
cursor.execute("SELECT COUNT (*) FROM libros")

# con fetchall me trae una lista de tuplas
# si el pongo el [0] me trae una tupla
# si le pongo fetchone[0] me trae un int
# si a fechtone no le pongo el corchete me trae un tupla
print(cursor.fetchone()[0])

# modificar un campo de un registro

cursor.execute("UPDATE libros SET autor = 'mauro' WHERE id = 6 ")

# ahora voy a borrar el registro con ID 8

cursor.execute("DELETE FROM libros WHERE id = 8")
# para que se reflejen los cambios en la base de datos, se usa commit
conexion.commit()

cursor.execute("SELECT * FROM libros")

print(cursor.fetchall())


conexion.close()
