"""
Gestion de descuentos

Imaginá que en tu tienda querés implementar un sistema de descuentos automáticos.
Vas a desarrollar un programa que permita calcular el precio final de un producto
después de aplicar un descuento. Para hacerlo:

Crea una función que reciba como parámetros el precio original del producto y 
el porcentaje de descuento, y que retorne el precio final con el descuento aplicado.
Luego, pedí que se ingrese el precio y el porcentaje de descuento. 
Mostrá el precio final después de aplicar el descuento.

"""

# variables Globales

precio_original = 0
porcentaje_descuento = 0


def ingreso_precio():
    precio_original = float(input("Ingrese el precio sin descuentos: $ "))
    return precio_original


def ingreso_porcentaje():
    porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: % "))
    return porcentaje_descuento


# Definir la función que calculará el precio final con descuento
def calcular_descuento(a, b):
    if precio_original > 0 and porcentaje_descuento > 0:
        descuento = (porcentaje_descuento / 100) * precio_original
        precio_final = precio_original - descuento
        return precio_final


# codigo a ejecutar
# si los numero es 0 o negativo, no se puede calcular el descuento y da un mensaje de error

precio_original = ingreso_precio()
porcentaje_descuento = ingreso_porcentaje()


if precio_original > 0 and porcentaje_descuento > 0:
    precio_con_descuento_final = calcular_descuento(
        precio_original, porcentaje_descuento
    )
    print(f"Precio con descuento: ${precio_con_descuento_final:.2f}")
else:
    print(
        "Error: El precio original y el porcentaje de descuento deben ser números positivos"
    )
