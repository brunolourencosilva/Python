import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE DADOS: DICIONARIO ') # dict => {}
print('='*70)

compras = {}
pessoas = {}
cores = {}
elementos = dict()
numeros = dict()

# Atribuindo valores

compras['id'] = 1
compras['item'] = 'Caderno'
compras['valor'] = 10.80

pessoas['id'] = '0010'
pessoas['nome'] = 'Sherlock Holmes'
pessoas['endereço'] = 'Baker Street'
pessoas['numero'] = '221B'
pessoas['cidade'] = 'Londres'
pessoas['pais'] = 'Inglaterra'

cores['red'] = 'Vermelho'
cores['green'] = 'Verde'
cores['blue'] = 'Azul'

elementos['Pb'] = 'Chumbo'
elementos['Au'] = 'Ouro'
elementos['N'] = 'Nitrogenio'

numeros[1] = 100
numeros[2] = 200
numeros[3] = 300

#saida simples
print(f'Minhas compras: {compras}')
print(f'Detetive: {pessoas}')
print(f'Cor RGB: {cores}')
print(f'Tabela periodica: {elementos}')
print(f'Listagem de numeros: {numeros}')
print()
print('-'*70)