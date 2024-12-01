"""
REGISTRO DE PRODCUTOS CON VALIDACIONES

Escribí una función que permita registrar un nuevo producto en el inventario,
pero con una condición: la cantidad de productos debe ser mayor que 0 y el precio también 
debe ser un valor positivo. 
Al ingresar una cantidad o precio no válido,
debe mostrar un mensaje de error y pedir los datos nuevamente hasta que sean correctos.

"""

# cargo colorama para darle forma al texto
from colorama import init, Fore, Style

inventario = {}


def alta_producto():

    while True:
        # Solicitar al usuario que ingrese los datos del producto
        producto_id = len(inventario) + 1  # asigno el ID
        nombre = input("Ingrese el nombre del producto: ")
        descripcion = input("Ingrese la descripcion del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio = float(input("Ingrese el precio del producto: "))
        categoria = input("Ingrese la categoria del producto: ")

        # validacion de precio y cantidad si es mayor a 0
        while cantidad <= 0 or precio <= 0:
            # si no es mayor a 0 entra en un bucle hasta que ingresa el valor correcto
            print(
                Fore.RED
                + Style.NORMAL
                + "\nError: La cantidad y el precio deben ser mayores que 0\n"
                + Style.RESET_ALL
            )
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))

        # Si es mayor a 0 lo agrego a un diccionario temporal
        inventario[producto_id] = {
            "nombre": nombre,
            "descripcion": descripcion,
            "cantidad": cantidad,
            "precio": precio,
            "categoria": categoria,
        }
        print("Producto agregado con exito")

        opcion = input("Desea agregar otro producto? (s/n): ").lower()
        if opcion != "s":
            break
    return inventario


alta_producto()
# invocar la funcion alta_producto y lo agrego al dicc global
print(inventario)
