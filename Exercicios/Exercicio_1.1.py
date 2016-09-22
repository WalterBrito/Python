# -*- coding: utf-8 -*-

# Calculo de aumento de salario

print("="*60)

salario = float(input("Digite o valor do salario: "))
aumento = float(input("Digite o valor do aumento: "))

print("O valor do salario: %.2f" % salario)
print("Valor do aumento foi de %d " % aumento)
print("O valor do salario com aumento: %.2f" % (salario + (salario * aumento / 100)))

print("="*60)
