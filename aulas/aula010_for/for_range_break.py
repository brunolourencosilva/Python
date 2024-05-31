import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE CONTROLE: BREAK')
print('='*70)

print()

for c in range(0,10):
    print(f'Valor: {c}')
    
    #condição para terminar a contagem
    if (c == 5):
        print(f'Cotagem interrompida no {c}')
        break
    
print('-'*70)
print('Fim do programa!')
print()