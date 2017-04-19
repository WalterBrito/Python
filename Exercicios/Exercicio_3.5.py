# -*- coding: utf-8 -*-

"""
Escreva um programa que leia um a quantidade de dias, horas, minutos
e segundos do usuário. Calcule o total em segundos.
"""
print(60 * "=")
dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

# Um minuto tem 60 segundos
# Uma hora tem 3600 (60 * 60) segundos
# Um dia tem 24 horas, logo 24 * 3600 segundos
total = (dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos)

print("Total em segundos e %d." % total)
print(60 * "=")
