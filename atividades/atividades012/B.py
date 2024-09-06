# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:06/09/2024
# atividade0012 B-Evolua o programa anterior para um código que pergunte ao usuário qual o intervalo que ele deseja ver impresso.

import os


os.system('cls')

class InicioFim:
    def __init__(self, inicio, final):
        self.inicio = inicio
        self.final = final

class Intervalo(InicioFim):
    
    def intervalo(self, inicio, final):
        
        contador = inicio
        for contador in range(final + 1):
            print(f'{contador}', end=' | ')
            contador += 1


inicio = int(input('Digite o valor inicial: '))
final = int(input('Digite o valor final: '))

objeto_contador = Intervalo(inicio,final)

intervalo = objeto_contador.intervalo(inicio,final)
