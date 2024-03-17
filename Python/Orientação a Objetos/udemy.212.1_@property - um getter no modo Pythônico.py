# - O Python tem uma forma específica dele para criar um getter.
#
# - Com o @property, o metodo se comporta como atributo. Ele não usa as parenteses '()'.
#   Se usar os parenteses, ocorrerá um erro.
#
# - Além disso, ao usar o decorador @property, não é necessário usar 'get_' no nome da função.


class Caneta:
    def __init__(self, cor, cor_da_tampa='Transparente'):
        self._cor = cor
        self._cor_da_tampa = cor_da_tampa

    @property
    def cor(self):
        return self._cor
    
    @property
    def cor_Da_Tampa(self):
        return self._cor_da_tampa
    
caneta1 = Caneta('Azul')
caneta2 = Caneta('Vermelha')
caneta3 = Caneta('Preta')

print(caneta1.cor, caneta1.cor_Da_Tampa)
print(caneta2.cor, caneta2.cor_Da_Tampa)
print(caneta3.cor, caneta3.cor_Da_Tampa)

# No exemplo acima, a função 'cor' foi chamada como um atributo. Ela não usou os parentese '()'.



# - Em Python, é possível que dois ou mais métodos tenham o mesmo nome, o que vai diferenca eles é
#   o decorador.
# - Um decorador tem que ser o @property, o outro será '<nome_do_metodo>.getter'.

class Caneta:
    def __init__(self, cor_inicial):
        self._cor = cor_inicial

    @property
    def cor(self, nova_cor):
        self._cor = nova_cor
    
    @cor.getter
    def cor(self):
        return self._cor
    
# No exemplo acima, dois métodos tem o mesmo nome, mas eles tem decoradores diferentes.
# O método com o decorador @property é um setter. Ele já está definido.
# O que tem o decorador @cor.getter, ficou assim para que os métodos fosse diferentes.
