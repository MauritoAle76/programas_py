import sqlite3

conexion = sqlite3.connect(
    r"c:\Users\Mauro\Desktop\talento_tech_Python\programas_py\Clase13\prueba.db"
)
cursor = conexion.cursor()

cursor.execute("select * FROM productos")

resultado = cursor.fetchall()
print(resultado)

for registro in resultado:
    print(
        "id",
        registro[0],
        "nombre",
        registro[1],
        "cantidad",
        registro[3],
        "precio",
        registro[4],
        "total valorizado",
        registro[3] * registro[4],
    )

    # cursor.execute(
    "INSERT INTO productos(nombre, descripcion, cantidad, precio) VALUES ('sal gruesa', 'de primera para chacinados', 10, 900)"
# )
# conexion.commit()

conexion.close()
