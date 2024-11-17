"""
El inventario de una tienda está almacenado en un diccionario, 
donde las claves son los nombres de los productos y los valores son las cantidades disponibles en stock. 
Creá un programa que:

Te permita ingresar el nombre de un producto.
Utilice el método .get() para buscar el stock disponible. Si el producto no existe,
deberá mostrar un mensaje diciendo "Producto no encontrado".
Si el producto está disponible, mostrará cuántas unidades quedan en stock.
"""

# claves son los nombres de los productos y los valores son las cantidades
inventario = {"manzana": 30, "pera": 25, "naranja": 20}

prod_a_buscar = input("Ingrese el nombre del producto: ").lower()
# buscamos el producto en el inventario
if inventario.get(prod_a_buscar):
    print(f"El producto {prod_a_buscar} tiene {inventario.get(prod_a_buscar)}")
else:
    print(f"{prod_a_buscar}, no esta en el inventario")
    # si el producto no existe, muestra un mensaje diciendo "Producto no encontrado"
