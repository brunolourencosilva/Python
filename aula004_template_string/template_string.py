import os
import datetime


os.system('cls')

print('-'*70)
print('ENTRADA DE DADOS EM PYTHON')
print('='*70)


nome = input('ENTRE COM UM NOME: ')
peso = input('ENTRE COM O PESO: ')
altura = input('ENTRE COM A ALTURA: ')

nascimento = int(input('DATA DE NASCIMENTO: '))
cep = int(input('ENTRE COM O SEU CEP: '))
bairro = str(input('ENTRE COM O BAIRRO: '))
rua = str(input('NOME DA RUA: '))
numero= str(input('ENTRE COM O NUMERO: '))

ano_atual  = datetime.datetime.now().year
idade = int(ano_atual) - nascimento

print('-'*70)
print('SAIDA DE DADOS')
print('='*70)
print('NOME..................: ', nome)
print('DATA DE NASCIMENTO....: ', nascimento)
print('PESO..................: ', peso)
print('ALTURA................: ', altura)

print(f'{nome}, VOCE TEM {idade} anos!')
print(f'CEP..................: {cep}')
print(f'BAIRRO...............: {bairro}')
print(f'RUA..................: {rua}')
print(f'NUMERO DA RUA........: {numero}')
print('-'*70)
print('')