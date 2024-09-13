# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:06/09/2024
# atividade0012 H-Faça um programa que imprima os valores no intervalo definidos pelo usuário.
# Defina 3 números que deverão ser ignorados, ou seja, que não serão impressos na tela.
import os


os.system('cls')


class Exibir:
    def __init__(self, inicio, final, ignorar1, ignorar2, ignorar3):
        self.inicio = inicio
        self.final = final
        self.ignorar1 = ignorar1
        self.ignorar2 = ignorar2
        self.ignorar3 = ignorar3

    def exibir_ignorados(self):
        print('-'*70)
        print(f'Numeros ignorados: {self.ignorar1} | {self.ignorar2} | {self.ignorar3}')
        print('-'*70)


class Ignora(Exibir):

    def intervalo_ignorando(self):

        # declaração
        contador = self.inicio

        # saida
        while contador <= self.final:
            # ignorando os números especificados
            if contador != self.ignorar1 and contador != self.ignorar2 and contador != self.ignorar3:
                print(contador, end=' | ')
            contador += 1

print('='*70)
inicio = int(input('Digite o valor inicial: '))
final = int(input('Digite o valor final: '))
print('-'*70)
ignorar1 = int(input("Digite o 1º número que sera ignorado: "))
ignorar2 = int(input("Digite o 2º número que sera ignorado: "))
ignorar3 = int(input("Digite o 3º número que sera ignorado: "))

exibindo = Exibir(inicio, final, ignorar1, ignorar2, ignorar3)
exibindo.exibir_ignorados()

intervalo = Ignora(inicio, final, ignorar1, ignorar2, ignorar3)
intervalo.intervalo_ignorando()
