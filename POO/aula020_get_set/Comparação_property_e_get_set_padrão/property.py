class MinhaClasse:
    def __init__(self,valor):
        self._atributo = valor
    
    @property
    def atributo(self):
        return self._atributo
    
    @atributo.setter
    def atributo(self,valor):
        self._atributo = valor

obj = MinhaClasse(10)
# O atributo trabalha como uma variavel
obj.atributo = 20 # (set)
# Saida semelhante a uma variavel
print(obj.atributo) # (get)