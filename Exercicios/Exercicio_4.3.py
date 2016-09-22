# -*- coding: utf-8 -*-

"""
Escreva um programa que pergunte o salário do funcionário e calcule
o valor do aumento. Para salários superiores a R$ 1.250,00, calcule
um aumento de 10%. para inferiores ou iguais, a 15%.
"""


print(60 * "=")
salário = float(input("Digite o valor do salário: "))
aumento1 = (salário * 0.10)
aumento2 = (salário * 0.15)

if salário > 1250:
    print("O salário é maior que 1.250,00")
    print("O aumento é de %.2f reais." % aumento1)
    print("O novo salário é de R$ %.2f reais." % (salário + aumento1))
if salário <= 1250:
    print("O salário é menor que 1.250,00")
    print("O aumento é de %.2f reais." % aumento2)
    print("O novo salário é de R$ %.2f reais." % (salário + aumento2))

print(60 * "=")
