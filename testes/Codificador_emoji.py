import string
import os



# Emojis para representar o alfabeto (Você pode substituir por outros emojis)
alfabeto_emojis = [
    '😀', '😁', '😂', '🤣', '😃', '😄', '😅', '😆', '😇', '😈',
    '😉', '😊', '😋', '😎', '😍', '😏', '😐', '😑', '😒', '😓',
    '😔', '😕', '😖', '😗', '😘', '😙', '😚', '😛', '😜', '😝',
    '😞', '😟', '😠', '😡', '😢', '😣', '😤', '😥', '😦', '😧',
    '😨', '😩', '😪', '😫', '😬', '😭', '😮', '😯', '😰', '😱',
    '😲', '😳', '😴', '😵', '😶', '😷', '😸', '😹', '😺', '😻',
    '😽', '😾', '😿', '🙀', '🙁', '🙂', '🙃', '🙄', '🙅', '🙆',
    '🙇', '🙈', '🙉', '🙊', '🙋', '🙌', '🙍', '🙎', '🙏', '🤑',
    '🤐', '🤓', '🤔', '🤕', '🤖', '🤗', '🤘', '🤙', '🤚', '🤛',
    '🤜', '🤝', '🤞', '🤟', '🤠', '🤡', '🤢', '🤣', '🤤', '🤥'
]

# Cria um mapeamento de letras para emojis
alfabeto = string.ascii_lowercase  # Alfabeto em minúsculas
mapeamento_emojis = dict(zip(alfabeto, alfabeto_emojis))

# Função para traduzir texto para emojis
def texto_para_emojis(texto):
    texto = texto.lower()  # Converte o texto para minúsculas
    return ''.join(mapeamento_emojis.get(char, char) for char in texto)

# Função para traduzir emojis de volta para texto
def emojis_para_texto(emojis):
    emojis_para_letras = {emoji: letra for letra, emoji in mapeamento_emojis.items()}
    return ''.join(emojis_para_letras.get(emoji, emoji) for emoji in emojis)

while True:
    os.system('cls')
    print('1 - CODIFICAR | 2 - DECODIFICAR')
    opacao = input('Deseja codificar ou decodificar? ')
    print('-'*70)
    if opacao == '1':
        frase = input('Infome a mensagem em texto: ')
        frase_emojis = texto_para_emojis(frase)
        print(f"Texto em emojis: {frase_emojis}")
        input('Pressione qualque tecla pra continuar')
    elif opacao == '2':
        binario = (input('Infome a mensagem codificada: '))
        frase_decodificada = emojis_para_texto(frase_emojis)
        print(f"Texto decodificado: {frase_decodificada}")
        input('Pressione qualque tecla pra continuar')
    else:
        print('ERRO!!')
        input('Pressione qualque tecla pra continuar')
# # Teste do programa
# frase = input('Infome a mensagem em texto: ')
# frase_emojis = texto_para_emojis(frase)
# print(f"Texto original: {frase}")
# print(f"Texto em emojis: {frase_emojis}")

# # Converter de volta
# frase_decodificada = emojis_para_texto(frase_emojis)
# print(f"Texto decodificado: {frase_decodificada}")