# # definir variables
# sueldoEnero, sueldoFebrero = 1500, 28900
# # sueldoFebrero = 28900
# sueldoMarzo = 86930
# sueldoAbril = 9853
# sueldoMayo = 98683
# sueldoJunio = 1000


# # calcular promedios

# promedioPrimeroSeisMeses = int(
#     (sueldoEnero + sueldoFebrero + sueldoMarzo + sueldoAbril + sueldoMayo + sueldoJunio)
#     / 6
# )

# print(
#     "El ingreso promedio en el semestre es de" "",
#     promedioPrimeroSeisMeses,
#     "" "Pesos donde" "",
#     promedioPrimeroSeisMeses,
#     "es el valor calculado",
# )

# # segundo desafio usando el imput

# eneroManual = int(input("ingrese el sueldo del mes de enero" " "))
# febreroManual = int(input("ingrese el sueldo del mes de febrero" " "))
# marzoManual = int(input("ingrese el sueldo del mes de marzo" " "))
# abrilManual = int(input("ingrese el sueldo del mes de abril" " "))
# mayoManual = int(input("ingrese el sueldo del mes de mayo" " "))
# junioManual = int(input("ingrese el sueldo del mes de junio" " "))

# promedioSeisMesesManual = int(
#     (eneroManual + febreroManual + marzoManual + abrilManual + mayoManual + junioManual)
#     / 6
# )

# print("El ingreso promedio en el semestre es de" "", promedioSeisMesesManual, "pesos")


# vamos a hacer este ejercicio usando listas

meses_del_año = [
    ["enero", 0],
    ["febrero", 0],
    ["marzo", 0],
    ["abril", 0],
    ["mayo", 0],
    ["junio", 0],
]
acumulador_de_sueldos = 0

indice = 0
while indice < len(meses_del_año):
    sueldo = float(input(f"ingrese el sueldo del mes de {meses_del_año[indice][0]} "))
    acumulador_de_sueldos = acumulador_de_sueldos + sueldo
    # de esta manera suma el valor de la variable sueldo en la poscion 1
    # si lo hago si meses_del_año = meses_del_año[indice][1] agrega una lista el mes
    # queda en 0 y el valor con el sueldo

    meses_del_año[indice][1] = meses_del_año[indice][1] + sueldo
    
    indice += 1

# vamos a buscar el sueldo mas alto de la lista
# el for no funciona bien, con el mes una vez tiro febrero y despues siempre junio

# sueldo_mas_alto = meses_del_año[0][1]
# mes_max = meses_del_año[0][0]

# for mes, sueldo in meses_del_año:
#     if sueldo > sueldo_mas_alto:
#         sueldo_mas_alto = sueldo
#         mes_max = mes

# probemos con whie

indice_1 = 0
sueldo_mas_alto = meses_del_año[0][1]
mes_max = meses_del_año[0][0]

while indice_1 < len(meses_del_año):

    if meses_del_año[indice_1][1] > sueldo_mas_alto:

        sueldo_mas_alto = meses_del_año[indice_1][1]
        mes_max = meses_del_año[indice_1][0]

    indice_1 += 1


print("*" * 30)
print(
    f"El sueldo mas alto para el alguinado fue el mes de {mes_max}  con un valor de $ {sueldo_mas_alto}"
)

print("*" * 30)
print(f"Su aguinaldo es de $ {sueldo_mas_alto / 2:.2f}")
print("-" * 30)


print(f"El acumulado de sueldos es de {acumulador_de_sueldos} pesos")
print(
    f"El promedio de los {len(meses_del_año)} meses es de {acumulador_de_sueldos/len(meses_del_año)}"
)
# queremos que nos diga que mes fue el mas alto para calcular el aguinaldo?
