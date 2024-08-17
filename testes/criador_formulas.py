import random
import itertools
import time

# Lista de elementos químicos e seus símbolos
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

# Função para gerar uma fórmula química aleatória
# def gerar_formula():
#     # Escolhe dois elementos aleatórios
#     elemento1, nome1 = random.choice(elementos)
#     elemento2, nome2 = random.choice(elementos)
    
#     # Gera números aleatórios para as quantidades dos elementos
#     quantidade1 = random.randint(1, 3)  # Quantidades entre 1 e 3
#     quantidade2 = random.randint(1, 3)  # Quantidades entre 1 e 3
    
#     # Cria a fórmula química
#     formula = f"{elemento1}{quantidade1}{elemento2}{quantidade2}"
    
#     return formula

# # Gera e imprime uma fórmula química aleatória
# print(gerar_formula())

# Função para gerar combinações de fórmulas químicas
# Função para gerar combinações de fórmulas químicas
def gerar_formulas(elementos, max_combinacoes=3):
    formulas = set()
    for r in range(1, max_combinacoes + 1):
        for combinacao in itertools.combinations_with_replacement(elementos, r):
            # Contar a quantidade de cada elemento na combinação
            formula = {}
            for elemento in combinacao:
                if elemento in formula:
                    formula[elemento] += 1
                else:
                    formula[elemento] = 1
            
            # Criar a fórmula química a partir da contagem de elementos
            formula_str = ''.join(f'{e}{formula[e] if formula[e] > 1 else ""}' for e in sorted(formula))
            formulas.add(formula_str)
    
    return formulas

# Gera fórmulas e imprime com um atraso
def imprimir_formulas_com_atraso(formulas, atraso=1):
    for formula in sorted(formulas):
        print(formula)
        time.sleep(atraso)

# Gera fórmulas e imprime
formulas = gerar_formulas(elementos, max_combinacoes=3)
imprimir_formulas_com_atraso(formulas, atraso=1)