import os


os.system('cls')


# Dicionários de mapeamento para codificação e decodificação
mapa_codificacao = {
    'a': '♠', 'b': '♣', 'c': '♥', 'd': '♦', 'e': '★', 'f': '☆',
    'g': '☀', 'h': '☁', 'i': '☎', 'j': '☂', 'k': '☃', 'l': '☺',
    'm': '☻', 'n': '♞', 'o': '⚑', 'p': '✈', 'q': '✉', 'r': '✖',
    's': '✦', 't': '✧', 'u': '✔', 'v': '✩', 'w': '✪', 'x': '✫',
    'y': '✬', 'z': '✭', ' ': '␣', '.': '⊙', ',': '⚫', '!': '⚡'
}

# Criando o dicionário inverso para decodificação
mapa_decodificacao = {v: k for k, v in mapa_codificacao.items()}

# Função para codificar a frase
def codificar(frase):
    frase_codificada = ''.join(mapa_codificacao.get(char, char) for char in frase.lower())
    return frase_codificada

# Função para decodificar a frase
def decodificar(frase_codificada):
    frase_decodificada = ''.join(mapa_decodificacao.get(char, char) for char in frase_codificada)
    return frase_decodificada

# Exemplo de uso
frase_usuario = input("Digite uma frase para codificar: ")
frase_codificada = codificar(frase_usuario)
print("Frase codificada:", frase_codificada)

frase_decodificada = decodificar(frase_codificada)
print("Frase decodificada:", frase_decodificada)
