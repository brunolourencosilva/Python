import os


os.system('cls')


def soma_valores(a,b,c):
    a+=1
    b+=1
    c+=1
    
    return a,b,c

valor_1,valor_2,valor_3 = soma_valores(10,10,10)

print(f'{valor_1},{valor_2},{valor_3}')