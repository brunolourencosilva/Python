# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:06/09/2024
# atividade0012 B-Evolua o programa anterior para um código que pergunte ao usuário qual o intervalo que ele deseja ver impresso.

import os


os.system('cls')

# Define a classe 'InicioFim' que irá armazenar os valores de início e final do intervalo
class InicioFim:
    def __init__(self, inicio, final):
        self.inicio = inicio
        self.final = final

# Define a classe Intervalo que herda atributos da classe InicioFim
class Intervalo(InicioFim):
    
    # Método para exibir os números dentro do intervalo
    def intervalo(self, inicio, final):
        
        # Usa um loop for para emprimir o intervalo
        contador = inicio
        for contador in range(inicio,final + 1):
            print(f'{contador}', end=' | ')
            contador += 1

inicio = int(input('Digite o valor inicial: '))
final = int(input('Digite o valor final: '))

# Cria um objeto da classe Intervalo pegando os valores de inicio e final
objeto_contador = Intervalo(inicio,final)
intervalo = objeto_contador.intervalo(inicio,final)
