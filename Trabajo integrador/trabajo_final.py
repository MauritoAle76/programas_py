"""
Este proyecto consiste en una aplicación con Python
que permita gestionar el inventario de una pequeña
tienda o comercio. La aplicación debe ser capaz de
registrar, actualizar, eliminar y mostrar productos
en el inventario. Además, debe incluir funcionalidades
para realizar búsquedas y generar reportes de stock
"""


# Menu de Opciones
def main():
    while True:  # arranco con un while
        print()
        print("Menu de Gestion de Productos\n")
        print("1. Alta de productos nuevos")
        print("2. Consulta de datos de productos")
        print("3. Modificar la cantidad de stock de un producto")
        print("4. Dar de baja productos")
        print("5. Listado completo de los productos")
        print("6. Lista de productos con cantidad bajo minimos")
        print("7. Salir\n")

        # Solicitar al usuario que selecione una opcion
        opcion = int(input("Por favor, seleccione la opcion deseada (1 - 7)  "))
        print()
        # Mostramos la opcion seleccionada
        print(f"Has seleccionado la opcion: {opcion}\n")

        if opcion == 1:
            print("Prodecemos al alta de producto")
        elif opcion == 2:
            print("Procedemos a llevarlo al menu de consultas")

        elif opcion == 3:
            print("Procedemos a modificar la cantidad ")

        elif opcion == 4:
            print("Procedemos a dar de baja el producto")

        elif opcion == 5:
            print("Procedemos a Listar la totalidad de articulos")

        elif opcion == 6:
            print("Procedemos a listar los articulos con bajo stock")

        elif opcion == 7:
            print("Saliendo de la app, muchas gracias por utilizar nuesto sistema\n")
            break
        else:
            print("La opción es incorrecta\n")


main()  # Llamamos a la función main para iniciar el programa.
