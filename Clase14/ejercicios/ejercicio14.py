import sqlite3

nuevas_personas = [
    ("Esteban", 32, "Mar del Plata"),
    ("Valeria", 25, "Bahía Blanca"),
    ("Fernando", 41, "Rosario"),
    ("Carolina", 29, "La Plata"),
    ("Juan", 35, "Córdoba"),
]
conexion = sqlite3.connect(
    r"C:\Users\Mauro\Desktop\talento_tech_Python\programas_py\Clase14\ejercicios\personas.db"
)
cursor = conexion.cursor()


def crear_tabla():
    conexion = sqlite3.connect(
        r"C:\Users\Mauro\Desktop\talento_tech_Python\programas_py\Clase14\ejercicios\personas.db"
    )
    cursor = conexion.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS personas 
                   (nombre TEXT NOT NULL,
                    edad INTEGER NOT NULL,
                    ciudad TEX NOT NULL,
                    id INTEGER PRIMARY KEY AUTOINCREMENT)
                    """
    )
    cursor.close


def insertar_personas():
    conexion = sqlite3.connect(
        r"C:\Users\Mauro\Desktop\talento_tech_Python\programas_py\Clase14\ejercicios\personas.db"
    )
    cursor = conexion.cursor()
    for individuo in nuevas_personas:
        cursor.execute(
            "INSERT INTO personas (nombre, edad, ciudad) VALUES (?,?,?)",
            individuo,
        )

    conexion.commit()

    cursor.close()


def eliminar_personas():
    # edad = []
    conexion = sqlite3.connect(
        r"C:\Users\Mauro\Desktop\talento_tech_Python\programas_py\Clase14\ejercicios\personas.db"
    )
    cursor = conexion.cursor()
    # ojo tuve que poner los coechetes para que no me de error. asi es una lista
    edad = [int(input("ingrese la edad de los registro que quiere eliminar: "))]
    cursor.execute(
        """ DELETE FROM personas WHERE edad  >= ? """,
        (edad),
    )
    conexion.commit()
    cursor.close()


def listar_todo():
    conexion = sqlite3.connect(
        r"C:\Users\Mauro\Desktop\talento_tech_Python\programas_py\Clase14\ejercicios\personas.db"
    )
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM personas")
    resultado = cursor.fetchall()
    print(resultado)
    cursor.close()


# crear_tabla()
insertar_personas()
listar_todo()
eliminar_personas()
listar_todo()


cursor.close
