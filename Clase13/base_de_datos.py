import sqlite3

conexion = sqlite3.connect("prueba.db")
cursor = conexion.cursor()

cursor.execute("select * FROM productos")

resultado = cursor.fetchall()

for registro in resultado:
    print("nombre", registro[0], "cantidad", registro[1])
