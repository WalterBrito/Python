# -*- coding: utf-8 -*-

# Pesquisa em uma lista
# Pesquisa feita pelo indice, retorna 2, pois é a posição do 25
# retorna None, pois 27 não existe na lista.

print(60 * "=")


def pesquise(lista, valor):
    if valor in lista:
        return lista.index(valor)
    return None

l = [10, 20, 25, 30]
print(pesquise(l, 25))
print(pesquise(l, 27))

print(60 * "=")
