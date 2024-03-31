###### EXPLICAÇÃO GERAL:
#
# - É um método que é usado para obter o valor de um atributo privado de uma classe.
#   É uma forma de controlar os dados de saída da classe.
#
# - É uma forma de implementar o conceito de encapsulamento, permitindo o acesso
#   controlado aos dados de um objeto.
#
# - A necessidade de um getter surge quando você quer restringir o acesso direto 
#   aos atributos de uma classe.
#
# - Também ajuda a evitar quebra de código do cliente. Por exemplo: Se um atributo no código do
#   da classe tiver seu nome alterado, é necessário alterar no código do cliente. Isso é quebra de código.
#   Porém, com um getter isso não acontece pois o atributo não é acessado diretamente.

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._velocidade = 0  # Atributo privado que armazena a velocidade

    def get_velocidade(self):
        return self._velocidade

    def acelerar(self, valor):
        self._velocidade += valor

# Criando uma instância de Carro
meu_carro = Carro("Toyota", "Corolla")

# Usando o método getter para obter a velocidade atual
print("Velocidade atual:", meu_carro.get_velocidade())

# Acelerando o carro
meu_carro.acelerar(50)

# Usando o método getter novamente para obter a velocidade atual
print("Velocidade atual:", meu_carro.get_velocidade())


# - Neste exemplo, _velocidade é um atributo privado que armazena a velocidade do carro.
#   O método get_velocidade() é um getter que retorna o valor atual da velocidade.
#   Ao usar este método, estamos acessando indiretamente o valor do atributo _velocidade,
#   em vez de acessá-lo diretamente. Isso ajuda a manter o controle sobre o acesso aos dados
#   internos da classe.
