import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE CONTROLE: CONTINUE')
print('='*70)

print()

for c in range(1, 11):
    if c == 5:
        #5 esta fora do loop, se retirar a linha abaxio,
        #ele não aparecera na saida< daixei para verificação!!
        print(f'O numero {c} esta fora do loop')
        continue
    
    print(f'O numero é {c}')

print('-'*70)
print()