# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:17/06/2024
# atividade007 G-Faça um programa que gere 10 números aleatórios. Após gerar esses números, crie duas listas novas com ordenação ascendente e descendente.
import os
import random


os.system('cls')

print('-'*70)
print('Programa que gera 10 números aleatórios.Após gerar esses números\nele cria duas listas novas com ordenação ascendente e descendente.')
print('='*70)

#criando lista
ascendente = []
descendente = []

numero_aleatorio = [random.randint(1, 100) for _ in range(10)]# Gerando um numero entre 1 e 100 mas usando apenas 10 dos numeros
ascendente.extend(numero_aleatorio)
descendente.extend(numero_aleatorio)

#colocando em ordem crescente
ascendente.sort()
print(ascendente)

#colocando em ordem decrescente
descendente.sort(reverse=True)
print(descendente)
