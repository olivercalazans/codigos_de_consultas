# - A principal função de um setter é fornecer um ponto centralizado para controlar como
#   os atributos de um objeto são modificados. Isso significa que, ao usar um setter, 
#   você pode adicionar lógica adicional para garantir que os valores atribuídos estejam
#   dentro de limites aceitáveis ou atendam a certos critérios de validação.

# - Alguns exemplos:
#       -> Verificar se o novo valor está dentro de um intervalo aceitável.
#       -> Converter o formato do valor (por exemplo, de uma string para um tipo numérico).
#       -> Executar uma ação específica sempre que o valor for modificado (por exemplo, atualizar um registro em um banco de dados).
#       -> Disparar notificações ou eventos relacionados à modificação do valor.

# - Mas a função primária do setter é modificar o valor de um atributo.
# - Mesmo nos exemplos acima, os valores são modificados. Pode ocorrer a apenas a modificação
#   ou uma lógica pode estar no escopo dela.
# - Ele é fundamental no princípio do encapsulamento.
# - Usar setter ajuda a evitar a quebra do código do cliente.

# EXEMPLO 1: MODIFICADOR DE VALOR.
class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    def set_nome(self, novo_nome):
        if isinstance(novo_nome, str):
            self._nome = novo_nome
        else:
            raise ValueError("O nome deve ser uma string.")

    def get_nome(self):
        return self._nome


pessoa = Pessoa("João")
print(pessoa.get_nome())  # Saída: João

pessoa.set_nome("Maria")
print(pessoa.get_nome())  # Saída: Maria

pessoa.set_nome(123)  # Isso gera um ValueError

# Neste exemplo, set_nome() é o setter para o atributo _nome da classe Pessoa. 
# Ele verifica se o novo nome passado como argumento é uma string e, se não for, lança um erro.
# Isso garante que apenas valores válidos sejam atribuídos ao atributo _nome. 



# EXEMPLO 2: VERIFICAÇÃO DE VALOR PARA PODER ALTERAR.
class Retângulo:
    def __init__(self, largura, altura):
        self._largura = largura
        self._altura = altura
    
    def set_largura(self, largura):
        if largura > 0:
            self._largura = largura
        else:
            raise ValueError("A largura deve ser maior que zero.")

    def set_altura(self, altura):
        if altura > 0:
            self._altura = altura
        else:
            raise ValueError("A altura deve ser maior que zero.")

# Neste exemplo, os setters set_largura() e set_altura() validam se os novos valores para
# largura e altura são maiores que zero. Se não forem, eles levantam um erro.
        


# EXEMPLO 3: REALIZANDO CÁLCULO ESPECÍFICO
class Círculo:
    def __init__(self, raio):
        self._raio = raio
        self._circunferência = 2 * 3.14 * raio
    
    def set_raio(self, raio):
        self._raio = raio
        self._circunferência = 2 * 3.14 * raio

    def get_circunferencia(self):
        return self._circunferência

# Neste exemplo, sempre que o raio de um círculo é modificado, a circunferência
# é recalculada e atualizada internamente.



# EXEMPLO 4: ATUALIZANDO ATRIBUTOS RELACIONADOS
class Produto:
    def __init__(self, preço, quantidade):
        self._preço = preço
        self._quantidade = quantidade
        self._total = preço * quantidade
    
    def set_preço(self, preço):
        self._preço = preço
        self._total = preço * self._quantidade

    def set_quantidade(self, quantidade):
        self._quantidade = quantidade
        self._total = self._preço * quantidade

    def get_total(self):
        return self._total

# Neste exemplo, sempre que o preço ou a quantidade de um produto é modificada,
# o total é recalculado e atualizado internamente.
