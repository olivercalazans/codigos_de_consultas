def teste_kwargs(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave} = {valor}')


dicionario = {'nome': 'oliver', 'idade': 24, 'sexo': 'masculino', 'hobby': 'ler'}

teste_kwargs(**dicionario)

# O argumento **kwargs recebe apenas dicionários.
# Ele recebe um dicionário inteiro e pode acessar todos os valores.
# Por acessar a chave e o valor, ele precisa ter duas variáveis. Como no FOR usado.
