##### FORMA ESTRUTURAL..: lista = [var <código>]
# |
# |- A lista será criada e armazenada na variável 'lista'.
# |- Está subentendido que 'var' na verdade é 'lista.append(var)'
# |- Obrigatóriamente um 'for' precisa ser usado.
#
# Ex. 1:
squares = [x**2 for x in range(10)]
#
# Resultado:
print(f'Ex. 1: {squares}')



##### FORMA ESTRUTURAL 2: lista = [var  if<condição>  for<condição> ]
# |
# |- O 'if' deve ser usado antes do 'for'.
# 
# Ex. 2:
numbers = [1, 2, 3, 4, 5, 6]
result = ["par" if num % 2 == 0 else "ímpar" for num in numbers]
#
# Resultado:
print(f'Ex. 2: {result}')



##### FORMA ESTRUTURAL 3: lista = [var.1  if.1  else  var.2  if.2]
# |
# |- É possível usar mais de um 'if'.
# |- Por não ser possível usar o 'elif', usa-se else entre os 'if'.
#
# Ex. 3:
numbers = [1, 2, 3, 4, 5, 6]
result = ["par" if num % 2 == 0 else "ímpar" if num % 2 != 0 else "múltiplo de 3" for num in numbers]
#
# Resultado:
print(f'Ex. 3: {result}')



##### FORMA ESTRUTURAL 4: lista = [var  for<condição>  for<condição>]
# |
# |- Para usar mais de um 'for', usa-se um depois do outro.
#
# Ex. 4:
coordenadas = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
#
#  Resultado:
print(f'Ex. 4: {coordenadas}')



##### FORMA ESTRUTURAL 5: lista = [ [ <list comprehension> ]  <list comprehension> ]
# |
# |- É possível usar uma list comprehension dentro de outra.
#
#  Ex. 5:
matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
matrix2 = [[row[i] for row in matrix] for i in range(4)]
#
#  Resultado:
print(f'Ex. 3: {matrix2}')
#
# OBS.: o matrix2 faz a mesm acoisa que o código abaixo.
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

