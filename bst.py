from collections import deque
from node import Node


class BinarySearchTree:
    def __init__(self):
        self.raiz = None

    def inserir(self, nome, idade):
        novo_nodo = Node(nome, idade)

        if self.raiz is None:
            self.raiz = novo_nodo
        else:
            self._inserir_recursivo(self.raiz, novo_nodo)

    def _inserir_recursivo(self, atual, novo):
        if novo.idade < atual.idade:
            if atual.esquerda is None:
                atual.esquerda = novo
            else:
                self._inserir_recursivo(atual.esquerda, novo)

        elif novo.idade > atual.idade:
            if atual.direita is None:
                atual.direita = novo
            else:
                self._inserir_recursivo(atual.direita, novo)

        else:
            if novo.nome < atual.nome:
                if atual.esquerda is None:
                    atual.esquerda = novo
                else:
                    self._inserir_recursivo(atual.esquerda, novo)
            else:
                if atual.direita is None:
                    atual.direita = novo
                else:
                    self._inserir_recursivo(atual.direita, novo)

    
    def em_ordem(self, nodo):
        if nodo:
            self.em_ordem(nodo.esquerda)
            print(f"Nome: {nodo.nome}   - Idade: {nodo.idade}")
            self.em_ordem(nodo.direita)

    
    def pre_ordem(self, nodo):
        if nodo:
            print(f"Nome: {nodo.nome}   - Idade: {nodo.idade}")
            self.pre_ordem(nodo.esquerda)
            self.pre_ordem(nodo.direita)

    
    def pos_ordem(self, nodo):
        if nodo:
            self.pos_ordem(nodo.esquerda)
            self.pos_ordem(nodo.direita)
            print(f"Nome: {nodo.nome}   - Idade: {nodo.idade}")

    
    def em_ordem_invertido(self, nodo):
        if nodo:
            self.em_ordem_invertido(nodo.direita)
            print(f"Nome: {nodo.nome}   - Idade: {nodo.idade}")
            self.em_ordem_invertido(nodo.esquerda)

    
    def em_largura(self):
        if self.raiz is None:
            return

        fila = deque()
        fila.append(self.raiz)

        while fila:
            atual = fila.popleft()
            print(f"Nome: {atual.nome}   - Idade: {atual.idade}")

            if atual.esquerda:
                fila.append(atual.esquerda)

            if atual.direita:
                fila.append(atual.direita)
