#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:17/06/2024
#atividade006 A-Crie a lista [1, 2, 3, 5, 6] e depois insira o valor que está faltando na posição correta.

import os


os.system('cls')

print('-'*70)
print('Uma lista com [1, 2, 3, 5, 6]\nque depois insere o valor que está faltando na posição correta.')
print('='*70) 

lista = [1,2,3,5,6]

#declaração
posicao = 3
numero = 4

print(f'Lista antes da incerção do 4: {lista}')

#verificando a posição na lista
if posicao >= 0 and posicao <= len(lista):

    lista.insert(posicao,numero) #inserindo o numero 4 na lista
    print('Lista apos a inserção:', lista)
else:
    print('Erro')