import json

CAMINHO = 'arquivo207.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome  = nome
        self.idade = idade

p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 11)
bd = [vars(p1), vars(p2), vars(p3)]

with open(CAMINHO, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)