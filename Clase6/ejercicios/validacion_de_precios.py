"""
Escribí un programa que permita al usuario ingresar el precio de un producto, 
pero que sólo acepte valores mayores a 0. Si el usuario ingresa un valor inválido (negativo o cero),
el programa debe mostrar un mensaje de error, y volver a pedir el valor hasta que se ingrese uno válido. 
Al final, el programa debe mostrar el precio aceptado.

Tips: 
Antes de empezar, pensá si es necesario usar contadores o acumuladores.
Recordá que input() siempre devuelve cadenas de caracteres.
"""

lista_nombre_art_con_precio = []
nombre_artiulo = None

# solicitar al usuario una opcion. agrego un while
while True:
    # Menu de Opciones
    print()
    print("Menu de Gestion de Productos\n")
    print("1. Alta de productos nuevos")
    print("3 Salir\n")
    opcion = int(input("ingrese 1 para dar de alta o 3 para salir (1 - 3)  "))

    # Mostramos la opcion seleccionada
    print(f"Has seleccionado la opcion: {opcion}\n")

    if opcion == 1:
        # Solicito al usuario que ingrese el  nombre del producto y el valor
        # lo almaceno en variables temporales
        nombre_artiulo = str(input("Ingrese el nombre del producto: "))
        precio_art = float(input("ingrese precio unitario: "))
        # si el valor del producto es mayor a 0 lo almaceno en la lista
        if precio_art > 0:
            lista_nombre_art_con_precio.append(nombre_artiulo)
            lista_nombre_art_con_precio.append(precio_art)

        else:
            while precio_art <= 0:
                print(
                    "Error, el precio debe ser mayor a 0. Por favor, ingrese un nuevo valor:  "
                )
                precio_art = float(input("ingrese precio unitario: "))
                if precio_art > 0:
                    lista_nombre_art_con_precio.append(nombre_artiulo)
                    lista_nombre_art_con_precio.append(precio_art)
    elif opcion == 3:
        print("Salir")
        break
else:
    print("La opción es incorrecta\n")

print(lista_nombre_art_con_precio)
