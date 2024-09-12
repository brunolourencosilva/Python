from math import pi

# Define a classe base Forma com o metodo area
# que não faz nada  (é quase uma classe abstrata)


class Forma:
    def area(self):
        pass

# Define a classe Circulo que herda de forma
# O construtor __init__ inicializando o atributo raio
class Circulo(Forma):
    def __init__(self,raio):
        self.raio = raio
    
    # Define o metodo area para calcular a area do
    # circulo usando a formula π * raio²
    def area(self):
        return pi * (self.raio ** 2)
    

# Define a classe Retangulo que herda de Forma
class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        
    # Define o metodo area para calcular a area
    # do retangulo usando a formula largura * altura
    def area(self):
        return self.largura * self.altura


# Define a classe Quadrado que herda de Retangulo
class Quadrado(Retangulo):
    def __init__(self, lado):
        super().__init__(lado,lado)
# Define uma função exibir_area que aceita um
# obejeto forma e imprime sua area
# O metodo area é chamada no obejeto forma
def exibir_area(forma):
    print(f'a area da forma é: {forma.area()}')


# Cria instancias e circulos, retangulos e quadrado
circulo = Circulo(5)
retangulo = Retangulo(4,6)
quadrado = Quadrado(3)

# Chama a função exibir_area para cada instancia
# O metodo area apropriado é chamado para
# cada objeto,mostrando polimorfismo
exibir_area(circulo)
exibir_area(retangulo)
exibir_area(quadrado)