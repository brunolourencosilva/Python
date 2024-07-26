# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:12/07/2024
# atividade009 H-Uma Academia deseja fazer uma pesquisa entre seus clientes para descobrir a média de altura 
# e peso de seus clientes.
# Faça um programa que pergunte a cada um dos clientes da academia seu código, nome, altura e peso.
# Após esse cadastramento, seu programa deverá listar os dados dos clientes e a média.
# Para sair do programa o usuário deverá digitar o valor zero(0). O número de clientes é indefinido.

import os


os.system('cls')

def obter_dados_cliente():
    """
    Solicita os dados do cliente e retorna um dicionário com as informações.
    """
    print('-'*70)
    codigo = input("Digite o código do cliente (ou 0 para sair): ")
    if codigo == '0':
        return None  # Indica que o usuário deseja sair

    nome = input("Digite o nome do cliente: ")

    # Solicitar altura e verificar se é um número válido
    altura = float(input("Digite a altura do cliente (em metros): "))
    
    # Solicitar peso e verificar se é um número válido
    peso = float(input("Digite o peso do cliente (em kg): "))
    
    return {
        'codigo': codigo,
        'nome': nome,
        'altura': altura,
        'peso': peso
    
    }


clientes = []

while True:
    dados_cliente = obter_dados_cliente()
    if dados_cliente is None:
        break
    clientes.append(dados_cliente)

if clientes:
    total_altura = 0
    total_peso = 0

    print("\nDados dos clientes:")
    for cliente in clientes:
        print(f"Código: {cliente['codigo']}")
        print(f"Nome: {cliente['nome']}")
        print(f"Altura: {cliente['altura']:.2f} m")
        print(f"Peso: {cliente['peso']:.2f} kg")
        print('-' * 30)

        total_altura += cliente['altura']
        total_peso += cliente['peso']

    media_altura = total_altura / len(clientes)
    media_peso = total_peso / len(clientes)

    print(f"Média de altura dos clientes: {media_altura:.2f} m")
    print(f"Média de peso dos clientes: {media_peso:.2f} kg")
else:
    print("Nenhum cliente foi cadastrado.")
