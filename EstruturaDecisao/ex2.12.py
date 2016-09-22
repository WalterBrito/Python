# -*- coding: utf-8 -*- 

"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
descontos são do Imposto de Renda, que depende do salário bruto (conforme
tabela abaixo) e 3%  para o Sindicato e que o FGTS corresponde a 11%  do Salário
Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido
corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao
usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
* Salário Bruto até 900 (inclusive) -  isento
* Salário Bruto até 1500 (inclusive) - desconto de 5%
* Salário Bruto até 2500 (inclusive) - desconto de 10%
* Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
Salário Bruto: (5 * 220)			: R$ 1100,00
(-) IR (5%)							: R$ 55,00				    	
(-) INSS ( 10%)						: R$ 110,00
FGTS (11%)							: R$ 121,00
Total de descontos					: R$ 165,00
Salário liquido						: R$ 935,00
"""

print("======================================================")

horas = input("Digite o numero de horas trabalhadas: ")
ghoras = input("Digite o ganho por horas: ")

bruto = ghoras * horas

cinco = (5 / 100.0) * bruto
dez = (10 / 100.0) * bruto
vinte = (20 / 100.0) * bruto
onze = (11 / 100.0) * bruto

if bruto <= 900:
       print("Seu salario bruto e de:", bruto - cinco)
       print("(-) IR (5%): R$", cinco)
       print("(-) INSS ( 10%): R$", dez)
       print("FGTS (11%): R$", onze)
       print("Total de descontos: R$", cinco + dez + onze)
       print("Salario Liquido: R$", bruto - (cinco + dez + onze)) 
elif bruto >= 900 and bruto <= 1500:
       print("Seu salario bruto e de:", bruto - dez)
       print("(-) IR (5%): R$",cinco)
       print("(-) INSS (10%): R$" ,dez)
       print("FGTS (11%): R$" ,onze)
       print("Total de descontos: R$", (cinco + dez + onze))
elif bruto > 1500:
       print("Seu salario bruto e de:", bruto - vinte)
       print("(-) IR (5%): R$", cinco)
       print("(-) INSS (10%): R$" ,dez)
       print("FGTS (11%): R$" ,onze)
       print("Total de descontos: R$", cinco + dez + onze)

print("======================================================")

