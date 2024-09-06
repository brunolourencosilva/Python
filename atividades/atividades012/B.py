# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:06/09/2024
# atividade0012 B-Evolua o programa anterior para um código que pergunte ao usuário qual o intervalo que ele deseja ver impresso.

import os


os.system('cls')

class Contador:
    def __init__(self, inicio, final):
        self.inicio = inicio
        self.final = final
        
    def intervalo(self, inicio, final):
        
        contador = inicio
        
        while contador <= final:
            print(f'numero: {contador}', end=' | ')
            contador += 1

        return 

inicio = int(input('Digite o valor inicial: '))
final = int(input('Digite o valor final: '))

objeto_contador = Contador(inicio,final)

intervalo = objeto_contador.intervalo(inicio,final)

print('-'*70)