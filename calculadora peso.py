# Solicita al usuario cuántas personas serán registradas
personas = int(input("Ingrese el número de personas que serán registradas: "))


# Valida que el número de personas sea mayor a 0
while personas <= 0:

    # Mensaje de error si el número es inválido
    print("El número de personas debe ser un entero positivo.")

    # Vuelve a pedir el número de personas
    personas = int(input("Ingrese el número de personas que serán registradas: "))


# Ciclo principal que se repetirá mientras haya personas por registrar
while personas > 0:

    # Imprime un título para separar registros
    print("\nRegistro de persona")


    # ---------------- VALIDACIÓN DEL NOMBRE ----------------

    # Ciclo infinito hasta que el nombre sea válido
    while True:

        # Solicita el nombre
        nombre = input("Ingrese su nombre: ")

        # Verifica si el campo está vacío
        if nombre.strip() == "":
            print("No se ha ingresado un nombre válido.")

        # Verifica que tenga mínimo 3 letras y solo letras
        elif len(nombre) >= 3 and nombre.isalpha():
            print("Nombre válido.")

            # Sale del ciclo porque el nombre es correcto
            break

        # Si no cumple las condiciones
        else:
            print("Nombre no válido. Debe tener al menos 3 caracteres y solo contener letras.")


    # ---------------- VALIDACIÓN DEL APELLIDO PATERNO ----------------

    while True:

        # Solicita apellido paterno
        apellidopaterno = input("Ingrese su apellido paterno: ")

        # Valida campo vacío
        if apellidopaterno.strip() == "":
            print("No se ha ingresado un apellido paterno válido.")

        # Verifica longitud y letras
        elif len(apellidopaterno) >= 3 and apellidopaterno.isalpha():
            print("Apellido paterno válido.")

            # Sale del ciclo
            break

        else:
            print("Apellido paterno no válido. Debe tener al menos 3 caracteres y solo contener letras.")


    # ---------------- VALIDACIÓN DEL APELLIDO MATERNO ----------------

    while True:

        # Solicita apellido materno
        apellidomaterno = input("Ingrese su apellido materno: ")

        # Valida vacío
        if apellidomaterno.strip() == "":
            print("No se ha ingresado un apellido materno válido.")

        # Verifica letras y longitud
        elif len(apellidomaterno) >= 3 and apellidomaterno.isalpha():
            print("Apellido materno válido.")

            # Sale del ciclo
            break

        else:
            print("Apellido materno no válido. Debe tener al menos 3 caracteres y solo contener letras.")


    # ---------------- VALIDACIÓN DE EDAD ----------------

    while True:

        # Solicita edad
        edad = input("Ingrese su edad: ")

        # Valida vacío
        if edad.strip() == "":
            print("No se ha ingresado una edad válida.")

        # Verifica que sea número y esté en rango válido
        elif edad.isdigit() and 0 < int(edad) < 120:
            print("Edad válida.")

            # Sale del ciclo
            break

        else:
            print("Edad no válida. Debe ser un número entero entre 1 y 119.")


    # ---------------- VALIDACIÓN DE PESO ----------------

    while True:

        # Solicita peso
        peso = input("Ingrese su peso en kg: ")

        # Valida vacío
        if peso.strip() == "":
            print("No se ha ingresado un peso válido.")

        # Verifica si es número decimal positivo
        elif peso.replace('.', '', 1).isdigit() and float(peso) > 0:
            print("Peso válido.")

            # Sale del ciclo
            break

        else:
            print("Peso no válido. Debe ser un número positivo.")


    # ---------------- VALIDACIÓN DE ESTATURA ----------------

    while True:

        # Solicita estatura
        estatura = input("Ingrese su estatura en metros: ")

        # Valida vacío
        if estatura.strip() == "":
            print("No se ha ingresado una estatura válida.")

        # Verifica si es decimal positivo
        elif estatura.replace('.', '', 1).isdigit() and float(estatura) > 0:
            print("Estatura válida.")

            # Sale del ciclo
            break

        else:
            print("Estatura no válida. Debe ser un número positivo.")


    # ---------------- CÁLCULO DEL IMC ----------------

    # Fórmula del IMC:
    # peso dividido entre estatura al cuadrado
    IMC = float(peso) / (float(estatura) ** 2)


    # ---------------- CLASIFICACIÓN DEL IMC ----------------

    # Evalúa el rango del IMC
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


    # ---------------- MOSTRAR RESULTADOS ----------------

    # Imprime encabezado
    print("\n--- DATOS DEL USUARIO ---")

    # Imprime nombre completo
    print(f"Nombre completo: {nombre} {apellidopaterno} {apellidomaterno}")

    # Imprime edad
    print(f"Edad: {edad} años")

    # Imprime peso
    print(f"Peso: {peso} kg")

    # Imprime estatura
    print(f"Estatura: {estatura} m")

    # Imprime IMC con 2 decimales
    print(f"El IMC de {nombre} es: {IMC:.2f}")


    # ---------------- CONTADOR ----------------

    # Resta una persona al contador
    personas = personas - 1