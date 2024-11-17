""" listas se encierran entre corchetes. los datos son string
"""

compras = [
    "Pan",
    "Mayonesa",
    "Arroz",
    "Mostaza",
    4,
]

print(compras[3])
print(compras)
compras[3] = (
    "yogur"  # solo puedo reemplazar  un elemento, pero no puedo agrandar la lista
)

print(compras[3])
print(compras)
# compras[4] = "Mostaza" #si la lista de de 4 lugares es decir de 0 a 3, no puedo agregar el 4 con esta sintaxis
compras.append("Mostaza")  # ahora si pude sumar un  elemento a la lista
print(compras[3])
print(compras)
print(len(compras))
compras.remove(
    "Pan"
)  # borra de la lista el primer pan que encuentra. Ojo detecta mayusculas o minusculas
print(compras[0])
print(compras)
print(f" la lista tiene {len(compras)} elementos")
print(type(compras[4]))

""" TUPLAS
A diferencia de las listas,... las tuplas no se pueden modificar
"""

compras_tupla = ("Milanesa", "Carne picada", "Huevo", "Sal", "Pimienta")

print(compras_tupla)

# compras_tupla[1] = "Carne molida"  # no se puede modificar una tupla

"""
Indice, tuplas y bucles

"""
# las listas y las tuplas se recorren por igual

indice = 0  # inicializo el valor del indice

while indice < len(
    compras
):  # le digo al  bucle que mientras el valor indice sea menor a la longitud de la lista. se ejecute
    print(
        f"Producto {indice + 1}: {compras[indice]}"
    )  # al inidice le suma 1 para que quede mas claro por que arranca de 0
    indice += 1  # incrementa el contador para poner fin al bucle
print("fin de bucle")

""" listas dentro de otras listas
"""
lista_dentro_de_otras_listas = [
    ["Pan", 3200, 40],
    ["Leche", 1200, 80],
    ["Manteca", 2500, 9],
]

# recorre la lista y genera una variable para que vaya asignando  el valor de cada elemento de la lista

print(len(lista_dentro_de_otras_listas))
indice_2 = 0

while indice_2 < len(lista_dentro_de_otras_listas):
    producto = lista_dentro_de_otras_listas[indice_2]
    print(f"Producto: {producto[0]}")
    print(f"Precio: {producto[1]}")
    print(f"Cantidad: {producto[2]}")
    print("-" * 30)
    indice_2 += 1
# para buscar un elemento dentro de una lista de lista el primer corchete se refiera a la lista
# y el segunro al indice de la lista
print(f" la lista dentro de la lista se busca asi {lista_dentro_de_otras_listas[0][1]}")
