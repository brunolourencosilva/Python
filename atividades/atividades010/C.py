# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:12/07/2024
# atividade009 C-Crie uma função que verifica se um aluno está cadastrado ou não em um dicionário.
# Se estiver cadastrado, imprima o nome desse aluno e o resto dos seus dados.
# O dicionário deverá conter nome, matrícula e a data de nascimento do aluno.

import os


os.system('cls')

dicionario = {}

def dados(cadastro):
    
    dicionario['Nome'] = nome
    dicionario['Matricula'] = matricula
    dicionario['Data de nascimento'] = data_nascimento
    
    if verificar_aluno in dicionario:
        for i in dicionario:
            print(i)
    else:
         print(f'O nome {verificar_aluno} não esta no sistema')   
    return cadastro

while True:
    os.system('cls')
    print('-'*70)
    print('SISTEMA ESCOLAR')
    print('1-CADASTRAR ALUNO')
    print('2-PROCURAR DADOS DO ALUNO')
    print('-'*70)
    escolha = input('Escolha uma opção: ')
    
    if escolha == '1':
        
        print('Dados do aluno')
        nome = input('Nome: ')
        matricula = input('Matricula: ')
        data_nascimento = input('Data de nascimento: ')
        print('-'*70)
        
        input('Pressione qualquer tecla para voltar')
        os.system('cls')
        
    elif escolha == '2':
        verificar_aluno = input('Nome do aluno que deseja procurar sobre: ')
        dados(cadastro=0)
        
        input('Pressione qualquer tecla para voltar')
        os.system('cls')
    else:
        print('Opção não encontrada!!')
        input('Pressione qualquer tecla para Continuar')
        os.system('cls')