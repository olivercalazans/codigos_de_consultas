# - A principal função do '__slots__' é otimizar o uso da memória RAM. Quando um instância
#   é criada, a classe cria um dicionário com todos os atributos. Os dicinários usam muita
#   memória, e com um grande número de objetos criados, a memória é usada excessivamente.
#   O '__slots__' reduz o uso do armazenamento alocando diretamente um espaço de memória
#   fixo para cada atributo especificado em __slots__.
# 
# - O valor fixo do slot é adaptavel. Ele cria um slot de valor fixo do mesmo tamanho do valor.
#   Se o valor for alterado, o slot será redimensionado para comportar o novo valor. Ele apenas
#   evita o uso excessivo de memória que os dicionários usam.
# 
# - O exemplo abaixo mostra a diferença do uso de memória ao usar e não usar o '__slots__'.

import sys

class PessoaSemSlots:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class PessoaComSlots:
    __slots__ = ['nome', 'idade']

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1_sem_slots = PessoaSemSlots('Alice', 30)
p2_sem_slots = PessoaSemSlots('Bob', 25)

p1_com_slots = PessoaComSlots('Alice', 30)
p2_com_slots = PessoaComSlots('Bob', 25)

print(sys.getsizeof(p1_sem_slots.__dict__))  # Tamanho do dicionário de p1_sem_slots
print(sys.getsizeof(p1_com_slots))           # Tamanho de p1_com_slots


# - Os nomes passados no '__slots__' não precisam ser iguais aos nomes dos atributos passados
#   no '__init__'. Mas é uma boa prática deixa-los iguais.
#
# - A quantidade de atributos passados no '__slots__' deve ser a mesma da qunatidade de parametros
#   passados no '__init__'. Se houver diferença, poderá ocorrer erros durante a execução.
#
# - A ordem de como são passados os atributos para o '__slots__' e os parametros para o '__init__'
#   não interfere e não causa erro. O que importa é a quantidade passada nos dois.
#
# - A alguns pontos a se considerar ao usar o '__slots__':
#
#   --> Imutabilidade:
#       O '__slots__' impede a criação de novos atributos dinamicamente. Para criar novos 
#       atributos, é necessário adicionar manualmente.  
#
#   --> Herança:
#       Se uma classe filha define __slots__, ela substitui os slots da classe pai,
#       a menos que você inclua todos os slots do pai na lista de slots da classe filha.
#
#   --> Depuração: 
#       O uso de __slots__ pode tornar a depuração mais complicada, pois os atributos
#       não aparecerão em listagens normais de dicionários de instância.
#
# - Apesar de não ser o proposito do '__slots__', ele pode auxiliar no encapsulamento e na proteção
#   dos dados, já que ele impede a criação novos atributos e acessa mais rapidamente os valores.