import os

from pacote.modulo_somar import somar
from pacote.subpacote.modulo_multiplicar import multiplicar as multi
from pacote.modulo_divisao import dividir

while True:
    os.system('cls')
    
    a = input('Entre com o valor de A: ')
    b = input('Entre com o valor de B: ')
    
    if not a.replace('.','',1).isdigit() or not b.replace('.','',1).isdigit():
        print('Por favor,entre com um numore valido.')
        continue
    
    a = float(a)
    b = float(b)
    
    resultado_soma = somar(a,b)
    resultado_produto = multi(a,b)
    resultado_divisão,erro = dividir(a,b)
    
    print('-'*70)
    print('CALCULOS MATEMATICA')
    print('='*70)
    print(f'Calculos da soma: {resultado_soma}')
    print(f'Calculos do produto: {resultado_produto}')
    print(f'Calculos da divisão: {resultado_divisão}, {erro}')
    print('-'*70)
    
    sair = input('Deseja sair do programa? (s/n): ').strip().lower()
    if sair == 's':
        print('Saindo do programa...')
        break