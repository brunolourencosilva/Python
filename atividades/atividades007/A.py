# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:17/06/2024
# atividade007 B-Após esta entrada de dados, faça o seguinte:
#• Mostre a quantidade de notas que foram lidas.
#• Exiba todas as notas na ordem em que foram informadas.
#• Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo da outra.
#• Calcule e mostre a soma das notas.
#• Calcule e mostre a média das notas.

import os


os.system('cls')

print('-'*70)
print('Programa de mostrar notas.')
print('='*70)

lista_notas = []
nota_lidas = 1
soma = 0
while True:
    #entrada
    notas = (input('informe a nota(pressione "s" ou "0" para sair): '.lower()))
    lista_notas.append(notas)
        #condicional
    print('='*70)
    if notas == 's' or notas == '0':
        break
    else:
        nota_lidas += 1

        print(f'Numeros das notas guardados........: {lista_notas}')#Imprimindo as notas que ja foram inseridas
        print(f'Quantidade de notas que foram lidas: {nota_lidas}')#.Imprimindo a quantidade de notas que ja foram inseridas
    
        nota_float = float(notas)
        soma += nota_float#..........................................Somando as notas
        print(f'Soma das notas.....................: {soma}')#......Imprimindo a soma das notas
        if nota_lidas > 0:
            media = soma / nota_lidas
            print(f'Media das notas....................: {media:.2f}')#......Imprimindo a media das notas
        else:
            print('Não foi possível calcular a média.')
    
        print('lista de notas revertidas:')#.........................Imprimindo a lista de nota invertida
        lista_notas.reverse()
        for notas in lista_notas:#...................................Imprimindo as notas invertidade uma embaixo da outra
            print(f'{notas}',end=('|'))
        continue