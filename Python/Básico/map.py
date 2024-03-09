##### FORMA ESTRUTURAL:  var = map(<função>, <iterável>)
# |
# |- O 'map' irá interar todos os valores de um iterável (lista, dicionário, etc) e irá passar para uma função.
# |- Por usar funções simples, geralmente usa-se o 'lambda'. Mas uma função 'def' pode ser usada.
# |- O 'map' faz a "mesma coisa" que um laço 'for'. Porém, ele é mais limitado.
#
# Ex. 1:
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
#
#Resultado:
squared_numbers = list(squared_numbers)
print(f'Ex. 1: {squared_numbers}')




##### FORMA ESTRUTURAL 2:  var = map(lambda <argumento 1>, <argumento 2>, ... : <expressão>, <iterável 1>, <iterável 2>, ...)
# |
# |- É possível iterar mais de um iterável de uma vez.
# |- O número de argumentos deve ser igual ao número de iteráveis.
# |- Caso a quantiade de valores nas listas sejam diferentes, atribui-se um valor predefinido para evitar erros.
# |- Para predefinir um valor usar a seguinte forma 'argumento=valor_predefinido'
#
# Ex. 2.1:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = map(lambda x, y: x + y, list1, list2)
#
# Resultado:
result = list(result)
print(f'Ex. 2.1: {result}')
#
# Ex. 2.2:
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30]
result = map(lambda x, y=0: x + y, list1, list2)
#
# Resultado:
result = list(result)
print(f'Ex. 2.2: {result}')
#
# Ex. 2.3:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
result = map(lambda x, y, z: x + y + z, list1, list2, list3)
#
# Resultado
result = list(result)
print(f'Ex. 2.3: {result}')



##### FORMA ESTRUTURAL 3:  var = map(<def>, <iterável 1>, <iterável 2>, ...)
# |
# |- Quando é usada uma função 'def', informa o nome da função sem os parenteses.
# |- Os argumentos que serão usados pela função 'def' deverão ser declarados depois.
#
# Ex. 3:
def sum_lists(x, y, z):
    return x + y + z
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
result = map(sum_lists, list1, list2, list3)
#
# Resultado
result = list(result)
print(f'Ex. 3: {result}')



##### FORMA ESTRUTURAL 4:  var = map(<função>, <iterável>)
# |
# |- Ela também pode ser usada para mudar o tipo de valores (inteiros para strings, string para inteiros, etc).
#
# Ex. 4.1:
string_numbers = ["1", "2", "3", "4", "5"]
int_numbers = map(int, string_numbers)
#
# Resultado:
int_numbers = list(int_numbers)
print(f'Ex. 4.1: {int_numbers}')
#
# Ex. 4.2:
str_numbers = map(str, int_numbers)
#
# Resultado:
str_numbers = list(str_numbers)
print(f'Ex. 4.2: {str_numbers}')