import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE CONTROLE COM IMPUT D IF')
print('='*70)

print()

soma = 0

for var_iteradora in range(0, 4):
    numero = int(input(f'{var_iteradora + 1}º numero: '))
    
    if (numero % 2 == 0):
        print(f'o numero {numero} é par')
    else:
        print(f'O numero {numero} é impar')

print('-'*70)
print()