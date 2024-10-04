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
