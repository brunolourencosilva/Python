import csv
import os


# Nome do arquivo CSV
arquivo = "aulas/aula018_arquivos/alunas.csv"

# Lista para armazenar os dados
lista = []

# Abrindo o arquivo CSV para leitura
with open(arquivo, 'r') as arquivos_csv:
    # Criando um leitor de csv que le o arquivo como dicionario
    leitura = csv.DictReader(arquivos_csv,delimiter=';')
    
    # Iterando sobre cada linha (registro) no arquivo CSV e adicionando a lista
    for linha in leitura:
        lista.append(linha)
        
os.system('cls')
print('-'*70)
print('Nome\tTelefone\tCidade')
print('='*70)

# Exibindo a lista resultante
for registro in lista:
    flag = 0
    for k, v in registro.items():
        print(v, end='\t')
        flag += 1
        if flag == 3:
            print()
print('-'*70)