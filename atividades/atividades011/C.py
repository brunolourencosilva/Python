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
        
    def media_notas(self,nota1, nota2, nota3, nota4):
        media = (nota1 + nota2 + nota3 + nota4) / 4
 
        return media
        

print('-'*70)
print('INFORME AS NOTAS')
nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))
nota3 = float(input('3ª nota: '))
nota4 = float(input('4ª nota: '))

resultado = Calcular(nota1, nota2, nota3, nota4)

print('-'*70)
print('-----NOTAS------------')
print(f'1ª NOTA: {nota1} | 2ª NOTA: {nota2}'
      F'3ª NOTA: {nota3} | 4ª NOTA: {nota4}')
print('-'*70)
print(f'MEDIA: {resultado.media_notas(nota1, nota2, nota3, nota4)}')