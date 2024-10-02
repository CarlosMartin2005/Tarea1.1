# Descripción:
# Escribe una función llamada es_primo(n) que reciba un número entero y devuelva
# True si el número es primo o False en caso contrario.
# Instrucciones:
# 1. Implementa la función es_primo(n).
# 2. Pide al usuario que ingrese un número entero.
# 3. Utiliza la función para determinar si el número es primo.
# 4. Muestre un mensaje indicando si el número es primo o no.
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

entero = int(input("Ingrese un número entero: "))
if es_primo(entero):
    print(f"{entero} es un número primo.")
else:
    print(f"{entero} no es un número primo.")