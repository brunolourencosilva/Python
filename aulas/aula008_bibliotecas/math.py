# IMportando as bibliotecas
import os
import math

# Limpando o terminal
os.system('cls')

print('-'*70)
print('Estudos da bibliotecas matemática math')
print('='*70)
print()

#declaração
base = 2
expoente = 3
angulo = 30
radicando = 81
co = 5   #cateto oposto
ca = 10  #cateto adjente

#processamento
potencia = math.pow(base, expoente)
raizQuadrada = math.sqrt(radicando)
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
hipotenusa = math.hypot(co, ca)

#saida
print(f'{base} elevada a {expoente} é igual a: {potencia}')
print(f'A raiz quadrada de {radicando} é: {raizQuadrada}')
print(f'O seno de {angulo} é: {seno:.2f}')
print(f'O cosseno de {angulo} é: {cosseno:.2f}')
print(f'A tangente de {angulo} é: {tangente:.2f}')
print(f'O valor de hipotenusa é: {hipotenusa:.2f}')
print(f'-'*70)
