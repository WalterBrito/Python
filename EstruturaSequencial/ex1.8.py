# -*- coding: UTF-8 -*-

'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
'''

print("======================================================")

horaTrab = int(input("Quantas voce ganha por hora?: "))
horasTrabMes = int(input("Quantas horas voce trabalha no mes?: "))

salario = horaTrab * horasTrabMes
print("Voce ganha por hora: R$ %d.00" % horaTrab)
print("O numero de horas trabalhadas no mes e: %d" % horasTrabMes)
print("O valor do seu salario e: R$ %.2f" % salario)

print("======================================================")
