import random
import time

class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.nivel = 1
        self.experiencia = 0
        self.itens = {'Poção de Vida': 3}

    def atacar(self, inimigo):
        if inimigo.esquivar():
            print(f"{inimigo.nome} esquivou do ataque!")
            return

        dano = self.ataque - inimigo.defesa
        dano = max(1, dano)  # Garante que o dano seja no mínimo 1

        if self.critico():
            dano *= 2
            print(f"Ataque crítico de {self.nome}!")

        inimigo.vida -= dano
        print(f"{self.nome} ataca {inimigo.nome} e causa {dano} de dano!")

    def defender(self):
        print(f"{self.nome} se prepara para defender!")
        self.defesa *= 2

    def usar_item(self):
        if self.itens['Poção de Vida'] > 0:
            self.vida += 10
            self.itens['Poção de Vida'] -= 1
            print(f"{self.nome} usou uma Poção de Vida e recuperou 10 de vida!")
        else:
            print("Você não tem mais Poções de Vida!")

    def critico(self):
        return random.random() < 0.2  # 20% de chance de ataque crítico

    def esquivar(self):
        return random.random() < 0.1  # 10% de chance de esquivar

    def receber_experiencia(self, exp):
        self.experiencia += exp
        print(f"{self.nome} recebe {exp} de experiência!")
        if self.experiencia >= 10:
            self.nivel_up()

    def nivel_up(self):
        self.nivel += 1
        self.vida += 5
        self.ataque += 2
        self.defesa += 1
        self.experiencia = 0
        print(f"{self.nome} subiu para o nível {self.nivel}!")

class Inimigo:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, personagem):
        if personagem.esquivar():
            print(f"{personagem.nome} esquivou do ataque!")
            return

        dano = self.ataque - personagem.defesa
        dano = max(1, dano)  # Garante que o dano seja no mínimo 1

        if self.critico():
            dano *= 2
            print(f"Ataque crítico de {self.nome}!")
        
        personagem.vida -= dano
        print(f"{self.nome} ataca {personagem.nome} e causa {dano} de dano!")

    def critico(self):
        return random.random() < 0.2  # 20% de chance de ataque crítico

    def esquivar(self):
        return random.random() < 0.1  # 10% de chance de esquivar

def gerar_inimigo():
    nomes = ["Goblin", "Orc", "Lobo Selvagem", "Esqueleto", "Zumbi"]
    nome = random.choice(nomes)
    vida = random.randint(5, 15)
    ataque = random.randint(1, 5)
    defesa = random.randint(1, 3)
    return Inimigo(nome, vida, ataque, defesa)

def batalha(personagem, inimigo):
    print(f"\nA batalha começa! {personagem.nome} VS {inimigo.nome}")
    while personagem.vida > 0 and inimigo.vida > 0:
        # Turno do jogador
        print(f"\nVida de {personagem.nome}: {personagem.vida}")
        print(f"Vida de {inimigo.nome}: {inimigo.vida}")
        acao = input("\nEscolha sua ação:\n1. Atacar\n2. Defender\n3. Usar Poção de Vida\nEscolha: ")
        
        if acao == '1':
            personagem.atacar(inimigo)
        elif acao == '2':
            personagem.defender()
        elif acao == '3':
            personagem.usar_item()
        else:
            print("Escolha inválida, turno perdido!")

        time.sleep(1)
        
        if inimigo.vida > 0:
            # Turno do inimigo
            personagem.defesa //= 2  # Reduz a defesa após o turno do jogador, se o jogador defendeu
            inimigo.atacar(personagem)

    if personagem.vida > 0:
        print(f"{personagem.nome} venceu a batalha!")
        personagem.receber_experiencia(5)
    else:
        print(f"{personagem.nome} foi derrotado...")

def missao(personagem):
    print(f"\n{personagem.nome} inicia uma nova missão!")
    inimigo = gerar_inimigo()
    batalha(personagem, inimigo)

def jogar():
    nome = input("Digite o nome do seu personagem: ")
    jogador = Personagem(nome, 20, 5, 3)

    while True:
        acao = input("\nO que deseja fazer?\n1. Nova Missão\n2. Ver Status\n3. Sair\nEscolha: ")
        if acao == '1':
            missao(jogador)
        elif acao == '2':
            print(f"\nStatus de {jogador.nome}:")
            print(f"Vida: {jogador.vida}")
            print(f"Ataque: {jogador.ataque}")
            print(f"Defesa: {jogador.defesa}")
            print(f"Nível: {jogador.nivel}")
            print(f"Experiência: {jogador.experiencia}/10")
            print(f"Poções de Vida: {jogador.itens['Poção de Vida']}")
        elif acao == '3':
            print("Saindo do jogo...")
            break
        else:
            print("Escolha inválida, tente novamente.")

if __name__ == "__main__":
    jogar()
