import os


os.system('cls')


def binario_para_texto(binario):
    binario = binario.replace(" ", "")  # Remove espaços
    texto = ""
    for i in range(0, len(binario), 8):  # Processa cada byte (8 bits)
        byte = binario[i:i+8]  # Pega o byte atual
        if len(byte) == 8:  # Garante que o byte tem 8 bits
            # Converte para decimal e depois para caractere
            texto += chr(int(byte, 2))
    return texto

def texto_para_binario(texto):
    binario = ""
    for caractere in texto:
        binario += format(ord(caractere), '08b') + " "  # Converte cada caractere para binário e adiciona um espaço
    return binario.strip()  # Remove o espaço extra no final

while True:
    os.system('cls')
    print('1 - CODIFICAR | 2 - DECODIFICAR')
    opacao = input('Deseja codificar ou decodificar? ')
    print('-'*70)
    if opacao == '1':
        texto = input('Infome a mensagem em texto: ')
        binario = texto_para_binario(texto)
        print(binario)
        input('Pressione qualque tecla pra continuar')
    elif opacao == '2':
        binario = (input('Infome a mensagem em binario: '))
        print(binario_para_texto(binario))
        input('Pressione qualque tecla pra continuar')
    else:
        print('ERRO!!')
        input('Pressione qualque tecla pra continuar')