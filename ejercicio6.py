
def fibonacci(n):
    list = [0, 1]
    for i in range(2, n):
        list.append(list[i-1] + list[i-2])

    return list

n = int(input("Ingrese el número de términos: "))
print("Secuencia de Fibonacci:")
print(*fibonacci(n), sep=", ")
