#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:26/04/2024
#atividade 002 Letra B
import os 
 
 
os.system('cls')

print('-'*70)
print('software de análise estatística ')
print('='*70)

#entrada de dados
print('ENTRADA DE DADOS\n')

valor1 = float(input('DIGITE O 1º VALOR: '))
valor2 = float(input('DIGITE O 2º VALOR: '))
valor3 = float(input('DIGITE O 3º VALOR: '))
print('-'*70)

#condicional

#maior valor
if (valor1 > valor2 and valor1 > valor3):
    print(f'O VALOR {valor1} É MAIOR ')
elif (valor2 > valor1 and valor2 > valor3):
    print(f'O VALOR {valor2} É MAIOR ')
else:
    print(f'O VALOR {valor3} É MAIOR ')
print('-'*70)

#menor valor    
if (valor1 < valor2 and valor1 <valor3):
    print(f'O VALOR {valor1} É MENOR ')
elif (valor2 < valor1 and valor2 < valor3):
    print(f'O VALOR {valor2} É MENOR ')
else:
    print(f'O VALOR {valor3} É MENOR ')
print('-'*70)

#valores iguais
if (valor1 == valor2 and valor1 ==valor3 and valor2 == valor3):
    print(f'OS VALORES {valor1}, {valor2} E {valor3} SÃO IGUAIS')
else:
    print(f'OS VALORES {valor1}, {valor2} E {valor3} SÃO DIFERENTES' )
print('-'*70)