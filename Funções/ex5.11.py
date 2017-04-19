# -*- coding: utf-8 -*-

"""
'''Desenha moldura'''. Construa uma função que desenhe um retângulo usando os
caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, ''linhas'' e
''colunas'', sendo que o valor por omissão é o valor mínimo igual a 1 e o valor
máximo é 20. Se valores fora da faixa forem informados, eles devem ser
modificados para valores dentro da faixa de forma elegante.
"""

print("=======================================================")

def valorPorOmissao(valor):
	if valor == '':
		return int(1)
	else:
		return faixaMinimaMaxima(int(valor))

def faixaMinimaMaxima(valor):
	if valor < 1:
		return 1
	elif valor > 20:
		return 20
	else:
		return valor

def criaLinha(linha):
	l = '+'
	for x in range(linha):
		l += '-'
	l += '+'
	print(l)

def criaColuna(linha, coluna):
	for y in range(coluna):
		for y in range(coluna):
			c = '|'
			c += ' '*linha
			c += '|'
			print(c)

def desenhaMoldura(linha, coluna):
	criaLinha(linha)
	criaColuna(linha, coluna)
	criaLinha(linha)

linha = int(input("Diga quantos +-----+, entre 1 e 20: "))
coluna = int(input("Diga quantos |    |, entre 1 e 20: "))
desenhaMoldura(valorPorOmissao(linha),valorPorOmissao(coluna))

print("=======================================================")



