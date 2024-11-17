"""
En un comercio, se necesita gestionar los productos y sus precios. Desarrollá un programa que permita:
Ingresar el nombre de tres productos y su precio correspondiente, 
guardándolos en un diccionario donde la clave es el nombre del producto y el valor es su precio.
Una vez ingresados, mostrará todos los productos y sus precios en pantalla
"""

inventario = {}
print()
for p in range(3):
    producto = input("Ingrese nombbre del prodcuto: ").upper()
    precio = float(input("Ingrese precio del producto: "))
    inventario[producto] = precio
print()
print("~" * 30)


for producto, precio in inventario.items():

    print(f"Producto : {producto} cantidad : {precio}")
print("~" * 30)
