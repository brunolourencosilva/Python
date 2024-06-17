# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:17/06/2024
# atividade006 G-Ler uma lista com 10 números, depois apresente o maior e o menor número da lista

import os


os.system('cls')

print('-'*70)
print('Programa que le uma lista com 10 números\nE depois apresente o maior e o menor número da lista.')
print('='*70)

numero_lista = []

#entrada
print('Digite 10 numeros:')
for num in range(10):
    numero = input(f'{num+1}: ')
    numero_lista .append(numero)

#variáveis de maior e menor número
maior_numero = numero_lista[0]
menor_numero = numero_lista[0]

#encontrando o maior e o menor número
for numero in numero_lista:
    
    if numero > maior_numero:
        maior_numero = numero
    if numero < menor_numero:
        menor_numero = numero

print(f'O maior número da lista é: {maior_numero}')
print(f'O menor número da lista é: {menor_numero}')