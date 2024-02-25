class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def depositar(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor

    def extrato(self):
        print(f'Titular: {self.titular}\nNúmero: {self.numero}\nSaldo: {self.saldo}\nLimite: {self.limite}')

    def transfere(self, destino, valor):
        self.saldo -= valor
        destino.saldo += valor


c1 = Conta('123-7', 'João', 500.0, 1000.0)
c1.extrato()
