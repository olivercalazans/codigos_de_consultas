import sys

class Pessoa:
    def __init__(self, idade):
        self.__idade = idade

p1 =Pessoa(20)

print('Teste 1:\n')
try:
    p1.__idade += 20
    print(p1.__idade)
except:
    print(sys.exc_info())

# --> Para impedir que os atributos sejam acessados de fora da classe é necessário usar um modificador
#     de acesso. Em python, esse modificador é o underline/underscore duplo "(__)".

print('\nTeste 2:\n')
p1._Pessoa__idade += 20
print(p1._Pessoa__idade)

# --> Porém, isso não impede que o atributo seja acessado, pois o Python apenas renomeia o atributo.
#     O que antes era "__idade" passou a ser "_Pessoa__idade". Ele coloca o nome da classe junto
#     do atributo.
# --> Ao reescrever o atributo, como usado acima, é possivel acessar-lo.

print('\nTeste 3:\n')
print(dir(p1))

# --> Por não ficar realmente protegido, os programadores usam apenas um underline/underscore "(_)"
#     para indicar que aquele atributi deve ser protegido.
# --> Mas para o Python, apenas um underline/underscore não tem efeito. O atributo fica normal.
# --> Com apenas um, o atributo é chamado de protegid. Ele apenas sinaliza que é perigoso usa-lo.