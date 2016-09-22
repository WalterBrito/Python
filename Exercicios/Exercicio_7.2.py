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
terceira = ""

for letra in primeira:
    if letra in segunda and letra not in terceira:
        terceira += letra

if terceira == "":
    print("Caracterers comuns não encontrados.")
else:
    print("Caracteres em comum: %s" % terceira)

print(60 * "=")
