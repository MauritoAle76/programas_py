# Declaramos una variable tipo lista para almacenar
# Dejo precargada una lista para facilitar las pruebas
# id, npmbre, precio, cantidad
lista_productos = [
    [1, "YERBA", 89, 8],
    [2, "AZUCAR", 3, 2],
    [3, "ARROZ", 25, 253],
]


# Comenzamos con un Bucle del tipo while, que se ejecutará hasta que el usuario ingrese 4
while True:
    print("-" * 30)
    print("\tMenú de opciones")
    print("-" * 30)
    print("1. Alta de producto")
    print("2. Listar productos")
    print("3. Busqueda por nombre")
    print("4. Dar de baja stock por ventas")
    print("5. Dar de alta  stock por compras")

    print("6. Salir")
    print("-" * 30)

    # Pedimos al usuario que ingrese una opción
    opcion = input("\nIngrese la opción que desee: ")
    print("-" * 30)

    # Opción 1: debemos solicitar codigo =! 0 y nombre y precio y cantidad del producto
    # Para nuestra demo almacenamos el dato en la lista

    if opcion == "1":
        # Bloque de codigo para alta de producto
        codigo_de_producto = int(
            input(
                "\nAlta de Produnto, ingrese codigo de producto, o  0 para cancelar: "
            )
        )
        # bucle while para seguir ingresando mientras el codigo se != 0
        while codigo_de_producto != 0:

            nombre_producto = input("Nombre de producto: ").upper()
            precio_de_produto = float(input("Ingrese precio de Producto : "))
            cantidad_producto = int(input("Cantidad: "))
            # Agrego los productos a una lista dentro de otra lista
            lista_productos.append(
                [
                    codigo_de_producto,
                    nombre_producto,
                    precio_de_produto,
                    cantidad_producto,
                ]
            )

            # vuevo a pedir un nuevo codigo para saber si continua el ingreso o se cancela y vuelve al menu principal

            codigo_de_producto = int(
                input("ingrese codigo de producto, o  0 para cancelar:  ")
            )

    # Opción 2: mostramos la list con un print
    # tenemos 2 opciones de visualizacion
    elif opcion == "2":
        # Bloque de codigo para listar de producto
        que_listar = input(
            "Elija el tipo de listado, 0 para imprimir la lista completa o 1 para listar separado por articulo:   "
        )
        if que_listar == "0":
            print(
                f"Lista de productos: {lista_productos}"
            )  # listar una lista de lista por reglon
            print()
        else:
            print(f"Productos ingresados: ")
            for producto in lista_productos:
                print(
                    f"Codigo: {producto [0]}  Nombre: {producto[1]}  Precio: {producto[2]}  Cantidad: {producto[3]} "
                )
                print()
    elif opcion == "3":
        # Bloque de codigo para buscar producto. y lo convertimos a mayuscula
        producto_consultado = input(
            "ingrese el nombre del producto a  buscar: "
        ).upper()

        # usamos un while para recorrer la lista
        indice = 0
        # la variable encontrado los usamos como flag
        encontrado = False

        while indice < len(lista_productos):
            producto_buscado = lista_productos[indice]

            # si encuentra el producto
            if producto_consultado == producto_buscado[1]:
                print(f"Producto encontrado: {producto_buscado[1]} esta en stock.")
                print(
                    f" Nombre {producto_buscado[1]}, Cantidad : {producto_buscado[3]}"
                )
                encontrado = (
                    True  # cuando encuentra el producto reasigna la variable con True
                )
                break
            indice = (
                indice + 1
            )  # sin entrar el if o entrando al if siempre suma uno al indice para seguir recorriendo

        if (
            encontrado != True
        ):  # este if esta fuera del while  para que se ejecute una sola vez cuando el prodcuto no esta en la lista

            print(producto_consultado, " Producto SIN STOCK")

    # OPcion 4 para dar de baja del stock un articulo buscando por el ID
    elif opcion == "4":
        encontrado = False
        # el for recorre la lista buscando el ID si lo encuentra verifica
        # si la cantidd vendida es menor al stock  disponible

        ingrese_ID = int(input("ingrese el ID del producto a dar de baja: "))
        for ID in lista_productos:
            if ingrese_ID == ID[0]:
                canti_vendida = int(input("Ingrese la cantidad vendida: "))
                encontrado = (
                    True  # cambia el estado solo si lo encuentra esta dentro el IF
                )
                if (
                    canti_vendida <= ID[3]
                ):  # si la cantidad es menor al stock hace la venta
                    ID[3] = ID[3] - canti_vendida

                else:  # sino muestra mensaje de bajo stock
                    print()
                    print("-" * 30)
                    print("No hay suficiente stock para realizar la venta")
                    print("-" * 30)
                    break
        if (
            not encontrado
        ):  # esta por afuera del for y solo avisa si no encontro el producto
            print("*" * 30)
            print("Producto no encontrado")
            print("*" * 30)
    elif opcion == "5":
        # Opcion 5, damos de incrementamos el stock, llamando del ID
        # funciona igual que la opcion 4 pero en lugar de restar, suma
        encontrado = False

        ingrese_ID = int(input("ingrese el ID del producto a dar de alta stock : "))
        for ID in lista_productos:
            if ingrese_ID == ID[0]:
                canti_comprada = int(input("Ingrese la cantidad comprada: "))
                encontrado = True
                ID[3] = ID[3] + canti_comprada

        # esta por afuera del for y solo avisa si no encontro el producto

        if not encontrado:
            print("*" * 30)
            print("Producto no encontrado")
            print("*" * 30)

    # Opción 6: el Bucle while debe terminar para salir
    elif opcion == "6":
        break

    # Si la opción ingresada no es válida, mostramos un mensaje de error
    else:
        print("Opcione  no válida, por favor intente de nuevo")
