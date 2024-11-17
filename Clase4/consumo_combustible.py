""" Clase 04 - Ejercicio 2

Consumo de combustible
Realizar una aplicación en Python que;
A partir de la cantidad de litros de combustible que consume un coche por cada 100 km de recorrido, 
el costo de cada litro de combustible y la longitud del viaje realizado (en kilómetros), 
muestra un detalle de los litros consumidos y el dinero gastado.

"""

# Declarar variables

autonomia_cada_100_km = None
precio_por_lts_combust = None
distancia_a_recorrer = None
litros_consumidos = None
importe_a_gastar = None

# Entrada
while True:
    print()
    distancia_a_recorrer = int(input("Por favor ingrese los km a recorrer: "))

    ida_y_vuelta = input("¿Es un viaje de ida y vuelta? (s/n): ").lower()

    autonomia_cada_100_km = float(input("Cuanto combustible consume cada 100 km? "))

    precio_por_lts_combust = float(
        input("Porfavor indique el Precio del litro del combustible: ")
    )

    # Proceso

    if ida_y_vuelta == "s":
        distancia_a_recorrer = distancia_a_recorrer * 2

    Calculo_consumo_en_lts = distancia_a_recorrer * autonomia_cada_100_km / 100

    calculo_en_pesos = Calculo_consumo_en_lts * precio_por_lts_combust

    # Salida

    print(
        f"Usted va a consumir {Calculo_consumo_en_lts:.2f} lts de Combustible, esto nos da un imoprte de: $ {calculo_en_pesos:.2f}.-"
    )
    print()

    opcion = input(
        "ingrese x para salir o cualquier tecla para volver a calcular "
    ).lower()
    if opcion == "x":
        break
