###### EXPLICAÇÃO GERAL:
#
# - Condições para ser uma classe abstrata:
#           - Deve herdar a classe ABC ou a metaclasse ABCMeta
#           - Ter pelo menos um método abstrato (ter o decorador @abstractmethod)
#           - Não podem ser instânciadas diretamente
#           - Não possui funções com corpo
#           - Devem ser implementados nas subclasses
#           - Em Python, elas tem como metaclasse a ABCMeta
#
# - São usadas quando:
#
#           - várias classes diferentes tem instâncias e métodos em comum. Evita repetição de código.
#           - Necessidade de assinatura.
#
# - Quando uma classe herda uma classe abstrata que contém métodos abstratos, é obrigatório fornecer implementações a todos eles.
#   Do contrário, a classe herdeira também será considerada uma classe abstrata e não poderá ser instânciada diretamente.
#
# - Para definir uma classe abstrata, é necessário importar a biblioteca 'abc' e usar '(ABC)' 
#   depois do nome da classe.
#
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass



# - É possível criar @property, @setter, @classmethod, @staticmethod e @method como abstratos. Para isso, coloca o decorador
#   @abstractmethod como o mais interno.
#
from abc import ABC, abstractmethod

class MinhaClasseAbstrata(ABC):
    def __init__(self, valor):
        self._valor = valor

    @property
    @abstractmethod
    def propriedade_abstrata(self):
        pass

    @propriedade_abstrata.setter
    @abstractmethod
    def propriedade_abstrata(self, novo_valor):
        pass

    @classmethod
    @abstractmethod
    def metodo_de_classe_abstrato(cls):
        pass

    @staticmethod
    @abstractmethod
    def metodo_estatico_abstrato():
        pass

    @abstractmethod
    def metodo_abstrato(self):
        pass

class MinhaSubclasse(MinhaClasseAbstrata):
    def __init__(self, valor):
        super().__init__(valor)

    @property
    def propriedade_abstrata(self):
        return self._valor

    @propriedade_abstrata.setter        
    def propriedade_abstrata(self, novo_valor):
        self._valor = novo_valor

    @classmethod
    def metodo_de_classe_abstrato(cls):
        print("Método de classe concreto")

    @staticmethod
    def metodo_estatico_abstrato():
        print("Método estático concreto")

    def metodo_abstrato(self):
        print("Método concreto")

obj = MinhaSubclasse(10)
print(obj.propriedade_abstrata)
obj.propriedade_abstrata = 20
print(obj.propriedade_abstrata)
MinhaSubclasse.metodo_de_classe_abstrato()
MinhaSubclasse.metodo_estatico_abstrato()
obj.metodo_abstrato()



# - Para definir uma classe abstrata, é necessário importar a biblioteca 'abc' e usar '(ABC)' 
#   depois do nome da classe.
#
from abc import ABC, abstractmethod
import math

class Shape(ABC):           # Classe abstrata
    @abstractmethod
    def area(self):
        pass



# - Classes abstratas ajudam no encapsulamento, sergurança e manutenção do código.
