# -*- coding: utf-8 -*-

"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11%  para o Imposto de Renda, 8%  para o INSS e
5%  para o sindicato, faça um programa que nos dê:
a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido.
e. calcule os descontos e o salário líquido, conforme a tabela
abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

print("======================================================")


horaTrab = int(input("Quanto voce ganha por hora?: "))
horaTrabMes = int(input("Digite o numero de horas trabalhadas (Mes): "))

salarioBruto = horaTrab * horaTrabMes
impostoRenda = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05

print("Salario Bruto: R$ %.2f" % salarioBruto)
print("Voce pagou ao imposto de renda: %.2f" % impostoRenda)
print("Voce pagou ao inss: R$ %.2f" % inss)
print("Voce pagou ao sindicato: %.2f" % sindicato)
print("Salario Liquido: R$ %.2f" % (salarioBruto - impostoRenda - inss - sindicato))


print("======================================================")
