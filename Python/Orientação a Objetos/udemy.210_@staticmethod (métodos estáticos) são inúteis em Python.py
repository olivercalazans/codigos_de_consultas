# - Os métodos estáticos em Python não recebem 'self' ou 'cls'.
#
# - Ela pode ser usada na classe ou pelo objeto.
#
# - Geralmente são usadas para organizar o código ou para evitar problemas de herança.

class Classe:
    def __init__(self, tipo):
        self.tipo = tipo

    @staticmethod
    def funcao_estatica():
        print('iai')

c1 = Classe('teste')
c1.funcao_estatica()
Classe.funcao_estatica()