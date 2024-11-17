"""

Consultar el stock de productos


Tu programa debe permitir al usuario consultar el inventario de una tienda para verificar si un producto está en stock. 
Si el producto está en la lista, el programa debe informarlo, si no, debe mostrar un mensaje indicando que no está disponible.

Tips: 

Usá una lista para almacenar los productos en stock.

Permití que el usuario ingrese el nombre de un producto a consultar.

Recorre la lista con un bucle while para verificar si el producto está en stock.

También pueden usar el método lista.index(elemento_a_buscar)

"""

# con el metodo index tengo limitaciones para buscar, por que no me busca en lista de lista
# ademas es sensible a Str o int.... asi que lo mejor es un for o un while para iterar la lista
# y  verificar si el producto esta en stock

lista_productos = [1, "YERBA", 89, 8]


elemento_a_buscar = input("ingrese el producto a consultar: ").upper()
indice_en_lista = lista_productos.index(elemento_a_buscar)
print(
    f" El producto {lista_productos[indice_en_lista]} tiene un stock  de {lista_productos[2]} unidades"
)

# como busco con index?
