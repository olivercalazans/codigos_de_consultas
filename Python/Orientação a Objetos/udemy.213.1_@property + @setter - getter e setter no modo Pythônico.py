# - Em Python, os métodos não precisam do '_set' antes do nome.
# - E dois ou mais métodos podem ter o mesmo nome, desde que o decorador seja diferente.

class Caneta:
    def __init__(self, cor_inicial):
        self._cor = cor_inicial

    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, nova_cor):
        self._cor = nova_cor

# No exemplo acima, dois métodos tem o nome 'cor', mas o decorador de um é o @property e do outro
#   é o 'cor.setter'.
# É necessário que um dos métodos tenha o @property para que o outro possa receber '<nome>.setter'.
        


# - Também é possível usar o setter no __init__.
# - Pode ser uma boa prática em certas ocasiões.

class Caneta:
    def __init__(self, cor):
        self._cor = cor

    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, nova_cor):
        print('setter')
        self._cor = nova_cor

# - No exemplo acima o setter foi passada para o __init__.
# - Assim que a classe é iniciada, o valor é definido pelo setter.
        