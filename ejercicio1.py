# Descripción:
# Cree una clase llamada Rectangulo que represente un rectángulo. La clase debe
# tener los siguientes atributos:
# • base (float)
# • altura (float)
# Y los siguientes métodos:
# • area(): Calcula y devuelve el área del rectángulo.
# • perimetro(): Calcula y devuelve el perímetro del rectángulo.
# Instrucciones:
# 1. Define la clase Rectangulo con el constructor __init__ que inicialice base y
# altura.
# 2. Implementa los métodos area y perimetro.
# 3. Cree una instancia de Rectangulo con base 5 y altura 3.
# 4. Muestre el área y el perímetro del rectángulo.

class Rectangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return print(f"El area del rectangulo es de: {self.base * self.altura}")

    def perimetro(self) -> float:
        return print(f"El perímetro del rectángulo es de: {(self.base + self.altura) * 2}")

rectangulo1 = Rectangulo(5, 3)
rectangulo1.area()
rectangulo1.perimetro()