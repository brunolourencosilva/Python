#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:31/04/2024
#atividade005 G-Faça um programa que calcule os números primos em um intervalo pré-determinado pelo usuário.

#IMCOMPLETO E NÃO FUNCUONA
import os


os.system('cls')

print('-'*70)
print('Programa que calcule os números primos em um intervalo pré-determinado pelo usuário')
print('='*70)

#entrada
inicio = int(input('Digite o valor inicial do intervalo: '))
fim = int(input('Digite o valor final do intervalo: '))

contador = inicio 

while contador <= fim:
    contador += 1

    if (contador / contador)and (contador / 1):
        print(f'{contador} esse numero é primo')

print('-'*70)