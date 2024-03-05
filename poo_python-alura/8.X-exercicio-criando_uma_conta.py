import datetime


class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome      = nome
        self.sobrenome = sobrenome
        self.cpf       = cpf
        

class Conta:
    def __init__(self, numero, cliente, saldo, limite=1000.0):
        self.numero  = numero
        self.titular = cliente
        self.saldo   = saldo
        self.limite  = limite
        self.historico = Historico()

    def depositar(self, valor):
        self.saldo += valor
        print('\nValor depositado.')
        self.historico.transacoes.append(f'Deposito de {valor}')

    def sacar(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
            print('\nSaque bem sucedido.')
            self.historico.transacoes.append(f'Saque de {valor}')
        else:
            print('\nO valor excede o saldo disponível.')

    def extrato(self):
        print(f'\nTitular: {self.titular}\nNúmero: {self.numero}\nSaldo: {self.saldo}\nLimite: {self.limite}')

    def transfere(self, destino, valor):
        if self.saldo > valor:
            self.saldo -= valor
            destino.saldo += valor
            print('\nValor transferido com sucesso.')
            self.historico.transacoes.append(f'Transferencia de {valor} para {destino}')
        else:
            print('\nNão foi possível transferir. Saldo insuficiente.')


class Historico:
    def __init__(self):
        self.data_abretura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print(f'Data de abertura: {self.data_abretura}')
        print('Transações: ')
        for i in self.transacoes:
            print(f'    - {i}\n')


cliente1 = Cliente('João', 'Ferreira', '12345678912')
cliente2 = Cliente('José', 'Azevedo', '12345678901')

conta1 = Conta('123-4', cliente1, 500.0)
conta2 = Conta('456-7', cliente2, 600.0, 300.0)

conta1.depositar(100)
conta1.sacar(50)
conta1.transfere(conta2,100)
conta1.extrato()

conta1.historico.imprime()
