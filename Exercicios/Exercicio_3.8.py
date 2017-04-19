# -*- coding: utf-8 -*-

"""
Escreva um programa que calcule o tempo de uma viagem de carro.
Pergunte a distância a percorrer e a velocidade média esperada 
para a viagem.
"""

print(60 * "=")

distancia = float(input("Digite a distancia a percorrer (km): "))
velocidade = float(input("Digite a velocidade media: "))

tempoViagem = distancia / velocidade

print("O tempo da viagem e de %d horas." % tempoViagem)

tempoSeg = int(tempoViagem * 3600)  # Convertendo de horas para segundos
horas = int(tempoSeg / 3600)
tempoSeg = int(tempoSeg % 3600)
minutos = int(tempoSeg / 60)
segundos = int(tempoSeg % 60)
print("%02d:%02d:%02d" % (horas, minutos, segundos))

print(60 * "=")
