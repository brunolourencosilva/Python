# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:06/09/2024
# atividade0012 H-Faça um programa que imprima os valores no intervalo definidos pelo usuário.
# Defina 3 números que deverão ser ignorados, ou seja, que não serão impressos na tela.

class Intervalo:
    def __init__(self, inicio, final, ignorar1, ignorar2, ignorar3):
        self.inicio = inicio
        self.final = final
        self.ignorar1 = ignorar1
        self.ignorar2 = ignorar2
        self.ignorar3 = ignorar3
    
    def exibir_ignorados(self, ignorar1, ignorar2, ignorar3):
        print(f'Numeros ignorados: {ignorar1} | {ignorar2} | {ignorar3}')

class (Intervalo):
    
    def intervalo(self, inicio, final):
        
        contador = inicio
        for contador in range(final + 1):
            print(f'{contador}', end=' | ')
            contador += 1


inicio = int(input('Digite o valor inicial: '))
final = int(input('Digite o valor final: '))

objeto_contador = Intervalo(inicio,final)

intervalo = objeto_contador.intervalo(inicio,final)

        