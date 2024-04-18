# Curso de desenvolvimento de sistema
# Autor:Bruno Lourenço
# Data:17/04/2024
# Atividade numero 1


# Importando bibliotecas
import os

import datetime

# Limpando terminal
os.system('cls')


print('-'*70)
print('DADOS DO VEICULO')
print('-'*70)

# Entrada de dados com casting
nome_do_carro = str(input('ENTRE COM O NOME DO VEICULO: '))
altura = float(input('COLOQUE A AlTURA DO CARRO: '))
data_compra = int(input('INFORMA O ANO DA COMPRA DO VEICULO: '))

# Definindo se a variavel é vedadeira ou falsa
concerto = True

ano_atual = datetime.datetime.now().year
idade_carro = int(ano_atual) - data_compra

# Saida interpolada
print('-'*70)
print('saida dos dados do veiculo')
print('-'*70)
print(f'O veiculo {nome_do_carro} tem {idade_carro} anos.')
print(f'Altura..........: {altura}M de altura')
print(f'Data de compra..: {data_compra}')
print(f'Nome do veiculo.: {nome_do_carro}')
print(f'Veiculo tem dano: {concerto}')

# Saida dos tipos das variaveis
print('-'*70)
print('Tipo das variaveis')
print('='*70)
print('Variavel Nome.......: ', type(nome_do_carro))
print('Variavel altura.....: ', type(altura))
print('Variavel data compra: ', type(data_compra))
print('variavel concerto...: ', type(concerto))