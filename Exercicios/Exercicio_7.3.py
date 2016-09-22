# -*- coding: utf-8 -*-

"""
Escreva um programa que leia duas strings e gere uma terceira
apenas com os caracteres que aparecem em uma delas.

1° string: CTA
2° string: ABC
3° string: BT

A ordem dos caracteres da terceira string não é importante.
"""

print(60 * "=")

primeira = input("Digite a 1° palavra: ")
segunda = input("Digite a 2° palavra: ")
terceira = ""

# Para cada letra na primeira string
for letra in primeira:
    if letra not in segunda and letra not in terceira:
        terceira += letra

# Para cada letra na primeira string
for letra in segunda:
    if letra not in primeira and letra not in terceira:
        terceira += letra

if terceira == "":
    print("Caracterers incomuns não encontrados.")
else:
    print("Caracteres incomum: %s" % terceira)

print(60 * "=")