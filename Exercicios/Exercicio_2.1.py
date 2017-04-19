# -*- coding: utf-8 -*-

"""
Escreva uma expressão para determinar se uma pessoa deve ou não
pagar imposto. Considere que pagam imposto pessoas cujo salário
é maior que R$ 1.200,00.
"""

print("="*60)


salario = float(input("Digite o valor do salario: "))

if salario > 1200:
	print("Voce ira pagar imposto!")
else:
	print("Voce não ira pagar imposto.")


print("="*60)