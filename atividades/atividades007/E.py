# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:17/06/2024
# atividade007 E-Crie uma lista com 6 nomes, depois verifique se o nome ‘Pedro’ está nessa lista.
import os


os.system('cls')

print('-'*70)
print('Uma lista com 6 nomes,que depois verifica\nse o nome ‘Pedro’ está nessa lista.')
print('='*70)

lista_nome = []

for i in range(6):
    nome = str(input('Digite um nome: '.lower()))
    lista_nome.append(nome)
    
if 'pedro' in lista_nome:
    print("O nome Pedro esta na lista")
else:
    print("O nome Pedro não esta na lista")