# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:06/09/2024
# atividade0012 L-Faça um programa que verifique se o usuário e senha estão inseridos em um banco de dados (fake).
# O usuário só terá acesso se digitar os dados corretos e, assim, sair do laço.

import os


os.system('cls')

class Dados:
    def __init__(self,nome_usuario,senha,verficar_senha,verficar_usuario):
        self.nome_usuario = nome_usuario
        self.senha = senha
        self.verficar_senha = verficar_senha
        self.verficar_usuario = verficar_usuario
        
    def exibir_senha_errada(self):
        print('Senha incorreta!!!')
    
    def exibir_senha_correta(self):
        print('Voce digitou a senha certa')
        print('Agora voce pode acessar seus dados')

class Verificar(Dados):
    
    def verificando_senha(self,senha,verficar_senha,verficar_usuario,nome_usuario):

        if(senha != verficar_senha):
            self.exibir_senha_errada()
        
        elif(nome_usuario != verficar_usuario):
            self.exibir_senha_errada()
        else:
            self.exibir_senha_correta()

nome_usuario = str(input('Digite um nome de usuario: '))
senha = input('Digite uma senha: ')
print('.'*70)

verficar_usuario = input(f'Digite seu nome de usuario novamente: ')
verficar_senha = input(f'Digite sua senha novamente: ')

objecto = Verificar(nome_usuario,senha,verficar_senha,verficar_usuario)
print('.'*70)
objecto.verificando_senha(nome_usuario,senha,verficar_senha,verficar_usuario)
print('.'*70)