import os


os.system('cls')

class Classepai: # Super Classe
    # Metodo Construtor
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    # Para sobrecarregar
    # Vai ser usada para soma 2 numeros
    def metodo_classe(self):
        print('Aqui vao multiplicar a e b!!')
        resultado = self.a + self.b
        print(f'Este calculo esta sendo realizado')
        print(f'pelo Metodo da Classe Pai!!')
        print(f'O resultado da soma de {self.a} e {self.b} = {resultado}')
        
class ClasseFilha(Classepai): # Classe Derivada
    # Metodo construtor
    def __init__(self, a, b):
        super().__init__(a, b) # Chama o construtor da classe pai
        # NÃO é necessario redefinir a variavel self.a e self.b,
        # pois ja foram inicializados pelo construtor da classe pai
    
    # Sobrecarga de metodo
    def metodo_classe(self):
        # Primeiro,execute o metodo da classe Pai
        super().metodo_classe()
        # Depois, executa o metodo da classe Filha
        resultado = self.a + self.b
        print(f'O resultado da soma na Classe Filha é: {resultado}')

# Programa principal
teste = ClasseFilha(1,2)
teste.metodo_classe()