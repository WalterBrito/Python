# -*- coding: utf-8 -*-

"""
Crie um programa que leia um arquivo-texto e elimine os espaços
repetidos entre palavras e no fim das linhas. O arquivo de saida
também não deve ter mais de uma linha em branco repetida.
"""

print("=" * 60)

import sys

if len(sys.argv) != 3:
    print("\n Python entrada saida\n\n\n")
    sys.exit(1)

entrada = sys.argv[1]
saida = sys.argv[2]

arquivo = open(entrada, "r", encoding="utf-8")
arq_saida = open(entrada, "r", encoding="utf-8")
branco = 0

for linha in arquivo:
    """ Elimina espaços a direita substitua por strip se também
    quiser eliminar espaços a esquerda"""
    linha = linha.rstrip()
    linha = linha.replace(" ", "")

    if linha == "":
        # Conta linhas em branco
        branco += 1
    else:
        # Se a linha não está em branco, zera o contador
        branco = 0
    # não escreve a partir da segunda linha em branco    
    if branco < 2:    
        arq_saida.write(linha + "\n")


arquivo.close()
arq_saida()

print("=" * 60)
