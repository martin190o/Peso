personas = int(input("Ingrese el número de personas que serán registradas: "))

# Validar cantidad de personas
while personas <= 0:
    print("El número de personas debe ser un entero positivo.")
    personas = int(input("Ingrese el número de personas que serán registradas: "))


# Ciclo para registrar personas
while personas > 0:

    print("\nRegistro de persona")


    # VALIDAR NOMBRE
    while True:

        nombre = input("Ingrese su nombre: ")

        if nombre.strip() == "":
            print("No se ha ingresado un nombre válido.")

        elif len(nombre) >= 3 and nombre.isalpha():
            print("Nombre válido.")
            break

        else:
            print("Nombre no válido. Debe tener al menos 3 caracteres y solo contener letras.")


    # VALIDAR APELLIDO PATERNO
    while True:

        apellidopaterno = input("Ingrese su apellido paterno: ")

        if apellidopaterno.strip() == "":
            print("No se ha ingresado un apellido paterno válido.")

        elif len(apellidopaterno) >= 3 and apellidopaterno.isalpha():
            print("Apellido paterno válido.")
            break

        else:
            print("Apellido paterno no válido. Debe tener al menos 3 caracteres y solo contener letras.")


    # VALIDAR APELLIDO MATERNO
    while True:

        apellidomaterno = input("Ingrese su apellido materno: ")

        if apellidomaterno.strip() == "":
            print("No se ha ingresado un apellido materno válido.")

        elif len(apellidomaterno) >= 3 and apellidomaterno.isalpha():
            print("Apellido materno válido.")
            break

        else:
            print("Apellido materno no válido. Debe tener al menos 3 caracteres y solo contener letras.")


    # VALIDAR EDAD
    while True:

        edad = input("Ingrese su edad: ")

        if edad.strip() == "":
            print("No se ha ingresado una edad válida.")

        elif edad.isdigit() and 0 < int(edad) < 120:
            print("Edad válida.")
            break

        else:
            print("Edad no válida. Debe ser un número entero entre 1 y 119.")


    # VALIDAR PESO
    while True:

        peso = input("Ingrese su peso en kg: ")

        if peso.strip() == "":
            print("No se ha ingresado un peso válido.")

        elif peso.replace('.', '', 1).isdigit() and float(peso) > 0:
            print("Peso válido.")
            break

        else:
            print("Peso no válido. Debe ser un número positivo.")


    # VALIDAR ESTATURA
    while True:

        estatura = input("Ingrese su estatura en metros: ")

        if estatura.strip() == "":
            print("No se ha ingresado una estatura válida.")

        elif estatura.replace('.', '', 1).isdigit() and float(estatura) > 0:
            print("Estatura válida.")
            break

        else:
            print("Estatura no válida. Debe ser un número positivo.")


    # CALCULAR IMC
    IMC = float(peso) / (float(estatura) ** 2)

    if IMC >= 0 and IMC <= 15.99:
        print("Delgadez severa")

    elif IMC >= 16.00 and IMC <= 16.99:
        print("Delgadez moderada")

    elif IMC >= 17.00 and IMC <= 18.49:
        print("Delgadez leve")

    elif IMC >= 18.50 and IMC <= 24.99:
        print("Normal")

    elif IMC >= 25.00 and IMC <= 29.99:
        print("Sobrepeso")

    elif IMC >= 30.00 and IMC <= 34.99:
        print("Obesidad leve")

    elif IMC >= 35.00 and IMC <= 39.00:
        print("Obesidad media")

    elif IMC >= 40.00:
        print("Obesidad mórbida")


    # MOSTRAR DATOS
    print("\n--- DATOS DEL USUARIO ---")
    print(f"Nombre completo: {nombre} {apellidopaterno} {apellidomaterno}")
    print(f"Edad: {edad} años")
    print(f"Peso: {peso} kg")
    print(f"Estatura: {estatura} m")
    print(f"El IMC de {nombre} es: {IMC:.2f}")


    # Restar una persona registrada
    personas = personas - 1