#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:3/06/2024
#atividade005 K-Crie um programa que pede que o usuário digite um nome ou uma frase,
#verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em tela esse resultado.

import os


os.system('cls')

print('-'*70)
print('Verificador que fala se a frase é um palíndromo ou não')
print('='*70)

#entrada
nome = input('Digite uma frase: ')
print('-'*70)
#invertendo a frase
frase_inversa = nome[::-1]

#condicional
if nome == frase_inversa:
    reposta = f'Essa frase é um palíndromo!!\n{nome} | {frase_inversa}'
else:
    reposta = f'Essa frase não é um palíndromo!!'
    
#saida
print(f'{reposta}')