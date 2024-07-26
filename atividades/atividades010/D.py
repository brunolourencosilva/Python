# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:12/07/2024
# atividade009 D-Crie uma função que receba uma temperatura em fahrenheit e retorne o valor em graus célsius.

import os


os.system('cls')

def f_para_c(farenheit):
    """Função que muda fahrenheit para célsius

    Args:
        farenheit (float): A temperatura em fahrenheit

    Returns:
        _float_:retorna o valor em graus celsius 
    """    
    temperatura_celsius = (farenheit - 32) * 5/9
    return temperatura_celsius

temperatura_farenheit = float(input('Informe uma temperatura em farenheit: '))

temperatura_celsius = f_para_c(temperatura_farenheit)

print(f'A temperatura {temperatura_farenheit} em celsius é: {temperatura_celsius}')