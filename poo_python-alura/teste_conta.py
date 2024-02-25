class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
      
conta = Conta()

conta.titular = 'João'
conta.saldo   = 120.0

print(conta.titular)
