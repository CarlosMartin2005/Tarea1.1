
class CuentaBancaria:
    def __init__(self, titular: str):
        self.titular = titular
        self.saldo = 0

    def depositar(self, cantidad: float):
        if cantidad < 0:
            return "No se puede depositar una cantidad negativa."
        else:
            self.saldo += cantidad
        return self.saldo

    def retirar(self, cantidad: float):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            return self.saldo
        else:
            return "Fondos insuficientes."

    def mostrar_saldo(self):
        return print(f"El saldo actual es de: {self.saldo}")

cuentaAhorro = CuentaBancaria("Carlos Peña")
print(cuentaAhorro.depositar(100))
cuentaAhorro.mostrar_saldo()
print(cuentaAhorro.retirar(50))
cuentaAhorro.mostrar_saldo()
