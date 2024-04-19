#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:19/04/2024
#atividade001 C-Faça um programa que peça 4 notas, após a entrada de dados calcular a média das notas digitadas.


import os 


os.system('cls')


print('-'*70)
print('entrada de dados')
print('='*70)

#entrada
print('-'*70)
print('INFORME AS NOTAS')
nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))
nota3 = float(input('3ª nota: '))
nota4 = float(input('4ª nota: '))

#processo
soma = nota1 + nota2 + nota3 + nota4
media = (nota1 + nota2 + nota3 + nota4) / 4

#saida

print('-'*70)
print('-----NOTAS------------')
print(f'1ª NOTA: {nota1} | 2ª NOTA: {nota2}'
      F'3ª NOTA: {nota3} | 4ª NOTA: {nota4}')
print('-'*70)
print(f'MEDIA: {media}')