# -*- coding: utf-8 -*-

"""
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes
e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor
foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar
numeros aleatórios, simulando os lançamentos dos dados.
"""

print("=======================================================")

import random

def lancar():
	vetor = [0, 1, 2, 3, 4, 5, 6]
	random.shuffle(vetor)   # Erro
	return vetor[0]

listaVetor = {}.fromkeys(range(7), 0)
print(listaVetor)

for i in range(1000000):
	f = lancar()
	listaVetor[f] = listaVetor[f] + 1

for k,v in listaVetor.items():
	print("Valor: ",k," - ",v," vezes.",  (v * 100/1000000))

print("=======================================================")