# -*- coding: utf-8 -*-

"""
Escreva um programa que leia duas strings e gere uma terceira, 
na qual os caractereres da segunda foram retirados da primeira.

1° string: AATTGGAA
2° string: TG
3° string: AAAA
"""

print(60 * "=")


primeira = input("Digite a 1° palavra: ")
segunda = input("Digite a 2° palavra: ")

terceira = ""

for p in primeira:
    if p in segunda:
        terceira += p


if terceira == "":
    print("Caracteres foram removidos ")
else:
    print("Caracteres %s foram removidos de %s, gerando: %s" %
          (segunda, primeira, terceira))


print(60 * "=")
