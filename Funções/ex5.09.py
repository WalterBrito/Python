# -*- coding: utf-8 -*-

"""
'''Data com mês por extenso'''. Construa uma função que receba uma data no
formato ''DD/MM/AAAA'' e devolva uma string no formato ''D de
mesPorExtenso de AAAA''. Opcionalmente, valide a data e retorne NULL caso a
data seja inválida.
"""

print("========================================================")

def dataExt(data):
	mesesStr = ["Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
	dia = int(data[0:2])
	mes = int(data[3:5])
	ano = int(data[6:10])
	print(dia, "de", mesesStr[mes-1], "de", ano)

i = 0
while i == 0:
	# No python 3 nao funciona, apenas com raw_input.
	dataStr = raw_input("Digite uma data (DD/MM/AAAA): ")
	dataExt(dataStr)
	i = int(input("\nDigite 0 para continuar ou 1 para sair:"))
	if i == 1:
		print("\nAte a proxima!\n\n")

print("========================================================")