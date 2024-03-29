# - Classes abstratas são classes que não podem ser instanciada, não criam objetos, mas servem de base
#   para subclasses usarem.
# 
# - São usadas quando várias classes diferentes tem instancias e métodos em comum. Então, para evitar
#   a repetição de código, uma classe abstrata é criada para ser usada por subclasses.
#
# - Para definir uma classe abstrata, é necessário importar a biblioteca 'abc' e usar '(ABC)' 
#   depois do nome da classe.
#
# - Classes abstratas ajudam no encapsulamento, sergurança e manutenção do código.

from abc import ABC, abstractmethod
import math

class Shape(ABC):           # Classe abstrata
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):        # Subclasse 1
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):     # Subclasse 1
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Tentar instanciar uma classe abstrata resultará em um erro
# shape = Shape()  # Isso lançará um TypeError

# Instanciando as subclasses concretas
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Calculando área e perímetro das formas
print("Círculo:")
print("Área:", circle.area())  # Saída: Área: 78.53981633974483
print("Perímetro:", circle.perimeter())  # Saída: Perímetro: 31.41592653589793

print("\nRetângulo:")
print("Área:", rectangle.area())  # Saída: Área: 24
print("Perímetro:", rectangle.perimeter())  # Saída: Perímetro: 20
