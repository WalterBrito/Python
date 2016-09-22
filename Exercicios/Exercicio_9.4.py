# -*- coding: utf-8 -*-

"""
Crie um programa que receba o nome de dois arquivos como parâmetros
da linha de comando e que gere um arquivo de saida com as linhas
do primeiro e do segundo arquivo.  
"""

print(60 * "=")

import sys

# Verifica se os paramêtros foram passados
if(len(sys.argv) != 4):
    # O nome do programa é o primeiro da lista
    print("\nPython.py primeiro segundo saida\n\n")
else:
    primeiro = open(sys.argv[1], "r")
    segundo = open(sys.argv[2], "r")
    saida = open(sys.argv[3], "w")

    # Funciona de forma similar ao readlines
    for l1 in primeiro:
        saida.write(l1)
    for l2 in segundo:
        saida.write(l2)

    primeiro.close()
    segundo.close()
    saida.close()


print(60 * "=")
