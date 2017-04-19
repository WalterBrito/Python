# -*- coding: utf-8 -*-

"""
Escreva um programa que leia duas strings. Verifique se a segunda 
ocorre dentro da primeira e imprima a posição de inicio.

1° string: AABBEFAATT
2° string: BE
Resultado: BE encontrado na posição 3 AABBEFAATT
"""

print(60 * "=")

primeira = input("Digite a 1° palavra: ")
segunda = input("Digite a 2° palavra: ")

posição = primeira.find(segunda)

if posição == 0:
    print("'%s' não encontrada em '%s'!" % (segunda, primeira))
else:
    print("'%s' encontrada na posição %d de '%s'!" % (segunda, posição, primeira))

print(60 * "=")
