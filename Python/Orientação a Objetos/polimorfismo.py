###### EXPLICAÇÃO GERAL:
#
# - Polimorfismo é um dos princípios fundamentais da programação orientada a objetos (POO)
#   que permite que objetos de diferentes tipos sejam tratados de maneira uniforme.
#
# - Em python, há dois tipos de polimorfismo:
#       - Polimorfismo de métodos.
#       - Polimorfismo de sobrecarga de operador


#### POLIMORFISMO DE MÉTODOS
#
# - É um conceito que permite que métodos com o mesmo nome se comportem de maneira diferente em classes
#   diferentes. Em Python, esse tipo de polimorfismo é alcançado através da sobreposição de métodos,
#   onde uma classe filha implementa um método com o mesmo nome e assinatura (lista de parâmetros)
#   que um método na classe pai.
#
## Chamada polimórfica:
#
# - A chamada polimórfica é a capacidade de chamar um método de um objeto sem se preocupar com a
#   classe específica do objeto. Pois quando o objeto é criado, o método será implementado no objeto
#   da forma que ele foi implementado na classe, mesmo o método tendo o nome igual a o método da
#   classe pai ou tendo sido modificado para se adaptar a classe.
#
## Sobreposição de Métodos:
#
# - Em Python, uma classe filha pode substituir (ou sobrescrever) um método definido em sua classe pai,
#   fornecendo uma implementação diferente para o mesmo método. Isso permite que diferentes classes
#   compartilhem o mesmo nome de método, mas executem diferentes ações com base no tipo do objeto.
#
class Animal:
    def som(self):
        print("Som genérico de animal.")

class Cachorro(Animal):
    def som(self):
        print("Au Au!")

class Gato(Animal):
    def som(self):
        print("Miau!")

cachorro = Cachorro()
gato = Gato()

cachorro.som()  # Saída: Au Au!
gato.som()      # Saída: Miau!
#
## Métodos abstratos
#
# - Métodos abstratos são métodos definidos em uma classe base, mas que não possuem implementação.
#   Em vez disso, eles fornecem apenas uma assinatura, especificando os parâmetros que o método
#   recebe e o que ele retorna. A implementação real do método é deixada para as classes derivadas,
#   que devem fornecer sua própria implementação para esse método.
#
# - Existem duas formas: Usando o 'abc' e manualmente.
#
# Exemplo com o 'abc' (Abstract Base Classes)
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return 3.14 * self.raio ** 2

formas = [Retangulo(5, 4), Circulo(3)]

for forma in formas:
    print("Área da forma:", forma.calcular_area())
#
# Manualmente
#
class Forma:
    def calcular_area(self):
        raise NotImplementedError("Método abstrato, deve ser implementado por subclasses")

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return 3.14 * self.raio ** 2

formas = [Retangulo(5, 4), Circulo(3)]

for forma in formas:
    print("Área da forma:", forma.calcular_area())
