import os


os.system('cls')

# Definindo uma função para empacotar
def empacotar(*lista_numeros):
    print(f'empacotados: {lista_numeros}')
    for i in lista_numeros:
        print(f'Empacotados: {i}')

# Invocando a função empacotar
empacotar(1,2,3,4,5)

# Desempacotano (lista)
def desempacotar(a,b,c,d,e):
    print('Desempacotar: ')
    print(f'A = {a}')
    print(f'B = {b}')
    print(f'C = {c}')
    print(f'D = {d}')
    print(f'e = {e}')
    
# invocando a função desempacotador
lista_numero = [1,2,3,4,5]
desempacotar(*lista_numero) # *args

# Packing Dicionario
def empacotar_dicionario(**dados_dicionarios): # **Kwargs
    print(f'Dados do dicinario: {dados_dicionarios}')
    for k,v in dados_dicionarios.items():
        print(f'Chave: {k}, valor: {v}')

print('-'*70)
print('---Dicionario')
empacotar_dicionario(nome = 'Juquinha', idade = 70,peso = 70.5)

# Unpacking Dicionario
print('-'*70)
def desempacotar_dicionario(nome,idade,peso):
    print(f'Nome = {nome}')
    print(f'Idade = {idade}')
    print(f'Peso = {peso}')
    
dicionario = dict(nome = 'Maria',idade = 70,peso = 70.5)
desempacotar_dicionario(**dicionario)
print()