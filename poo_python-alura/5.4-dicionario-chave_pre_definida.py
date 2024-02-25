lista1 = ['abacaxi','uva','pera','maça',23,11,2.4,21.56,12,34,21,1.4,'pato',True]

dic = {'float':list(),'int':list(),'bool':list(),'str':list()}

for i in lista1:
    if type(i) == float: dic['float'].append(i)
    elif type(i) == int: dic['int'].append(i)
    elif type(i) == bool: dic['bool'].append(i)
    elif type(i) == str: dic['str'].append(i)

print(dic['float'])
print(dic['int'])
print(dic['bool'])
print(dic['str'])


# É possível criar dicionários com chaves definidas
# Cada chave pode ter apenas um valor, porém, esse valor pode ser uma lista, string, etc.
