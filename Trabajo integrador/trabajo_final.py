"""
Este proyecto consiste en una aplicación con Python
que permita gestionar el inventario de una pequeña
tienda o comercio. La aplicación debe ser capaz de
registrar, actualizar, eliminar y mostrar productos
en el inventario. Además, debe incluir funcionalidades
para realizar búsquedas y generar reportes de stock
"""

# -----Programa para el PROYECTO FINAL desde CERO -----

# importo el colorama
# esto no lo conozco muy bien, lo voy a investigar con el IA Geminis
from colorama import init, Fore, Style

# me traigo el modulo
import sqlite3

# me conecto a la base de datos y si no exite la creo
conexion = sqlite3.connect("inventario.db")

# creo un cursor
cursor = conexion.cursor()

# cierro la conexion
conexion.close()

# --------------- DECLARACION de Variables: listas, tuplas y diccionarios ------------------------

inventario = []

producto = {
    "nombre": None,
    "descripcion": None,
    "cantidad": None,
    "precio": None,
    "categoria": None,
}


# ******************** ****DECLARACION DE FUNCIONES *******************
# creo tabla inventario
def crear_tabla():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL,
        categoria TEXT
        )"""
    )
    conexion.commit()
    conexion.close()


def alta_producto():  # para la opcion 1 del menu
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    while True:
        # Solicitar al usuario que ingrese los datos del producto
        nombre = input(
            "Ingrese el nombre del producto: "
        ).upper()  # str. lo asigno con un metodo
        descripcion = input(
            "Ingrese la descripcion del producto: "
        ).capitalize()  # str. lo asigno con un metodo
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio = float(input("Ingrese el precio del producto: "))
        categoria = input("Ingrese la categoria del producto: ").capitalize()

        # validacion de precio y cantidad si es mayor a 0
        while cantidad <= 0 or precio <= 0:
            # si no es mayor a 0 entra en un bucle hasta que ingresa el valor correcto
            print(
                Fore.RED
                + Style.NORMAL
                + "Error: La cantidad y el precio deben ser mayores que 0"
                + Style.RESET_ALL
            )  # le damos color ROJO
            print()
            cantidad = int(input("Ingrese la cantidad del producto: "))
            print()
            precio = float(input("Ingrese el precio del producto: "))

        # Si es mayor a 0 lo agrego al lista temporal y luego lo agrego al inventario Global
        inventario_temp = (nombre, descripcion, cantidad, precio, categoria)
        inventario.append(inventario_temp)
        print(Fore.BLUE + "\nProducto agregado con exito\n" + Style.RESET_ALL)

        # sigo agregando productos hasta que el usuario decida salir
        # cuando sale del bucle sale del programa
        # recien ahi se graban los datos en la BD y cierra la conexion
        # se crea un for para que se puedan agregar varios productos ala BD
        opcion = input("Desea agregar otro producto? (s/n): ").lower()
        if opcion != "s":
            for producto in inventario:
                cursor.execute(
                    "INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?,?,?,?,?)",
                    producto,
                )
            conexion.commit()
            inventario.clear()
            break

    conexion.close()
    return inventario


def mostrar_todos_los_productos():
    print("FUNCION EN DESARROLO para la OPCION 2")
    # conecto a la base y creo el cursor
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    cursor.execute()
    print("Listado completo de la tienda")


def actualizar_cantidad():
    print("FUNCION EN DESARROLLO para la OPCION 3")


def eliminar_producto():
    print("FUNCION EN DESARROLLO para la OPCION 4")


def buscar_producto():
    print("FUNCION EN DESARROLLO para la OPCION 5")


def generar_reporte_bajo_stock():
    print("FUNCION EN DESARROLLO para la OPCION 6")


# Menu de Opciones
def mostrar_menu():
    print()
    print(Fore.YELLOW + Style.BRIGHT + "=" * 30 + Style.RESET_ALL)
    print(Fore.BLUE + "Menu de Gestion de Productos" + Style.RESET_ALL)
    print(Fore.YELLOW + Style.BRIGHT + "=" * 30)
    print(Style.RESET_ALL)
    print(Fore.GREEN + "1. Alta de productos nuevos")
    print("2. Mostrar todos los productos")
    print("3. Actualizar la cantidad de un producto")
    print("4. Dar de baja productos")
    print("5. Buscar un producto")
    print("6. Reporte de bajo stock")
    print(Fore.RED + "7. Salir\n" + Style.RESET_ALL)

    # Solicitar al usuario que selecione una opcion
    opcion = int(input("Por favor, seleccione la opcion deseada (1 - 7)  "))
    # Agregan un modulo de validacion para evitar errores - PENDIENTE
    return opcion


def main():
    while True:
        opcion = (
            mostrar_menu()
        )  # mostrar el menu de opciones la opcion viene de la Funcion
        print()
        print(
            "Usted seleciono la opcion",
            opcion,
        )
        print()
        if opcion == 1:
            inventario = alta_producto()

        elif opcion == 2:
            mostrar_todos_los_productos()

        elif opcion == 3:
            actualizar_cantidad()

        elif opcion == 4:
            eliminar_producto()

        elif opcion == 5:
            buscar_producto()

        elif opcion == 6:
            generar_reporte_bajo_stock()

        elif opcion == 7:
            print("Saliendo de la app, muchas gracias por utilizar nuesto sistema\n")
            break
        else:
            print(Fore.RED + "La opción es incorrecta\n" + Style.RESET_ALL)


######  INVOCAMOS A LA FUNCION PRINCIPAL  #######

crear_tabla()

main()
