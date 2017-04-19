# -*- coding: utf-8 -*-

"""
Escreva uma expressão para determinar se uma  pessoa deve ou não pagar
imposto. Considere que pagam imposto pessoas cujo salário é maior que R$
1.200,00.
"""

print(60 * "=")
salario = 1200
valor = float(input("Digite o valor do salario: "))

if valor > salario:
    print("Voce deve pagar imposto!")
else:
    print("Voce está isento(a) do imposto.")
print(60 * "=")