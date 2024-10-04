
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