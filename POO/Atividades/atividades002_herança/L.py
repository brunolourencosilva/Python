# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:06/09/2024
# atividade0012 L-Faça um programa que verifique se o usuário e senha estão inseridos em um banco de dados (fake).
# O usuário só terá acesso se digitar os dados corretos e, assim, sair do laço.

import os


os.system('cls')

#  Define a classe Dados que irá armazenar os valores de senha e usuario
class Dados:
    def __init__(self,nome_usuario,senha):
        self.nome_usuario = nome_usuario
        self.senha = senha
        
    # Método para exibir que o usuario colocou a senha e nome corretamente
    def exibir_senha_usuario_correto(self):
        print('Voce digitou a senha e o nome de usuario corretamente')
        print('Agora voce pode acessar o seu dispositivo!! tenha um bom dia :)')
    
    # Método para exibir que o usuario colocou a senha e nome incorretamente
    def exibir_senha_usuario_incorreto(self):
        print('Voce digitou o a senha e o nome de usuario incorretamente!! :(')
        
#  Define a classe Verificar herdando da classe Dados
class Verificar(Dados):
    def __init__(self,nome_usuario,senha):
        self.nome_usuario = nome_usuario
        self.senha = senha

    # Método para verificar se o nome e senha estão corretos
    def verificando_senha(self,nome_usuario,senha):

        if senha != self.senha or nome_usuario != self.nome_usuario:
            self.exibir_senha_usuario_incorreto()
        else:
            self.exibir_senha_usuario_correto()
# Entrada de dados
while True:
    
    nome_usuario = str(input('Digite um nome de usuario: '))
    senha = input('Digite uma senha: ')
    print('.'*70)

    verficar_usuario = input(f'Digite seu nome de usuario novamente: ')
    verficar_senha = input(f'Digite sua senha novamente: ')
    
    # Cria um objeto da classe Verficar pegando os valores do nome e senha
    objeto_verificar = Verificar(nome_usuario,senha)
    objeto_verificar.verificando_senha(verficar_usuario,verficar_senha)
    
    print('.'*70)
    input('Pressione Enter para recomeçar o programa!!!')
    os.system('cls')