productos = {"manzana": 30, "pera": 25, "banana": 20}


productos["manzana"] = 60


productos["Naranjas"] = 25

print(productos.get("manzanas"))  # cuando no lo encuentra da none
print(f"EL producto  tiene en estock {productos.get("manzana", "no existe")}")
# cuando no lo encuentra da el mensaje que le pongo
print(productos.get("manzana"))  # cuando lo encuentra da el valor


print(productos)
