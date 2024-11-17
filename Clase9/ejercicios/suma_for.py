"""
Desarrollá una función que calcule la suma de los números naturales hasta un número dado utilizando un bucle for.
La suma de los números naturales hasta el número n se define como la suma de todos los números enteros positivos
desde 1 hasta n.

Por ejemplo, la suma de los números naturales hasta 6 es 1 + 2 + 3 + 4 + 5 + 6 = 21.

La función debe recibir un número entero n y devolver la suma de los números naturales hasta n.



Tips: 

¡Usá range()!
"""

STAR = 1
que_numero = int(input("Ingrese un numero entero positivo: "))
print("~" * 40)
suma = 0
for numero in range(STAR, que_numero + 1):

    suma = numero + suma

print("")
print("-" * 40)
print("La suma de los numeros es :", suma)
print("-" * 40)
print("")
