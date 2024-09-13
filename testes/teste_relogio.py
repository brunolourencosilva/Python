import os
from datetime import datetime
import time


os.system('cls')

class Dados():
    def __init__(self, horas, minutos, segundos):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos
    
    def exibir_tempo(self):
        print(f"Hora atual: {str(self.horas).zfill(2)}:{str(self.minutos).zfill(2)}:{str(self.segundos).zfill(2)}")
        time.sleep(1)
        os.system('cls')
        

class BigBang(Dados):
    def __init__(self, horas, minutos, segundos):
        super().__init__(horas, minutos, segundos)
        
    def definir_tempo(self):
        
        agora = datetime.now()
        self.horas = agora.hour
        self.minutos = agora.minute
        self.segundos = agora.second
        self.exibir_tempo()
  
while True:
    tempo = BigBang(0,0,0)
    tempo.definir_tempo()
    os.system('cls')