# -*- coding: utf-8 -*-

"""
Escreva um programa que pergunte o depósito inicial é a taxa 
de juros de uma poupança. Exiba os valores mês a mês para os 
24 primeiros meses. Escreva o total ganho com juros no periodo.
"""

print(60 * "=")

depósito = float(input("Digite o valor do depósito: "))
taxa = float(input("Digite o valor da taxa de juros: "))

mês = 1
saldo = depósito

while mês <= 24:
    saldo = saldo + (saldo * (taxa / 100))
    print("Saldo do mês %d é de R$%.2f" % (mês, saldo))
    mês += 1
print("O ganho obtido com os juros foi de R$%.2f" % (saldo - depósito))

print(60 * "=")
