# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:12/07/2024
# atividade009 C-Crie uma função que verifica se um aluno está cadastrado ou não em um dicionário.
# Se estiver cadastrado, imprima o nome desse aluno e o resto dos seus dados.
# O dicionário deverá conter nome, matrícula e a data de nascimento do aluno.

import os

os.system('cls')

# Dicionário para armazenar os dados dos alunos
dicionario = {}

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

def verificar_aluno(nome):
    """
    Verifica se um aluno está cadastrado e imprime seus dados.

    Args:
        nome (str): Nome do aluno a ser verificado.
    """
    if dicionario.get('Nome') == nome:
        for chave, valor in dicionario.items():
            print(f"{chave}: {valor}")
    else:
        print(f'O nome {nome} não está no sistema')

while True:
    os.system('cls')
    print('-' * 70)
    print('SISTEMA ESCOLAR')
    print('1 - CADASTRAR ALUNO')
    print('2 - PROCURAR DADOS DO ALUNO')
    print('-' * 70)
    escolha = input('Escolha uma opção: ')
    
    if escolha == '1':
        print('Dados do aluno')
        nome = input('Nome: ')
        matricula = input('Matrícula: ')
        data_nascimento = input('Data de nascimento: ')
        cadastrar_aluno(nome, matricula, data_nascimento)
        print('-' * 70)
        input('Pressione qualquer tecla para voltar')
        
    elif escolha == '2':
        verificar_nome = input('Nome do aluno que deseja procurar: ')
        verificar_aluno(verificar_nome)
        input('Pressione qualquer tecla para voltar')
        
    else:
        print('Opção não encontrada!')
        input('Pressione qualquer tecla para continuar')