import os


os.system('cls')

class Classepai: # Super Classe
    # Metodo Construtor
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    # Para sobrecarregar
    # Vai ser usada para soma 2 numeros
    def metodo_classe(self,a,b):
        pass

class Classefilha(Classepai): # Classe derivada
    # Metodo construtor
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    # Sobrecarga de metodo
    def metodo_classe(self):
        return self.a + self.b

# Programa principal
teste = Classefilha(1,2)
teste.metodo_classe()