import os


os.system('cls')


# Definindo uma função
def calcular_velocidade_media(distancia, tempo):
    # Vm ΔS/ΔT
    velocidade_media = distancia / tempo
    metros = distancia/100
    km = distancia/1000
    
    verificação = input('Esse valor é metro ou kilometro?: ')
    if verificação == 'metro':
        metros = distancia/100
        velocidade_media = metros/tempo
    
    return velocidade_media

distancia = float(input('Digite a distancia pecorrida (em km): '))
    
tempo = float(input('Digite o tempo gasto (em horas): '))


# Calcular a velocidade media usando a função criada
velocidade = calcular_velocidade_media(distancia, tempo)

# Exibir o resultado
print(f'A velocidade media é {velocidade:.2f} Km')