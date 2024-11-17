""" Imagina  que estás ayudando a una tienda de videojuegos a organizar su inventario.
El dueño te pide que escribas un programa que verifique si hay stock suficiente de un videojuego y
, si no hay, que avise que hay que reponerlo. 

El programa debería pedirle al usuario que ingrese la cantidad actual en stock y, 
en base a esa cantidad, mostrar si se necesita hacer un nuevo pedido o no.

"""

stock_art = int
video_nomb = str

# Entrada
# ingresar el stock

video_nomb = str(input("Ingrese el nombre del articulo:   "))
print()
stock_art = int(input("Ingrese el stock actual:   "))

# Proceso
if stock_art <= 5:
    print(f"El stock del articulo {video_nomb}, esta por debajo del stock de seguridad")
    print(f"El stock actual de de: {stock_art}")
    print(f"Realice un pedido al proveedor".upper())
else:
    print()
    print(f"Tenemos suficiente Stock de {video_nomb}, el stock es de: {stock_art}")
    print()

# Salida
