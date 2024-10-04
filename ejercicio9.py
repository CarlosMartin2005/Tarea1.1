# Ejercicio 9: Adivina el Número
# Descripción:
# Cree un programa que genere un número aleatorio entre 1 y 100, y permita al usuario
# adivinar el número. El programa debe indicar si el número ingresado es mayor o
# menor al número generado hasta que el usuario lo adivine.
# Instrucciones:
# 1. Utiliza el módulo random para generar el número aleatorio.
# 2. Cree un ciclo que permita al usuario seguir intentando.
# 3. Muestre mensajes indicando si el número a adivinar es mayor o menor.
# 4. Felicita al usuario cuando adivine el número y Muestre el número de intentos
# realizados.
# Ejemplo de salida:
# ¡Adivina el número entre 1 y 100!
# Ingresa tu intento: 50
# El número es mayor.
# Ingresa tu intento: 75
# El número es menor.
# Ingresa tu intento: 62
# ¡Felicitaciones! Has adivinado el número en 3 intentos.
import random

x = random.randint(1, 100)
cont = 0

print("¡Adivina el número entre 1 y 100!")

while True:
    cont += 1
    intento = int(input("Ingresa tu intento: "))
    if intento > x:
        print("El número es menor.")
    elif intento < x:
        print("El número es mayor.")
    else:
        print(f"¡Felicitaciones! Has adivinado el número en {cont} intentos.")
        break
