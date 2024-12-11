# importacion de modulos

import sqlite3
from colorama import init, Fore, Style


# los nombres COMIENZAN con db_ por la siglas Date Base


# variable constante
ruta_db = "inventario.db"

# ***************************************
# CONECTAR A LA BASE DE DATOS
# ****************************************


def db_conexion_a_la_base_de_datos():
    # me conecto a la base de datos y si no exite la creo
    conexion = sqlite3.connect(ruta_db)

    # creo un cursor
    cursor = conexion.cursor()
    return cursor, conexion


# *********************************************
# CREAR LA TABLA INVENTARIO
# ********************************************


def db_crear_tabla():
    conexion = sqlite3.connect(ruta_db)
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


# *****************************************
#           FUNCION GUARDAR EN BD
# *****************************************


def db_guardar_registros_en_tabla_productos(inventario):
    # me conecto a la base de datos
    conexion = sqlite3.connect(ruta_db)

    # creo un cursor
    cursor = conexion.cursor()

    # ejecuto la sentencia SQL para insertar datos en la tabla productos
    # tiene que ser igual a la cantidad de campos que tiene la tabla productos y la lista inventario
    # como tiene ID autoincremental, el campo ID se omite ya que la DB le asigna valor
    instruccion = "INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria, minimo_stock) VALUES (?,?,?,?,?,?)"
    datos = (
        inventario["nombre"],
        inventario["descripcion"],
        inventario["cantidad"],
        inventario["precio"],
        inventario["categoria"],
        inventario["minimo_stock"],
    )
    cursor.execute(instruccion, datos)

    # guardo los cambios en la BD
    conexion.commit()
    # cierro la conexion
    conexion.close()

    # imprime mensaje para confirmar la operacion al usario

    mensaje = print(Fore.BLUE + "\nProducto agregado con exito\n" + Style.RESET_ALL)

    return mensaje


# *****************************************
#         ELIMINAR REGISTRO DE LA BD
# *****************************************


def db_eliminar_registro_de_tabla_productos(id):
    # me conecto a la base de datos
    conexion = sqlite3.connect(ruta_db)
    # creo un cursor
    cursor = conexion.cursor()
    # query
    instruccion = f"DELETE FROM productos WHERE id = ? "
    datos = (id,)
    # ejecuto la sentencia SQL para eliminar datos de la tabla productos
    cursor.execute(instruccion, datos)
    # guardo los cambios en la BD
    conexion.commit()
    # cierro la conexion
    conexion.close()
    # imprime mensaje para confirmar la operacion al usario
    mensaje = (
        Fore.BLUE + "\nEl producto ha sido eliminado con exito\n" + Style.RESET_ALL
    )
    return mensaje


# *****************************************
#         ACTUALIAR EN BASE DE DATOS
# *****************************************


def db_actualizar_datos_en_base(nombre_columna, variable_a_actualizar, id_actualizar):
    # me conecto a la base de datos
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    instruccion = f"UPDATE productos SET {nombre_columna} = ? WHERE id = ?"
    datos = (variable_a_actualizar, id_actualizar)
    cursor.execute(instruccion, datos)
    conexion.commit()
    conexion.close
    print(Fore.GREEN + "\nvalor actualizado con exito" + Style.RESET_ALL)


# *****************************************
#               BUSCAR PRODUCTOS
# por ID
# *****************************************terminada


def db_buscar_producto_por_id(id):
    # me conecto a la base de datos
    conexion = sqlite3.connect(ruta_db)
    # creo un cursor
    cursor = conexion.cursor()
    instruccion = f"SELECT * FROM productos WHERE id = ? "
    datos = (id,)
    cursor.execute(instruccion, datos)
    resultado_busqueda_id = cursor.fetchone()

    return resultado_busqueda_id

    conexion.close()


# *****************************************
#               BUSCAR PRODUCTOS
# trae todos
# *****************************************


def db_buscar_productos():
    # conecto a la base y
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    # Obtengo datos de la base Genero la Query
    instruccion = """SELECT * FROM productos"""
    # El cursor va con el parametro,
    cursor.execute(instruccion)
    # se almacena la consulta en una variable para luego
    # trabajarla con un for
    listado = cursor.fetchall()
    return listado
    cursor.close()


def db_reporte_de_bajo_stock():
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()

    instruccion = """SELECT * FROM productos WHERE  cantidad < minimo_stock """

    cursor.execute(instruccion)

    resultado = cursor.fetchall()
    conexion.close()

    return resultado
