import os


class Veiculo:
    def __init__(self,marca,modelo,ano,cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        
# Solicitando entrada de dados do usuairo
os.system('cls')
print('-'*70)
marca = input('Digite a marca do veiculo: ')
modelo = input('Digite o modelo do veiculo: ')
ano = int(input('Digite o ano do veiculo: '))
cor = input('Digite a cor do veiculo: ')

# Criando um objeto da classe Veiculo com os dados fornecidos pelo usuario
veiculo1 = Veiculo(marca,modelo,ano,cor)

# Acessando e imprimindo atributos do objeto
print('-'*70)
print('\nInformações do Veiculos: ')
print('='*70)
print(f'Marca: {veiculo1.marca}')
print(f'Modelo: {veiculo1.modelo}')
print(f'Ano: {veiculo1.ano}')
print(f'Cor: {veiculo1.cor}')
print('-'*70)