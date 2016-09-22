# -*- coding: utf-8 -*-

"""
Crie um programa que leia os arquivos pares.txt e impares.txt e
que crie um só arquivo paresimpares.txt com todas as linhas dos outros
dois arquivos, de forma a preservar a ordem númerica.
"""

print(60 * "=")


def lêNúmero(arquivo):

    while True:
        número = arquivo.readline()
        # Verifica se conseguiu lê algo
        if número == "":
            return None
        # Ignora linhas em branco
        if número.strip() != "":
            return int(número)


def escreveNúmero(arquivo, n):
    arquivo.write("%d\n" % n);


pares = open("pares.txt", "r")
impares = open("impares.txt", "r")
paresimpares = open("paresimpares.txt", "w")
numPar = lêNúmero(pares)
numImpar = lêNúmero(impares)

while True:
    """ Termina se ambos forem None"""
    if numPar == None and numImpar == None:
        break
    if numPar != None and (numImpar == None or numPar <= numImpar):
        escreveNúmero(paresimpares, numPar)
        numPar = lêNúmero(pares)
    if numImpar != None and (numPar == None or numImpar <= numPar):
        escreveNúmero(paresimpares, numImpar)
        numImpar = lêNúmero(impares)

paresimpares.close()
pares.close()
impares.close()



print(60 * "=")
