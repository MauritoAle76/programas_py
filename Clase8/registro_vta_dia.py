"""
Desarrollá un programa que permita registrar las ventas diarias de un comercio durante 5 días.
Al finalizar, el sistema debe mostrar el total de ventas realizadas en cada día y el promedio de ventas.

Tips: 
Usá un bucle while que permita al usuario ingresar el monto de las ventas diarias.
Asegurate de validar que el monto ingresado sea un valor positivo.
Usá un acumulador para la suma de las ventas.
"""

dias_venta = 0
lista = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado")
total_ventas = 0

# la condicion del ciclo e un len para que varie segun los dias de la lista
while dias_venta < len(lista):

    monto_vta_dia = float(input(f"Ingrese la venta del dia  {lista[dias_venta]} :$  "))
    if monto_vta_dia >= 0:
        total_ventas += monto_vta_dia
        dias_venta += 1
    else:
        print("NO SE ADMITEN NUMEROS NEGATIVOS")
# print(dias_venta)
# los print se incorporan variables para que sean dinamicos a los cambios de la tupla o de la variable
print(f"Las ventas acumuladas  en los {len(lista)} dias son: ${total_ventas:.2f}")
print(f"El promedio de las ventas es $ {total_ventas/(dias_venta):.2f}.")
