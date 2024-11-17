"""
Desarrollá un programa que permita al usuario ingresar el nombre de varios productos y
la cantidad en stock que hay de cada uno. El programa debe seguir pidiendo que ingrese productos 
hasta que el usuario decida salir, ingresando "salir" como nombre de producto.
Después de que el bucle termine, el programa debe mostrar la cantidad total de productos ingresados.

Tips: 
Vas a necesitar un contador.
Tené presente las estructuras condicionales
"""

lista_articulo_nombre = []
lista_articulo_nombre.clear()
articulo_cantidad = 0
totalizador_de_cantidad = 0

while True:
    articulo_nombre = str(
        input("Ingrese el nombre del articulo, o salir para terminar:  ").upper()
    )
    lista_articulo_nombre.append(articulo_nombre)
    if articulo_nombre == "SALIR":
        lista_articulo_nombre.remove("SALIR")
        break
    else:
        articulo_cantidad = int(input("ingrese la cantidad: "))
        lista_articulo_nombre.append(articulo_cantidad)
        totalizador_de_cantidad += articulo_cantidad

print(f"La cantidad de articulos ingresados de de : {totalizador_de_cantidad}\n")
print(
    f"Los articulos ingresados al inventerio son los siguientes: {lista_articulo_nombre}\n"
)
