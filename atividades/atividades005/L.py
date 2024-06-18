# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:3/06/2024
# atividade005 J-Faça um programa que verifique se o usuário e senha estão inseridos em um banco de dados (fake).
# O usuário só terá acesso se digitar os dados corretos e, assim, sair do laço.

import os


os.system('cls')

print('-'*70)
print('Programa que verifique se o usuário e senha\nestão inseridos em um banco de dados (fake).')
print('='*70)


nome_usuario = str(input('Digite um nome de usuario: '))
senha = input('Digite uma senha: ')
print('.'*70)

#
while (True):
    
    verficador_usuario = input(f'Digite seu nome de usuario novamente: ')
    verficador_senha = input(f'Digite sua senha novamente: ')
    
    if (nome_usuario != verficador_usuario): #verfificando se o nome de usuario foi colocado certo
        print('Senha errada')
    elif(senha != verficador_senha):#verfificando se a senha foi colocada certa
        print('Senha errada')
    else:
        print('-'*70)
        print('Voce digitou a senha certa')
        print('Agora voce pode acessar seus dados')
        break

print('-'*70)