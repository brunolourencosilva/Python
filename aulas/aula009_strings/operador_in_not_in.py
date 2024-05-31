import os


os.system('cls')
print('-'*70)
print('Operadores uteis para'
      +' String e Estrutura de dados')
print('='*70)

texto = 'Ola, Mundo'

print(f'Texto: {texto}')
if 'Mundo' in texto: # Verifica a palavra dentro da string
    print('A palavra "Mundo" esta presente na string')
else:
    print('A palavra "mundo" não esta presente na string')

print('.'*70)

texto2 = "Ola, Python"

print(f'Texto: {texto2}')
if "mundo" not in texto2: #Verificar a palavrva dentro da string
    print('A palavra "Mundo" não esta presente na string')
else:
    print('A palavra "Mundo"esta presente na string')
    
print('.'*70)