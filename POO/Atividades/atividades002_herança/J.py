# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:06/09/2024
# atividade0012 J-Crie um programa que realiza a contagem de 1 até 100, usando apenas de números ímpares,
# ao final do processo exiba na tela quantos números ímpares foram encontrados nesse intervalo, assim como a soma dos mesmos.

import os


os.system('cls')

class Dados:
    def __init__(self,impares=0,soma=0,quantidade=0):
        self.impares = impares
        self.soma = soma
        self.quantidade = quantidade
    
    def exibir(self,quantidade,soma):
        print()
        print('-'*70)
        exibindo_quantidade = print(f'Quantidade de impares: {quantidade}')
        exibindo_soma = print(f'Soma dos impares: {soma}')
        return exibindo_quantidade,exibindo_soma
        
        
class Calcular(Dados):
    def __init__(self,impares=0,soma=0,quantidade=0):
        self.impares = impares
        self.soma = soma
        self.quantidade = quantidade
    
    def contagem_impares(self):
        inicio = 0 
        fim = 100
        quantidade = 0
        soma = 0
        for i in range(inicio,fim):
            
            if i % 2 != 0:
                print(f'{i}',end=' | ')
                quantidade += 1
                soma += i
        
        return quantidade,soma
        
impares = 0
soma = 0
quantidade = 0

objeto_calcular = Calcular(impares,soma,quantidade)
quantidade,soma = objeto_calcular.contagem_impares()
objeto_calcular.exibir(quantidade,soma)

