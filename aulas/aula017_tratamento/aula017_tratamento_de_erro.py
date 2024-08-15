# ZeroDivisionError
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print('Erro: Divisão por zero!!!')

# ValueError
try:
    numero = int('Não é um numero')
except ValueError:
    print('Erro: Valor invalido!!!')

# TypeError
try:
    soma = '5' + 5
except TypeError:
    print('Erro: Tipo de dado incompativel!!!')

# IndexError
lista = [1,2,3]
try:
    item = lista[5]
except IndexError:
    print("Erro: Indice fora do intervalo da lista!!!")

# KeyError
dicionario = {'chave': 'valor'}
try:
    valor = dicionario['chave_inexistente']
except KeyError:
    print('Error: chave não encontrada no dicionario!!!')

# FileNotFoundError
try:
    with open('arquivo_inexistente.txt', 'r') as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print('Error: Arquivo não encotrado!!!')
    
# IOError
try:
    with open('arquivo.txt', 'w') as arquivos:
        conteudo = arquivos.read()
except IOError:
    print('Erro: Operação de E/S falhou!!!')

# AttributeError
class Exemplo:
    def __init__(self):
        self.atributo = 'valor'

objeto = Exemplo()
try:
    print(objeto.atributo_inexistente)
except AttributeError:
    print('Erro: Atributo não encontrado no objeto!!!')
    
# ImportError
try:
    import modulo_inexistente # type: ignore - Ignora o erro
except ImportError:
    print('Erro: Modulo não encontrado!!!')

# RuntimeError
try:
    raise RuntimeError('Este é um erro de execusão!!!')
except RuntimeError as e:
    print(f'Erro: {e}')