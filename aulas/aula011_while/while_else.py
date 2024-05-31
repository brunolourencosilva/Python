import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE CONTROLE WHILE ELSE')
print('='*70)
print()

print()

contador = 1

while contador <7:
    print("Contador é:", contador)
    contador += 1
    
    #se eu tirar essa condicional o else sera executado
    if contador == 4:
        print(f'contador chegou em {contador}.Break no while!!')
        break
else:
    print("While finalizado!")
    
print()