def teste_args(arg, *args):
    print(f'Primeiro argumento: {arg}')
    for i in args:
        print(f'Outro argumento: {i}')

textos = ('python','é','para','doidos','e','malucos')

teste_args(*textos)

# O número arbitrário (*arg) só aceita lista e tuplas.
# Ele é usado quando não se sabe a quantidade de argumentos que serão passados.
# O asterisco (*) avisa a função que um argumento, que também usa o (*), terá varios valores.