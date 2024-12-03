"""
VISUALIZACION PERSONALIZADA DE PRODUTOS 
Agregá una función al sistema explicado en la clase,
que permita simular la venta de un producto. 
El usuario o usuaria deberá ingresar el código del producto y la cantidad a vender. 
Si la cantidad en stock es suficiente, la función debe restar esa cantidad del inventario.
Si la cantidad solicitada es mayor a la disponible, debe mostrar un mensaje de error.

"""

# variables
inventario = {
    1: {"nombre": "YERBA", "cantidad": 40, "precio": 8000},
    2: {"nombre": "AZUCAR", "cantidad": 90, "precio": 7800},
    3: {"nombre": "SAL", "cantidad": 40, "precio": 580},
    4: {"nombre": "ARROZ", "cantidad": 40, "precio": 580},
    5: {"nombre": "FIDEOS", "cantidad": 40, "precio": 580},
    6: {"nombre": "HUEVO", "cantidad": 40, "precio": 900},
}


# FUNCIONES


#  dar de baja del stock un articulo buscando por el ID:
def dar_de_baja_stock_por_vta(inventario, codigo_producto, cantidad):
    if inventario.get(codigo_producto):
        if inventario.get(codigo_producto)["cantidad"] >= canti_vendida:
            inventario.get(codigo_producto)["cantidad"] -= canti_vendida
            print("venta realizada con exito")

            return True
        else:
            print(
                "\nVenta no realizada por falta de stock, baje la cantidad a vender\n"
            )
    else:
        print("Producto no encontrado el ID", codigo_producto, " no existe")


# inicio programa

codigo_producto = int(input("Ingrese el ID: "))
canti_vendida = int(input("Ingrese la cantidad vendida: "))

if dar_de_baja_stock_por_vta(inventario, codigo_producto, canti_vendida):
    # Recorro la lista con un for para imprimir el diccionario
    for clave, productos in inventario.items():
        print(
            f"ID: {clave} - Nombre: {productos['nombre']} - Cantidad: {productos['cantidad']} - Precio: {productos['precio']}"
        )
