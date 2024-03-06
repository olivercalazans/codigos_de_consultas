lista = [12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52]

# a) maior elemento
maximo = max(lista)

# b) menor elemento
minimo = min(lista)

# c) números pares
pares = [i for i in lista if i % 2 == 0]

# d) repetições do primeiro número
repeticoes = [1 for i in lista if i == lista[0]]

# e) média dos elementos
media = sum(lista) / len(lista)

# f) soma dos valores negativos
soma = sum([i for i in lista if i < 0])


print(f'Número máximo.....: {maximo}')
print(f'Número mínimo.....: {minimo}')
print(f'Número pares......: {pares}')
print(f'Repetições........: {repeticoes}')
print(f'Média.............: {media:.3f}')
print(f'Soma dos negativos: {soma}')
