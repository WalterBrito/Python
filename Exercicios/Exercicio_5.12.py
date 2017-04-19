# -*- coding: utf-8 -*-


"""
Altere o programa anterior de forma a perguntar também o
valor depositado. Esse valor será depositado no inicio de 
cada mês, e você deve considera-lo para o calculo de juros
do mês seguinte.
"""

print(60 * "=")

depósito = float(input("Digite o valor do depósito: "))
taxa = float(input("Digite o valor da taxa de juros: "))
depMensal = float(input("Digite o valor depósitado: "))

mês = 1
saldo = depósito

while mês <= 24:
    saldo = saldo + (saldo * (taxa / 100)) + depMensal
    print("Saldo do mês %d é de R$%.2f" % (mês, saldo))
    mês += 1
print("O ganho obtido com os juros foi de R$%.2f" % (saldo - depósito))

print(60 * "=")
