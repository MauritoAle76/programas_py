usuarios = ({"nombre": "Juan"}, {"nombre": "Pedro"}, {"nombre": "Ana"})

# asigno variables globales
numero = int(input("ingrese el primer numero: "))
numero2 = int(input("ingrese el segundo numero: "))


# declaro funciones
def sumar(a, b):
    resultado = a + b  # estas variables son locales, viven solo dentro de la funcion
    resultado = resultado * 2
    resultado = resultado + 1
    print(resultado)
    return resultado


def multiplicar(a, b):
    multiplicar = a * b / 2
    return multiplicar


sumar = sumar(numero, numero2)
multiplicar = multiplicar(numero, numero2)

print(f"el resultado es, {sumar} pero si multiplico el resultado es: {multiplicar} ")

dic = {
    1: {"nombre": "Juan", "edad": 25},
    2: {"nombre": "Pedro", "edad": 30},
    3: {"nombre": "Ana", "edad": 20},
}

print(dic[1]["nombre"])
