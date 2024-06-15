##### FORMA ESTRUTURAL: var = {chave: valor for <item> in range(<valores>)}
# |
# |- O 'dict comprehension' cria dicionários de forma mais concisa.
#
# Ex. 1:
pares = {x: x**2 for x in range(10) if x % 2 == 0}
print(f'Ex. 1: {pares}')



##### FORMA ESTRUTURAL:  var = {<chave>: (<valor>, <valor2>, ...) for <item>, <item2>, ... in zip(<iterável1>, <iterável2>, ...) }
# |
# |- Podem ser usadas iteráveis para formar 'dicionários'.
# |- O número de variáveis deve ser igual a de iteráveis, na mesma ordem.
# |- O PRIMEIRO VALOR SEMPRE SERÁ A CHAVE. OS OUTROS SERÃO SERÃO OS VALORES DA CHAVE.
#
nomes = ["Alice", "Bob", "Charlie"]
idades = [25, 30, 35]
salarios = [3000, 4000, 5000]
#
# Ex. 2.1:
dicionario = {nome: idade for nome, idade in zip(nomes, idades)}
print(f'Ex. 2.1: {dicionario}')
#
# Ex. 2.2:
dicionario = {nome: (idade, salario) for nome, idade, salario in zip(nomes, idades, salarios)}
print(f'Ex. 2.2: {dicionario}')
