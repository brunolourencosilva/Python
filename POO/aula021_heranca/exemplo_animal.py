import os


class Animal:
    def __init__(self,nome):
        self.nome = nome
    
    def latir(self):
        return 'Isto está no metodo latin()'
    
    def miar():
        return 'Isto esta no metodo miar()'
    
class Cachorro(Animal):
    def latir(self):
        return f'{self.nome} está latindo!!'

class Gato(Animal):
    def miar(self):
        return f'{self.nome} está miando'

os.system('cls')
cao = Cachorro('Rex')
gato = Gato('Tobias')
print(cao.latir())
print(gato.miar())