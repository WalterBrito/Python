# -*- coding: utf-8 -*-

"""
Faça um programa que calcule o aumento de um salário. 
Ele deve solicitar o valor do salaŕio e a porcentagem
do aumento. Exiba o valor do aumento e do novo salário.
"""

print(60 * "=")

salario = float(input("Digite o valor do salario: "))
porcAumento = float(input("Digite o valor da porcentagem: "))


aumento = (salario * porcAumento / 100)
nSalario = salario + aumento

print("O aumento e de %.2f" % aumento)
print("Salario com aumento: R$ %.2f" % nSalario)

print(60 * "=")
