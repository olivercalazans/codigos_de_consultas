# Os atributos de classe são variáveis que são definidas dentro da classe mas fora de qualquer método.
# Eles podem ser acessados pelos metodos ou por chamadas da classe.
# É possivel acessa-los usando o "self" mas não é recomendado. Melhor usar o nome da classe.

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

print(Pessoa.ANO_ATUAL)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
