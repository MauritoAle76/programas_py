"""Desarrollá un programa que permita calcular el promedio de ventas de la tienda. Para esto:

Creá una función que reciba como parámetro una lista de ventas diarias y
devuelva el promedio de esas ventas.
Solicitá a la persona que ingrese las ventas de cada día durante una semana (7 días).
Usá la función para calcular y mostrar el promedio de ventas al finalizar.

"""


def calcular_promedio_ventas(total_ventas):
    promedio = sum(total_ventas) / len(total_ventas)
    return promedio


dias_venta = 0
lista = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")
total_ventas = []


# la condicion del ciclo e un len para que varie segun los dias de la lista

while dias_venta < len(lista):

    monto_vta_dia = float(input(f"Ingrese la venta del dia  {lista[dias_venta]} :$  "))
    if monto_vta_dia >= 0:
        venta_dia = monto_vta_dia
        total_ventas.append(venta_dia)
        dias_venta += 1
    else:
        print("NO SE ADMITEN NUMEROS NEGATIVOS")


print(total_ventas)
print("El promedio de ventas es: ", calcular_promedio_ventas(total_ventas))
