#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:25/04/2024
#estudo de condicional: parte 4
#operadores logicos

import os 


os.system('cls')

#declaração
a = 10
b = 5
c = 'john'

print('-'*70)
print('CONDICIONAIS: OPERADORES LOGICOCOS')
print('='*70)

# E (AND) VERDADEIRO
print('E (and) VERDADEIRO')
if (a > 5 and b != c):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso:Bloco executado')
    
print('.'*70)

#E (AND) FALSO
print('E (and) FALSO')
if (a > 5 and b == c):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')

print('.'*70)

#OU (OR) VERDADEIRO
print('OU (or) FALSO')
if (a < 5 or b == c):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Bloco executado')

print('.'*70)

#OU (OR) FALSO
print('OU (or) FALSO')
if (a < 5 or c == 'jane'):
    print('Verdadeiro: Bloco executado')
else:
    print('Falso: Boco executado')

print('-'*70)
print()