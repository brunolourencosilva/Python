# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:06/09/2024
# atividade0012 K-Crie um programa que pede que o usuário digite um nome ou uma frase,
# verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em tela esse resultado.

import os


os.system('cls')

class Dados:
    def __init__(self,frase):
        self.frase = frase
        self.frase_inversa = frase[::-1]
    
    def exibir_frase_revertidade(self,frase):
        print(f'Essa frase é um palíndromo!! \nFrase orginal: {frase} | Frase revertida: {self.frase_inversa}')
        
    def exibir_frase_nao_palidromo(self):
        print(f'Essa frase não é um palíndromo!!')
        
class Invertido(Dados):
    
    def invertendo(self):

        if self.frase == self.frase_inversa:
            self.exibir_frase_revertidade(frase)
        else:
           self.exibir_frase_nao_palidromo()

print('-'*70)
print('Verificador que fala se a frase é um palíndromo ou não')
print('='*70)

#entrada
frase = input('Digite uma frase: ')
print('-'*70)

objecto = Invertido(frase)
objecto.invertendo()