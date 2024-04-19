import os


os.system('cls')

print('-'*70)
print('OPERADORES ARITIMETICOS')
print('-'*70)

# Entrada de dados
print('--- SOMA')
print('-'*70)
parcela_1 = float(input('ENTRE COM A 1 PARCELA: '))
parcela_2 = float(input('ENTRE COM A 2 PARCELA: '))

print()
print('--- SUBTRAÇÃO')
print('-'*70)
minuendo = float(input('ENTRE COM O MINUENDO: '))
subtraendo = float(input('ENTRE COM O SUBTRAENDO: '))

print()
print('--- PRODUTO')
print('-'*70)
multiplicando = float(input('ENTRE COM O MULTIPLICADOR: '))
multiplicador = float(input('ENTRE COM O MULTIPLICADOR: '))

print()
print('--- DIVISAO')
print('-'*70)
dividendo = float(input('ENTRE COM O DIVIDENDO: '))
divisor = float(input('ENTRE COM O DIVISOR: '))
# Processo
soma = parcela_1 + parcela_2
diferenca = minuendo - subtraendo
produto = multiplicando * multiplicador
quociente = dividendo / divisor

# Saida
print('='*70)
print('RESULTADOS')
print('-'*70)
print(f'A SOMA DE {parcela_1} + {parcela_2} É: {soma}')
print(f'A SUBTRAÇÃO DE{minuendo} - {subtraendo} É: {diferenca}')
print(f'A MULIPLIÇÃO DE {multiplicando} X {multiplicador} É: {produto} ')
print(f'A DIVISÃO DE {dividendo} ÷ {divisor} É: {quociente}')