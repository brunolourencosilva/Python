# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:02/09/2024
# atividade0011 C-Faça um programa que peça 4 notas, após a entrada de dados calcular a média das notas digitadas.
import os


os.system('cls')

class Calcular:
    def __init__(self, nota1, nota2, nota3, nota4):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
    
    def media_notas(self):
        try:
            if float(nota1) < 0 or float(nota2) < 0 or float(nota3) < 0 or float(nota4) < 0:
                return "Insira valores maiores ou igual a zero"
            else:
                media = (float(self.nota1) + float(self.nota2) + float(self.nota3) + float(self.nota4)) / 4
                return f'A media é: {media}'

        except (TypeError,ValueError):
            return 'Insira apenas valores numéricos'



print('-'*70)
print('INFORME AS NOTAS')
nota1 = input('1ª nota: ')
nota2 = input('2ª nota: ')
nota3 = input('3ª nota: ')
nota4 = input('4ª nota: ')

resultado = Calcular(nota1, nota2, nota3, nota4)
media = resultado.media_notas()

print('-'*70)
print('-----NOTAS------------')
print(f'1ª NOTA: {nota1} | 2ª NOTA: {nota2} | '
F'3ª NOTA: {nota3} | 4ª NOTA: {nota4}')
print('-'*70)
print(media)
    