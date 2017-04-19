# -*- coding: utf-8 -*-

"""
Escreva um programa para aprovar um empréśtimo bancário para
a compra de uma casa. O programa deve perguntar o valor da
casa a comprar, o salário  é a quantidade de anos a pagar.
O valor da prestação mensal não pode ser superior a 30%  do
salário. Calcule o valor da prestação como sendo o valor da
casa a comprar divido pelo número de meses a pagar.
"""

print(60 * "=")

valCasa = float(input("Digite o valor da casa: "))
salário = float(input("Qual o valor do salário: "))
qntAnos = int(input("Digite a quantidade de anos a pagar: "))

nMeses = qntAnos * 12
valPrest = (valCasa / nMeses)

if valPrest > salário * 0.3:
    print("Empréstimo não efetuado!")
    print("O valor da prestação é superior a 30%  do salário.")
else:
    print("Empréstimo efetuado com sucesso.")
    print("Valor da prestação: R$ %.2f" % valPrest)


print(60 * "=")
