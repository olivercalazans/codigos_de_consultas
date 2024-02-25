def cria_conta(numero, titular, saldo, limite):
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta

def depositar(conta, valor):
    conta['saldo'] += valor

def saca(conta, valor):
    conta['saldo'] -= valor

def extrato(conta):
    print('Número: {}\nSaldo: {}'.format(conta['numero'], conta['saldo']))


conta = cria_conta('123-7', 'João', 500.0, 1000.0)
depositar(conta, 50.0)
extrato(conta)

saca(conta, 20)
extrato(conta)
