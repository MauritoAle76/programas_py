# -----Programa para el PROYECTO FINAL desde CERO -----

# importo el colorama
# esto no lo conozco muy bien, lo voy a investigar con el IA Geminis
from colorama import init, Fore, Style

# me traigo el modulo de la Base de datos
import sqlite3

# importo los modulos de las funciones
# lo que empieza con db son funciones de la base de datos
# y lo que empieza con menu son funciones del menu


from funciones_base_de_datos import db_crear_tabla
from menu_funciones import *


# --------------- DECLARACION de Variables: listas, tuplas y diccionarios ------------------------

# Variable CONSTANTE
# aqui se cambia la ruta una vez y aplica en todas las funciones

ruta_db = "inventario.db"

# Dic... como ayuda memoria de la esctructura de la BD
# se utiliza en el punto 1 del menu como dicc local,
# para luego ser almacenados en la base de datos

producto = {
    "nombre": None,
    "descripcion": None,
    "cantidad": None,
    "precio": None,
    "categoria": None,
    "minimo_stock": None,
}


def main():
    # primero creo la base de datos y la tabla, si es que no existe
    db_crear_tabla()  # esta funcion se importa del modulo funciones BD
    # Luego arranca el ciclo del menu
    while True:
        opcion = (
            menu_mostrar_menu()
        )  # mostrar el menu de opciones la opcion viene de la Funcion yla variable opcion es el return de la funcion
        print()
        print(
            "Usted seleciono la opcion : ",
            opcion,
        )
        print()
        if opcion == 1:
            menu_alta_producto()

        elif opcion == 2:
            menu_mostrar_todos_los_productos()

        elif opcion == 3:
            menu_actualizar_cantidad()

        elif opcion == 4:
            menu_eliminar_producto()

        elif opcion == 5:
            menu_buscar_producto()

        elif opcion == 6:
            menu_generar_reporte_bajo_stock()

        elif opcion == 7:
            print("Saliendo de la app, muchas gracias por utilizar nuesto sistema\n")
            break
        else:
            print(Fore.RED + "La opción es incorrecta\n" + Style.RESET_ALL)


######  INVOCAMOS A LA FUNCION PRINCIPAL  #######

if __name__ == "__main__":
    main()
