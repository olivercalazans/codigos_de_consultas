###### EXPLICAÇÃO GERAL:
#
# - Os modificadores do encapsulamento em Python são diferntes de outas linguagens.
# - Apesar de ser diferente, há uma convensção que ajuda a "usar" esses conceitos.
# - Os 3 conceitos são:
#           1° Public
#           2° Protected
#           3° Private

### PUBLIC:
#
# - O 'public' indica que o(s) atributo(s) pode(m) ser usado(s) em qualquer lugar.
#       - Pode ser usado dentro da classe;
#       - Pode ser usado em subclasses;
#       - Pode ser usado fora da classe.
#
# - Atributos públicos não usam underline '_', diferente dos protegidos e dos provados que usam esse
#   caracter para indicar que não são públicos.
#
class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor


### PROTECTED:
#
# - O 'protected' são os atributos são restritos.
#       - Pode ser usado dentro da classe;
#       - Pode ser usado em subclasses.
#       - Não pode ser usado fora da classe;
#
# - Atributos protegidos usam 1 underline '_' para indicar que eles são limitados, que devem ser protegidos.
#
class Carro:
    def __init__(self, modelo, cor):
        self._modelo = modelo
        self._cor = cor


### PRIVATE:
#
# - O 'private' são os atributos são mais restritos.
#       - Pode ser usado dentro da classe;
#       - Não pode ser usado em subclasses.
#       - Não pode ser usado fora da classe;
#
# - Atributos protegidos usam 2 underlines '_' para indicar que eles são privados.
# - Porém, ao usar 2 underlines, o Python tem um comportamento diferente. Mesmo ele sendo privado,
#   o Python não impede que ele seja acessado fora da classe. Mas, com os atributos privados, ele
#   modifica o nome do atributo. Assim, dificulta o acesso ao atributo.
# - A modificação ocorre da seguinte maneira:
#           - O Python adiciona o nome da classe antes do nome do atributo.
#           - Exemplo: '__<nome_do_atributo>' passa passa a ser '_<nome_da_classe>__<nome_do_atributo>'
#
# - Essa desconfiguração de nome não ocorre dentro da classe, apenas fora dela.
# - Então, dentro da classe, o nome normal do atributo pode ser usado.
#
class Carro:
    def __init__(self, modelo, cor):
        self.__modelo = modelo      # '__modelo' -> '_Carro__modelo'
        self.__cor = cor            # '__cor' -> '_Carro__cor'

    @property
    def retorno(self):
        return f'Modelo: {self.__modelo}, Cor: {self.__cor}'    # Dentro da classe, o nome é normal.
    
carro_1 = Carro('Uno', 'vermelho')
print(carro_1._Carro__modelo)       # Fora da classe, o nome tem que ser modificado.
