# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:12/07/2024
# atividade009 F-Crie uma função que receba 2 listas:
# - lista 1: nome, peso, idade
# - lista 2: John, 40, 1.8
# - Sua função deverá criar um dicionário contendo chave e valor utilizando como base essas duas listas.
# Depois, seu programa deverá imprimir esse dicionário utilizando uma estrutura de repetição for.

import os


os.system('cls')

def criar_dicionario(lista_chaves, lista_valores):
    """
    Cria um dicionário a partir de duas listas, uma contendo as chaves e outra os valores.

    Args:
        lista_chaves (list): Lista contendo as chaves do dicionário.
        lista_valores (list): Lista contendo os valores do dicionário.

    Returns:
        dict: Dicionário criado a partir das duas listas.
    """
    dicionario = dict(zip(lista_chaves, lista_valores))
    return dicionario

lista_chaves = ['nome', 'peso', 'altura']
lista_valores = ['John', 40, 1.8]

# Criação do dicionário
dicionario = criar_dicionario(lista_chaves, lista_valores)

# Impressão do dicionário usando uma estrutura de repetição for
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")