# -*- coding: utf-8 -*-

"""
Modifique a questão anterior para pesquisar dois valores, Em vez de apenas
p, leia outro valor v que também será procurado. Ba impressão, indique qual
dos dois valores foi achado primeiro. 
"""

print(60 * "=")

l = [15, 7, 27, 39]

p = int(input("Digite o valor de p procurar: "))
v = int(input("Digite o valor de v procurar: "))
x = 0
achouP = -1
achouV = -1
primeiro = 0

while x < len(l):
    if l[x] == p:
        achouP = x
    if l[x] == v:
        achouV = x
    x += 1

if achouP != -1:
    print("p: %d enconrtrado na posição %d" % (p, achouP))
else:
    print("p: %d não encontrado." % p)

if achouV != -1:
    print("v: %d enconrtrado na posição %d" % (v, achouV))
else:
    print("v: %d não encontrado." % v)

# Verifica se ambos foram encontrados

if achouP != -1 and achouV != -1 :
    """Como achouP e achouV guardam a posição onde 
    foram encontrados"""

    if achouP <= achouV:
        print("p foi encontrado primeiro.")
    else:
        print("v foi encontrado primeiro.")

print(60 * "=")

