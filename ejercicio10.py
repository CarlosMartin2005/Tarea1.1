import random
import string

def generar_contrasena(lngt):
    # Definir los caracteres que se pueden usar en la contraseña
    mayusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = "!@#$%^&*(),.?\":{}|<>"

    # Asegurarse de que la contraseña tenga al menos un caracter de cada tipo 
    # tomando un caracter aleatorio de cada tipo
    contrasena = [
        random.choice(mayusculas),
        random.choice(minusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]

    # Combinar los caracteres en una lista
    caracteres = mayusculas + minusculas + numeros + simbolos

    # De esa lista, elegir caracteres aleatorios para completar la contraseña
    # Se restan 4 caracteres porque ya se eligieron los 4 caracteres obligatorios
    # k es la cantidad de caracteres a elegir, si no se pone k=, se elige 1 sin importar el valor de lngt
    contrasena += random.choices(caracteres, k=lngt-4)

    # Mezclar la contraseña, que es una lista de caracteres
    random.shuffle(contrasena)

    # Convertir la lista de caracteres en una cadena
    # Se usa '' para unir los caracteres sin separador
    return ''.join(contrasena)

try:
    longitud = int(input("Ingrese la longitud de la contraseña (mínimo 8 caracteres): "))
    if longitud < 8:
        raise ValueError("La longitud de la contraseña debe ser al menos 8 caracteres")
    print("Contraseña generada:", generar_contrasena(longitud))
except ValueError as e:
    print(e)
