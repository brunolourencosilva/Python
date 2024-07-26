# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:12/07/2024
# atividade009 B-Crie uma função que cadastre o nome de uma aluno,a matrícula e a data de nascimento.
# Depois imprima os resultados cadastrados utilizando uma estrutura de repetição for.

import os


os.system('cls')

dicionario = []

def cadastrar_aluno(nome, matricula, data_nascimento):
    """
    Cadastra um novo aluno no dicionário.
    
    Args:
        nome (str): Nome do aluno a ser cadastrado.
        matricula (str): Matrícula do aluno a ser cadastrado.
        data_nascimento (str): Data de nascimento do aluno a ser cadastrado.
    """
    dicionario['Nome'] = nome
    dicionario['Matricula'] = matricula
    dicionario['Data de nascimento'] = data_nascimento
    print('Aluno cadastrado com sucesso!')

print('Dados do aluno')
nome = input('Nome: ')
matricula = input('Matrícula: ')
data_nascimento = input('Data de nascimento: ')
cadastrar_aluno(nome, matricula, data_nascimento)
print('-' * 70)
input('Pressione qualquer tecla para voltar')
        
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")