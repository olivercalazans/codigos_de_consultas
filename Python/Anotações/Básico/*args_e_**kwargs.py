### Em Python, *args é um parâmetro especial que pode ser usado em definições de funções para permitir um número
#   variável de argumentos posicionais. O termo args é apenas uma convenção de nomeação; o que o torna especia é o 
#   asterisco (*) antes dele. Esse parâmetro coleta todos os argumentos posicionais passados para a função em uma tupla.
#
# - Pode ser usado para chamadas de funções.
# - Pode ser usado em funções, lambdas e classes.


def somar(*args):
    total = 0
    for numero in args:
        total += numero
    return total

print(somar(1, 2, 3))  # Saída: 6
print(somar(1, 2, 3, 4, 5))  # Saída: 15

# CHAMADAS DE FUNÇÕES -------------------------------------
valores = (1, 2, 3)
print(somar(*valores))  # Saída: 6

# LAMBDA --------------------------------------------------
funcao = lambda *args: sum(args)
print(funcao(1, 2, 3, 4))  # Saída: 10

# CLASSE --------------------------------------------------
class Exemplo:
    def __init__(self, *args):
        self.args = args

    def imprimir_args(self):
        print(self.args)

objeto = Exemplo(1, 2, 3, 4)
objeto.imprimir_args()  # Saída: (1, 2, 3, 4)



print('\n----------------------------------------------\n')



### Em Python, **kwargs é outro parâmetro especial que pode ser usado em definições de funções para permitir um
#   número variável de argumentos nomeados. Assim como *args, o termo kwargs é uma convenção de nomeação, sendo
#   o duplo asterisco (**) o que o torna especial. Esse parâmetro coleta todos os argumentos nomeados passados
#   para a função em um dicionário, onde as chaves são os nomes dos argumentos e os valores são os valores passados.
#
# - Pode ser usado para chamadas de funções.
# - Pode ser usado em funções, lambdas e classes.
#
# OBS.: Quando você passa um dicionário de argumentos nomeados (**kwargs) para uma função, os pares chave-valor
#       são desempacotados e passados como argumentos nomeados para a função. Na chamada da função, as variáveis 
#       são atribuídas na mesma ordem que os argumentos da função, desde que os nomes das chaves no dicionário 
#       correspondam aos nomes dos parâmetros na definição da função. Isso também pode ser feito em métodos.

def minha_funcao(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

minha_funcao(nome="Alice", idade=30, cidade="São Paulo")
# Saída:
# nome: Alice
# idade: 30
# cidade: São Paulo

# CHAMDA DE FUNÇÃO ----------------------------------------
# EXEMPLO DA 'OBS'.
def minha_funcao(nome, idade):
    print(f"Nome: {nome}, Idade: {idade}")

dados = {"nome": "Alice", "idade": 30}
minha_funcao(**dados)

# LAMBDA --------------------------------------------------
funcao = lambda **kwargs: kwargs["nome"] if "nome" in kwargs else "Nome não fornecido"
print(funcao(nome="Maria"))  # Saída: Maria

# CLASSE 1: DADOS EM UMA ÚNICA INSTÂNCIA --------------------------------------------------
class MinhaClasse:
    def __init__(self, **kwargs):
        self.dados = kwargs

    def imprimir_dados(self):
        for chave, valor in self.dados.items():
            print(f"{chave}: {valor}")

objeto = MinhaClasse(nome="Carlos", idade=25, cidade="São Paulo")
objeto.imprimir_dados()

# CLASSE 2: DADOS EM INSTÂNCIAS SEPARADAS -------------------------------------------------
# EXEMPLO DA 'OBS'.
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Dicionário de argumentos nomeados
dados = {"nome": "Alice", "idade": 30}

# Desempacotando os argumentos nomeados para inicializar uma instância de Pessoa
pessoa = Pessoa(**dados)

# Acessando os atributos da instância
print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}")
