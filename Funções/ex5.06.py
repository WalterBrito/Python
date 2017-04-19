# -*- coding: utf-8 -*-

"""
Faça um programa que use a função valorPagamento para determinar o valor a ser
pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o
valor da prestação e o número de dias em atraso e passar estes valores para a
função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao
programa que a chamou. O programa deverá então exibir o valor a ser pago na
tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e
assim continuar até que seja informado um valor igual a zero para a prestação.
Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que
conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor
a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor
da prestação. Quando houver atraso, cobrar 3%  de multa, mais 0,1%  de juros por
dia de atraso.
"""

print("=========================================================")

def valorPagamento(valorPrest, diasAtr):
	pgt = valorPrest
	prestJuros = valorPrest
	multa = valorPrest*0.03
	if diasAtr > 0:
		i = 0
		while i < diasAtr:
			prestJuros = prestJuros + prestJuros*0.001
			i += 1
		juros = prestJuros - valorPrest
		return float(multa + valorPrest + juros)
	else:
		return float(valorPrest)

i = 0
while i == 0:
	valorPrest = int(input("Digite o valor da prestacao: "))
	diasAtr = int(input("Digite o numero de dias de atraso: "))
	print("Total a pagar: R$", round(valorPagamento(valorPrest, diasAtr)))
	i = int(input("\nDigite 0 para continuar ou 1 para sair: "))
	if i == 1:
		print("\nAte a proxima!\n\n")

print("=========================================================")