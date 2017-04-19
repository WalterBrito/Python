# -*- coding: utf-8  -*-

"""
Altere o programa anterior permitindo ao usuário informar as populações e as
taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
"""


print("==============================================================")


while True:
	paisA = int(input("Digite um numero de anos para pais A: "))
	paisB = int(input("Digite um numero de anos para pais B: "))
	taxaCrescA = float(input("Digite a taxa de crescimento (ex. 0.2 para 2%): "))
	taxaCrescB = float(input("Digite a taxa de crescimento (ex. 0.014 para 14%): "))

	anos = 1 
	while paisA < paisB:

		paisA = paisA * (1 + taxaCrescA)
		paisB = paisB * (1 + taxaCrescB)
		anos = anos + 1

	print("paisA: ", round(paisA))
	print("paisB: ", round(paisB))
	print("Pais A ultrapassará pais B ou ira se igualar em: %d anos." % anos)
	

	sair = input("Deseja sair do programa (S-Sim / N-Nao):")
	if sair == 's':
		break



print("==============================================================")
