from bst import BinarySearchTree

arvore = BinarySearchTree()

pessoas = [
    ("Ana", 48),
    ("Rafael", 39),
    ("Clara", 21),
    ("Diego", 34),
    ("Bianca", 41),
    ("Thiago", 22),
    ("Renata", 60),
    ("Felipe", 55),
    ("Sandra", 70),
    ("Igor", 33)
]

for nome, idade in pessoas:
    arvore.inserir(nome, idade)

print("\nIn Order:")
arvore.em_ordem(arvore.raiz)

print("\nPre Order:")
arvore.pre_ordem(arvore.raiz)

print("\nPos Order:")
arvore.pos_ordem(arvore.raiz)

print("\nDec Order:")
arvore.em_ordem_invertido(arvore.raiz)

print("\nLargura:")
arvore.em_largura()
