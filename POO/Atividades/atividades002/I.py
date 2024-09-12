# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:06/09/2024
# atividade0012 I-Faça um algoritmo que imprima a frase "estou em looping" e,
# em seguida, solicite ao usuário digitar uma letra. Caso a letra seja o “f" finalize a aplicação.
# Do contrário, imprima novamente a mesma frase até que o caractere “f" seja digitado.

import os


os.system('cls')

class Exibir:
    def __init__(self,letra):
        self.letra = letra
        
    def exibindo_loop(self):
        print('Estou em loop >:)')

class Looping(Exibir):
    def __init__(self,letra):
        self.letra = letra
        
    def loop(self,letra):

        if (letra != 'f'):
            print('letra "F" não foi digitada,o loop continuara')
            continuando_loop = Exibir(letra)
            continuando_loop.exibindo_loop()
            
            print('.'*70)
        
        else:
            print('-'*70)
            print('A letra "F" foi digitado,voce parou o loop!!')

letra = str
while letra != 'f':
    
    letra = str(input('Digite a letra "F" para parar o loop: ')).lower()
    
    Validação = Looping(letra)
    Validação.loop(letra)