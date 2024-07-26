# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:12/07/2024
# atividade009 I-Faça um programa de perguntas e respostas sobre os estados e capitais brasileiras.
# O programa deverá exibir para o usuário o está e perguntar qual a sua capital.
# Se o usuário errar a resposta, o programa será finalizado apresentando quantas perguntas estão corretas.
# Utilize ao menos uma função e não há a necessidade de modularizar o código.

import os


os.system('cls')

def perguntar_estado_capital(estado, capital_correta):
    """
    Faz uma pergunta ao usuário sobre a capital de um estado e verifica a resposta.
    
    Args:
        estado (str): Nome do estado para o qual o usuário deve fornecer a capital.
        capital_correta (str): Capital correta do estado.
    
    Returns:
        bool: True se a resposta estiver correta, False caso contrário.
    """
    resposta = input(f"Qual é a capital de {estado}? ").strip()
    return resposta.lower() == capital_correta.lower()

# Dicionário de estados e capitais
estados_capitais = {
    "São Paulo": "São Paulo",
    "Rio de Janeiro": "Rio de Janeiro",
    "Minas Gerais": "Belo Horizonte",
    "Espírito Santo": "Vitória",
    "Bahia": "Salvador",
    "Pernambuco": "Recife",
    "Ceará": "Fortaleza",
    "Pará": "Belém",
    "Maranhão": "São Luís",
    "Goiás": "Goiânia",
    "Distrito Federal": "Brasília",
    "Santa Catarina": "Florianópolis",
    "Paraná": "Curitiba",
    "Rio Grande do Sul": "Porto Alegre",
    "Mato Grosso": "Cuiabá",
    "Mato Grosso do Sul": "Campo Grande",
    "Acre": "Rio Branco",
    "Amazonas": "Manaus",
    "Rondônia": "Porto Velho",
    "Roraima": "Boa Vista",
    "Amapá": "Macapá",
    "Tocantins": "Palmas"
}

perguntas_corretas = 0

# Loop para perguntar sobre cada estado
for estado, capital in estados_capitais.items():
    if perguntar_estado_capital(estado, capital):
        print("Resposta correta!")
        perguntas_corretas += 1
    else:
        print(f"Resposta errada! A capital correta de {estado} é {capital}.")
        break
print('-'*70)
print(f"\nNúmero de perguntas corretas: {perguntas_corretas}")