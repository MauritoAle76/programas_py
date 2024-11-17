# comandos \n hace lienas. \t tabula

print("azucar\narroz")

print("probado")


nombre = "Mauro"

edad = 48

ciudad = "Cañuelas"


print(f"Me llamo {nombre}, tengo {edad} y soy de la cuidad de {ciudad}")
print(
    "probando 2 Me llamo ",
    nombre,
    "tengo ",
    edad,
    " y son de la ciuddad ",
    ciudad,
)
print(
    "probando 3 Me llamo {nombr}, tengo {ed} y soy de la cuidad de {ciudad} ".format(
        nombr=nombre, ed=edad, ciudad=ciudad
    )
)
print()  # otra manera de escribir un print sin f-string pudee ser un signo + o una coma
print(
    "me llamamo " + nombre, "  tengo " + str(edad) + " y soy de la cuidad de " + ciudad
)


