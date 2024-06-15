##### FORMA ESTRUTURAL:  var = lambda  <argumentos>: <expressão>
# |
# |- Uma expressão 'lambda' é uma maneira de criar funções anônimas (sem nome).
# |- Os argumentos são os valores que ela vai receber (variáveis).
# |- A expressão é o que a função vai fazer com o(s) argumento(s).
#
# Ex. 1:
funcao_lambda = lambda x: x ** 2
#
# Resultado:
var = funcao_lambda(3)
print(f'Ex. 1: {var}')
#
# Um 'lambda' faz a mesma coisa que a função abaixo.
def func_lambda (x):
    var = x ** 2
    return var



##### FORMA ESTRUTURAL 2:  var = map(lambda <argumento>: <expressão>, <iterável>)
# |
# |- O 'map' ira iterar uma lista/tupla/dicionário e o 'lambda' será aplicado a cada valor.
# |- Todos os valores do iterável serão alterados de acordo com a função do 'lambda'.
# |- O arquivo do 'map' dará mais detalhes de como usa-lo.
#
# Ex. 2:
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
#
# Resultado:
squared_numbers_list = list(squared_numbers)
print(f'Ex. 2: {squared_numbers_list}')



##### FORMA ESTRUTURAL 3:  var = filter(lambda <argumento>: <expressão>, <iterável>)
# |
# |- O 'filter' irá iterar uma lista/tupla/dicionário e o lambda será aplicado a cada valor.
# |- A condição determinada no 'lambda' irá manter os valores que retornarem 'True'.
# |- O arquivo do 'filter' dará mais detalhes de como usa-lo.
#
# Ex. 3:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
#
# Resultado:
even_numbers_list = list(even_numbers)
print(f'Ex. 3: {even_numbers_list}')




##### FORMA ESTRUTURAL 4:  var = sorted( <iterável>, key=lambda <argumento>: <expressão[posição ou chave]>)
# |
# |- O 'sorted' receberá um iterável de iteraveis (lista de listas, lista de dicionários, etc) e aplicará o lambda em
# |  um valor específico escolhido.
# |- O valor poder ser a posição, se for uma lista/tupla/etc, ou uma chave, se for um dicionário.
# |- PARA ORGANIZAR DE FORMA DECRESCENTE É NECESSÁRIO USAR 'reverse=True' ao final.
#
# Ex. 4:
people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]
sorted_people         = sorted(people, key=lambda x: x['age'])
sorted_people_reverse = sorted(people, key=lambda x: x['age'], reverse=True)
#
# Resultado:
print(f'Ex. 4.1: {sorted_people}')
print(f'Ex. 4.2: {sorted_people_reverse}')
