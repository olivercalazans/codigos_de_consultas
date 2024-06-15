###### EXPLICAÇÃO GERAL:
#
# - O "__dict__" e o "vars" são formas de acessar todos os atributos declarados no "__init__".
# - Eles retornam uma dicionário com chaves e valores de acordo como foram declarados.
# - Porém, o "__dict__" pode ser usado para criar, modificar e apagar dados do objeto.
#

class Pessoa:
    ANO_ATUAL = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ANO_ATUAL - self.idade
        # return self.ano_atual - self.idade
    

p1 = Pessoa('Oliver', 24)
p2 = Pessoa('Kenya', 18)

print(p1.__dict__)
print(vars(p2))

p1.__dict__['idade'] = 100
del p1.__dict__['nome']
p1.__dict__['sobrenome'] = 'calazans'
print(p1.__dict__)
