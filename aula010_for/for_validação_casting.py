import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE CONTROLE VALIDAÇÃO E CASTING')
print('='*70)

soma = 0

for c in range(0,5):
    
    numero = input('Digite um numero [0-5]: ')
    
    #validação
    if (not (numero.isnumeric())):
        print(f'"{numero}" Entrada invalida!!')
        print()
    else:
        #casting da varivel, ou seja, vai virar um inteiro
        numero = int(numero)
        
        #validando o intervalo pedido
        if (numero >= 0 and numero <= 5):
            print(f'o numero {numero} esta dentro do intervalo [0-5]!')
            print()
        else:
            print(f'"{numero}" entrada invalida!!')
            print()

print('-'*70)
print()