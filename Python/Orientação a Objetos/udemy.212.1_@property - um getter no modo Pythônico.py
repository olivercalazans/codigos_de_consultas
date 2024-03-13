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