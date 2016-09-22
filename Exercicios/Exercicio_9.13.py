# -*- coding: utf-8 -*-

"""
Crie um programa que imprima as linhas de um arquivo. Esse programa deve receber 
três parâmetros pela linha de comando: O nome do arquivo, a linha inicial e a última 
linha a imprimir.  
"""

print("=" * 60)

import sys

# Verifica se os paramêtros foram passados
if (len(sys.argv) != 4):
    # Lembre-se de que o nome do programa é o primeiro da lista
    print("\nPython nomeDoArquivo inicio fim\n\n")
else:
    nome = sys.argv[1]
    inicio = int(sys.argv[2])
    fim = int(sys.argv[3])
    arquivo = open(argv[3])

    for linha in arquivo.readlines()[inicio - 1:fim]:
        """Como a linha termina com ENTER, retiramos o último caractere
        antes de imprimir"""
        print(linha[:-1])

    arquivo.close()

print("=" * 60)
