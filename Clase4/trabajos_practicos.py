""" Clase 04 - Ejercicio 1

Ticket de la compra
Escribir un programa que solicite el nombre, la cantidad y el valor unitario de tres productos.

Luego, debe calcular el importe de IVA (21%) de cada producto.

Por último, debe mostrar en la terminal el ticket de la operación con todos los datos de la compra. 
"""

nombre_1 = None
nombre_2 = None
nombre_3 = None
cantidad_1 = None
cantidad_2 = None
cantidad_3 = None
valor_unitario_1 = None
valor_unitario_2 = None
valor_unitario_3 = None

iva_1 = None
iva_2 = None
iva_3 = None


# entrada

nombre_1 = input("Le solicitamos que ingrese el nombre del primer articulo: ")
cantidad_1 = float(input("Indique la cantidad:  "))
valor_unitario_1 = float(input("Indique el valor del producto: "))
iva_1 = float(input("Indique el porcentaje del iva. Por Ej 21 o 10,50:   "))

nombre_2 = input("Le solicitamos que ingrese el nombre del segundo articulo: ")
cantidad_2 = float(input("Indique la cantidad:  "))
valor_unitario_2 = float(input("Indique el valor del producto: "))
iva_2 = float(input("Indique el porcentaje del iva. Por Ej 21 o 10,50:   "))

nombre_3 = input("Le solicitamos que ingrese el nombre del tercer articulo: ")
cantidad_3 = float(input("Indique la cantidad:  "))
valor_unitario_3 = float(input("Indique el valor del producto: "))
iva_3 = float(input("Indique el porcentaje del iva. Por Ej 21 o 10,50:   "))

# # Proceso

calculo_1_vta = cantidad_1 * valor_unitario_1

calculo_2_vta = cantidad_2 * valor_unitario_2

calculo_3_vta = cantidad_3 * valor_unitario_3

importe_iva_1 = calculo_1_vta * iva_1 / 100
importe_iva_2 = calculo_2_vta * iva_2 / 100
importe_iva_3 = calculo_3_vta * iva_3 / 100

importe_total_1 = calculo_1_vta + importe_iva_1
importe_total_2 = calculo_2_vta + importe_iva_2
importe_total_3 = calculo_3_vta + importe_iva_3


importe_neto = calculo_1_vta + calculo_2_vta + calculo_3_vta

importe_iva_total = importe_iva_1 + importe_iva_2 + importe_iva_3

total_ticket = importe_neto + importe_iva_total

# salida
print()
print(
    f"Producto {nombre_1}  cantidad {cantidad_1} valor unitario {valor_unitario_1} iva {iva_1} % importe IVA {importe_iva_1} = total {importe_total_1}\n"
)
print(
    f"Producto {nombre_2}  cantidad {cantidad_2} valor unitario {valor_unitario_2} iva {iva_2}  % importe IVA {importe_iva_2} = total {importe_total_2}\n"
)
print(
    f"Producto {nombre_3}  cantidad {cantidad_3} valor unitario {valor_unitario_3:.2f} iva {iva_3}  % importe IVA {importe_iva_3} = total {importe_total_3}\n"
)
print()
print(f"IMPORTE NETO: $ {importe_neto:.2f}\n")

print(f"IVA TOTAL : $ {importe_iva_total:.2f}\n")

print(f"El importe total es $ {total_ticket:.2f}\n ")


""" Clase 04 - Ejercicio 2

Consumo de combustible
Realizar una aplicación en Python que;
A partir de la cantidad de litros de combustible que consume un coche por cada 100 km de recorrido, 
el costo de cada litro de combustible y la longitud del viaje realizado (en kilómetros), 
muestra un detalle de los litros consumidos y el dinero gastado.

"""
# Declarar variables

# autonomia_cada_100_km = None
# precio_por_lts_combust = None
# distancia_a_recorrer = None
# litros_consumidos = None
# importe_a_gastar = None

# # Entrada
# distancia_a_recorrer = int(input("Por favor igrese los km a recorrer: "))
# print()
# precio_por_lts_combust = float(
#     input("Porfavor indique el Precio del litro del combustible: ")
# )
# print()
# autonomia_cada_100_km = float(input("Cuanto combustible consume cada 100 km? "))
# print()

# # Proceso

# Calculo_consumo_en_lts = distancia_a_recorrer * autonomia_cada_100_km / 100
# calculo_en_pesos = Calculo_consumo_en_lts * precio_por_lts_combust

# # Salida

# print(
#     f"Usted va a consumir {Calculo_consumo_en_lts:.2f} lts de Combustible, esto nos da un imoprte de: $ {calculo_en_pesos:.2f}.-"
# )
# print()
