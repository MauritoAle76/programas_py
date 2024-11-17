""" Validacion de precios.... es el ejercicio de la clase 6... simplificado por el profe

se escribe mucho menos codigo y hace lo mismo

se usa el while como un IF asi hace 2 cosas al mismo tiempo

"""

# Declaro  listas

lista_nombre_art_con_precio = []

# las variables no la declaro por que son temporales en el codigo

# El menu es mejor si esta en un bucle  while para que se repita hasta que el usuario quiera salir

# solicitar al usuario una opcion.
while True:
    # Menu de Opciones
    print()
    print("Menu de Gestion de Productos\n")
    print("1. Alta de productos nuevos")
    print("3 Salir\n")
    opcion = int(input("ingrese 1 para dar de alta o 3 para salir  "))

    # Mostramos la opcion selecionada
    print(f"Su opcion es {opcion}\n ")

    if opcion == 1:
        # Le pido al usuario que ingrese valor y producto
        # Lo almaceno en variables tempoales
        nombre_artiulo = str(input("ingrese el nombre del producto: "))
        precio_articulo = float(input("Ingrese el valor del producto : "))

        # El while se usa como If es decir como bucle y como condicional
        # Mientras el valor sea menor a cero el bucle sigue, caso contrario lo agrega a la lista

        while precio_articulo <= 0:
            print(
                "Error, el precio debe ser mayor a 0. Por favor ingrese un nuevo valor: "
            )
            precio_articulo = float(input("Ingrese el valor del producto : "))

        # el programa llega a este punto solo cuando el precio ingresado es mayor a 0
        lista_nombre_art_con_precio.append(nombre_artiulo)
        lista_nombre_art_con_precio.append(precio_articulo)

    elif opcion == 3:
        print("salir")
        break
    else:
        print("La opcion ingresada es incorrecta\n")

print(f"Los articulos ingresados son: {lista_nombre_art_con_precio}")
