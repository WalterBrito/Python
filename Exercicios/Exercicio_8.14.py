# -*- coding: utf-8 -*-

"""
utilizando a função type, escreva uma função recursiva que imprima 
os elementos de uma lista. Cada elemento deve ser impresso separadamente,
um por linha. Considere o caso de listas dentro de listas, 
como = L[1, [2, 3, 4, [5, 6, 7]]]. A cada nivel, imprima a lista mais a 
direita, como fazemos ao identar blocos em python. Dica: envie o nivel atual 
como parâmetro e utiĺize-o para calcular a quantidade de espaços em branco a 
esquerda de cada elemento. 
"""

print(60 * "=")

espaçosPorNivel = 4


def imprimeElementos(l, nivel=0):
    espaços = ' ' * espaçosPorNivel * nivel

    if type(l) == list:
        print(espaços, "[")

        for e in l:
            imprimeElementos(e, nivel + 1)
        print(espaços, "]")
    else:
        print(espaços, l)

lista = [1, [2, 3, 4, [5, 6, 7]]]
imprimeElementos(lista)


print(60 * "=")
