# -*- coding: utf-8 -*-

"""
Faça um programa para imprimir 40 vezes o simbolo de = se este 
for o primeiro caractere da linha. Adicione também a opção para
parar de imprimir até que se pressione qualquer tecla cada vez
que uma linha iniciar com . como do arquivo original.
"""

print(60 * "-")

largura = 79
entrada = open("entrada.txt")

for linha in entrada.readlines():
    if linha[0] == ";":
        continue 
    elif linha[0] == ">":
        print(linha[1:].rjust(largura))
    elif linha[0] == "*":
        print(linha[1:].center(largura))
    elif linha[0] == "=":
        print(linha[:1] * 40)
    elif linha[0] == ".":
        input("Digite uma tecla para sair: ")
        print()            
    else:
        print(linha)

entrada.close()                  


print(60 * "-")