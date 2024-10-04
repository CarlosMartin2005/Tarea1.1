# Escribe una función llamada fibonacci(n) que imprima los primeros n números de la
# secuencia de Fibonacci.
# Instrucciones:
# 1. Implementa la función fibonacci(n).
# 2. Pide al usuario que ingrese el valor de n.
# 3. Llama a la función para mostrar la secuencia.
# Ejemplo de salida:
# Ingrese el número de términos: 7
# Secuencia de Fibonacci:
# 0, 1, 1, 2, 3, 5, 8

def fibonacci(n):
    list = [0, 1]
    for i in range(2, n):
        list.append(list[i-1] + list[i-2])

    return list

n = int(input("Ingrese el número de términos: "))
print("Secuencia de Fibonacci:")
print(*fibonacci(n), sep=", ")

# Output:
# Ingrese el número de términos: 7
# Secuencia de Fibonacci:
# 0, 1, 1, 2, 3, 5, 8