
class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b) -> float:
        if b == 0:
            return "No se puede dividir por cero."
        else:
            return a / b

calculadora = Calculadora()
print(calculadora.sumar(5, 20))
print(calculadora.restar(100, 20))
print(calculadora.multiplicar(5, 4))
print(calculadora.dividir(5, 5))