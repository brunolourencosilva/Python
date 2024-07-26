# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:12/07/2024
# atividade009 E-Crie uma função que receba a altura e o peso de uma pessoa. Depois retorne o seu IMC.

import os

    
os.system('cls')

def dados(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC) com base no peso e na altura fornecidos.

    Args:
        peso (float): Peso da pessoa
        altura (float): Altura da pessoa

    Returns:
        float: O valor calculado do IMC
    """
    imc = peso / (altura ** 2)
    return imc

print('INFORME OS SEGUINTE DADOS PARA DESCOBRIR O IMC')
altura = float(input('Informe o valor da altura: '))
peso = float(input('Informe o valor do peso: '))

resultado_imc = dados(peso, altura)
print(f"O IMC é: {resultado_imc:.2f}")