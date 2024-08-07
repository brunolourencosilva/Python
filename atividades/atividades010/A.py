# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:12/07/2024
# atividade009 A-Crie uma função que receba uma lista de números.
# Depois retorne duas listas com os números pares, os números ímpares,
# a quantidade de números pares e a quantidade de números ímpares.

import os


os.system('cls')

lista_pares = []
lista_impares = []
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def pares_impares(lista):
    """Verificando se o numero é par ou impar,e colocando dentro de uma lista

    Args:
        lista (list): Lista de numeros

    Returns:
        Retorna os pares e impare dentro de uma lista
    """    
    for num in lista:
        if num % 2 == 0:
            pares = num
            lista_pares.append(pares)
            quantidade_pares = len(lista_pares)
        else:
            impares = num
            lista_impares.append(impares)
            quantidade_impares = len(lista_impares)
            
    return lista, quantidade_impares, quantidade_pares

pares_impares(lista)
print(f'Pares: {lista_pares}')
print(f'Quantidade de pares: {}')
print('-'*70)
print(f'Impares: {lista_impares}')
print(f'Quantidade de impares: {}')