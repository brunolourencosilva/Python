import random
import time

# Lista de elementos químicos com símbolos e nomes
elementos = [
    ("H", "Hidrogênio"), ("He", "Hélio"), ("Li", "Lítio"), ("Be", "Berílio"),
    ("B", "Boro"), ("C", "Carbono"), ("N", "Nitrogênio"), ("O", "Oxigênio"),
    ("F", "Flúor"), ("Ne", "Neônio"), ("Na", "Sódio"), ("Mg", "Magnésio"),
    ("Al", "Alumínio"), ("Si", "Silício"), ("P", "Fósforo"), ("S", "Enxofre"),
    ("Cl", "Cloro"), ("Ar", "Argônio"), ("K", "Potássio"), ("Ca", "Cálcio"),
    ("Sc", "Escândio"), ("Ti", "Titânio"), ("V", "Vanádio"), ("Cr", "Cromo"),
    ("Mn", "Manganês"), ("Fe", "Ferro"), ("Co", "Cobalto"), ("Ni", "Níquel"),
    ("Cu", "Cobre"), ("Zn", "Zinco"), ("Ga", "Gálio"), ("Ge", "Germânio"),
    ("As", "Arsênio"), ("Se", "Selênio"), ("Br", "Bromo"), ("Kr", "Criptônio"),
    ("Rb", "Rubídio"), ("Sr", "Estrôncio"), ("Y", "Ítrio"), ("Zr", "Zircônio"),
    ("Nb", "Nióbio"), ("Mo", "Molibdênio"), ("Tc", "Tecnécio"), ("Ru", "Rutênio"),
    ("Rh", "Ródio"), ("Pd", "Paládio"), ("Ag", "Prata"), ("Cd", "Cádmio"),
    ("In", "Índio"), ("Sn", "Estanho"), ("Sb", "Antimônio"), ("Te", "Telúrio"),
    ("I", "Iodo"), ("Xe", "Xenônio"), ("Cs", "Césio"), ("Ba", "Bário"),
    ("La", "Lantânio"), ("Ce", "Cério"), ("Pr", "Praseodímio"), ("Nd", "Neodímio"),
    ("Pm", "Promécio"), ("Sm", "Samário"), ("Eu", "Europio"), ("Gd", "Gadolínio"),
    ("Tb", "Térbio"), ("Dy", "Disprósio"), ("Ho", "Hólmio"), ("Er", "Érbio"),
    ("Tm", "Túlio"), ("Yb", "Itérbio"), ("Lu", "Lutécio"), ("Hf", "Háfnio"),
    ("Ta", "Tântalo"), ("W", "Tungstênio"), ("Re", "Rênio"), ("Os", "Ósmio"),
    ("Ir", "Irídio"), ("Pt", "Platina"), ("Au", "Ouro"), ("Hg", "Mercúrio"),
    ("Tl", "Talco"), ("Pb", "Chumbo"), ("Bi", "Bismuto"), ("Po", "Polônio"),
    ("At", "Astato"), ("Rn", "Radônio"), ("Fr", "Francium"), ("Ra", "Radônio"),
    ("Ac", "Actínio"), ("Th", "Tório"), ("Pa", "Protactínio"), ("U", "Urânio"),
    ("Np", "Neptúnio"), ("Pu", "Plutônio"), ("Am", "Amerício"), ("Cm", "Curíum"),
    ("Bk", "Berkélio"), ("Cf", "Califórnio"), ("Es", "Einsteínio"), ("Fm", "Férmio"),
    ("Md", "Mendelevio"), ("No", "Nobelium"), ("Lr", "Laurêncio"), ("Rf", "Rutherfórdio"),
    ("Db", "Dubnío"), ("Sg", "Seabórgio"), ("Bh", "Bohriam"), ("Hs", "Hássio")
]

# Função para combinar dois elementos e formar um novo "elemento"
def combinar_elementos(elemento1, elemento2):
    novo_simbolo = elemento1[0] + elemento2[0]
    novo_nome = elemento1[1] + "-" + elemento2[1]
    return novo_simbolo, novo_nome

# Função para gerar elementos automaticamente
def gerar_elementos_automaticamente(intervalo=2):
    while True:
        elemento1 = random.choice(elementos)
        elemento2 = random.choice(elementos)
        novo_simbolo, novo_nome = combinar_elementos(elemento1, elemento2)
        print(f"Novo elemento gerado: {novo_nome} ({novo_simbolo})")
        time.sleep(intervalo)

# Executa o gerador de elementos automaticamente
gerar_elementos_automaticamente()