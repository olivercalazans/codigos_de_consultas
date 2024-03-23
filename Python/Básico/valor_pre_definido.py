# - Em Python, é possível definir valores padrão para os parâmetros de uma função. Isso é conhecido como
#   "predefinição de valores" ou "valores padrão de parâmetros". Essa técnica permite que você defina valores
#   padrão para os parâmetros de uma função, de modo que se um argumento correspondente não for fornecido ao chamar
#   a função, o valor padrão será utilizado.

# - Ela pode ser usada em funções, classes e lambdas.


# FUNÇÃO
def saudacao(nome, mensagem="Olá"):
    print(f"{mensagem}, {nome}!")

# CLASSE
class Pessoa:
    def __init__(self, nome, idade=0):
        self.nome = nome
        self.idade = idade

# LAMBDA
soma = lambda x, y=0: x + y