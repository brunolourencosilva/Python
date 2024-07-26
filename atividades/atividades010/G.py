# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:12/07/2024
# atividade009 G-Crie um programa que peça ao usuário 2 números maiores que 0 e menores que 11.
# Depois mostre um menu com as seguintes operações:
# 1. Soma: 2. Subtração : 3. Produto : 4. Divisão : 4. Divisão inteira : 6. Resto da divisão.
# O usuário deverá escolher um número maior ou  igual a 1 e menor ou igual a 6.
# Em seguida, você criará funções que retornem os resultados das operações, imprimindo os resultados na tela

import os


os.system('cls')

def soma(a, b):
    return a+b

def subtracao(a, b):
    return a - b

def produto(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero"

def divisao_inteira(a, b):
    if b != 0:
        return a // b
    else:
        return "Erro: Divisão por zero"

def resto_divisao(a, b):
    if b != 0:
        return a % b
    else:
        return "Erro: Divisão por zero"

# Solicitar números ao usuário
while True:
    num1 = int(input("Digite o primeiro número (maior que 0 e menor que 11): "))
    num2 = int(input("Digite o segundo número (maior que 0 e menor que 11): "))
    
    if 0 < num1 < 11 and 0 < num2 < 11:
        os.system('cls')
        print("\nEscolha uma operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Produto")
        print("4. Divisão")
        print("5. Divisão inteira")
        print("6. Resto da divisão")
        opcao = int(input("Digite um número entre 1 e 6: "))
        
        if opcao == 1:
            resultado = soma(num1, num2)
            print(f"O resultado é: {resultado}")
            input('Pressione enter para continuar')
            os.system('cls')
            
        elif opcao == 2:
            resultado = subtracao(num1, num2)
            print(f"O resultado é: {resultado}")
            input('Pressione enter para continuar')
            os.system('cls')
            
        elif opcao == 3:
            resultado = produto(num1, num2)
            print(f"O resultado é: {resultado}")
            input('Pressione enter para continuar')
            os.system('cls')
            
        elif opcao == 4:
            resultado = divisao(num1, num2)
            print(f"O resultado é: {resultado}")
            input('Pressione enter para continuar')
            os.system('cls')
            
        elif opcao == 5:
            resultado = divisao_inteira(num1, num2)
            print(f"O resultado é: {resultado}")
            input('Pressione enter para continuar')
            os.system('cls')
            
        elif opcao == 6:
            resultado = resto_divisao(num1, num2)
            print(f"O resultado é: {resultado}")
            input('Pressione enter para continuar')
            os.system('cls')
            
        else:
            print('opção invalida')
            input('Pressione enter para continuar')
    else:
        print('Numeros invalidos!!')
        input('Pressione enter para continuar')