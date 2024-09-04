# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:02/09/2024
# atividade0011 B-Faça um programa que peça o ano do seu nascimento e calcule a sua idade.
import os
import datetime


os.system('cls')

class Calcular:
    def __init__(self,ano_nascimento):
        self.ano_nascimento = ano_nascimento
        
    def idade(self,ano_nascimento):
        
        while True:
            
            ano_atual = datetime.datetime.now().year
            idade_atual = int(ano_atual) - ano_nascimento
            return idade_atual


while True:
    os.system('cls')
    print('-'*70)
    print('INFORME SUA IDADE')
    ano_nascimento = int(input('ANO DE NASCIMENTO: '))
    
    if ano_nascimento < 0:
        print('Entrada invalida!!!!')
        input('Pressione Enter para continuar')
        os.system('cls')
        
    elif ano_nascimento > 0:
        resultado = Calcular(ano_nascimento)
        print('-'*70)
        print(f'VOCE TEM {resultado.idade(ano_nascimento)} ANOS DE IDADE!!!')
        input('Pressione Enter para continuar')
        os.system('cls')
            
    else:
        print('Entrada invalida!!!!')
        input('Pressione Enter para continuar')
        os.system('cls')