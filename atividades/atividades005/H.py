#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:31/04/2024
#atividade005 H-Faça um programa que imprima os valores no intervalo definidos pelo usuário.
#Defina 3 números que deverão ser ignorados, ou seja, que não serão impressos na tela.

import os


os.system('cls')

print('-'*70)
print('Programa que imprima os valores no intervalo definidos pelo usuário')
print('='*70)

#entrada
inicio = int(input("Digite o valor inicial do intervalo: "))
fim = int(input("Digite o valor final do intervalo: "))

ignorar1 = int(input("Digite o 1º número que sera ignorado: "))
ignorar2 = int(input("Digite o 2º número que sera ignorado: "))
ignorar3 = int(input("Digite o 3º número que sera ignorado: "))
print('-'*70)

#declaração
contador = inicio 

#saida
while contador <= fim:
    #ignorando os números especificados
    if contador != ignorar1 and contador != ignorar2 and contador != ignorar3:
        print(contador)
    contador += 1
    
print("="*70)
print()