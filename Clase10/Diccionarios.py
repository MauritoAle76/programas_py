""" # creo un diccionario entre {}

productos_en_diccionarios = {"manzana": 30, "pera": 25, "naranja": 20}

print(type(productos_en_diccionarios))

print(productos_en_diccionarios)  # imprime el contenido del diccionario


# accedo a un valor del diccionario mediante su clave entre {}
# hay que respetar la syntasis de las listas, tuplas para imprimir

print(f"accedo a un produto del diccionario: {productos_en_diccionarios["pera"]}")

# pero si no lleva string el print la syntasys es asi:
print(productos_en_diccionarios["manzana"])

# metodo get()
# busca por la clave y devuelve el valor, si no existe devuelve None
print(productos_en_diccionarios.get("pera"))
print(productos_en_diccionarios.get("arroz"))
# si no se usa get y el valor no esta en el diccionario, se lanza un error
# print(productos_en_diccionarios["arroz"])

# para agregar o crear

productos_en_diccionarios["uva"] = 25  # agrego uva al final de la lista

print(productos_en_diccionarios)

# para modificar el valor asociado a una clave
productos_en_diccionarios["pera"] = 35  # cambio el valor de la pera
print(productos_en_diccionarios)

# para borrar se usa el comando del

del productos_en_diccionarios["naranja"]
print(f"Elimino con del {productos_en_diccionarios}")

# tambien se borrar con el comando pop()

borro_con_pop = productos_en_diccionarios.pop("manzana", "no hay ARROZ")
print(f"borro con pop : {borro_con_pop}")
print(f" haber como quedo : {productos_en_diccionarios}")
# recorrer el diccionario    con metodos
# 1. items() Devuelve una lista de tuplas con las claves y los valores del diccionario
for producto, cantidad in productos_en_diccionarios.items():
    print(f"Producto : {producto} cantidad : {cantidad}")

print(productos_en_diccionarios.items())  # imprime la lista de tuplas

# 2. keys() #imprine solo la clave
for producto in productos_en_diccionarios.keys():
    print(f"devuelve la clave: {producto}")

# 3. values()
for cantidad in productos_en_diccionarios.values():
    print(f"devuelve la cantidad: {cantidad}")

# que pasa si recorro sin metodo, da error

# for produ, canti in productos_en_diccionarios:
#   print(f"devuelve la clave: {produ} cantidad: {canti}")
producto = "uva"

if producto in productos_en_diccionarios:
    print(f"El stock del producto {producto} es {productos_en_diccionarios[producto]}")

# TypeError: dict.items() takes no arguments (1 given)?
dic_para_borrar = {"a": 1, "b": 2, "c": 3}
print(dic_para_borrar)
dic_para_borrar.clear()
print(dic_para_borrar)
dic_para_borrar = {"rojo": 5, "azul": 90}
print(dic_para_borrar)  # imprime el diccionario
del dic_para_borrar  # si no asigno nada entre corchete , se borra el diccionario
# |rint(dic_para_borrar) # no queda ni siquiera vacio la diferencia de clear


# ejercio de ventas diarias y acumular ventas
inventario = {"manzanas": 50, "peras": 40, "bananas": 89}
ventas_dia = {}

# se pide tres produstos
for _ in range(3):
    produ = input("Ingrese la producto vendido: ")
    canti = int(input("Ingrese la cantidad vendida: "))
    # verificamos que tenga stock
    if produ in inventario:
        ventas_dia[produ] = canti
    else:
        print("no tenemos ese producto en stock")

print(ventas_dia)
print(inventario)
"""

# diccionario de diccionarios

dic = {
    1: {"nombre": "Juan", "edad": 25},
    2: {"nombre": "Pedro", "edad": 30},
    3: {"nombre": "Ana", "edad": 20},
}

print(dic[1]["nombre"])

dic[4] = {"nombre": "Jose", "edad": 25}

print(dic)
