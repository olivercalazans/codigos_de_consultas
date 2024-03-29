# - Um mixin é uma classe projetada apenas para hospedar um conjunto de métodos que podem ser 
#   herdados por outras classes. Ao contrário da herança tradicional, onde a classe base define
#   a estrutura e o comportamento das classes derivadas, os mixins focam em fornecer recursos
#   adicionais que podem ser combinados com várias classes.
#
# - Vantagens dos mixins:
#
#    - Promovem a reutilização de código e evitam a duplicação.
#    - Permitem a composição de funcionalidades de forma flexível.
#    - Podem ser mais fáceis de entender do que a herança múltipla complexa.
#
# - Desvantagens dos mixins
#
#    - Podem levar a conflitos de nomes de métodos se não forem usados corretamente.
#    - Podem tornar a hierarquia de classes confusa se muitos mixins forem usados.
#    - Podem adicionar complexidade desnecessária se a herança simples for suficiente.

# Mixin para adicionar funcionalidade de voar
class FlyingMixin:
    def fly(self):
        print("Estou voando!")

# Mixin para adicionar funcionalidade de nadar
class SwimmingMixin:
    def swim(self):
        print("Estou nadando!")

# Classe base para animais
class Animal:
    def speak(self):
        pass

# Classe para pássaros que podem voar
class Bird(Animal, FlyingMixin):
    def speak(self):
        print("Piu piu!")

# Classe para peixes que podem nadar
class Fish(Animal, SwimmingMixin):
    def speak(self):
        print("Glub glub!")

# Classe para pássaro aquático que pode voar e nadar
class Duck(Bird, SwimmingMixin):
    def speak(self):
        print("Quack quack!")

# Criando instâncias e testando funcionalidades
bird = Bird()
fish = Fish()
duck = Duck()

bird.fly()  # Saída: Estou voando!
fish.swim()  # Saída: Estou nadando!
duck.fly()  # Saída: Estou voando!
duck.swim()  # Saída: Estou nadando!
