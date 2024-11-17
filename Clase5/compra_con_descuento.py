"""Escribe un programa en Python que solicite al usuario el monto total de la compra y la cantidad de artículos 
que está comprando. El programa debe determinar el descuento aplicable según las siguientes reglas:
Si la cantidad de artículos comprados es mayor o igual a 5 y el monto total es mayor a $10000, 
aplica un descuento del 15%.
Si la cantidad de artículos comprados es menor a 5 pero mayor o igual a 3, aplica un descuento del 10%.
Si la cantidad de artículos comprados es menor a 3, no se aplica descuento.
Al final, el programa debe imprimir el monto total de la compra después de aplicar cualquier descuento o simplemente el monto original si no hay descuento.

"""

# variables
monto_compra = None
canti_art = None
descuento_en_pesos = None
# Entrada

monto_compra = float(input("Ingrese el importe en Pesos $:  "))
canti_art = int(input("ingrese la cantidad de articulos de la compra: "))


# Proceso

# Descuento a aplicar
if canti_art >= 5 and monto_compra > 10000:
    descuento_en_pesos = monto_compra - (monto_compra * (15 / 100))
    print(f" Usted tiene un descuento de un 15% sobre el total de la compra")
    print(f"El importe a abonar es de $ : {descuento_en_pesos} .-")
elif canti_art >= 3 and canti_art < 5 and monto_compra >= 0:
    descuento_en_pesos = monto_compra - (monto_compra * (10 / 100))
    print(f" Usted tiene un descuento de un 10% sobre el total de la compra")
    print(f"El importe a abonar es de $ : {descuento_en_pesos} .-")
else:
    print("Debe comprar mas de 3 articulos para obtener  un descuento")
    print(f"No se aplica descuento el monto a pagar es de $ {monto_compra}.-")
