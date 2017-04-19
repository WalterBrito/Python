# -*- coding: utf-8 -*-

"""
Escreva um programa que leia três strings. Imprima o resultado
da  substituição na primeira, dos caracteres da segunda pelos
da terceira. 

1° string: AATTCGAA
2° string: TG
3° string: AC

Resultado: AAAACCAA
"""

print(60 * "=")

primeira = input("Digite a 1° palavra: ")
segunda = input("Digite a 2° palavra: ")
terceira = input("Digite a 3° palavra: ")

if len(segunda) == len(terceira):
    resultado = ""

    for letra in primeira:
        posição = segunda.find(letra)

        if posição != -1:
            resultado += terceira[posição]
        else:
            resultado += letra

    if resultado == "":
        print("Todos os caracteres foram removidos.")
    else:
        print("Os caracteres %s foram substituidos por %s em %s, gerando: %s" %
              (segunda, terceira, primeira, resultado))
else:
    print("ERRO: A segunda e a terceira string devem ter o mesmo tamanho.")

print(60 * "=")
