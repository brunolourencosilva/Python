import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE CONTROLE M SOMATORIO')
print('='*70)

print()

soma = 0

for var_interadora in range(0, 4):
    numero = int(input(f'Digite o {var_interadora + 1}ª numero: '))
    
    #calculo
    soma += numero #mesma coisa:soma = soma + numero

print('-'*70)
print(f'A soma dos numeros é: {soma}')
print('-'*70)
print()