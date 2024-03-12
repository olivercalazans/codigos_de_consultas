# - Metodos de classe são funções definidas dento de uma classe.
#
# - Métodos de classe em Python operam principalmente em variáveis de classe (compartilhadas por todas as instâncias da classe)
#   e não em atributos de instância (específicos de cada objeto). 
#
# - Esses metodos podem ser chamados na própria classe e podem acessar e modificar atributos da classe.
#
# - Para alterar atributos de instância, ele pode alterar uma variável de classe e usar ela para alterar
#   um atributo de instância.
#
# - O primeiro argumento de um método de classe é o 'cls', a própria classe. Ele não recebe o 'self'.
# - Elas são úteis quando:
#   |
#   |- Métodos de fábrica: Cria instâncias de uma classe de uma maneira específica que pode não envolver
#   |  diretamente a criação do objeto.
#   |- Métodos utilitários: Quando você deseja ter métodos que operam em atributos da classe, 
#   |  independentemente de instâncias específicas.
#   |- Métodos que lidam com a classe em si: Quando você precisa executar operações na classe,
#      como alterar variáveis de classe compartilhadas ou realizar ações que afetam todas as instâncias da classe.
#
# - Os metodos de classe podem ser usados mesmo sem um objeto criado.

class Pessoa:
    ano = 2024 # atributo de classe.

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):  # Recebe 'cls', a própria classe.
        Pessoa.ano += 1

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)
    

p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa('Anônima', 23)
p4 = Pessoa.criar_sem_nome(25)
Pessoa.metodo_de_classe()

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)
print(Pessoa.ano)