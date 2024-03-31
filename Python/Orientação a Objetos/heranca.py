###### EXPLICAÇÃO GERAL:
#
# - Para evitar a repetição de códigos, POO tem o conceito de herança. A herança é o uso de uma classe 
#   existente dentro de outra. Com isso, todos os atributos e métodos da classe pai podem
#   ser usados na classe filho (herdeira).
#
# - Uma antagem da herança é que podem ser criadas extenções nas novas classes reutilisando os
#   os atributos e métodos da classe pai sem ter que reescreve-los.
#
# - Porém, há algumas coisas que precisam ser feitas:
#
#   --> Usando atributos da classe pai na herdeira, versão 1:
#       - Se não fizer dessa maneira, os atributos serão sobrescritos.
#
#       - SINTAXE: <nome_da_classe_pai>.__init__(self, <atributo_pai1>, <atributo_pai2>, ...).
#
class ClasseA:                  
    def __init__(self, x):    
        self.x = x

class ClasseB:
    def __init__(self, y):
        self.y = y

class ClasseC:
    def __init__(self, x, y):
        # Chamando o __init__() de ClasseA e ClasseB
        ClasseA.__init__(self, x)
        ClasseB.__init__(self, y)

        # Outras inicializações específicas de ClasseC
        self.z = self.x + self.y

objeto_c = ClasseC(10, 20)
print(objeto_c.x)  # Saída: 10
print(objeto_c.y)  # Saída: 20
print(objeto_c.z)  # Saída: 30


#   --> Usando atributos da classe pai na herdeira, versão 2:
#       - Uma outra forma de acessar o python é usando a função 'super()'. Ela faz a mesma coisa da forma
#         declarada anteriormente, mas usar essa função é recomendada pois ela é menos propensa a erros.
#       
#       - OBS: CASO O HERDIERO TENHA MAIS DE UM PAI, E ELES TENHA ATRIBUTOS COM O MESMO NOME, O PYTHON
#              IRA USAR O ALGORITIMO C3 PARA DETERMINAR DE QUAL PAI ELA IRÁ USAR O ATRIBUTO.
#              PARA VER A ORDEM USAR: __mro__ OU O MÉTODO mro().
#
#       - SINTAXE: super().__init__(self, <atributo_pai1>, ...)
#
class Pai:
    def __init__(self, nome_pai):
        self.nome_pai = nome_pai

class Filha(Pai):
    def __init__(self, nome_pai, nome_filha):
        super().__init__(nome_pai)  # Chamando o __init__() da classe pai
        self.nome_filha = nome_filha

# Criando um objeto da classe Filha
objeto_filha = Filha("João", "Maria")

# Atributos da classe Pai
print(objeto_filha.nome_pai)  # Saída: "João"

# Atributos da classe Filha
print(objeto_filha.nome_filha)  # Saída: "Maria"


#   --> Usando métodos da classe pai na herdeira:
#       - Chamar métodos da classe pai é parecido com a forma que chamamos os atrbutos.
#         Assim como mostra o exemplo abaixo.
#
class Pai:
    def metodo_pai(self):
        print("Método da classe pai")

class Filha(Pai):
    def metodo_filha(self):
        print("Método da classe filha")

# Criando uma instância da classe Filha
objeto_filha = Filha()

# Chamando um método da classe filha
objeto_filha.metodo_filha()  # Saída: "Método da classe filha"

# Chamando um método da classe pai
objeto_filha.metodo_pai()  # Saída: "Método da classe pai"


#   --> Modificando métodos da classe pai na herdeira:
#       - As vezes, é necessário modificar um método da classe pai para poder usar na herdeira.
#         então é possível sobreescrever o método na classe filha. Assim, o nome do método continua
#         o mesmo, mas seu escopo pode ser diferente. O MÉTODO MODIFICADO SÓ FUNCIONA NA CLASSE DE
#         QUEM A MODIFICOU. O MÉTODO DO PAI CONTINUA O MESMO.
#
class Pai:
    def metodo(self):
        print("Método da classe pai")

class Filha(Pai):
    def metodo(self):
        print("Método da classe filha, completamente diferente da classe pai")

# Criando uma instância da classe Filha
objeto_filha = Filha()

# Chamando o método da classe filha
objeto_filha.metodo()  # Saída: "Método da classe filha, completamente diferente da classe pai"


#   --> Criando extensão sem alterar o método da classe pai:
#       - É possível criar uma extensão para um método da classe pai sem alterar o método chamado.
#         Com essa abordagem, o método pai fará seu trabalho e o método do herdeiro poderá usar o 
#         resultado para fazer modificações para gerar um resultado diferente.
#
#       - SINTAXE: super().<nome_do_metodo>()
#
#       - OBS: SE OS NOMES DOS ATRIBUTOS FOREM DIFERENTES ENTRE A CLASSE PAI E FILHO, PODERÁ HAVER ERRO.
#
class Matematica1:
    def __init__(self, base_maior, base_menor):
        self.base_maior = base_maior
        self.base_menor = base_menor

    def adicao(self):
        return self.base_maior + self.base_menor
    
class Matematica2(Matematica1):
    def __init__(self, base_maior, base_menor, altura):
        super().__init__(base_maior, base_menor)
        self.altura = altura

    def area_do_trapezio(self):
        soma = super().adicao()     # Não é necessário passar arguntos. O método pai já tem.
        resultado = (soma * self.altura) / 2
        return resultado
    
calculo = Matematica2(3, 2, 2)
print(calculo.area_do_trapezio())
