# Registro de Personas e IMC en Python

Proyecto realizado en Python que permite registrar múltiples personas mediante la terminal, validando los datos ingresados y calculando automáticamente el Índice de Masa Corporal (IMC).

## Descripción

El programa solicita al usuario la cantidad de personas que serán registradas.  
Posteriormente, para cada persona, pide:

- Nombre
- Apellido paterno
- Apellido materno
- Edad
- Peso
- Estatura

Todos los datos son validados para evitar entradas incorrectas o vacías.

Después de ingresar la información, el sistema calcula el IMC de la persona y muestra su clasificación correspondiente.

## Funciones del programa

- Validación de nombres y apellidos
- Validación de edad
- Validación de peso y estatura
- Cálculo automático del IMC
- Clasificación del IMC:
  - Delgadez severa
  - Delgadez moderada
  - Delgadez leve
  - Normal
  - Sobrepeso
  - Obesidad leve
  - Obesidad media
  - Obesidad mórbida

## Tecnologías utilizadas

- Python 3

## Cómo ejecutar el programa

1. Descargar o clonar el repositorio.
2. Abrir la terminal en la carpeta del proyecto.
3. Ejecutar el siguiente comando:

```bash
python nombre_del_archivo.py
```

## Ejemplo de uso

```text
Ingrese el número de personas que serán registradas: 1

Registro de persona
Ingrese su nombre: Martin
Nombre válido.

Ingrese su apellido paterno: Lopez
Apellido paterno válido.
```

## Autor

Proyecto realizado por Martin como práctica de programación en Python.