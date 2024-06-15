##### FORMA ESTRUTURAL:  for <var> in <iterável>:
# |
# |- O for irá iterar todos os valore de um iterável (lista, tupla, dicionário**)
# |- Ele cria uma variável temporária que só pode ser usada dentro do laço.
# 
# Ex. 1:
print('Ex. 1: ', end='')
numeros = [1,2,3,4,5]
for i in numeros:
    print(i, end=', ')
#
print('\n')



##### FORMA ESTRUTURAL 2:  for <var> in range(<inicio>, <fim>, <salto>):
# |
# |- O for cria uma sequencia de números que poderá ser usada dentro do laço.
# |- A sequencia pode ser modificada. Onde começa e termina. Se haverá saltos ou não.
# |- O valor do saltos é o último parametro do 'range'.
# |- Dessa forma, é possível manipular vários iteráveis de uma vez.
# 
# Ex. 2.1:
print('\nEx. 2.1: ', end='')
#
for i in range(10):             # 'for' básico.
    print(i, end=', ')
#
#
# Ex. 2.2:
print('\nEx. 2.2: ', end='')
#
for i in range(5, 15):          # Escolhendo início e fim.
    print(i, end=', ')
#
#
# Ex. 2.3:
print('\nEx. 2.3: ', end='')
#
for i in range(-10, 10, 2):     # Escolhendo salto.
    print(i, end=', ')
#
print('\n')



##### FORMA ESTRUTURAL 3:  for <var_indice>, <var_valor> in enumerate(<iterável>):
# |
# |- A função 'enumerate' itera cada valor e seu indice(posição).
#
# Ex. 3:
print('\nEx. 3:')
nomes = ["Alice", "Bob", "Charlie"]
#
for indice, nome in enumerate(nomes):
    print(f"    - Índice: {indice}, Nome: {nome}")
#
print('\n')



##### FORMA ESTRUTURAL 4:  for <var_1>, <var_2>, ... in zip(<iterável_1>, iterável_2, ...):
# |
# |- A função 'zip' itera mais de um iterável por vez.
# |- O número de variáveis deve ser o mesmo número de iteráveis.
#
nomes = ['Alice', 'Bob', 'Charlie']
idades = [25, 30, 35]
salarios = [3000, 4000, 5000]
#
# Ex. 4.1:
print('Ex. 4.1:')
for nome, idade in zip(nomes, idades):
    print(f'    - {nome} tem {idade} anos.')
#
# Ex. 4.2:
print('Ex. 4.2:')
for nome, idade, salario in zip(nomes, idades, salarios):
    print(f'    - {nome} tem {idade} anos e recebe R${salario}.')



##### FORMA ESTRUTURAL 5:  for <var_chave>, <var_valor> in <iterador_do_dicionário>:
# |
# |- Existem 3 formas de iterar com dicionários: chave, valor, chave e valor.
#
meu_dict = {'a': 1, 'b': 2, 'c': 3}
#
# Ex. 5.1:
print('\nEx. 5.1: ', end='')
for chave in meu_dict:
    print(chave, end=', ')
#
# Ex. 5.2:
print('\nEx. 5.2: ', end='')
for valor in meu_dict.values():
    print(valor, end=', ')
#
# Ex. 5.3:
print('\nEx. 5.3:')
for chave, valor in meu_dict.items():
    print(f'    - Chave: {chave}, Valor: {valor}')

