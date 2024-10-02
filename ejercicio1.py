
class Rectangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def area(self):
        return print(f"El area del rectangulo es de: {self.base * self.altura}")

    def perimetro(self):
        return print(f"El perímetro del rectángulo es de: {(self.base + self.altura) * 2}")

rectangulo1 = Rectangulo(5, 3)
rectangulo1.area()
rectangulo1.perimetro()
