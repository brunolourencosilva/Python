#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:24/04/2024
#estudo de condicional: parte 3
#operadores relacionais

import os


os.system('cls')

a = 10 
b = 5
c = 'José'
d = 'José'

print('-'*70)
print('condicionais: Operadores relacionias')
print('='*70)

#igualdade (==)
if c == d:
    print('-'*70)
    print(f'{c} é igual {d}')
    print('='*70)
else:
    print(f'{c} não é igual a {d}')
    
#diferença (!=)
if a != c:
    print('-'*70)
    print(f'{a} é diferente de {c}')
    print('='*70)
else:
    print(f'{a} não é diferente de {c}')
    
#maior que (>)
if a > b:
    print('-'*70)
    print(f'{a} é maior que {b}')
    print("="*70)
else:
    print(f'{a} é maior que {b}')
    
#menor que (<)
if b < a:
    print('-'*70)
    print(f'{b} é menor que  {a}')
    print('='*70)
else:
    print(f'{b} não é menor que {a}')

#maior ou igual a(>=)
if a >= b:
    print('-'*70)
    print(f'{a} é maior ou igual a {b}')
    print('='*70)
else:
    print(f'{b} não é menor que {b}')
    
#menor ou igual a (<=)
if b <= a:
    print('-'*70)
    print(f'{b} é menor ou igual a {a}')
    print('='*70)
else:
    print(f'{b} não é ou igual a {a}')
    
print('FIM DO PROGRAMA!!')
print('-'*70)
print()