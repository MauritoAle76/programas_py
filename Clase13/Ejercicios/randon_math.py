"""
Escribí un programa en Python que genere cinco códigos únicos de cinco dígitos
para usarlos como identificadores de productos en un inventario.
Para esto, utilizá el módulo random. Cada código generado debe ser diferente de los otros.

Tip: Podés usar random.randint() para generar números dentro de un rango determinado.

"""

import random

numero = random.randint(1, 100)

# set es para crear un conjunto, donde los valores no se pueden repetir
codigo = set()
# si se repite no llega a la longitud de 5 y el ciclo no se detiene
while len(codigo) < 5:
    # for numero_aleatoria in range(5):
    codigo_temporal = int(random.randint(1, 12))
    codigo.add(codigo_temporal)

print(codigo)


import math

numero_redondeo = math.floor(4.8)
numero_redondeo1 = round(4.65682789989787899, 2)
print(numero_redondeo1)


precios = []

while len(precios) < 10:
    precio_tem = round(float(random.uniform(10.00, 100.00)), 2)
    precios.append(precio_tem)

print(precios)
