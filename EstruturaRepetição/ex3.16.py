# -*- coding: utf-8  -*-

"""
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial
várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
"""

print("==============================================================")

num = input("Digite um numero (0 a 16) para calcularmos o seu fatorial ou digite s para sair: ")
while num != "s":
    numCalc = int(num)
    fatorial = 1
    while numCalc > 0:
        fatorial = fatorial*numCalc
        numCalc = numCalc - 1   
    print("Fatorial de ", num, " = ", fatorial)
    num = input("digite um numero (0 a 16) para calcularmos o seu fatorial ou digite s para sair: ")


print("==============================================================")
