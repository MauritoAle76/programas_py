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


# --------------- DECLARACION de Variables: listas, tuplas y diccionarios ------------------------

# lista de productos, donde se almacenan temporalmente los datos ingresados por el usuario
# en el punto 1 del menu, para luego ser almacenados en la base de datos

inventario = []

# Dic... como ayuda memoria de la esctructura de la BD
# no lo uso
producto = {
    "nombre": None,
    "descripcion": None,
    "cantidad": None,
    "precio": None,
    "categoria": None,
    "minimo_stock": None,
}


# ******************** ****DECLARACION DE FUNCIONES *******************


def conexion_a_la_base_de_datos():
    # me conecto a la base de datos y si no exite la creo
    conexion = sqlite3.connect("inventario.db")

    # creo un cursor
    cursor = conexion.cursor()
    return cursor, conexion


# ***************************************
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
        categoria TEXT NOT NULL,
        minimo_stock INTEGER NOT NULL
        )"""
    )
    conexion.commit()
    conexion.close()


# *****************FUNCION ALTA PRODUCTOS *************************
# funcion para el alta de producto, le pide al usuarios los datos
# los guarda en la lista INVENTARIO, y luego los almacena en la base de datos
# llamando a otra fucion


def alta_producto():  # para la opcion 1 del menu
    while True:
        # Solicitar al usuario que ingrese los datos del producto

        nombre = input(
            Fore.BLUE + "Ingrese el nombre del producto: " + Style.RESET_ALL
        ).upper()  # str. lo asigno con un metodo
        descripcion = input(
            Fore.BLUE + "Ingrese la descripcion del producto: " + Style.RESET_ALL
        ).capitalize()  # str. lo asigno con un metodo
        cantidad = int(
            input(Fore.BLUE + "Ingrese la cantidad del producto: " + Style.RESET_ALL)
        )
        precio = float(
            input(Fore.BLUE + "Ingrese el precio del producto: " + Style.RESET_ALL)
        )
        categoria = input(
            Fore.BLUE + "Ingrese la categoria del producto: " + Style.RESET_ALL
        ).capitalize()
        minimo_stock = int(
            input(
                Fore.BLUE + "Ingrese la cantidad de STOCK MINIMO : " + Style.RESET_ALL
            )
        )

        # validacion de precio y cantidad si es mayor a 0
        while cantidad <= 0 or precio <= 0 or minimo_stock <= 0:
            # si no es mayor a 0 entra en un bucle hasta que ingresa el valor correcto
            print(
                Fore.RED
                + Style.NORMAL
                + "Error: La cantidad, precio y Stock minimo deben ser mayores que 0"
                + Style.RESET_ALL
            )  # le damos color ROJO
            print()

            cantidad = int(input("Ingrese la cantidad del producto: "))
            print()

            precio = float(input("Ingrese el precio del producto: "))

            minimo_stock = int(input("Ingrese la cantidad de STOCK MINIMO : "))

        # Si es mayor a 0 lo agrego se guarda en la lista
        inventario = (
            nombre,
            descripcion,
            cantidad,
            precio,
            categoria,
            minimo_stock,
        )

        # llamo a la funcion dentro de otra funcion,
        # para que se ejecute la funcion grabar en la BD

        guardar_registros_en_tabla_productos(inventario)

        # sigo agregando productos hasta que el usuario decida salir

        opcion = input("Desea agregar otro producto? (s/n): ").lower()
        if opcion != "s":
            break


# *********FUNCION GUARDAR EN BD****************


def guardar_registros_en_tabla_productos(inventario):
    # me conecto a la base de datos
    conexion = sqlite3.connect("inventario.db")

    # creo un cursor
    cursor = conexion.cursor()

    # ejecuto la sentencia SQL para insertar datos en la tabla productos
    # tiene que ser igual a la cantidad de campos que tiene la tabla productos y la lista inventario
    # como tiene ID autoincremental, el campo ID se omite ya que la DB le asigna valor
    cursor.execute(
        "INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria, minimo_stock) VALUES (?,?,?,?,?,?)",
        inventario,
    )

    # guardo los cambios en la BD
    conexion.commit()
    # cierro la conexion
    conexion.close()

    # imprime mensaje para confirmar la operacion al usario

    mensaje = print(Fore.BLUE + "\nProducto agregado con exito\n" + Style.RESET_ALL)

    return mensaje


# *************FUNCION ACTUALIZAR*********************


def actualizar_datos_en_base(nombre_columna, variable_a_actualizar, id_actualizar):
    # me conecto a la base de datos
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    instruccion = f"UPDATE productos SET {nombre_columna} = ? WHERE id = ?"
    datos = (variable_a_actualizar, id_actualizar)
    cursor.execute(instruccion, datos)
    conexion.commit()
    conexion.close
    print(Fore.GREEN + "\nvalor actualizado con exito" + Style.RESET_ALL)


# ************** MOSTRAR TODOS LOS PRODUCTOS***********
def mostrar_todos_los_productos():

    # conecto a la base y
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    # Obtengo datos de la baser
    cursor.execute("""SELECT * FROM productos""")
    # se almacena la consulta en una variable para luego
    # trabajarla con un for
    listado = cursor.fetchall()

    # For para que se imprima por linea y se vea mas ordenado
    print("Listado completo de la tienda\n")
    for producto in listado:
        """print(
            f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: {producto[4]}, Categoría: {producto[5]}, Mínimo Stock: {producto[6]}\n"
        )"""
        # le dimos un poco de color para mejorar la visual del listado
        print(
            f"{Fore.YELLOW}ID: {producto[0]} {Style.RESET_ALL}| "
            f"{Fore.GREEN}Nombre: {producto[1]} {Style.RESET_ALL}| "
            f"{Fore.CYAN}Descripción: {producto[2]} {Style.RESET_ALL}| "
            f"{Fore.MAGENTA}Cantidad: {producto[3]} {Style.RESET_ALL}| "
            f"{Fore.RED}Precio: {producto[4]} {Style.RESET_ALL}| "
            f"{Fore.BLUE}Categoría: {producto[5]} {Style.RESET_ALL}| "
            f"{Fore.LIGHTWHITE_EX}Mínimo Stock: {producto[6]} {Style.RESET_ALL}"
        )
    # simpre cerrar la conexion
    conexion.close()


def actualizar_cantidad():

    # Debe poder actulizar la cantidad de un producto, el precio y el sctock minimo
    id_actualizar = int(input("\n¿Qué producto deseas actualizar?, ingresa el ID: "))
    while True:
        # le pregunto al usuario que producto quiere actualizar
        print("\n 1. Si desea actualizar la cantidad? :")
        print("\n 2. Si desea actualizar el precio? :")
        print("\n 3. Si desea actualizar el stock minimo? :")
        print("\n 4. Si desea salir de la opción de actualizar? :")

        opcion = input("\nElija una opcion : ")
        # ingresa el nuevo valor y se graba en la BD. y cicla hasta que el usuario desea salir

        if opcion == "1":
            cantidad = int(input("¿Indique la nueva cantidad?: "))
            actualizar_datos_en_base("cantidad", cantidad, id_actualizar)

        elif opcion == "2":
            precio = float(input("¿Indique el nuevo PRECIO?: "))
            actualizar_datos_en_base("precio", precio, id_actualizar)

        elif opcion == "3":
            stock_minimo = int(input("¿Cual es el nuevo STOCK MINIMO?: "))
            actualizar_datos_en_base("minimo_stock", stock_minimo, id_actualizar)

        elif opcion == "4":
            print("Saliendo del menu actualizar")
            break

        else:
            print("Opción no válida, por favor elija una opción válida")


def eliminar_producto():
    # Eliminar producto por ID
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    nombre_produ = input(
        Fore.LIGHTRED_EX
        + "Ingrese el Nombre del producto que desea eliminar: "
        + Style.RESET_ALL
    ).upper()

    # instrucciones sql

    instruccion_delete = "DELETE FROM productos WHERE nombre = ?"
    instruccion_validar = "SELECT * FROM productos WHERE nombre = ?"
    cursor.execute(instruccion_validar, (nombre_produ,))
    resultado = cursor.fetchall()

    # validacion antes de borrar
    if resultado:
        print(
            Fore.LIGHTRED_EX
            + f"\n Usted va a eliminar el siguiente registro: ID {resultado[0][0]}, Nombre {resultado[0][1]}"
            + Style.RESET_ALL
        )

        sos = input(
            Fore.BLUE
            + f"\n Esta seguro de eliminar el registro... 'SI' o 'NO' "
            + Style.RESET_ALL
        ).lower()

        if sos == "si":
            cursor.execute(instruccion_delete, (nombre_produ,))
            print(
                Fore.LIGHTRED_EX
                + "\n El producto ha sido eliminado con exito exito"
                + Style.RESET_ALL
            )
        else:
            print(Fore.LIGHTBLUE_EX + "\nNo se elimino el registro" + Style.RESET_ALL)

    else:
        print(f"\n{nombre_produ} no se encontro en la base")
    # Confirmo cambios y guardo
    conexion.commit()
    conexion.close()


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

if __name__ == "__main__":
    crear_tabla()
    main()
