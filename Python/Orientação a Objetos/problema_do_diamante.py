###### EXPLICAÇÃO GERAL:
#
# - O "problema do diamante" em Python refere-se a uma situação em que uma classe herda de duas
#   classes que têm uma classe base em comum. Isso pode levar a ambiguidades e conflitos de
#   métodos e atributos.
#
class A:
    def quem_sou_eu(self):
        print("Classe A")

class B(A):
    def quem_sou_eu(self):
        print("Classe B")

class C(A):
    def quem_sou_eu(self):
        print("Classe C")

class D(B, C):
    pass

objeto_d = D()
objeto_d.quem_sou_eu()
#
# - Para resolver esse problema, o Python segue a ordem de resolução de método (MRO). O MRO
#   determina a ordem na qual as classes pai são pesquisadas para encontrar métodos e atributos.
#
print(D.__mro__)
#
# - No entanto, se você deseja especificar explicitamente qual implementação de método usar,
#   você pode chamar o método da classe desejada diretamente
#
B.quem_sou_eu(objeto_d)  # Saída: Classe B
C.quem_sou_eu(objeto_d)  # Saída: Classe C
#
# - Usar o método 'super()' vários erros, incluindo o problema do dimante. O método 'super()' sabe
#   como lidar de forma inteligente com heranças múltiplas.
#
class A:
    def quem_sou_eu(self):
        print("Classe A")

class B(A):
    def quem_sou_eu(self):
        super().quem_sou_eu()
        print("Classe B")

class C(A):
    def quem_sou_eu(self):
        super().quem_sou_eu()
        print("Classe C")

class D(B, C):
    def quem_sou_eu(self):
        super().quem_sou_eu()
        print("Classe D")

objeto_d = D()
objeto_d.quem_sou_eu()


