# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:12/07/2024
# atividade009 A-Crie uma função que receba uma lista de números.
# Depois retorne duas listas com os números pares, os números ímpares,
# a quantidade de números pares e a quantidade de números ímpares.


import os

os.system('cls')

def pares_impares(lista):
    """Verificando se o número é par ou ímpar, e colocando dentro de uma lista

    Args:
        lista (list): Lista de números

    Returns:
        list: Retorna as listas de pares, ímpares, quantidade de pares e quantidade de ímpares
    """
    lista_pares = []
    lista_impares = []
    
    for num in lista:
        if num % 2 == 0:
            lista_pares.append(num)
        else:
            lista_impares.append(num)
            
    quantidade_pares = len(lista_pares)
    quantidade_impares = len(lista_impares)
    
    return lista_pares, lista_impares, quantidade_pares, quantidade_impares

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares, impares, quantidade_de_pares, quantidade_de_impares = pares_impares(lista)

print(f'Pares: {pares}')
print(f'Quantidade de pares: {quantidade_de_pares}')
print('-'*70)
print(f'Ímpares: {impares}')
print(f'Quantidade de ímpares: {quantidade_de_impares}')