nombre = input("Ingrese su nombre: ")
if nombre.strip() == "":
    print("No se ha ingresado un nombre válido.")
elif len(nombre) >=3 and nombre.isalpha():
    print("Nombre válido.")
else:
    print("Nombre no válido. Debe tener al menos 3 caracteres y solo contener letras.")