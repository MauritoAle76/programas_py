# importacion de modulos

from funciones_base_de_datos import *
from colorama import init, Fore, Style


# Menu de Opciones
def menu_mostrar_menu():
    print()
    print(Fore.YELLOW + Style.BRIGHT + "=" * 30 + Style.RESET_ALL)
    print(Fore.BLUE + "Menu de Gestion de Productos" + Style.RESET_ALL)
    print(Fore.YELLOW + Style.BRIGHT + "=" * 30)
    print(Style.RESET_ALL)
    print(Fore.GREEN + "1. Alta de productos nuevos")
    print("2. Mostrar todos los productos")
    print("3. Actualizar datos de un producto")
    print("4. Dar de baja productos")
    print("5. Buscar un producto")
    print("6. Reporte de bajo stock")
    print(Fore.RED + "7. Salir\n" + Style.RESET_ALL)

    # Solicitar al usuario que selecione una opcion
    opcion = int(
        input(
            Fore.GREEN
            + "Por favor, seleccione la opcion deseada (1 - 7)  "
            + Style.RESET_ALL
        )
    )

    return opcion


# *****************FUNCION ALTA PRODUCTOS ************************* Terminada
# funcion para el alta de producto, le pide al usuarios los datos
# los guarda en un DICCIONARIO, y luego los almacena en la base de datos
# llamando a otra fucion para registrar
# ******************************************************************


def menu_alta_producto():  # para la opcion 1 del menu
    print("-" * 30)
    print("ALTA DE UN PRODUCTO")
    print("-" * 30)
    print()

    while True:
        # Solicitar al usuario que ingrese los datos del producto
        print(Fore.BLUE + "\n Ingrese los datos del producto nuevo\n" + Style.RESET_ALL)
        nombre = input(
            Fore.BLUE + " El nombre : " + Style.RESET_ALL
        ).upper()  # str. lo asigno con un metodo
        descripcion = input(
            Fore.BLUE + "La descripcion del producto: " + Style.RESET_ALL
        ).capitalize()  # str. lo asigno con un metodo
        cantidad = int(input(Fore.BLUE + "La cantidad : " + Style.RESET_ALL))
        precio = float(input(Fore.BLUE + "El precio : " + Style.RESET_ALL))
        categoria = input(Fore.BLUE + "La categoria : " + Style.RESET_ALL).capitalize()
        minimo_stock = int(
            input(Fore.BLUE + "Defina un STOCK MINIMO : " + Style.RESET_ALL)
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

            cantidad = int(input("Reingrese cantidad : "))
            print()

            precio = float(input("Reingrese el precio : "))

            minimo_stock = int(input("Reingrese cantidad de STOCK MINIMO : "))

        # Si es mayor a 0 lo agrego se guarda en un diccionario
        inventario = {
            "nombre": nombre,
            "descripcion": descripcion,
            "cantidad": cantidad,
            "precio": precio,
            "categoria": categoria,
            "minimo_stock": minimo_stock,
        }

        # llamo a la funcion dentro de otra funcion,
        # para que se ejecute la funcion grabar en la BD
        # La funcion tiene como paramatro el Diccionario

        db_guardar_registros_en_tabla_productos(inventario)

        # sigo agregando productos hasta que el usuario decida salir

        opcion = input(
            Fore.GREEN + "Desea agregar otro producto? (s/n): " + Style.RESET_ALL
        ).lower()
        if opcion != "s":
            break


# ************** MOSTRAR TODOS LOS PRODUCTOS*********** Terminada
# esta funcion muestra todos los productos que se encuentran en la BD
# los imprime en pantalla con un formato agradable
# se uutiliza un bucle for para recorrer la lista de productos
# opcion 2 del menu

# ******************************************************


def menu_mostrar_todos_los_productos():
    print("-" * 30)
    print("LISTAR TODOS LOS PRODUCTO")
    print("-" * 30)
    print()
    # me capturo el return de la funcion que busca TODOS los prodcutos
    listado = db_buscar_productos()

    # lo itero con For para que se imprima por linea y se vea mas ordenado
    print(Fore.LIGHTGREEN_EX + "Listado completo de la tienda\n" + Style.RESET_ALL)

    for producto in listado:

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


# ************** ACTUALIZAR PRODUCTOS POR CATEGORIA*********** Terminada
# esta funcion originalmente solo actualizaca la cantidad de un producto
# pero luego se le agregaron mas campos para que se actualizara Precios y Stock Minimo
# opcion 3 del menu
# **************************************************************


def menu_actualizar_cantidad():
    print("-" * 30)
    print("ACTUALIZAR DATOS DE UN PRODUCTO")
    print("-" * 30)
    print()
    # Debe poder actulizar la cantidad de un producto, el precio y el sctock minimo
    id_actualizar = int(input("\n¿Qué producto deseas actualizar?, ingresa el ID: "))
    id = db_buscar_producto_por_id(id_actualizar)
    while id:
        # Mensaje para confirmar e informar el producto que se va actualizar
        print(f"\n El ID {id_actualizar} corresponde a: {id[1]}")

        # le pregunto al usuario que producto quiere actualizar
        print("\n 1. Si desea actualizar la CANTIDAD? :")
        print("\n 2. Si desea actualizar el PRECIO? :")
        print("\n 3. Si desea actualizar el STOCK MINIMO? :")
        print("\n 4. SALIR: ")

        opcion = input("\nElija una opcion : ")
        # ingresa el nuevo valor y se graba en la BD. y cicla hasta que el usuario desea salir

        if opcion == "1":
            cantidad = int(
                input(
                    f"El producto {id[1]} tiene un stock de : {id[3]} -- Ingrese  la nueva cantidad?: "
                )
            )
            db_actualizar_datos_en_base("cantidad", cantidad, id_actualizar)

        elif opcion == "2":
            precio = float(
                input(
                    f"El producto {id[1]} tiene un precio de : $ {id[4]} . - Ingrese el nuevo PRECIO?: $ "
                )
            )
            db_actualizar_datos_en_base("precio", precio, id_actualizar)

        elif opcion == "3":
            stock_minimo = int(
                input(
                    f"El producto {id[1]} tiene definido como stock minimo: {id[6]} ¿Cual es el nuevo STOCK MINIMO?: "
                )
            )
            db_actualizar_datos_en_base("minimo_stock", stock_minimo, id_actualizar)

        elif opcion == "4":
            print("\nSaliendo del menu actualizar")
            break

        else:
            print("Opción no válida, por favor elija una opción válida")

    print(f"\nNo se encontro el ID: {id_actualizar} en la base de datos")


# *********ELIMINAR PRODUCTOS************** Terminada
# Esta funcion elimina un producto de la base de datos
# se le pide al usuario que ingrese el id del producto que quiere eliminar
# se valida si la opcion es la correcta antes de eliminar
# Opcion 4 del menu
# *******************************************


def menu_eliminar_producto():
    print("-" * 30)
    print("ELIMINAR PRODUCTO")
    print("-" * 30)
    print()
    # Eliminar producto por ID
    id = int(
        input(
            Fore.LIGHTRED_EX
            + "Ingrese el Nombre del producto que desea eliminar: "
            + Style.RESET_ALL
        )
    )
    resultado = db_buscar_producto_por_id(id)
    # validacion antes de borrar
    if resultado:
        print(
            Fore.LIGHTRED_EX
            + f"\n Usted va a eliminar el siguiente registro: ID {resultado[0]}, Nombre {resultado[1]}"
            + Style.RESET_ALL
        )

        sos = input(
            Fore.GREEN
            + f"\n Esta seguro de eliminar el registro... 'SI' o 'NO' "
            + Style.RESET_ALL
        ).lower()

        if sos == "si":
            mensaje = db_eliminar_registro_de_tabla_productos(id)
            print(mensaje)
        else:
            print(Fore.BLUE + "\nNo se elimino el registro" + Style.RESET_ALL)

    else:
        print(
            Fore.BLUE + f"\n El ID '{id}' no se encontro en la base" + Style.RESET_ALL
        )


# **************Buscar por ID*************
# busca un producto por el ID
# opcionalmente puede buscar por nombre y categoria
# Opcion 5 del menu
# *****************************************


def menu_buscar_producto():
    print("-" * 30)
    print("BUSCAR PRODUCTO")
    print("-" * 30)
    print()
    id = int(input("Ingrese el ID del producto: "))
    resultado = db_buscar_producto_por_id(id)

    if not resultado:
        print(f"\n El ID '{id}' no se encontro en la base")
    else:
        print(
            f"\n Se encontro el siguiente registro: ID: {resultado[0]}, Nombre: {resultado[1]}"
        )


# ******** REPORTE BAJO STOCK***************
# la funcion debe mostrar los productos que estan igual o por debajo de la cantidad minima
# la cantidad minima se fija cuando se da de alta un producto
# Opcion 6 del menu
# *******************************************


def menu_generar_reporte_bajo_stock():
    print("-" * 30)
    print("REPORTE DE BAJO STOCK")
    print("-" * 30)
    print()
    print("FUNCION EN DESARROLLO para la OPCION 6")

    resultado = db_reporte_de_bajo_stock()
    if not resultado:
        print("\n No hay productos con stock bajo")
    else:
        print("\n Los siguientes productos estan con stock bajo:")
        for producto in resultado:
            print(
                f"\n ID: {producto[0]}, Nombre: {producto[1]}, Cantidad : {producto[3]}"
            )
